# Tools

Six standalone Python command-line tools that serve the method's quality mechanisms: measure flicker, check a loop,
stabilize frames, make sure versions never mix, present a review. They have no dependency on any project, are
**tested** on synthetic sequences ([`tests/test_tools.py`](../tests/test_tools.py)) and are demonstrated end to end by
[`examples/demo.py`](../examples/README.md).

| Tool | Purpose | Needs |
|---|---|---|
| [`flicker.py`](#flickerpy) | Measure flicker in a frame sequence or a video; flicker map | numpy, OpenCV |
| [`loop_check.py`](#loop_checkpy) | Check a complete looping sequence: frames, seam, flicker | numpy, OpenCV |
| [`stabilize.py`](#stabilizepy) | Remove temporal spikes without spatial blur | numpy, OpenCV |
| [`fingerprint.py`](#fingerprintpy) | Fingerprint a production's dependencies; safe resume | standard library |
| [`review_page.py`](#review_pagepy) | Offline HTML review page from a JSON plan | standard library |
| [`review_video.py`](#review_videopy) | Forward, side-by-side review video | ffmpeg |

## Install and run

From a clone of this repository (dependencies pinned in `uv.lock`):

```bash
uv run python tools/flicker.py --seq <frames> --label trial
uv run pytest tests/test_tools.py
```

Without uv: `python -m pip install numpy opencv-python-headless`, then `python tools/<tool>.py`. Every tool prints its
options with `--help`. `scripts/new_project.py` copies the tools into a project's `tools/` folder so that the project
keeps the exact version it was built with; update them from this repository rather than editing them in place.

**Common conventions.** Frame sequences are folders of images sorted by name (`--pattern` selects them; 8 or 16-bit,
grey, BGR or BGRA PNG). Luminance uses BT.709 weights on a 0-255 scale whatever the bit depth. Measurements are
printed as one JSON object on standard output. Exit code 0 means success; `loop_check.py` and `review_page.py` return
1 when they find a problem.

<a id="flickerpy"></a>

### `flicker.py`

Measures the pixels that light up then go dark, from the temporal acceleration of luminance
A(t) = I(t+1) − 2·I(t) + I(t−1), on a frame sequence or a decoded video.

```bash
python tools/flicker.py --seq renders/final --label v3 [--pattern 'frame_*.png'] [--start 0 --end 299 --step 1]
    [--threshold 24] [--region 0.2,0.1,0.8,0.6] [--map flicker_v3.png] [--json measures.json]
python tools/flicker.py --seq review.mp4 --label h264
```

Output fields: `frames`, `size`, `mean_acceleration` (mean |A|), `flicker_pct` (share of pixels where |A| exceeds the
threshold with a sign change, i.e. back and forth), `isolated_pct` (among them, 1 to 9-pixel blobs: point flicker), plus
`label` and `sequence`. `--json` accumulates measurements under their label in one file. `--map` writes a PNG: red for
isolated points, yellow for areas.

- **When**: diagnosing a stability regression; before/after a fix; source frames against encoded videos, to find
  where the defect originates.
- **Contribution**: makes measurable a defect the eye sees but cannot locate; separates computation from encoding.
- **Limit**: an intended variation (blink, flash) is counted; judge with the video in front of you, at final size and
  quality.

<a id="loop_checkpy"></a>

### `loop_check.py`

Checks a complete sequence meant to loop: frame count, readable files, seam (ratio between the last → first frame
difference and the mean consecutive difference), flicker across the seam.

```bash
python tools/loop_check.py --seq renders/final --expected 300 [--pattern 'frame_*.png'] [--max-ratio 2.0]
    [--json check.json]
```

Output fields: `frames`, `expected`, `unreadable`, `mean_consecutive_diff`, `max_consecutive_diff`,
`min_consecutive_diff`, `seam_diff`, `seam_ratio`, `flicker_pct`, `ok`. Exit code 1 when frames are missing or
unreadable, or when the seam ratio exceeds `--max-ratio`. A seam difference close to zero reveals a duplicated last
frame (a visible pause).

- **When**: after each complete production, before encoding.
- **Contribution**: detects a jump at the seam, a missing frame or a duplicated final frame.
- **Limit**: complements, without replacing, the check of the scene's **state** at the period.

<a id="stabilizepy"></a>

### `stabilize.py`

Temporal stabilization: a median of three frames motion-compensated with dense optical flow (OpenCV DIS), **limited to
spikes**: a pixel is changed only if it lies outside the interval of its two warped neighbours. No spatial blur.

```bash
python tools/stabilize.py --src renders/final --dst renders/stable --loop [--threshold 6] [--strength 1.0]
    [--guard 120] [--frames 0..19] [--pattern 'frame_*.png']
```

Writes the frames under the same names in `--dst` and prints the share of changed pixels. Without `--loop`, the first
and last frames are copied unchanged; with `--loop`, frame 0 has the last frame as its neighbour.

- **When**: after a render whose residual flicker comes from sampling (very intense reflections, small bright details).
- **Contribution**: strong flicker reduction without loss of sharpness; lighter videos at equal quality.
- **Safeguards**: pixels are left untouched where the flow is inconsistent forward and backward (textureless area) or
  where the gap exceeds `--guard` (occlusion, wrong warp). The tests check both.
- **Limit**: this is not a denoiser; inspect sensitive areas (faces, text) at 200 %. Start with `--threshold 6`; lower
  values (4) treat more pixels on very noisy scenes.

<a id="fingerprintpy"></a>

### `fingerprint.py`

SHA-256 fingerprint of a production's dependencies (files, glob patterns, values such as the software version or the
quality profile). `ensure` moves the outputs of another state to `_stale/`, never deleting them; `pending` lists the
missing or incomplete units (PNG without its IEND chunk, empty file).

```bash
python tools/fingerprint.py compute --dep scene.blend --dep config/scene.toml --dep 'layers/*.png' --extra tool="Blender 4.2"
python tools/fingerprint.py ensure --outputs renders/v1/desktop --dep ... [--extra quality=final] [--stale renders/v1/_stale]
python tools/fingerprint.py pending --outputs renders/v1/desktop --count 300 [--template 'frame_{:04d}.png']
python tools/fingerprint.py run --outputs renders/v1/desktop -- python scripts/render.py --batch 0
```

`run` executes the command while `<outputs>/RUNNING` (holding the process id) marks the production as in progress,
removes the marker at the end and returns the command's exit code; `fingerprint.running(outputs)` does the same around
a block of Python code. The [`guard_production.py`](../hooks/README.md) hook uses this marker to freeze the
dependencies listed in `VERSION.json`.

`ensure` writes `<outputs>/VERSION.json` (fingerprint, date, per-file digests, extra values) and prints the
fingerprint prefix with the action taken: `new`, `unchanged` or `… moved to <stale folder>`. File paths are part of the
fingerprint: always call it from the same folder, with the same relative paths.

- **When**: before each production batch, and for any resume after an interruption.
- **Contribution**: no unit of an old state slips into a deliverable; safe resume; history kept.
- Integration into a render loop:

  ```python
  from fingerprint import ensure, pending
  deps = ["scenes/main.blend", "config/scene.toml", "scripts/render/job.py", "layers/*.png"]
  from fingerprint import running
  ensure("renders/v3/desktop", deps, {"renderer": "4.2", "quality": "final"})
  todo = pending("renders/v3/desktop", 300)
  with running("renders/v3/desktop"):    # dependencies frozen for the agent while the loop runs
      for start in range(0, len(todo), 10):
          render(todo[start:start + 10])  # one process per batch; check disk space before each one
  ```

<a id="review_pagepy"></a>

### `review_page.py`

Generates a local, self-contained, offline HTML page from a JSON plan: sections, looping videos played forward,
images, measurement tables. Light or dark theme follows the system; captions are mandatory; missing files are flagged.

```bash
python tools/review_page.py --plan review.json --output review/step/index.html [--open]
```

Plan format (paths relative to the page):

```json
{
  "title": "Iteration 4 - sample element",
  "lang": "en",
  "intro": "What the page shows and what is expected from the reviewer.",
  "sections": [
    {"title": "Whole scene, desktop", "text": "Forward playback, final size.",
     "media": [{"file": "before.mp4", "caption": "Before"}, {"file": "after.mp4", "caption": "After"}],
     "table": {"columns": ["Measure", "Before", "After"], "rows": [["Flicker", "1.33 %", "0.16 %"]]}}
  ]
}
```

Exit code 1 when a file is missing (also listed on standard error as `MISSING <file>`).

- **When**: at each step presented to the lead.
- **Contribution**: homogeneous comparisons (same size, labelled columns), nothing forgotten, no publication needed.

<a id="review_videopy"></a>

### `review_video.py`

Turns one or several frame sequences into an H.264 review video (CRF 14), **played forward**, over several loops, side
by side at the same height.

```bash
python tools/review_video.py --seq renders/final --output review.mp4 [--loops 3] [--fps 30] [--height 1080]
python tools/review_video.py --seq before/ --seq after/ --output before_after.mp4
```

Frames are selected with `--pattern` and staged under sequential names in a temporary folder, so any file name works
on Linux, macOS and Windows. `--height` must be even. Column captions belong in the review page.

- **When**: before/after comparisons, review of a loop (several loops to judge the seam).
- **Contribution**: applies the review rules by default (never back and forth, same size).

## Adding a tool

A script enters only once **generalized** (no project path, name or setting), **tested** on synthetic data in
`tests/`, and documented in this file with its usage, contribution and limits
([`CONTRIBUTING.md`](../CONTRIBUTING.md#after-each-project)). Keep tools standalone: standard library, numpy and
OpenCV only, unless a new dependency is justified in the pull request.
