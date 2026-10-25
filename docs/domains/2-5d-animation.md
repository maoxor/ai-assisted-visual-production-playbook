# 2.5D animation of a subject from a single image

Practices **[proven]** unless stated otherwise.

## Objective and fundamental limit

Bring an existing illustration to life (breathing, micro-expressions, secondary elements) **without regenerating the
subject** and without betraying its identity, anatomy, proportions or details
([decision 0004](../decisions/0004-preserve-the-source.md)). There is a single view: do not invent a rotation that
would reveal a profile absent from the source; amplitudes stay within what the view can support.

## Method: layers projected from the camera

1. **Cut out what must move, and only that**: the plate (body and background), the head, the secondary elements. Each
   added cut-out must bring a benefit.
2. **Precise masks**, especially on dark contours and junctions: point-assisted segmentation, then manual correction.
3. **Relative depth** estimated by a local model to give each layer relief (check the licence of the variant used:
   [AI guide](ai-models-and-assets.md)).
4. **Meshes placed along the rest camera's rays**: at rest, the camera sees exactly the source image. When the subject
   moves, the texture stays attached to the geometry, without sliding, and the effects placed in front (glass,
   reflections) react to the animated state.
5. **Rebuild only the hidden areas that will be revealed**, by mirroring the neighbouring texture or copying samples;
   resolve the edges so that the rest state recomposes the source.
6. **Named controllers** and multipliers per motion family: 0 gives the rest state, 1 the normal setting, 3 an
   exaggeration for diagnosis.

## Deforming without stretching: anchored fields

- An area moves **as a block** thanks to plateau kernels, without stretching; local stretching is measured and capped.
- **Anchors** (zero displacement on an area or line) hold what must not move: centre and volume of the lips, bridge of
  the nose, attachment points.
- **Fix the construction, not the amplitude**: if an area "swells", a neighbouring motion is often moving its edges;
  anchors solve the problem without reducing the amplitude.
- **When geometry cannot go further, use shading**: an opening (nostril, crease) that cannot grow without stretching
  the skin becomes readable by darkening its furrow.
- **Animated creases**: on a self-lit texture, only colour can carry the deepening of a crease; crease maps deepen with
  the weight of the motion.

## Rhythm and hierarchy of motion

- **The torso carries the breath**; the neck, the lower face and the shoulders follow with different **offsets** and
  **amplitudes**; the head follows less, to stay settled.
- **A breathing curve drawn in phases** rather than a sine wave: active inhalation, hold, exhalation with an elastic
  return, pause. Several breaths of different durations and amplitudes in the loop, with an exact seam.
- **Precomputed channels per element**, one key per frame: each element reads its own curve.
- **Occasional micro-expressions**, spread over the loop, never simultaneous nor repeated at every breath.
- **No constant agitation**: the pause in each cycle is essential.
- **Compare several rhythms in the whole piece** and choose on presence, at normal speed.

## Animated graphic elements (strokes, signs, inscriptions)

1. **Isolate** the ink layer (alpha and premultiplied colour) so that the rest state reproduces the source exactly;
   rebuild the support underneath, its hue matched to the surroundings.
2. **Vectorize**: skeleton, then strokes oriented in the writing direction.
3. **Animate the shape**, not just the light: light accompanies a change of shape; it does not replace it.
4. **Compare several directions** (rewriting along the strokes, recomposition) and keep the one whose **every
   intermediate state is a clean drawing**.
5. **Structure the sequence**: intent, transformation, hold, return; compare several rhythms at final size.
6. **Precompute** into an atlas read at the surface's coordinates, so that the element stays attached during motion;
   reflections show the same animation.

## Checks

- **Close-up without effects, fixed camera**, over the whole loop, at normal speed: real, frozen, exaggerated ×3, slow
  motion.
- **Rig audit**: what the rig actually animates; check deformations and animated materials, not just object matrices.
- **Optical flow per area** and rest / peak / difference contact sheets, motion by motion.
- **Protected areas** tracked on their animated position, not on fixed coordinates.
- **Perceptibility**: the motion reads at normal speed and final size; slow motion is only for diagnosis.

## What often fails

| Trial | Why |
|---|---|
| Marked head rotation | Reveals a profile absent from the source |
| Large geometric deformation of an opening | Stretches the skin; prefer shading |
| Constant quivering of secondary elements | Agitation that pulls attention away from the subject |
| Decorative inner glow | A light blotch without a role |
| Free recomposition of a stroke | Confusing intermediate states |
