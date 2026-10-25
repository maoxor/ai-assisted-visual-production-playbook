## What and why

<!-- What changes in the method or the tools, and why, in generic form. -->

## Scope

- [ ] patch · [ ] minor · [ ] major (new decision in `docs/decisions/`, or a breaking change in a tool's command line)

## Checks

- [ ] No project content: no deliverable, name, figure or quotation (decision 0007)
- [ ] Every new practice carries a level: [proven], [extrapolated] or [proposed]
- [ ] Method, not aesthetic choice
- [ ] English names and documentation
- [ ] `python3 scripts/check_repo.py`: 0 errors (with your local deny list)
- [ ] `uv run pytest` and `uv run ruff check .` green; a changed tool comes with a test on synthetic data and an updated `tools/README.md`
- [ ] `CHANGELOG.md` updated; version consistent in `pyproject.toml` and `.claude-plugin/`
