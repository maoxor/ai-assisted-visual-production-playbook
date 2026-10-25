# Getting started

This guide goes in order, from installation to the end of a project. It assumes no particular technique or art
direction.

<a id="requirements"></a>

## Requirements

| Need | Version | Used by | Check |
|---|---|---|---|
| Git | any recent | cloning, project history | `git --version` |
| Python | 3.10 or later | tools, scripts, demo | `python3 --version` |
| [uv](https://docs.astral.sh/uv/) (recommended) | recent | isolated, locked environment (`uv.lock`) | `uv --version` |
| numpy, opencv-python-headless | see `pyproject.toml` | `flicker.py`, `loop_check.py`, `stabilize.py`, demo | installed by `uv run` or pip |
| ffmpeg (optional) | 4.4 or later, with libx264 | `review_video.py`, demo review video | `ffmpeg -version` |
| Claude Code (optional) | recent | skills, plugin, `CLAUDE.md` | `claude --version` |

`scripts/new_project.py`, `scripts/check_repo.py`, `tools/fingerprint.py` and `tools/review_page.py` use the Python
standard library only. No environment variable or external service is required; nothing is sent over the network.

## 0. Install and verify (5 minutes)

```bash
git clone https://github.com/maoxor/ai-assisted-visual-production-playbook.git
cd ai-assisted-visual-production-playbook
uv run pytest                     # installs the locked dependencies in .venv, then runs the tests
uv run examples/demo.py --open    # end-to-end demonstration on synthetic frames
```

Without uv:

```bash
python3 -m venv .venv && . .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install numpy opencv-python-headless pytest
python -m pytest && python examples/demo.py --open
```

The environment works when the tests pass (the review video test is skipped without ffmpeg) and the demo prints a
flicker reduction and `loop ok: True`. Expected output: [`examples/README.md`](examples/README.md).

## 1. Learn the method (10 minutes)

1. Read the [principles](docs/principles.md), at least P1 to P3, P7, P8 and P15.
2. Read the [anti-patterns](docs/quality/anti-patterns.md): the mistakes not to repeat.
3. Read the [collaboration defaults](docs/quality/collaboration.md) and decide which ones you keep.

## 2. Create the project skeleton

```bash
python3 scripts/new_project.py ~/dev/my-project --name "My project"
```

The script creates, **without overwriting anything**:

```
my-project/
  CLAUDE.md                        agent instructions, with the applied method (to complete)
  AGENTS.md                        points other agents to CLAUDE.md
  docs/BRIEF.md                    scoping
  docs/instruction-register.md     durable, active and replaced instructions; requests and their status
  docs/experiments/_template.md    numbered experiment log
  docs/research/_template.md       research note
  docs/work-logs/_template.md      log of a long workstream
  docs/decisions/_template.md      structural decision (ADR)
  docs/DELIVERY_REPORT.md          delivery report
  docs/RETROSPECTIVE.md            retrospective (stays in the project)
  docs/status-update.md            status update template
  archive/_template-README.md      README of an archived version
  .claude/skills/                  work-log, test-first-change, visual-iteration
  .claude/hooks/, .claude/settings.json   guard hooks (--no-hooks to skip)
  tools/                           toolkit (--no-tools to skip it)
  config/  outputs/                parameters; outputs kept apart
  .gitignore                       large outputs excluded
```

Running it again only adds what is missing and lists what it kept. Then run `git init` in the project (recommended:
[P10](docs/principles.md#p10)). If you installed the [plugin](skills/README.md#install), the skills are already
available and you may delete `.claude/skills/`.

## 3. Scope ([scoping](docs/workflow/01-scoping.md))

- Fill in `docs/BRIEF.md`: objective, **key criterion**, references (and what not to reproduce from them), deliverables
  and final conditions, constraints, assumptions, tensions, blocking questions.
- Fill in `docs/instruction-register.md` with the durable constraints.
- Complete `CLAUDE.md`: map, verification commands, final conditions.
- For a study, start from the [feasibility study prompt](templates/prompts/01-feasibility-study.md).

## 4. Translate the method to your domain ([adapting](docs/workflow/adapting.md))

In the "Applied method" section of `CLAUDE.md`, write down:

- the **production unit** and the **final conditions** (where results are judged);
- the **sample** that carries the main risk;
- the **families of checks**, translated (fidelity, locality, overlaps, edges, animation, loop, stability, encoding or
  performance, leftovers);
- the **costs to keep apart**.

## 5. Research, prototype, iterate

- [Targeted research](docs/workflow/02-research.md) → `docs/research/<topic>.md`, with the D/T/H/O legend.
- [Minimal prototype](docs/workflow/03-prototyping.md): one instance of each risky element; a check that can fail for
  each risk; cost per unit measured.
- [Evidence-based iteration](docs/workflow/04-evidence-based-iteration.md): `visual-iteration` skill; numbered log;
  [visual review](docs/quality/checklists/visual-review.md) before each presentation; review page
  (`tools/review_page.py`).
- [Art direction](docs/workflow/05-art-direction.md): contrasting variants with a counter-trial, annotated view,
  preview in motion, written choice.

## 6. Produce, validate, deliver

- [Before production](docs/quality/checklists/pre-production.md): approval, validated excerpt, register reviewed, cost
  measured, resumable pipeline (`tools/fingerprint.py`).
- [Validation](docs/workflow/07-validation.md) on the whole piece, in final conditions (`tools/loop_check.py`,
  `tools/flicker.py`, `tools/review_video.py`).
- [Delivery](docs/quality/checklists/delivery.md): definition of done, `docs/DELIVERY_REPORT.md`.

## 7. Throughout the project

- **Resume**: [checklist](docs/quality/checklists/session-resume.md) at the start of every session.
- **Communicate**: open the results; [short status updates](templates/status-update.md).
- **Lose nothing**: archive before every new version ([template](templates/archived-version-readme.md)).

## 8. At the end: feed the method back

Fill in `docs/RETROSPECTIVE.md` **in the project**, then bring only the generic lessons back to this playbook
([`CONTRIBUTING.md`](CONTRIBUTING.md#after-each-project)).
