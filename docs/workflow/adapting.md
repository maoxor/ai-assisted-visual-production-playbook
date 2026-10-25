# Adapting the method to another project

The method has been proven on **offline 3D rendering delivered to the web**, on **real-time 3D for the web** and on
**web applications**. This document shows how each generic concept translates to other contexts. The other columns
are **[extrapolated]**: they have not been applied yet.

## What never changes

The [principles](../principles.md), the [evidence-based iteration](04-evidence-based-iteration.md) loop, the
distinction between checks and approval, the [definition of done](../quality/README.md#definition-of-done), continuity
(logs, versions, register) and the separation between method and aesthetics.

## Translating the concepts

| Generic concept | Offline rendering, web video [proven] | Web application [proven] | Real-time web 3D [proven] | Motion design, 2D animation [extrapolated] | Game [extrapolated] | Document, presentation, identity [extrapolated] |
|---|---|---|---|---|---|---|
| Production unit | Frame of a sequence | Feature, screen | Generated asset (glTF) and its feature inventory | Shot, sequence | Scene, level, effect | Page, slide, variant |
| Final conditions | Display size, normal speed, final processing, encoded video played in the browser | Real browsers and devices, real data, CI | The delivered asset in the bench, same renderer as the reference, closest framing of the application, frame rate in motion | Final output, sound, target screen | Target hardware, frame rate, production build | Real print or screen format, final export |
| Sample | One element, a few seconds of excerpt, a difficult frame | A user journey, a critical screen | One part (an appendage, an opening) at the closest framing | A key shot | A room, an effect, a test scene | A typical page, a dense slide |
| Minimal prototype | Subject, one effect element, one foreground element, one camera move | One route end to end, tested | One part of each kind, rigged and moving, exported and captured in the bench | Animatic | Vertical slice | Mock-up of one page with real content |
| Elimination (diagnosis) | Switch off a light, paint a surface black, hide an element | Disable a module, Git bisect, test doubles | Disable a part, a motion layer, a material pass | Hide a layer | Disable a system, a render pass | Remove a style, a font |
| Fingerprint and resume | SHA-256 of sources and scripts in `VERSION.json` | Commits, CI, immutable migrations | Same configuration → same binary asset; versioned toolkit copy with checksums | Project versions, named renders | Versioned builds, hashed assets | Named exported versions |
| Non-regression | Element-by-element composition, trajectories, flicker | Unit, integration and e2e tests, architecture contract | Feature inventory, motion signatures, atlas integrity, captures side by side with the reference | Frame-by-frame comparison | Automated tests, reference captures | Visual comparison of pages |
| Complementary metrics | SSIM, VMAF, flicker, WCAG contrast, time per frame | Coverage, LCP, CLS, response time | Texels per pixel, edge length, wave and swing, frame cost | Cadence, contrast | Frame time (ms), memory | Contrast, legibility, weight |
| Costs to keep apart | Computation, weight, decoding, page smoothness | Development, build, performance, maintenance | Generation, baking, asset weight, frame cost | Rendering, weight, playback | Production, memory, frame time, download | Production, printing, weight |

## How to adapt the workflow

1. **Name the production unit and the final conditions** of the new project: without them, you do not know where to
   judge.
2. **Choose the sample** that carries the main risk.
3. **Translate the families of checks** from [validation](07-validation.md). Example: "locality of effects" becomes "a
   style change only affects the targeted components".
4. **Choose the complementary metrics** and write down what they do not prove ([P1](../principles.md#p1)).
5. **Identify the costs to keep apart** ([P13](../principles.md#p13)).
6. **Write these choices in the project's `CLAUDE.md`** ([template](../../templates/project-claude-md.md)), "Applied
   method" section.
7. **After the project**, report here what worked and what was missing: an [extrapolated] column becomes [proven]
   ([`CONTRIBUTING.md`](../../CONTRIBUTING.md)).

## Changing art direction

Art direction is an **input** of the process, never an output of this playbook.

- Start again from the new project's references and intent; no earlier aesthetic choice is carried over by default.
- Keep the **mechanisms**: reference analysis on equivalent crops, element roles, contrasting variants with a
  counter-trial, annotated view, preview in motion, written choice.
- A project's lessons are observations, not general bans: a filter, material or metaphor rejected once remains possible
  elsewhere.

## Changing technology

The method depends on no software. For another stack:

- replace the tools listed in [tooling](../tooling/README.md) with their equivalents, justifying each addition
  (provenance, licence, maintenance, concrete benefit);
- keep declarative configuration, stable seeds and pinned versions ([P11](../principles.md#p11));
- rebuild a test bench that applies named modifications to a copy of the reference state.

## Different constraints

| Constraint | Adaptation |
|---|---|
| Very short deadline | Keep scoping and the definition of done; one primary source per topic; a single sample; deliver what is verified and say what is not ([delivery under time pressure](08-delivery.md#delivery-under-time-pressure)) |
| Modest machine | Cost profile from the prototype on; smaller samples; for a video, favour stabilization and downscaling over supersampling |
| Team work | Git is mandatory, branches and work logs, written decisions, CI ([web applications](../domains/web-applications.md)) |
| Public distribution and rights | Provenance and licence of every resource; the rights question isolated from scoping on; nothing published without approval |
