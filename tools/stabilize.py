"""Temporal stabilization of rendered frames: motion-compensated temporal median, limited to spikes.

  python stabilize.py --src renders/final --dst renders/stable --loop
  python stabilize.py --src ... --dst ... --threshold 6 --strength 1.0 --frames 0..19 [--pattern 'frame_*.png']

Principle: for each frame t, frames t-1 and t+1 are warped onto t with dense optical flow (OpenCV DIS, computed on the
images themselves, so it also follows what is seen through transparent surfaces and in reflections, unlike a
renderer's vector pass, which follows the first surface hit). A pixel is changed only if it lies outside the interval
of its two warped neighbours by at least "threshold" levels (out of 255): it lights up or goes dark on a single frame,
which is exactly flicker. It is then brought back into the interval (median of the three values). A smooth change
(sliding highlight, moving subject) is untouched: the median of three increasing values is the middle one.
Safeguards: the flow must be consistent forward and backward (otherwise the pixel is left as is), and pixels whose
difference with the warped neighbours stays huge (occlusion, wrong warp) are left as is. With --loop, frame 0 has
frame n-1 as its neighbour (the video loops).
No spatial blur: each pixel keeps its value or takes the value of a temporal neighbour at the same scene location.

Start with --threshold 6 (default); lower values (e.g. 4) treat more pixels on very noisy scenes. Check the result at
200 % on sensitive areas (faces, text) and measure flicker before and after (flicker.py).
Same idea as SpotLess (Doom9 forum).
"""
import argparse
import sys
import time
from pathlib import Path

import cv2
import numpy as np


def read(path):
    image = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    return image, (65535.0 if image.dtype == np.uint16 else 255.0)


def gray8(image, peak):
    g = image if image.ndim == 2 else cv2.cvtColor(image[..., :3], cv2.COLOR_BGR2GRAY)
    return np.clip(g.astype(np.float32) * (255.0 / peak), 0, 255).astype(np.uint8)


def flow(dis, a8, b8):
    """Flow from a to b: for each pixel of a, where it lies in b."""
    return dis.calc(a8, b8, None)


def warp(image, f):
    h, w = f.shape[:2]
    gx, gy = np.meshgrid(np.arange(w, dtype=np.float32), np.arange(h, dtype=np.float32))
    return cv2.remap(image, gx + f[..., 0], gy + f[..., 1], interpolation=cv2.INTER_LINEAR,
                     borderMode=cv2.BORDER_REPLICATE)


def consistency(f_ab, f_ba):
    """Forward-backward flow error (pixels): small where the warp is reliable."""
    back = warp(f_ba, f_ab)
    return np.linalg.norm(f_ab + back, axis=2)


def stabilize_frame(cur, prv, nxt, peak, dis, threshold, strength, guard):
    if cur.ndim == 2:                                   # grey frames: process as BGR, return one channel
        out, share = stabilize_frame(*(np.repeat(x[..., None], 3, axis=2) for x in (cur, prv, nxt)), peak, dis,
                                     threshold, strength, guard)
        return out[..., 0], share
    c8, p8, n8 = gray8(cur, peak), gray8(prv, peak), gray8(nxt, peak)
    f_cp, f_pc = flow(dis, c8, p8), flow(dis, p8, c8)
    f_cn, f_nc = flow(dis, c8, n8), flow(dis, n8, c8)
    p = warp(prv.astype(np.float32), f_cp)
    n = warp(nxt.astype(np.float32), f_cn)
    c = cur.astype(np.float32)
    lum = lambda x: 0.0722 * x[..., 0] + 0.7152 * x[..., 1] + 0.2126 * x[..., 2]   # BGR
    lc, lp, ln = lum(c), lum(p), lum(n)
    low, high = np.minimum(lp, ln), np.maximum(lp, ln)
    s = threshold * peak / 255.0
    spike = lc > high + s
    dip = lc < low - s
    reliable = (consistency(f_cp, f_pc) < 0.75) & (consistency(f_cn, f_nc) < 0.75)
    gap = np.maximum(lc - high, low - lc)
    plausible = gap < guard * peak / 255.0
    mask = (spike | dip) & reliable & plausible
    # chosen value: the closest warped neighbour (median of the three); colours stay together (no mixing)
    towards_high = np.where((lp >= ln)[..., None], p, n)
    towards_low = np.where((lp <= ln)[..., None], p, n)
    target = np.where(spike[..., None], towards_high, towards_low)
    out = c.copy()
    out[mask] = c[mask] + strength * (target[mask] - c[mask])
    return np.clip(out + 0.5, 0, peak).astype(cur.dtype), float(mask.mean() * 100)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--src", required=True, help="folder of the source frames")
    ap.add_argument("--dst", required=True, help="output folder (same file names)")
    ap.add_argument("--frames", default=None, help="a..b (default: all)")
    ap.add_argument("--threshold", type=float, default=6.0,
                    help="minimum distance outside the neighbour interval, levels out of 255 (default: 6)")
    ap.add_argument("--strength", type=float, default=1.0, help="share of the correction applied, 0 to 1 (default: 1)")
    ap.add_argument("--guard", type=float, default=120.0, help="above this gap (levels out of 255) the warp is deemed wrong and the pixel is kept (default: 120)")
    ap.add_argument("--loop", action="store_true", help="the sequence loops: frame 0 neighbours the last frame")
    ap.add_argument("--pattern", default="frame_*.png", help="image pattern (default: frame_*.png)")
    a = ap.parse_args(argv)
    src, dst = Path(a.src), Path(a.dst)
    dst.mkdir(parents=True, exist_ok=True)
    files = sorted(src.glob(a.pattern))
    if a.frames:
        i0, i1 = (int(x) for x in a.frames.split(".."))
        files = files[i0:i1 + 1]
    count = len(files)
    dis = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
    cache = {}

    def frame(i):
        if i not in cache:
            cache[i] = read(files[i])
            for j in list(cache):
                if abs(j - i) > 2 and not (a.loop and min(abs(j - i), count - abs(j - i)) <= 2):
                    del cache[j]
        return cache[i]

    t0 = time.time()
    shares = []
    for i in range(count):
        if not a.loop and (i == 0 or i == count - 1):
            cv2.imwrite(str(dst / files[i].name), frame(i)[0])     # ends of an open sequence: unchanged
            continue
        cur, peak = frame(i)
        prv, _ = frame((i - 1) % count)
        nxt, _ = frame((i + 1) % count)
        out, share = stabilize_frame(cur, prv, nxt, peak, dis, a.threshold, a.strength, a.guard)
        cv2.imwrite(str(dst / files[i].name), out)
        shares.append(share)
    mean_share = float(np.mean(shares)) if shares else 0.0
    print(f"STABILIZED {count} frames in {time.time() - t0:.1f} s | changed pixels {mean_share:.2f} % on average",
          flush=True)


if __name__ == "__main__":
    sys.exit(main())
