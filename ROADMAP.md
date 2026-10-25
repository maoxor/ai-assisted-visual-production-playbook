# Roadmap

What remains to strengthen the method. Each completed action is removed by a commit that says how, and the maturity
level concerned is updated. Each line has a matching **Gap** issue or can become one.

## Prove what is proposed or extrapolated

These actions need real projects or hardware: they cannot be completed by writing documents or simulated tests.

| Action | Why | Done when | Issue |
|---|---|---|---|
| Apply the method to a **motion design**, **game or real-time**, or **document** project | These columns of the [adaptation guide](docs/workflow/adapting.md) are [extrapolated] | One column becomes [proven], with the adjustments reported | [#1](https://github.com/maoxor/ai-assisted-visual-production-playbook/issues/1) |
| Use [`new_project.py`](scripts/new_project.py), the [`visual-iteration`](skills/visual-iteration/SKILL.md) skill and the "Applied method" section of the [`CLAUDE.md` template](templates/project-claude-md.md) on a real project | Tested in temporary folders and CI only; [proposed] | Skeleton, skill and template adjusted from real use; maturity [proven] | [#2](https://github.com/maoxor/ai-assisted-visual-production-playbook/issues/2) |
| Use the [rendering-project hooks](hooks/README.md) in a real production | Tested with simulated events only; [proposed] | Hooks adjusted from real use; maturity [proven] | [#3](https://github.com/maoxor/ai-assisted-visual-production-playbook/issues/3) |
| Apply the [physical device procedure](docs/domains/web-background-video.md#physical-devices), including Apple colour compensation on iPhone and iPad | Playback and colour were only checked in emulation and on macOS; [proposed] | First results recorded; procedure adjusted; maturity [proven] | [#4](https://github.com/maoxor/ai-assisted-visual-production-playbook/issues/4) |
| Apply the [time and budget](templates/project-brief.md) table and the [multi-person roles](docs/quality/collaboration.md#several-people) | Written from experience but [proposed] | Used in a project; adjusted; maturity [proven] | — |

## New tools

| Action | Why | Done when |
|---|---|---|
| Generalize a **video playback test bench** (Playwright: dropped frames, seams, rotation, emulation) into `tools/` | The bench is rebuilt for each project | Generic tool tested on a synthetic page in CI |
| Generalize a **named-modification test bench** for Blender (copies of the reference scene, crops, labelled contact sheets) | The principle is described in the [rendering guide](docs/domains/offline-3d-rendering.md), not tooled | Generic tool tested on a synthetic scene |

Contributions are welcome on any line: see [`CONTRIBUTING.md`](CONTRIBUTING.md).
