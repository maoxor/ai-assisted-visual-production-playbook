# Examples

## `demo.py`: the toolkit end to end, on synthetic data

```bash
uv run examples/demo.py --open
# or, with numpy and opencv-python-headless installed:
python examples/demo.py --open
```

The demo needs no project data. It generates a seamless 80-frame loop (a periodic texture sliding 4 px per frame) with
single-frame sparkles on 0.2 % of the pixels, then calls every tool through its documented command line, printing
each command so you can reuse it on your own frames:

| Step | Tool | What it shows |
|---|---|---|
| 1 | — | Synthetic loop written to `outputs/demo/raw/` |
| 2 | [`fingerprint.py`](../tools/README.md#fingerprintpy) `ensure` | The output folder is tied to the generator and its settings; outputs of another state would be moved to `_stale/` |
| 3 | [`flicker.py`](../tools/README.md#flickerpy) | Flicker of the raw frames, with a flicker map |
| 4 | [`stabilize.py`](../tools/README.md#stabilizepy) `--loop` | Temporal spikes removed, closed loop, no spatial blur |
| 5 | `flicker.py`, [`loop_check.py`](../tools/README.md#loop_checkpy) | Flicker after stabilization; frame count and loop seam |
| 6 | [`review_video.py`](../tools/README.md#review_videopy) | Raw and stabilized side by side, forward, two loops (skipped without ffmpeg) |
| 7 | [`review_page.py`](../tools/README.md#review_pagepy) | Offline page `outputs/demo/review/index.html` with the video, maps and measurements |

Options: `--output <folder>` (default `outputs/demo`, ignored by Git), `--frames <n>` (a divisor of 320, default 80),
`--open` (open the review page).

### Expected result

The sequence is deterministic. On the reference run (macOS, Python 3.12, OpenCV 4.x), the summary line reads:

```text
Summary: flicker 0.2689 % -> 0.0184 % (93 % less); loop ok: True (seam ratio 1.0); page: …/outputs/demo/review/index.html
```

Small differences in the third decimal can come from OpenCV's optical flow on other versions or platforms; the
automated test ([`tests/test_examples.py`](../tests/test_examples.py)) only requires a reduction of at least 70 % and a
loop seam ratio between 0.8 and 1.25.

### Reusing it on your own frames

Replace step 1 with your own frame folder and keep the commands printed by the demo. Judge the result on the review
video at final size and normal speed: the measurements complement that judgement; they do not replace it
([P1](../docs/principles.md#p1)).
