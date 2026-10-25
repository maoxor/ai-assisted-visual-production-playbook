# Templates

Templates ready to copy into a project. `python3 scripts/new_project.py <path> --name "<name>"` installs them
automatically ([`GETTING_STARTED.md`](../GETTING_STARTED.md)). You may copy and adapt them without attribution
([`LICENSE`](../LICENSE)).

| Template | Use | Location in the project |
|---|---|---|
| [`project-brief.md`](project-brief.md) | Scoping: objective, key criterion, constraints, assumptions | `docs/BRIEF.md` |
| [`project-claude-md.md`](project-claude-md.md) | The agent's instructions for the project, with the applied method | `CLAUDE.md` |
| [`instruction-register.md`](instruction-register.md) | Durable, active and replaced instructions; requests and their status | `docs/instruction-register.md` |
| [`experiment-log.md`](experiment-log.md) | Numbered log of a version's trials | `docs/experiments/<version>.md` |
| [`research-note.md`](research-note.md) | Problem, sources (D/T/H/O), method, trial, result | `docs/research/<topic>.md` |
| [`work-log.md`](work-log.md) | Log of a long workstream (branch, plan, checks, next actions) | `docs/work-logs/<date>-<topic>.md` |
| [`decision-record.md`](decision-record.md) | Structural decision (ADR) | `docs/decisions/NNNN-<title>.md` |
| [`status-update.md`](status-update.md) | Short status update | Message |
| [`delivery-report.md`](delivery-report.md) | Final report: done, tested, limitations | `docs/DELIVERY_REPORT.md` |
| [`retrospective.md`](retrospective.md) | End-of-project retrospective, which stays in the project | `docs/RETROSPECTIVE.md` |
| [`archived-version-readme.md`](archived-version-readme.md) | `README` of an archived version | `archive/<version>/README.md` |
| [`prompts/`](prompts/README.md) | Prompt templates addressed to the agent | Message |

Placeholders are written `<like this>`; `new_project.py` fills in `<project name>` and the first date.
