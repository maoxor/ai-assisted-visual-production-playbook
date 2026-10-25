# Changelog

Format: [versioning](CONTRIBUTING.md#versioning). Each release has a `vX.Y.Z` Git tag.

## v2.2.1 — 2026-10-25

- `check_repo.py` also checks the author and committer address of every commit in the history (GitHub noreply
  addresses only); CI checks out the full history for it. Three merge commits had been created with a personal
  address; they were rewritten with the noreply address (content unchanged) and the v2.1.0 and v2.2.0 tags and
  releases recreated on the rewritten commits.

## v2.2.0 — 2026-10-25

- **Real-time 3D for the web** guide, [proven]: references and feature inventory before generation, detail budget from
  the closest framing, measure without rendering to iterate and render to prove, shared toolkit copied with checksums,
  construction by shape, motion, swing and atlas checks.
- The **real-time web 3D** column of the adaptation guide becomes [proven]; games remain [extrapolated].
- Anti-patterns **A21** (every check passes on a rudimentary result) and **A22** (a measurement reported without a
  threshold).
- P1: a threshold is never moved to let a candidate pass; a suspected instrument is tested on a known case.
- Evidence-based iteration, rule 8: a review note describes the final capture, not the generator's intent.

## v2.1.0 — 2026-10-25

- **Hooks for rendering projects** ([`hooks/`](hooks/README.md)), [proposed]: `guard_archive.py` (archives
  read-only), `guard_production.py` (dependencies of a running production frozen), `guard_large_files.py` (no media or
  large files committed, including files staged by the same command line). Installed by `new_project.py`
  (`--no-hooks` to skip); 15 tests with simulated events. The process check never sends a signal on Windows.
- **`fingerprint.py run`** and `fingerprint.running()`: mark a production as in progress (`RUNNING` file) for the
  hooks.
- **Physical device test procedure** for web video, [proposed], with a checklist line.
- **Scoping**: time and budget estimation (brief table, step 8 of scoping), [proposed].
- **Collaboration**: roles when several people are involved, [proposed].
- **Web applications**: "Audit, then counter-audit" [proven]: an independent counter-audit after an audit's fixes,
  concurrency checked explicitly, every finding reproduced by a test first.
- **Repository**: pre-commit Git hook (`scripts/git-hooks/`), ruff lint in CI, Dependabot (Actions and uv), CODEOWNERS,
  `CITATION.cff`, `.editorconfig`, bug report template; `main` protected by required checks.
- **Roadmap** rewritten: what remains needs real projects, hardware or new tools.

## v2.0.1 — 2026-10-25

- The repository is public; private vulnerability reporting is enabled.
- Plugin installation from GitHub verified (`/plugin marketplace add`, then `/plugin install`); the roadmap item is
  closed.
- Decision 0008 records the publication.

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
