"""Review video: turn an image sequence (or several, side by side) into a video playable anywhere, played forward.

  python review_video.py --seq renders/final --output review.mp4 [--loops 3] [--fps 30] [--height 1080]
  python review_video.py --seq before/ --seq after/ --output before_after.mp4      # side by side, same height

Rules (method: docs/workflow/07-validation.md): FORWARD playback only (never back and forth), several loops to judge
a loop seam, same height for every column, high quality H.264 (CRF 14) for review: this is not a delivery export.
Column captions belong in the review page (review_page.py). Requires ffmpeg in the PATH.

Frames are selected with a Python glob pattern (--pattern, sorted by name), then linked under sequential names in a
temporary folder, so the tool works the same on Linux, macOS and Windows, whatever the file names.
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def stage(files, folder):
    """Expose files under sequential names (hard link when possible, copy otherwise); returns the ffmpeg pattern."""
    suffix = files[0].suffix.lower()
    for i, f in enumerate(files):
        dst = Path(folder) / f"{i:06d}{suffix}"
        try:
            os.link(f, dst)
        except OSError:
            shutil.copy2(f, dst)
    return str(Path(folder) / f"%06d{suffix}")


def command(inputs, output, fps=30, loops=1, height=1080, crf=14):
    """ffmpeg command for staged inputs: a list of (sequential pattern, frame count)."""
    args, filters = [], []
    for i, (pattern, _) in enumerate(inputs):
        args += ["-framerate", str(fps), "-stream_loop", str(max(0, loops - 1)), "-start_number", "0",
                 "-i", pattern]
        filters.append(f"[{i}:v]scale=-2:{height}:flags=lanczos,setsar=1[v{i}]")
    if len(inputs) > 1:
        filters.append("".join(f"[v{i}]" for i in range(len(inputs))) + f"hstack=inputs={len(inputs)}[v]")
        video_out = "[v]"
    else:
        video_out = "[v0]"
    n_frames = min(n for _, n in inputs)
    return ["ffmpeg", "-y", "-v", "error", *args, "-filter_complex", ";".join(filters), "-map", video_out,
            "-frames:v", str(n_frames * loops), "-r", str(fps), "-c:v", "libx264", "-preset", "slow",
            "-crf", str(crf), "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(output)]


def make(seqs, output, pattern="*.png", fps=30, loops=1, height=1080, crf=14):
    """Build the review video; returns the number of frames written."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg not found in the PATH")
    if height % 2:
        raise ValueError("--height must be even (H.264 with 4:2:0 chroma)")
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="review_video_") as tmp:
        inputs = []
        for i, s in enumerate(seqs):
            files = sorted(Path(s).glob(pattern))
            if not files:
                raise FileNotFoundError(f"no {pattern} image in {s}")
            folder = Path(tmp) / str(i)
            folder.mkdir()
            inputs.append((stage(files, folder), len(files)))
        cmd = command(inputs, output, fps, loops, height, crf)
        subprocess.run(cmd, check=True)
    return min(n for _, n in inputs) * loops


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seq", action="append", required=True, help="image folder (repeatable: side by side)")
    ap.add_argument("--output", required=True, help="output MP4 file")
    ap.add_argument("--pattern", default="*.png", help="image pattern inside each folder (default: *.png)")
    ap.add_argument("--fps", type=int, default=30, help="frame rate (default: 30)")
    ap.add_argument("--loops", type=int, default=1, help="number of chained loops, played forward (default: 1)")
    ap.add_argument("--height", type=int, default=1080, help="height of every column, even number (default: 1080)")
    ap.add_argument("--crf", type=int, default=14, help="H.264 quality, lower is better (default: 14)")
    a = ap.parse_args(argv)
    frames = make(a.seq, a.output, a.pattern, a.fps, a.loops, a.height, a.crf)
    print(f"VIDEO {a.output} ({frames} frames)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
