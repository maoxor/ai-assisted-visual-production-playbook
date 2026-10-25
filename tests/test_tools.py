"""Toolkit tests on synthetic sequences (no project data needed).

  uv run pytest tests/test_tools.py
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np
import pytest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))

import fingerprint  # noqa: E402
import flicker  # noqa: E402
import loop_check  # noqa: E402
import review_page  # noqa: E402
import review_video  # noqa: E402
import stabilize  # noqa: E402

N, H, W = 30, 48, 64


def sliding_band(t, n=N):
    """8-bit image: a soft bright band moving steadily and back in place at t = n (loop)."""
    x = np.arange(W, dtype=np.float32)
    centre = (t / n) * W
    d = np.minimum(np.abs(x - centre), W - np.abs(x - centre))
    row = 40 + 160 * np.exp(-(d / 8.0) ** 2)
    image = np.repeat(row[None, :], H, axis=0)
    return np.clip(np.stack([image] * 3, axis=-1), 0, 255).astype(np.uint8)


def write_sequence(folder, images, template="frame_{:04d}.png"):
    folder.mkdir(parents=True, exist_ok=True)
    for i, image in enumerate(images):
        cv2.imwrite(str(folder / template.format(i)), image)
    return folder


def smooth_sequence(n=N):
    return [sliding_band(t, n) for t in range(n)]


def flickering_sequence(n=N, seed=1, jump=70):
    """Smooth sequence + isolated pixels lighting up by "jump" every other frame."""
    rng = np.random.default_rng(seed)
    points = rng.integers(0, [H, W], size=(40, 2))
    out = []
    for t, image in enumerate(smooth_sequence(n)):
        image = image.astype(np.int16)
        if t % 2:
            image[points[:, 0], points[:, 1]] += jump
        out.append(np.clip(image, 0, 255).astype(np.uint8))
    return out


def textured_sequence(n=N, jump=0, seed=3, h=96, w=128):
    """Soft texture sliding 1 px per frame (reliable optical flow); option: blinking pixels."""
    rng = np.random.default_rng(seed)
    base = cv2.GaussianBlur(rng.uniform(40, 200, (h, w + n)).astype(np.float32), (0, 0), 2.0)
    points = rng.integers(8, [h - 8, w - 8], size=(60, 2))
    out = []
    for t in range(n):
        image = base[:, t:t + w].copy()
        if jump and t % 2:
            image[points[:, 0], points[:, 1]] += jump
        out.append(np.repeat(np.clip(image, 0, 255).astype(np.uint8)[..., None], 3, axis=2))
    return out


# -- flicker ---------------------------------------------------------------------------------------------------------

def test_flicker_smooth_motion_is_near_zero(tmp_path):
    d = write_sequence(tmp_path / "smooth", smooth_sequence())
    result, _, _ = flicker.measure(flicker.load(d))
    assert result["frames"] == N
    assert result["flicker_pct"] < 0.05


def test_flicker_detects_blinking_pixels(tmp_path):
    d = write_sequence(tmp_path / "blink", flickering_sequence())
    result, map_points, _ = flicker.measure(flicker.load(d))
    assert result["flicker_pct"] > 0.5
    assert result["isolated_pct"] > 0.5            # 1-pixel blobs: classified as isolated points
    assert map_points.max() > 0


def test_flicker_region_and_cli(tmp_path):
    d = write_sequence(tmp_path / "blink", flickering_sequence())
    out = tmp_path / "m.json"
    result = flicker.main(["--seq", str(d), "--label", "trial", "--region", "0,0,0.5,1", "--json", str(out),
                           "--map", str(tmp_path / "map.png")])
    assert result["size"] == [W // 2, H]
    assert json.loads(out.read_text())["trial"]["label"] == "trial"
    assert (tmp_path / "map.png").exists()


def test_flicker_16_bit(tmp_path):
    images = [(image.astype(np.uint16) * 257) for image in smooth_sequence()]
    d = write_sequence(tmp_path / "16", images)
    lum = flicker.load(d)
    assert 0 <= min(frame.min() for frame in lum) and max(frame.max() for frame in lum) <= 255.01


def test_flicker_rejects_fewer_than_three_frames():
    with pytest.raises(ValueError):
        flicker.measure([np.zeros((4, 4))] * 2)


# -- loop check ------------------------------------------------------------------------------------------------------

def test_perfect_loop_ok(tmp_path):
    d = write_sequence(tmp_path / "loop", smooth_sequence())
    report = loop_check.check(d, expected=N)
    assert report["ok"], report
    assert 0.5 < report["seam_ratio"] < 1.5


def test_loop_with_jump_detected(tmp_path):
    images = [sliding_band(t * 0.5, N) for t in range(N)]          # covers only half the cycle: jump at the seam
    d = write_sequence(tmp_path / "jump", images)
    report = loop_check.check(d, expected=N)
    assert not report["ok"]
    assert report["seam_ratio"] > 2


def test_loop_missing_frame(tmp_path):
    d = write_sequence(tmp_path / "missing", smooth_sequence())
    (d / "frame_0007.png").unlink()
    assert loop_check.main(["--seq", str(d), "--expected", str(N)]) == 1


def test_loop_duplicated_last_frame_is_visible(tmp_path):
    images = smooth_sequence() + [sliding_band(0, N)]               # frame N = frame 0: pause at the seam
    d = write_sequence(tmp_path / "dup", images)
    report = loop_check.check(d)
    assert report["seam_diff"] < 0.01                               # signature of a duplicated frame
    assert report["frames"] == N + 1


# -- stabilization ---------------------------------------------------------------------------------------------------

def test_stabilization_removes_blinking_without_touching_motion(tmp_path):
    src = write_sequence(tmp_path / "src", textured_sequence(jump=60))
    dst = tmp_path / "dst"
    stabilize.main(["--src", str(src), "--dst", str(dst), "--threshold", "4"])
    before = flicker.measure(flicker.load(src))[0]["flicker_pct"]
    after = flicker.measure(flicker.load(dst))[0]["flicker_pct"]
    assert before > 0.3 and after < before * 0.3
    clean = textured_sequence(jump=0)
    stable = [cv2.imread(str(p)) for p in sorted(dst.glob("frame_*.png"))]
    gap = np.mean([np.abs(a.astype(float) - b.astype(float)).mean() for a, b in zip(clean, stable, strict=True)])
    assert gap < 1.0                                                # the sliding texture is preserved


def test_stabilization_guard_leaves_huge_jumps(tmp_path):
    """Beyond --guard (120 levels), the warp is deemed wrong (occlusion): the pixel is not changed."""
    src = write_sequence(tmp_path / "src", textured_sequence(jump=255))
    dst = tmp_path / "dst"
    stabilize.main(["--src", str(src), "--dst", str(dst), "--threshold", "4", "--guard", "120"])
    before = flicker.measure(flicker.load(src))[0]["flicker_pct"]
    after = flicker.measure(flicker.load(dst))[0]["flicker_pct"]
    assert after > before * 0.8


def test_stabilization_smooth_sequence_unchanged(tmp_path):
    src = write_sequence(tmp_path / "src", textured_sequence())
    dst = tmp_path / "dst"
    stabilize.main(["--src", str(src), "--dst", str(dst)])
    for a, b in zip(sorted(src.glob("*.png")), sorted(dst.glob("*.png")), strict=True):
        assert np.abs(cv2.imread(str(a)).astype(int) - cv2.imread(str(b)).astype(int)).max() <= 1


def test_stabilization_keeps_alpha_channel(tmp_path):
    """Renders often carry an alpha channel: it must survive stabilization untouched."""
    src = tmp_path / "src"
    images = []
    for image in textured_sequence(n=8, jump=60):
        rgba = np.dstack([image, np.full(image.shape[:2], 200, np.uint8)])
        images.append(rgba)
    write_sequence(src, images)
    dst = tmp_path / "dst"
    stabilize.main(["--src", str(src), "--dst", str(dst), "--threshold", "4"])
    out = [cv2.imread(str(p), cv2.IMREAD_UNCHANGED) for p in sorted(dst.glob("frame_*.png"))]
    assert len(out) == 8 and all(o.shape[2] == 4 for o in out)
    assert all(int(o[..., 3].min()) == 200 == int(o[..., 3].max()) for o in out)


def test_stabilization_grey_frames(tmp_path):
    src = write_sequence(tmp_path / "src", [image[..., 0] for image in textured_sequence(n=8, jump=60)])
    dst = tmp_path / "dst"
    stabilize.main(["--src", str(src), "--dst", str(dst), "--threshold", "4"])
    out = [cv2.imread(str(p), cv2.IMREAD_UNCHANGED) for p in sorted(dst.glob("frame_*.png"))]
    assert len(out) == 8 and all(o.ndim == 2 for o in out)
    before = flicker.measure(flicker.load(src))[0]["flicker_pct"]
    after = flicker.measure(flicker.load(dst))[0]["flicker_pct"]
    assert after < before * 0.5


# -- fingerprint -----------------------------------------------------------------------------------------------------

def test_fingerprint_stable_and_sensitive(tmp_path):
    a = tmp_path / "settings.toml"
    a.write_text("samples = 512\n")
    fp1, _ = fingerprint.fingerprint([a], {"tool": "renderer 5.2"})
    fp2, _ = fingerprint.fingerprint([a], {"tool": "renderer 5.2"})
    assert fp1 == fp2
    assert fingerprint.fingerprint([a], {"tool": "renderer 5.3"})[0] != fp1
    a.write_text("samples = 1024\n")
    assert fingerprint.fingerprint([a], {"tool": "renderer 5.2"})[0] != fp1


def test_fingerprint_pattern_without_file_rejected(tmp_path):
    with pytest.raises(FileNotFoundError):
        fingerprint.fingerprint([str(tmp_path / "*.png")])


def test_ensure_moves_stale_outputs(tmp_path):
    dep = tmp_path / "settings.toml"
    dep.write_text("a = 1\n")
    outputs = tmp_path / "renders" / "desktop"
    fp, action = fingerprint.ensure(outputs, [dep])
    assert action == "new"
    (outputs / "frame_0000.png").write_bytes(b"x")
    assert fingerprint.ensure(outputs, [dep])[1] == "unchanged"
    dep.write_text("a = 2\n")
    fp2, action = fingerprint.ensure(outputs, [dep])
    assert fp2 != fp and "moved" in action
    assert not (outputs / "frame_0000.png").exists()
    stale = list((tmp_path / "renders" / "_stale").iterdir())
    assert len(stale) == 1 and (stale[0] / "frame_0000.png").exists()   # never deleted


def test_ensure_outputs_without_fingerprint(tmp_path):
    dep = tmp_path / "d.txt"
    dep.write_text("x")
    outputs = tmp_path / "s"
    outputs.mkdir()
    (outputs / "old.png").write_bytes(b"x")
    _, action = fingerprint.ensure(outputs, [dep])
    assert "without fingerprint" in action


def test_pending_incomplete_png(tmp_path):
    d = write_sequence(tmp_path / "f", smooth_sequence(5))
    p = d / "frame_0002.png"
    p.write_bytes(p.read_bytes()[:-20])                             # truncated PNG (interrupted write)
    (d / "frame_0004.png").unlink()
    assert fingerprint.pending(d, 5) == [2, 4]


# -- review page -----------------------------------------------------------------------------------------------------

def test_review_page_flags_missing_files(tmp_path):
    cv2.imwrite(str(tmp_path / "before.png"), sliding_band(0))
    plan = {"title": "Trial", "sections": [{"title": "S", "media": [
        {"file": "before.png", "caption": "Before"}, {"file": "after.mp4", "caption": "After"}],
        "table": {"columns": ["Measure", "Before"], "rows": [["x", "1"]]}}]}
    (tmp_path / "plan.json").write_text(json.dumps(plan))
    code = review_page.main(["--plan", str(tmp_path / "plan.json"), "--output", str(tmp_path / "index.html")])
    page = (tmp_path / "index.html").read_text()
    assert code == 1 and "Missing file: after.mp4" in page and 'src="before.png"' in page
    assert "http://" not in page and "https://" not in page          # self-contained, offline page


def test_review_page_requires_captions(tmp_path):
    with pytest.raises(ValueError):
        review_page.build({"sections": [{"title": "S", "media": [{"file": "a.png"}]}]}, tmp_path / "i.html")


# -- review video (when ffmpeg is available) -------------------------------------------------------------------------

@pytest.mark.skipif(not shutil.which("ffmpeg") or not shutil.which("ffprobe"), reason="ffmpeg not installed")
def test_review_video_loops_and_side_by_side(tmp_path):
    a = write_sequence(tmp_path / "a", smooth_sequence(12))
    b = write_sequence(tmp_path / "b", smooth_sequence(12))
    out = tmp_path / "review.mp4"
    review_video.main(["--seq", str(a), "--seq", str(b), "--output", str(out), "--loops", "2", "--height", "48"])
    probe = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                            "stream=nb_read_frames,width,height", "-of", "json", str(out)],
                           capture_output=True, text=True, check=True)
    stream = json.loads(probe.stdout)["streams"][0]
    assert int(stream["nb_read_frames"]) == 24                      # 12 frames x 2 loops, forward
    assert stream["width"] == 2 * W and stream["height"] == H


@pytest.mark.skipif(not shutil.which("ffmpeg") or not shutil.which("ffprobe"), reason="ffmpeg not installed")
def test_review_video_any_file_names(tmp_path):
    """Names with spaces or glob characters work: frames are staged under sequential names."""
    d = write_sequence(tmp_path / "odd [names]", smooth_sequence(6), template="shot A {:02d}.png")
    out = tmp_path / "out" / "review.mp4"
    assert review_video.make([d], out, height=48) == 6
    probe = subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                            "stream=nb_read_frames", "-of", "json", str(out)],
                           capture_output=True, text=True, check=True)
    assert int(json.loads(probe.stdout)["streams"][0]["nb_read_frames"]) == 6


def test_review_video_rejects_odd_height(tmp_path):
    if not shutil.which("ffmpeg"):
        pytest.skip("ffmpeg not installed")
    d = write_sequence(tmp_path / "a", smooth_sequence(4))
    with pytest.raises(ValueError):
        review_video.make([d], tmp_path / "o.mp4", height=47)
