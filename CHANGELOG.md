# Changelog

Format: [versioning](CONTRIBUTING.md#versioning). Each release has a `vX.Y.Z` Git tag.

## v2.0.0 — 2026-10-25

Open-source release ([decision 0008](docs/decisions/0008-open-source-release.md)).

- **Renamed** to `ai-assisted-visual-production-playbook`, a name that states who (AI-assisted), what (visual
  production) and the form (playbook).
- **English** throughout: documentation, templates, prompts, skills, scripts. Maturity levels are now [proven],
  [extrapolated] and [proposed]; the "lead" designates the person who directs the work.
- **Licence**: MIT; templates and skills also under MIT No Attribution. Added `CODE_OF_CONDUCT.md` and `SECURITY.md`.
- **Reproducible installation**: `pyproject.toml` and `uv.lock`; documented requirements and checks in
  `GETTING_STARTED.md`.
- **End-to-end demonstration**: `examples/demo.py` runs every tool on a synthetic loop and builds a review page.
- **Claude Code plugin**: `.claude-plugin/plugin.json` and `marketplace.json`; the skills install with
  `/plugin install visual-production@visual-production-playbook`.
- **Tools**:
  - `review_video.py` no longer depends on ffmpeg's glob pattern: frames are staged under sequential names, so it works
    on Windows and with any file name; odd heights are rejected with a clear message; new `--crf` option.
  - `stabilize.py` now accepts grey frames (it failed on them) and keeps the alpha channel of BGRA frames.
  - `flicker.py` maps make sparse flicker visible (any flickering pixel is drawn at level 80 or more).
  - `review_page.py` defaults to English (`"lang"` in the plan) and opens pages on Windows too.
  - Every option has a help text.
- **Tests** moved to `tests/` and extended: scaffolder, repository checks, demonstration, grey and BGRA frames, file
  names with spaces; CI runs on Linux (Python 3.10 to 3.13), macOS and Windows.
- **Repository checks**: English maturity markers, required files, skill front matter, consistent versions across
  `CHANGELOG.md`, `pyproject.toml` and the plugin manifests; ignored output folders skipped.
- **Documentation**: new `docs/README.md` (map and relations), complete tool reference, decision 0008, collaboration
  defaults presented as replaceable defaults.

## v1.0.0 — 2026-10-25

First version (documentation in French at the time).

- Sixteen project-independent quality principles.
- Ten-step workflow, from scoping to communication, and a guide to adapt it to other domains.
- Definition of done, evaluation grid, twenty anti-patterns, collaboration preferences, five checklists.
- Domain guides: offline 3D rendering, 2.5D animation, web background video, web applications, AI models and
  third-party resources.
- Tooling: inventory, provenance and licensing, shared machine, Claude Code configuration.
- Seven method decisions, including the absence of any project content (0007).
- Document templates and eleven prompt templates.
- Skills: `work-log`, `test-first-change`, `visual-iteration`.
- Tested tools: `flicker.py`, `loop_check.py`, `stabilize.py`, `fingerprint.py`, `review_page.py`, `review_video.py`.
- Scripts: `check_repo.py` (links, anchors, maturity, structure, confidentiality, local deny list) and
  `new_project.py`.
