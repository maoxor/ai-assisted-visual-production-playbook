# Reduce production and distribution cost

```markdown
<Observation: the announced times do not allow iteration.> **Solve this production problem first, before launching a
new long computation.**

Reminder of the objective: <…>. The validation deliverable is **a real <duration> excerpt of the final production**
(<n> consecutive units), with the settings and processing planned for the full production. Stills or a degraded preview
do not allow this validation.

## 1. Identify the real causes of the cost
Inspect the whole pipeline. Check the actual use of the hardware (accelerator, fallbacks), the cost of the elements
(<transparency, materials, geometry, lights…>), the settings (<samples, supersampling, bounces…>), memory, compilation
times, disk writes and unnecessary rebuilds. Measure a few representative units, including a difficult one; separate
start-up from steady state; attribute the expenses with isolated tests. No setting is untouchable: its usefulness must
be demonstrated visually.

## 2. Research
Official documentation, repositories, forums, comparable production feedback, without sub-agents.

## 3. Compare measured solutions
A few consistent profiles on the same units and a short demanding passage: time, memory, sharpness, details,
stability, compatibility. Also explore method changes (replace, simplify, remove what is invisible, split between
computation and post-processing). Do not freeze what must evolve; no unverified interpolation; no global blur. A short
table: measured times, gain, visible differences, recommendation.

## 4. Separate computation and distribution
Handle separately: production time, weight and transfer, decoding and playback. Exports suited to the displayed sizes
and the devices; a codec comparison on the difficult passages; real integration tested (start, seams, dropped frames,
constrained network, poster, fallback). Separate physical devices from emulation.

## 5. Produce the requested excerpt
Choose the best measured trade-off; an updated estimate for the excerpt and for the whole; produce the excerpt with the
delivery parameters on a passage that allows an artistic decision. Deliver: playable excerpts, access to the sources,
settings and observed times, quality / performance comparison, limitations, preview page. Keep previous versions. Do
not launch the full production before I approve the excerpt; continue autonomously with the analysis, trials and their
implementation.
```
