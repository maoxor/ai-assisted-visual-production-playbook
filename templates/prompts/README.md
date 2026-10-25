# Prompt templates

Requests to address to the agent, to be completed: the `<…>` fields receive the project's context. Write them in your
own working language; the structure is what matters.

## The structure that works [proven]

1. **Objective and intent**, in one or two sentences, with what changes compared with before ("This instruction
   explicitly replaces…").
2. **Take stock of the existing work**: inspect, check in the files, archive, stop obsolete tasks, separate outputs.
3. **Targeted research**: primary sources, D/T/H/O statuses, stop as soon as a trial is possible, without sub-agents.
4. **Work requested**, topic by topic: the observed defect, the intended effect, what to avoid.
5. **Demonstrate before the long computation**: the exact list of expected comparisons (same framing, size and speed).
6. **Checks**: a list of checks; measurements are a complement.
7. **Deliverables**.
8. **Execution mode**: autonomy on what is reversible, local, no production without approval, "a launched computation
   is not a delivery".
9. **Key criterion**, in bold, at the end of the request.

## Catalogue

| Prompt | When |
|---|---|
| [`01-feasibility-study.md`](01-feasibility-study.md) | Start of a project: research, comparison of approaches, plan, no implementation |
| [`02-full-delivery.md`](02-full-delivery.md) | Move from the study to a complete, verified delivery |
| [`03-new-version.md`](03-new-version.md) | Change scope or open a new version |
| [`04-reference-analysis.md`](04-reference-analysis.md) | Reproduce the quality of a reference (render, material, style) |
| [`05-sample-fix.md`](05-sample-fix.md) | Fix a precise defect on a sample, without generalizing |
| [`06-art-direction.md`](06-art-direction.md) | Delegate a distribution of treatments or an art direction |
| [`07-regression.md`](07-regression.md) | A defect has appeared since a version |
| [`08-optimization.md`](08-optimization.md) | Reduce production and distribution cost |
| [`09-responsive-integration.md`](09-responsive-integration.md) | Responsive integration: rotation, tablets, split screen |
| [`10-creative-exploration.md`](10-creative-exploration.md) | Open ideas: propose, try, let the lead choose |
| [`11-urgent-delivery.md`](11-urgent-delivery.md) | Out of time: deliver what is ready |

## Writing tips

- **Designate without ambiguity**: "the element on the right of the image, as seen by the viewer"
  ([A17](../../docs/quality/anti-patterns.md#a17)).
- **Say what replaces what** when an instruction changes.
- **List the expected comparisons**: that is what will be shown.
- **Say whether full production is authorized** at the end of the step.
- **Short messages along the way** ("Show the render", "Give me a status update"): the agent answers by opening the
  result or with a [short update](../status-update.md).
