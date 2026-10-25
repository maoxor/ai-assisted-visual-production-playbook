---
name: visual-iteration
description: Improve a visual or animated result (render, animation, interface, video) through a reference → isolated trial → comparison → integration loop, judged in final conditions. Use for any visual fix or exploration before a long production.
---

# Evidence-based visual iteration

## 1. Prepare

- Reread the request and the instruction register (`docs/instruction-register.md`); list every point requested.
- Choose a representative **sample** (one element, an excerpt of a few seconds, a difficult frame). Do not touch the
  rest until the sample is approved.
- Produce the **reference of the current state** with the trial's settings (same framing, same quality). If it is
  rebuilt, check that it gives the same result.

## 2. Understand the cause

- If the cause is not obvious: **diagnosis by elimination** — neutralize one possible cause at a time (light source,
  material set to black, element hidden, effect cut off) until the defect disappears.
- Locate the stage where the defect originates (generation, rendering, denoising, downscaling, encoding, playback) and
  fix it there.
- Check the real meaning and effect of each parameter in the tool used: measure, do not assume.

## 3. Try

- **One variable per trial**, named (`e1`, `e2`…), applied to a copy: the reference is never modified.
- Compare several amplitudes or dosages rather than a single value.
- If a trial fails: examine its construction, not only its intensity.

## 4. Compare in final conditions

- Labelled side by side, **same framing, same size, same speed**: reference / before / after, or current trial / new
  trial.
- Final display size **and** close-ups; diagnostic view **and** final processing (blur, encoding).
- Whole piece animated, **forward playback**, looping; every format.
- **Latest version** as the base. Check yourself that the difference is visible before presenting.
- Measurements as a complement (and the cost: time, weight), never as evidence on their own.
- Tools, if the project has them (`tools/` or the playbook): `review_video.py` (forward, side by side), `flicker.py`,
  `loop_check.py`, `review_page.py`.

## 5. Integrate

- Non-regression checks (rest unchanged, protected areas, valid geometry).
- Archive the configuration in force, integrate into the configuration, regenerate.
- Log (`docs/experiments/`): no., trial, finding, kept or rejected and why.

## 6. Present

- Open the comparison for the user and check that it opened; a short update: what works, what remains, the next
  action.
- Every requested point with its status: done, trial rejected (reason), missing.
- Separate my checks from their approval; do not generalize or launch production without their approval.
