# Offline 3D rendering

Practices **[proven]** with Blender (Cycles, GPU, OIDN denoising), transferable to any offline renderer unless stated
otherwise.

## Architecture of a reproducible rendering project

```
config/*.toml                  named parameters: composition, materials, motion, quality, encoding
scripts/prep/                  data preparation (segmentation, depth, layers)
scripts/build/                 generates the scene from the configuration
scripts/render/                renders one unit or one batch
scripts/post/                  reduction to final size, stabilization
scripts/qa/                    checks, comparisons, review pages
scenes/<scene>_<version>.*     generated scene, packed textures
renders/<version>/…            outputs separated by version (outside Git)
qa/<version>/…                 logs, measurements, comparisons, reports
archive/<version>/             complete state of every past version
```

- **The scene is generated**, never retouched by hand: a lasting change goes through the configuration, then
  regeneration.
- **The current version** is read from the configuration (`project.version`); every script derives its paths from it,
  which prevents outputs from mixing.
- **Override without editing the configuration** (`build --set 'key=value'`): the basis of variants and trials.
- **The scene file opens without running a script**: animation drivers as simple expressions, packed textures,
  controllers exposed as named properties.
- **Neutral colour management** ("Standard" in Blender) when a source texture must be reproduced as is: a filmic view
  transform would alter it.

<a id="reproducibility"></a>

## Reproducibility

- All procedural geometry derives from **one project seed**; each element has its sub-seed, derived from a stable value
  (name, number, CRC32), **never** from `hash()` ([A11](../quality/anti-patterns.md#a11)).
- **Numbering acts as a seed**: adding an element must not renumber the others; existing numbers are reserved.
- A reference element can be **frozen** (its geometry read back from the reference), then checked bit-for-bit
  identical.
- AI model revisions and dependency versions pinned (lock file, model manifest).
- Every external resource has its provenance, licence and checksums (`SHA256SUMS`, provenance manifest).

## Test bench

- **Crops at final quality** on the loaded scene: much faster than the full frame, enough to judge a material.
- **Named modifications** applied to an in-memory copy; the reference scene is never modified by a trial.
- **Contact sheets** generated automatically: labelled columns, same framing.
- **Named variants** saved separately, then promoted to main scene by copy (the old one being kept).
- **Short camera move** on a frozen frame (small ellipse, a few dozen positions) to see whether reflections reveal the
  relief; associated measurement: temporal standard deviation within the element.
- **Three-quarter view** in a neutral material, with a camera shared between variants, to understand volumes.

<a id="diagnosis-by-elimination"></a>

## Diagnosis by elimination

A method for any lighting defect of unknown origin:

1. Render the area at final quality: this is the reference.
2. Neutralize **one** possible cause at a time:
   - a light source or part of the environment;
   - a surface painted black;
   - a hidden element;
   - a ray type cut off (transmission, reflection);
   - a face switched to pure refraction.
3. The cause is the one whose neutralization makes the defect disappear.
4. Fix **locally** (per-element setting) rather than globally if the cause is useful elsewhere.

Typical defects solved this way: continuous edge lines, light bands widened by depth of field, grey patches caused by a
light reflected on a curved surface, streaks returned by tilted facets, colour casts from a secondary source.

## Transparent materials

- **Check the meaning of each parameter in the engine**: shader transmission is not the light actually transmitted. A
  small calibration bench measures what really goes through; some parameters have no effect under some conditions
  ([A9](../quality/anti-patterns.md#a9)).
- **Dark glass in front of a dark background shows only its reflections**: for it to keep surface information, give it
  something to reflect (localized lights, glints, internal cracks).
- **Thin, intermittent edges come from the lighting** (narrow sources, the so-called *white-line* technique) and from a
  micro-bevel, not from thickening; an intensity floor produces a continuous frame.
- **Light linking** gives an element its own lighting that lights nothing else.
- **Decouple thickness and relief**: express relief as a fraction of the face size, not of the thickness, otherwise
  thinning flattens everything.
- **Specular tint on a dielectric** tends towards white at grazing angles; a coloured reflection at every angle needs a
  masked specular mix.
- **Depth of field decides what is visible**: at a wide aperture, bright details become blurry discs; choose the
  aperture from the reference.
- **Automatic geometry checks**: orientation from the signed volume, closure (non-manifold edges), face side,
  self-intersections ([A13](../quality/anti-patterns.md#a13)).

## Flicker: diagnosis and treatment

**Measurement.** Temporal acceleration of luminance, A(t) = I(t+1) − 2·I(t) + I(t−1); count the pixels that light up
then go dark, at final size, on the source frames then on the encoded videos
([`flicker.py`](../../tools/README.md#flickerpy)).

**Typical mechanism.** A pixel of medium on-screen intensity is the average of a few very intense reflections (tens or
hundreds of times display white). Only a few samples out of hundreds hit them, and that number changes from one frame
to the next. The denoiser processes each frame separately: it can do nothing.

**Locate the stage.** Compare rendering, denoising, downscaling, encoding and playback. If the encoding does not
flicker more than the source frames, the defect originates in rendering.

**Levers, from the most faithful to the most destructive:**

| Lever | Effect | Cost or loss |
|---|---|---|
| Higher sample ceiling (adaptive threshold unchanged) | Reduces edge flicker; identical average image | Time multiplied on the area |
| **Motion-compensated temporal stabilization, limited to spikes** | Strong reduction; lighter videos | A few tenths of a second per frame; no spatial blur |
| Supersampled render (200 %) | Moderate reduction | Time ×4 |
| Fixed seed | Weak | The remaining noise stays frozen on screen |
| Clamping, less intense sources | Effective | Dulls and thins the intended strokes: an art direction decision |
| Temporal denoising, frame averaging | Avoid | Trails on reflections; details erased |

Recommended combination: a reasonable ceiling, then stabilization
([`stabilize.py`](../../tools/README.md#stabilizepy)), validated by a before/after measurement and an inspection at
200 %.

## Rendering cost

- **Measure before optimizing.** When GPU sampling dominates (a frequent case), only the number of pixels, the number
  of samples and the cost of a sample (bounces in transparent materials, material complexity) matter.
- **Usual levers**, to be measured one by one:
  - lower minimum adaptive samples (often without loss);
  - higher adaptive threshold (watch the dark areas);
  - lower sample ceiling;
  - details invisible at final size removed;
  - less supersampling (loss of sharpness to measure);
  - bounces limited to what is visible.
- **Supersample then downscale** (125 to 150 %, Lanczos reduction in linear light) can give a sharpness that
  denoising alone does not reach; the gain is demonstrated on each project.
- **Build cost** to track too: face count, peak memory, build time.
- The **first frame** of a process includes scene preparation: it does not count in the steady state.

## Perfect loop

- Every motion is **periodic over the exact period**, matching in position **and** velocity.
- **No duplicated final frame**: frame N is not rendered, since it is frame 0.
- Scene check: the state at the period equals the initial state (transformations and deformations at zero
  difference).
- Frame check: the last → first frame difference is of the same order as the mean difference between two consecutive
  frames ([`loop_check.py`](../../tools/README.md#loop_checkpy)).
- Stabilization **as a closed loop**: frame 0 has the last frame as its neighbour.
