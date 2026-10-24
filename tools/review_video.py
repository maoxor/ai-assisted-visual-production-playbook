"""Review video: turn an image sequence (or several, side by side) into a video playable anywhere, played forward.

  python review_video.py --seq renders/final --output review.mp4 [--loops 3] [--fps 30] [--height 1080]
  python review_video.py --seq before/ --seq after/ --output before_after.mp4      # side by side, same height

Rules (method: docs/workflow/07-validation.md): FORWARD playback only (never back and forth), several loops to judge
a loop seam, same height for every column, high quality H.264 (CRF 14) for review: this is not a delivery export.
Column captions belong in the review page (review_page.py). Requires ffmpeg in the PATH.
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def command(seqs, output, pattern="*.png", fps=30, loops=1, height=1080, crf=14):
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg not found in the PATH")
    inputs, filters = [], []
    n_frames = None
    for i, s in enumerate(seqs):
        n = len(sorted(Path(s).glob(pattern)))
        if not n:
            raise FileNotFoundError(f"no {pattern} image in {s}")
        n_frames = n if n_frames is None else min(n_frames, n)
        inputs += ["-framerate", str(fps), "-stream_loop", str(max(0, loops - 1)),
                   "-pattern_type", "glob", "-i", str(Path(s) / pattern)]
        filters.append(f"[{i}:v]scale=-2:{height}:flags=lanczos,setsar=1[v{i}]")
    if len(seqs) > 1:
        filters.append("".join(f"[v{i}]" for i in range(len(seqs))) + f"hstack=inputs={len(seqs)}[v]")
        video_out = "[v]"
    else:
        video_out = "[v0]"
    return ["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(filters), "-map", video_out,
            "-frames:v", str(n_frames * loops), "-r", str(fps), "-c:v", "libx264", "-preset", "slow",
            "-crf", str(crf), "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an", str(output)]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seq", action="append", required=True, help="image folder (repeatable: side by side)")
    ap.add_argument("--output", required=True)
    ap.add_argument("--pattern", default="*.png")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--loops", type=int, default=1, help="number of chained loops (forward)")
    ap.add_argument("--height", type=int, default=1080)
    a = ap.parse_args(argv)
    cmd = command(a.seq, a.output, a.pattern, a.fps, a.loops, a.height)
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(cmd, check=True)
    print(f"VIDEO {a.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
