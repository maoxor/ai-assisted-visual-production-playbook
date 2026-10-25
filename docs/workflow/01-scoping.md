# 1. Scoping: understand the request and the existing work

**Objective.** Know precisely what is expected, with which resources and under which constraints, then move forward on
explicit assumptions without waiting for answers that would not change the solution.

## Inputs

- The request, often long and structured (see the [prompt templates](../../templates/prompts/README.md)).
- The references: images, mock-ups, videos, websites, products.
- The existing project: files, local instructions (`CLAUDE.md`), configuration, scripts, results, reports, running
  processes.

## Steps

1. **Inspect what actually exists** [proven]. Open the files; check the versions, paths and parameters the next steps
   depend on; list the active processes. An earlier report may be truncated: read values from the files instead of
   guessing them.
2. **Check which tools are actually available** [proven]: software and versions, hardware (GPU, memory), disk space,
   network access. Never assume that an integration or permission exists without checking it.
3. **Decompose the reference** [proven]. Separate what is visible from assumptions about how it was made: a single
   image reveals neither its software nor its pipeline. Also identify what must **not** be reproduced
   (inconsistencies, interface text, defects of the mock-up).
4. **List the parameters that drive the technical choice** [proven]: pre-rendered or interactive output, resolution,
   duration, loop, target platforms, hardware, budget, available software, rights.
5. **Write the working assumptions** [proven] and move forward with them. Ask a question only if its answer really
   changes the solution.
6. **Isolate the blocking questions** [proven]. Typical example: unconfirmed distribution rights do not prevent local
   technical preparation; the question stays open on its own, and attributions and signatures are kept until it is
   settled.
7. **Restate the objective and the key criterion** [proven]. A request often contains one sentence that sums
   everything up (for example: "even without effects, the subject must feel alive"). That criterion is used to judge
   every iteration.
8. **Open the instruction register** [proven] ([P15](../principles.md#p15)): durable constraints (local only, no
   sub-agents, rights) and choices already made.

## Outputs

- A short brief: objective, key criterion, constraints, assumptions, blocking questions
  ([brief template](../../templates/project-brief.md)).
- An [instruction register](../../templates/instruction-register.md).
- For a feasibility study: a diagnosis, a compact comparison of at most three approaches, a recommendation with a
  fallback, and the next action to approve.

## Exit criterion

The objective fits in one sentence; the key criterion is identified; the existing work has been inspected file by file;
the assumptions are written; the remaining questions are truly blocking and the work can proceed without them.

## Pitfalls

- **A truncated report taken as the truth**: read the values from the files.
- **An unflagged tension in the requirements**: two requirements that contradict each other (for example a physical
  effect that necessarily distorts an area that must stay intact). Flag it early and propose an explicit trade-off.
- **Reproducing the reference's defects**: it is a target for composition and material, not the truth about
  everything.
- **Imposing a complex stack without concrete benefit**: full reconstruction, AI generation or heavy tooling must prove
  their value against a simpler solution.
