# 7. Validation in final conditions

**Objective.** Make sure that the complete piece, not an excerpt or a prototype, holds in the real distribution
conditions, and make visible what could not be verified.

## Two levels [proven]

| Level | Who | Form |
|---|---|---|
| **Checks** | The agent | Commands run, results quoted, captures and videos to inspect |
| **Approval** | The lead | Explicit decision after seeing the result |

The two are never confused in a report ([P2](../principles.md#p2)).

## Families of checks [proven]

The details per moment are in the [checklists](../quality/checklists/README.md).

1. **Fidelity**: the subject, without effects, compared with the source, at equivalent framing and colour management.
2. **Locality of effects**: an effect acts only where it should; verified by isolating the other effects.
3. **Overlaps**: no black area, no stray outline, no artefact where several elements overlap.
4. **Edges and margins**: no visible edge at extreme positions, neither directly nor through a reflection or
   refraction.
5. **Animation**: no jump, no speed break, no stretching or texture sliding; motion perceptible at normal speed.
6. **Loop**: checked over the **complete period**, without a duplicated last frame (pause), with a seam of the same
   order as the difference between two consecutive frames. A short excerpt does not validate a long loop.
7. **Temporal stability**: flicker measured at final size, on the source frames and then on the encoded videos; an
   intended variation is not counted.
8. **Encoding**: details preserved, blacks without banding, loop seam without a quality jump.
9. **Real playback or execution**: in the target browsers, devices or environments; real and emulated are kept apart.
10. **Leftovers**: signature, logo, placeholder text, watermark, debug element; an explicit check on **every**
    deliverable ([A3](../quality/anti-patterns.md#a3)).
11. **Requests of the iteration**: each one restated with its status ([P15](../principles.md#p15)).

## Validation excerpt [proven]

Before the complete piece, produce **a real excerpt of the final production**: a continuous run of units (a few
consecutive seconds for a video), with the delivery settings and processing, on a passage that contains the important
motions and effects. Stills, a few repeated units or a degraded preview **do not allow** this validation
([A1](../quality/anti-patterns.md#a1)). Deliver the excerpt in the final format, access to the sources (to tell a
computation defect from a compression defect) and the timings actually observed.

## Review videos [proven]

- **Forward, looping, never back and forth** ([A7](../quality/anti-patterns.md#a7)).
- **Whole piece animated**, in addition to close-ups.
- **Labelled side by side**, at identical size and speed.
- **Latest version**; past versions only on request.
- **Several loop cycles** to judge the seam.
- **Show early**: a short or partial render is better than a long wait.

Tools: [`review_video.py`](../../tools/README.md#review_videopy) and
[`review_page.py`](../../tools/README.md#review_pagepy).

## Exit criterion

Whole-piece checks run and quoted; review videos produced and opened; real playback verified in the accessible
environments; impossible checks listed; the lead's approval requested, or recorded if it was given.
