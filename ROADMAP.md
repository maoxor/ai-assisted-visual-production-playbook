# Roadmap

Actions planned to strengthen the method. Each completed action is removed by a commit that says how, and the maturity
level concerned is updated. Larger items are tracked as **Gap** issues.

## Prove what is proposed or extrapolated

| Action | Why | Done when |
|---|---|---|
| Apply the method to a **motion design**, **game or real-time**, or **document** project | These columns of the [adaptation guide](docs/workflow/adapting.md) are [extrapolated] | One column becomes [proven], with the adjustments reported |
| Use the [`visual-iteration`](skills/visual-iteration/SKILL.md) skill on real visual work | Written from proven practices, never used as is | Skill corrected from use; maturity [proven] |
| Create a real project with [`new_project.py`](scripts/new_project.py) | Tested only in temporary folders and CI | Skeleton adjusted from real use |
| Use the "Applied method" section of the [`CLAUDE.md` template](templates/project-claude-md.md) from the first session | [proposed] | Observed effect on repeated instructions |

## Fill gaps

| Action | Why | Done when |
|---|---|---|
| Write and test **hooks for rendering projects** (read-only archives, dependencies of a running production, large files) | Described in [Claude Code](docs/tooling/claude-code.md#hooks), never written | Hooks shipped with tests in CI |
| Define a **test procedure on physical devices** (phones, tablets) | Video playback tests were only run in emulation | Procedure added to the [web video guide](docs/domains/web-background-video.md) and its checklist |
| Check **Apple colour compensation** on real iPhones and iPads | Observed on macOS only | Result recorded in the web video guide |
| Generalize a **video playback test bench** (Playwright) into `tools/` | The bench is rebuilt for each project | Generic tool, tested |
| Generalize a **named-modification test bench** for Blender | The principle is described, not tooled | Generic tool tested on a synthetic scene |
| Document **human time and budget** in scoping | The method has no estimation guidance | Section added to the [brief](templates/project-brief.md) |
| Describe **multi-person roles** (collaborators, reviewers) | The method describes a lead/agent pair | Section added to the collaboration defaults |

## Repository tooling

| Action | Why | Done when |
|---|---|---|
| Add a local **pre-commit hook** running `check_repo.py` with the deny list | CI does not know local deny lists | Hook documented in `CONTRIBUTING.md` |
| Test the **plugin installation** from the public repository | Manifests are validated locally (`claude plugin validate`); installation from GitHub requires a public repository | Installation verified and documented |
