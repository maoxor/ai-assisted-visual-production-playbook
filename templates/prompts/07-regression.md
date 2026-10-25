# Diagnose a regression

```markdown
Since <version>, <defect> is very visible; it was not perceptible in <earlier version>. Identify this regression and
fix it before continuing the production.

Compare the outputs and source data of the two versions on comparable areas and motions. Determine at which stage the
problem appears: <generation, rendering, denoising, resizing, encoding, playback>.

Examine the changes introduced since <earlier version>: <list>. Separate normal variations from unwanted artefacts.

Look for solutions in the official documentation, practitioners' feedback and relevant resources. Test the leads on a
representative excerpt, isolating causes rather than changing several parameters at once.

The goal is a result as clean and stable as possible, keeping <sharpness, textures, richness>. Do not hide the problem
with <a global blur / a treatment that erases details>.

Present an **<earlier version> / current / fixed** comparison, at normal speed, with close-ups of the affected areas,
on the sources and on the encoded deliverables, in every format. State the cause identified, the fixes kept and their
cost before relaunching the production.
```

Once the cause is found, the following comparisons are made on the **latest version**
([A6](../../docs/quality/anti-patterns.md#a6)).
