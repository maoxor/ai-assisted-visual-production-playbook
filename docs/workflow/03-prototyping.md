# 3. Minimal prototype

**Objective.** Check on the smallest possible case that the main risks are manageable, before investing in production.

## Principle [proven]

The prototype contains **one instance of each risky element**, and nothing else. For a composited scene, for example:
the subject, one effect element in front of it, one foreground element and a short camera move. For an application:
one route end to end, with its tests.

It is decided during the feasibility study and built before the complete piece.

## What the prototype must prove

For each risk, plan a check **that can fail**:

| Typical risk | Check |
|---|---|
| Fidelity to the subject or source | Render of the rest state compared with the source, with equivalent colour management (PSNR, ꟻLIP, visual difference) |
| Locality of an effect | Move the effect to several positions and measure the difference outside its footprint |
| Overlaps | Stack the transparent elements or layers; no black area, no artefact |
| Noise and stability | Static scene rendered with several seeds; standard deviation in sensitive areas |
| Loop seam | State of the scene at the period compared with the initial state |
| Revealed edges | Margins at the extreme camera or layout positions |
| Cost | Time per unit at final quality |

## Variants to compare in the prototype [proven]

When two techniques are possible (a physical effect or compositing, for example), compare them on the prototype and
keep the one that best meets the requirements.

## Exit criterion

Every risk identified during scoping has a measured result and a capture; the cost per unit is known; the risks not
yet retired are written down with how they will be handled.

## Pitfall [proven]

A prototype that "works" does not validate production: more elements, final processing and an animated subject reveal
defects absent from the prototype. The prototype's checks are **adapted** to the new scope, not copied: a
pixel-by-pixel comparison with the source only holds for the rest state, and an intended temporal variation is not
flicker ([A18](../quality/anti-patterns.md#a18)).
