"""Loop check: verify a complete sequence meant to loop (frames present and readable, seam, flicker).

  python loop_check.py --seq renders/final --expected 300 [--pattern 'frame_*.png'] [--json check.json]

Seam: mean luminance difference between the last frame and the first, compared with the mean difference between two
consecutive frames. An invisible seam is of the same order (ratio close to 1); a much larger ratio reveals a jump; a
last frame duplicating the first gives an almost zero difference on the seam (a visible pause).
Flicker is measured across the seam (the last two frames precede the sequence, the first two follow it).

Exit code 1 when frames are missing or unreadable, or when the seam ratio exceeds --max-ratio.
This check complements the verification of the scene state at the period (identical positions and velocities):
it does not replace it.
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flicker import list_frames, measure, read_luminance  # noqa: E402


def check(seq, expected=None, pattern="*.png", max_ratio=2.0):
    files = list_frames(seq, pattern)
    report = {"sequence": str(seq), "frames": len(files), "expected": expected, "unreadable": []}
    frames = []
    for f in files:
        try:
            frames.append(read_luminance(f))
        except (FileNotFoundError, ValueError, AttributeError):
            report["unreadable"].append(f.name)
    ok = not report["unreadable"] and (expected is None or len(files) == expected) and len(frames) >= 3
    if len(frames) >= 3:
        diffs = [float(np.abs(frames[i + 1] - frames[i]).mean()) for i in range(len(frames) - 1)]
        seam = float(np.abs(frames[0] - frames[-1]).mean())
        mean = float(np.mean(diffs))
        report.update(mean_consecutive_diff=round(mean, 3), max_consecutive_diff=round(float(np.max(diffs)), 3),
                      min_consecutive_diff=round(float(np.min(diffs)), 3), seam_diff=round(seam, 3),
                      seam_ratio=round(seam / mean, 3) if mean > 0 else None)
        looped = frames[-2:] + frames + frames[:2]
        report["flicker_pct"] = measure(looped)[0]["flicker_pct"]
        if mean > 0 and seam / mean > max_ratio:
            ok = False
    report["ok"] = bool(ok)
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seq", required=True)
    ap.add_argument("--expected", type=int, default=None, help="expected number of frames (e.g. 300)")
    ap.add_argument("--pattern", default="*.png")
    ap.add_argument("--max-ratio", type=float, default=2.0, help="tolerated seam / consecutive difference ratio")
    ap.add_argument("--json", default=None)
    a = ap.parse_args(argv)
    report = check(a.seq, a.expected, a.pattern, a.max_ratio)
    print(json.dumps(report))
    if a.json:
        Path(a.json).parent.mkdir(parents=True, exist_ok=True)
        Path(a.json).write_text(json.dumps(report, indent=1))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
