"""End-to-end demonstration of the toolkit on a synthetic looping sequence (no project data needed).

  uv run examples/demo.py [--output outputs/demo] [--frames 80] [--open]
  python examples/demo.py ...            # with numpy and opencv-python-headless installed

Steps, each one a documented command-line call of a tool in tools/:
1. generate a seamless loop: a periodic texture sliding 4 px per frame, plus single-frame sparkles (flicker);
2. fingerprint.py: protect the output folder with the fingerprint of the generator and its settings;
3. flicker.py: measure flicker on the raw frames and write a flicker map;
4. stabilize.py --loop: remove the temporal spikes, without spatial blur, treating the sequence as a loop;
5. flicker.py again, then loop_check.py: flicker after stabilization, frame count and loop seam;
6. review_video.py (if ffmpeg is installed): raw and stabilized side by side, played forward over two loops;
7. review_page.py: an offline HTML page gathering the video, the maps and the measurements.

The sequence is deterministic (fixed seed): the same command gives the same measurements on every machine, within
the small differences of OpenCV's optical flow between versions.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"


def periodic_texture(width, height, rng):
    """Smooth texture that wraps exactly horizontally and vertically (sum of sinusoids with integer frequencies)."""
    x = np.arange(width, dtype=np.float32)[None, :] / width
    y = np.arange(height, dtype=np.float32)[:, None] / height
    image = np.zeros((height, width), np.float32)
    for _ in range(24):
        kx, ky = rng.integers(1, 9), rng.integers(0, 6)
        phase = rng.uniform(0, 2 * np.pi)
        image += rng.uniform(0.3, 1.0) / (kx + ky) * np.sin(2 * np.pi * (kx * x + ky * y) + phase)
    image = (image - image.min()) / (image.max() - image.min())
    return 50 + 150 * image


def synthetic_loop(folder, frames=80, width=320, height=180, sparkle_share=0.002, sparkle_gain=80.0, seed=7):
    """Write a seamless loop with sparkle flicker; returns the list of written files."""
    rng = np.random.default_rng(seed)
    texture = periodic_texture(width, height, rng)
    shift = width // frames
    if shift * frames != width:
        raise ValueError("width must be a multiple of the frame count for a seamless loop")
    tint = np.array([0.9, 1.0, 1.08], np.float32)          # BGR, a slightly warm image
    folder.mkdir(parents=True, exist_ok=True)
    written = []
    for t in range(frames):
        lum = np.roll(texture, -shift * t, axis=1).copy()
        sparkles = rng.random((height, width)) < sparkle_share
        lum[sparkles] += sparkle_gain
        image = np.clip(lum[..., None] * tint, 0, 255).astype(np.uint8)
        path = folder / f"frame_{t:04d}.png"
        cv2.imwrite(str(path), image)
        written.append(path)
    return written


def short(value):
    """A path relative to the current folder when that is shorter, for readable commands."""
    if isinstance(value, Path):
        try:
            rel = os.path.relpath(value)
            return rel if len(rel) < len(str(value)) else str(value)
        except ValueError:                 # another drive on Windows
            return str(value)
    return str(value)


def run(tool, *args):
    """Run a tool exactly as a user would, print the command and return its standard output."""
    cmd = [sys.executable, str(TOOLS / tool), *map(str, args)]
    print("$", " ".join(["python", f"tools/{tool}", *map(short, args)]), flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout.strip():
        text = result.stdout.strip()
        print("  " + (text if len(text) < 400 else text[:400] + " …").replace("\n", "\n  "))
    if result.returncode not in (0, 1):
        print(result.stderr, file=sys.stderr)
        raise SystemExit(f"{tool} failed with exit code {result.returncode}")
    return result.stdout


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--output", default=str(ROOT / "outputs" / "demo"), help="output folder (default: outputs/demo)")
    ap.add_argument("--frames", type=int, default=80, help="loop length; 320 must be a multiple of it (default: 80)")
    ap.add_argument("--open", action="store_true", help="open the review page at the end")
    a = ap.parse_args(argv)
    out = Path(a.output).resolve()
    raw, stable, review = out / "raw", out / "stable", out / "review"

    print(f"1. Synthetic loop: {a.frames} frames, 320x180, sparkles on 0.2 % of the pixels of each frame")
    shutil.rmtree(raw, ignore_errors=True)
    synthetic_loop(raw, frames=a.frames)

    print("\n2. Fingerprint the stabilized outputs (generator script and settings)")
    run("fingerprint.py", "ensure", "--outputs", stable, "--dep", Path(__file__).resolve(),
        "--extra", f"frames={a.frames}", "--extra", "threshold=4")

    print("\n3. Flicker on the raw frames")
    measures = out / "measures.json"
    measures.unlink(missing_ok=True)
    review.mkdir(parents=True, exist_ok=True)
    before = json.loads(run("flicker.py", "--seq", raw, "--label", "raw", "--json", measures,
                            "--map", review / "flicker_raw.png"))

    print("\n4. Temporal stabilization, closed loop")
    run("stabilize.py", "--src", raw, "--dst", stable, "--loop", "--threshold", "4")

    print("\n5. Flicker after stabilization, then loop check")
    after = json.loads(run("flicker.py", "--seq", stable, "--label", "stable", "--json", measures,
                           "--map", review / "flicker_stable.png"))
    loop = json.loads(run("loop_check.py", "--seq", stable, "--expected", a.frames, "--json", out / "loop.json"))

    media = []
    print("\n6. Review video")
    if shutil.which("ffmpeg"):
        run("review_video.py", "--seq", raw, "--seq", stable, "--output", review / "raw_vs_stable.mp4",
            "--loops", "2", "--height", "180")
        media.append({"file": "raw_vs_stable.mp4", "caption": "Left: raw. Right: stabilized. Forward, two loops."})
    else:
        print("  ffmpeg not found: review video skipped")

    print("\n7. Review page")
    reduction = 100 * (1 - after["flicker_pct"] / before["flicker_pct"]) if before["flicker_pct"] else 0.0
    plan = {
        "title": "Toolkit demonstration",
        "lang": "en",
        "intro": "Synthetic seamless loop with single-frame sparkles, before and after temporal stabilization.",
        "sections": [
            {"title": "Whole sequence, final size", "text": "Judge in final conditions: forward playback, loop.",
             "media": media},
            {"title": "Flicker maps", "text": "Red: isolated flickering points. Yellow: flickering areas.",
             "media": [{"file": "flicker_raw.png", "caption": "Raw"},
                       {"file": "flicker_stable.png", "caption": "Stabilized"}]},
            {"title": "Measurements (complement, not proof)",
             "table": {"columns": ["Measure", "Raw", "Stabilized"],
                       "rows": [["Flicker (% of pixels)", before["flicker_pct"], after["flicker_pct"]],
                                ["Isolated points (%)", before["isolated_pct"], after["isolated_pct"]],
                                ["Loop seam ratio", "", loop.get("seam_ratio")],
                                ["Frames (expected)", a.frames, loop["frames"]]]}},
        ],
    }
    plan_file = review / "plan.json"
    plan_file.write_text(json.dumps(plan, indent=1), encoding="utf-8")
    page_args = ["--plan", plan_file, "--output", review / "index.html"] + (["--open"] if a.open else [])
    run("review_page.py", *page_args)

    print(f"\nSummary: flicker {before['flicker_pct']} % -> {after['flicker_pct']} % "
          f"({reduction:.0f} % less); loop ok: {loop['ok']} (seam ratio {loop.get('seam_ratio')}); "
          f"page: {review / 'index.html'}")
    return {"before": before, "after": after, "loop": loop, "page": review / "index.html"}


if __name__ == "__main__":
    main()
