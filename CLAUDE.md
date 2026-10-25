# AI-assisted visual production playbook

A generic method and toolkit: principles, workflow, quality, domain guides, templates, skills, Python tools. It
contains no project. Everything is written in English.

<!-- Loaded in every session: keep it short. -->

## Map

| Path | Content |
|---|---|
| `docs/` | The method (principles, workflow, quality, domains, tooling, decisions) |
| `templates/`, `skills/`, `hooks/` | Copied into projects by `scripts/new_project.py`; `skills/` is also the plugin's skill folder |
| `tools/` | Standalone Python CLIs, copied into projects; tests in `tests/` |
| `examples/demo.py` | End-to-end demonstration on synthetic frames |
| `scripts/` | `check_repo.py` (repository checks), `new_project.py` (scaffolder) |
| `.claude-plugin/` | Plugin and marketplace manifests |

## Verify (before concluding a task)

```bash
python3 scripts/check_repo.py
uv run pytest
uv run ruff check .
claude plugin validate .        # when the manifests or skills change
```

Never call something verified without running these commands; quote their results.

## Rules

- Read [`CONTRIBUTING.md`](CONTRIBUTING.md). Every practice carries a level: **[proven]**, **[extrapolated]** or
  **[proposed]**; never present as proven what is not.
- **No project content** ([decision 0007](docs/decisions/0007-no-project-content.md)): no deliverable, name, figure or
  quotation; rewrite as a generic rule.
- Method, not aesthetics: no style is prescribed.
- No secret, asset or personal data.
- Tools stay standalone scripts (no cross-project paths); a change to a tool comes with a test on synthetic data and an
  update of `tools/README.md`.
- Keep the version consistent in `CHANGELOG.md`, `pyproject.toml` and `.claude-plugin/plugin.json`.
- Git: dedicated branch, `type(scope): description` commits, no push or merge unless asked.
