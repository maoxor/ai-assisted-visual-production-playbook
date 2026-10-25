# <project name>

<One or two sentences: what the project produces, for whom.> Working language: <language>.

<!-- Loaded in every session: keep it short. Details in docs/. -->

## Map

| Path | Content |
|---|---|
| `config/` | Named parameters (source of truth); regenerate after a change |
| `scripts/` | Generation, production, checks, exports |
| `docs/BRIEF.md` | Objective, key criterion, constraints, assumptions |
| `docs/instruction-register.md` | Durable, active and replaced instructions; requests and their status |
| `docs/experiments/` | Numbered experiment log |
| `docs/work-logs/` | Logs of long workstreams |
| `docs/decisions/` | Structural decisions |
| `archive/` | Previous versions (never modified) |

## Verify (before concluding a task)

```bash
<the project's check commands>
```

Never call a piece of work verified without running these commands: quote their result.

## Applied method

Playbook: `ai-assisted-visual-production-playbook` (principles, workflow, checklists). In short:

1. **Resume first**: real state (processes, `git status`), log, instruction register; the files win.
2. **One variable at a time**, on a **sample**; a reference of the current state before each trial; diagnosis by
   elimination if the cause is unknown.
3. **Judge in final conditions**: <size, speed, final processing, platform>. Review videos forward, whole piece,
   latest version. Measurements complement; they never prove.
4. **Fix the cause**, never mask it (global blur, disabled test, reduced amplitude).
5. **Cost measured** before any long production; resumable production with a fingerprint of the dependencies.
6. **Lose nothing**: archive before changing, outputs separated by version, delete nothing (move it).
7. **Done** = final deliverables exist, open and were checked; done / tested / limitations report; every request with
   its status.
8. **Show**: open the results; short updates (what works, what remains, next action).

The method translated for this project:

- Production unit: <…>
- Final conditions: <…>
- Sample that carries the main risk: <…>
- Families of checks kept: <…>
- Costs to keep apart: <…>

## Mandatory rules

- Reversible decisions: take them without asking again. Publication, sending data to an external service, purchase,
  deletion, a reserved long production: explicit approval.
- Never touch other projects' or sessions' processes; heavy computations through the common lock if there is one.
- Added resource: provenance, licence, version, role and checksum recorded.
- Secrets: never read, displayed or committed.
- Git: dedicated branch, `type(scope): description` commits (why, evidence, limitations), no push or merge unless asked;
  the workstation's Git identity.

## Project-specific

- Formats and final conditions: <…>
- Protected areas, to preserve: <…>
- Approved art direction: <link to docs/decisions/…>
