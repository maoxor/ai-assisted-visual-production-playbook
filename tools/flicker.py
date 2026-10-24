"""Flicker: measure unwanted temporal variations in an image sequence or a decoded video.

  python flicker.py --seq renders/final --label v3 [--pattern 'frame_*.png'] [--start 0 --end 299]
      [--region x0,y0,x1,y1 (fractions, origin top-left)] [--map map.png] [--json measures.json]
  python flicker.py --seq review.mp4 --label h264

Principle: a sliding highlight changes smoothly from one frame to the next; a flickering pixel lights up then goes
dark (or the reverse). The temporal acceleration of luminance, A(t) = I(t+1) - 2*I(t) + I(t-1), is small for smooth
motion and large for flicker. Measures (luminance 0-255):
- "mean_acceleration": mean of |A|;
- "flicker_pct": share of pixels where |A| > threshold and the sign of I(t+1) - I(t) is opposite to the sign of
  I(t) - I(t-1) (back and forth);
- "isolated_pct": among them, those forming 1 to 9 pixel blobs (point flicker: sub-pixel sparkles, residual noise),
  as opposed to large areas (highlights that switch).
The map accumulates flickering pixels (red: isolated points; yellow: areas).

Measure at the final display size and final quality: a low-sample preview exaggerates flicker. Intentional variation
(blink, flash) is counted too: interpret with the video in front of you.
"""
import argparse
import json
from pathlib import Path

import cv2
import numpy as np

VIDEO_SUFFIXES = (".mp4", ".mov", ".mkv", ".webm")


def luminance_bgr(image):
    """BT.709 luminance (0-255) of an 8 or 16 bit BGR image."""
    a = image.astype(np.float32)
    if image.dtype == np.uint16:
        a *= 255.0 / 65535.0
    if a.ndim == 2:
        return a
    return 0.0722 * a[..., 0] + 0.7152 * a[..., 1] + 0.2126 * a[..., 2]


def read_luminance(path):
    image = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    if image is None:
        raise FileNotFoundError(path)
    if image.ndim == 3 and image.shape[2] == 4:
        image = image[..., :3]
    return luminance_bgr(image)


def list_frames(seq, pattern="*.png"):
    return sorted(Path(seq).glob(pattern))


def load(seq, start=0, end=10 ** 9, step=1, pattern="*.png"):
    """Luminances of a sequence (folder of images sorted by name) or of a video."""
    s = Path(seq)
    if s.suffix.lower() in VIDEO_SUFFIXES:
        cap = cv2.VideoCapture(str(s))
        frames, i = [], 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if start <= i <= end and (i - start) % step == 0:
                frames.append(luminance_bgr(frame))
            i += 1
        return frames
    files = list_frames(s, pattern)[start:end + 1][::step]
    return [read_luminance(f) for f in files]


def measure(frames, region=None, threshold=24.0):
    """Flicker measures on a list of luminance frames (at least 3)."""
    if len(frames) < 3:
        raise ValueError("at least 3 frames are required")
    if region:
        h, w = frames[0].shape
        x0, y0, x1, y1 = region
        frames = [f[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)] for f in frames]
    h, w = frames[0].shape
    map_points = np.zeros((h, w), np.float32)
    map_areas = np.zeros((h, w), np.float32)
    mean_acc, share, share_points = [], [], []
    for t in range(1, len(frames) - 1):
        d1 = frames[t] - frames[t - 1]
        d2 = frames[t + 1] - frames[t]
        acc = d2 - d1
        mask = ((np.abs(acc) > threshold) & (np.sign(d1) != np.sign(d2))
                & (np.abs(d1) > threshold / 3) & (np.abs(d2) > threshold / 3))
        mean_acc.append(float(np.abs(acc).mean()))
        share.append(float(mask.mean()))
        n, labels, stats, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), connectivity=8)
        small = np.zeros(n, bool)
        small[1:] = stats[1:, cv2.CC_STAT_AREA] <= 9
        points = small[labels]
        share_points.append(float(points.mean()))
        map_points += points
        map_areas += mask & ~points
    result = {"frames": len(frames), "size": [w, h], "mean_acceleration": round(float(np.mean(mean_acc)), 3),
              "flicker_pct": round(100 * float(np.mean(share)), 4),
              "isolated_pct": round(100 * float(np.mean(share_points)), 4)}
    return result, map_points, map_areas


def write_map(path, map_points, map_areas, n_frames):
    k = 255.0 * 6 / max(1, n_frames - 2)
    bgr = np.zeros(map_points.shape + (3,), np.uint8)
    bgr[..., 2] = np.clip((map_points + map_areas) * k, 0, 255)
    bgr[..., 1] = np.clip(map_areas * k, 0, 255)
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(path), bgr)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seq", required=True, help="image folder or video file")
    ap.add_argument("--label", required=True, help="name of the measurement")
    ap.add_argument("--pattern", default="*.png", help="image pattern inside the folder (default: *.png)")
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--end", type=int, default=10 ** 9)
    ap.add_argument("--step", type=int, default=1)
    ap.add_argument("--threshold", type=float, default=24.0, help="acceleration threshold (levels out of 255)")
    ap.add_argument("--region", default=None, help="x0,y0,x1,y1 as fractions of the image")
    ap.add_argument("--map", default=None, help="PNG image of flickering pixels")
    ap.add_argument("--json", default=None, help="JSON file where the measurement is stored under its label")
    a = ap.parse_args(argv)
    frames = load(a.seq, a.start, a.end, a.step, a.pattern)
    region = [float(v) for v in a.region.split(",")] if a.region else None
    result, map_points, map_areas = measure(frames, region, a.threshold)
    result.update(label=a.label, sequence=str(a.seq))
    print(json.dumps(result))
    if a.map:
        write_map(a.map, map_points, map_areas, result["frames"])
    if a.json:
        p = Path(a.json)
        data = json.loads(p.read_text()) if p.exists() else {}
        data[a.label] = result
        p.write_text(json.dumps(data, indent=1))
    return result


if __name__ == "__main__":
    main()
