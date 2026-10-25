# Quality: how to judge, when to stop

This folder makes explicit the **evaluation criteria** and the **mechanisms** that reach and then maintain a high level
of quality.

| Document | Role |
|---|---|
| This file | Definition of done, evaluation grid, quality mechanisms |
| [`checklists/`](checklists/README.md) | Checklists per moment: resume, visual review, pre-production, web video, delivery |
| [`anti-patterns.md`](anti-patterns.md) | Classic mistakes, with their prevention |
| [`collaboration.md`](collaboration.md) | Default collaboration preferences between the lead and the agent |

<a id="definition-of-done"></a>

## Definition of done [proven]

Work is done when **all** of the following are true:

1. The deliverables exist at their final location, in every requested format, fallbacks included.
2. They **open or play** in their target environment: file fully decoded, playback verified in the browser or tool.
3. The planned checks have been **run** and their results are quoted.
4. Each request of the iteration has a status: done, trial rejected (reason) or missing ([P15](../principles.md#p15)).
5. No leftover remains: signature, logo, placeholder text, debug file, trial setting.
6. The sources make it possible to **regenerate** the result (configuration, seeds, scripts, versions).
7. The previous version is **kept**.
8. The report separates *done*, *tested* (real or emulated) and *limitations*.
9. The generic lessons are brought back to this playbook, or noted as to be brought back.

**Not** done: a launched command, a running computation, a prototype, a plan, a rebuilt scene without a final render,
an export that was never played.

## Evaluation grid [proven]

To judge a proposal or an iteration, in order of priority: appearance and motion first, measurements second.

| # | Criterion | Question | How to check |
|---|---|---|---|
| 1 | **Intent** | Does the result serve the brief's objective and key criterion? | Reread the brief; look at the result at final size |
| 2 | **Subject** | Does the subject stay at the centre? Is its identity preserved? | Comparison with the source; view without effects |
| 3 | **Perceptibility** | Is each improvement visible in final conditions, at normal speed? | Side-by-side video, before/after, whole piece |
| 4 | **Coherence** | Do the elements belong to the same world (planes, lights, materials, rhythms)? | Overview; look for elements that feel pasted on |
| 5 | **Richness without confusion** | Is the material rich without blurring reading areas? | Close-ups of sensitive areas; functional check (legibility) |
| 6 | **Intentional variety** | Is mechanical repetition avoided (mosaic, identical oscillations, regular patterns)? | Inspection in motion; comparison of elements with each other |
| 7 | **Cleanliness** | Are there artefacts (flicker, edges, holes, halos, sliding texture, leftovers)? | Automatic checks and inspection at 100 % and 200 % |
| 8 | **Stability** | Does the result hold in motion and at the loop seam? | Several loop cycles; flicker measurement |
| 9 | **Cost** | Is the cost (production, weight, playback) known and justified? | Cost profile, weight, playback tests |
| 10 | **Reproducibility** | Can this exact result be regenerated? | Fingerprint, archived configuration, seeds |

For **art direction**, only criteria 1 to 6 are decisive, and the lead's judgement wins
([art direction](../workflow/05-art-direction.md)).

## Mechanisms that produce quality

| Mechanism | Contribution | Where |
|---|---|---|
| Reference of the current state before any trial | Makes the effect of each change measurable | [Iteration](../workflow/04-evidence-based-iteration.md) |
| One variable at a time, diagnosis by elimination | Finds the real cause; avoids corrections that mask each other | [Iteration](../workflow/04-evidence-based-iteration.md) |
| Sample before generalization | Fast iterations; cost checked before it is multiplied | [P7](../principles.md#p7) |
| Comparison at identical framing, size and speed | A fair visual decision, without presentation bias | [Validation](../workflow/07-validation.md) |
| Contrasting variants and counter-trial | Reveals the lead's real preference | [Art direction](../workflow/05-art-direction.md) |
| Declarative configuration, regeneration | No retouch lost; trials can be combined | [P11](../principles.md#p11) |
| Fingerprint of dependencies | No mixing of versions; safe resume | [Production](../workflow/06-production.md#fingerprint-and-resume) |
| Non-regression checks | A local fix does not break the whole | [Iteration](../workflow/04-evidence-based-iteration.md) |
| Cost profile | A practical iteration cycle; justified settings | [Production](../workflow/06-production.md#cost-profile) |
| Numbered log | Memory of dead ends; reliable resume | [Continuity](../workflow/09-continuity.md) |
| Instruction register | No request forgotten; instructions up to date | [P15](../principles.md#p15) |
| Done / tested / limitations report | Trust; informed decisions | [Delivery](../workflow/08-delivery.md) |
| Automatic guardrails (hooks, CI) | Checks that do not depend on the agent's goodwill | [Claude Code](../tooling/claude-code.md#hooks) |
