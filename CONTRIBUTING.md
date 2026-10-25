# Contributing

Thank you for helping. This playbook grows through **small, generic additions**, not rewrites. Git and GitHub record
when and why each rule changed. By contributing, you agree that your contribution is released under the
[MIT license](LICENSE) and that you follow the [code of conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

| You have… | Do this |
|---|---|
| A lesson from a project (a mistake fixed, a practice that worked) | Open a **Lesson learned** issue, in generic form |
| A proposal to change a principle, step, checklist, tool or template | Open a **Method change** issue, then a pull request |
| Found a gap (an untested practice, a missing check) | Open a **Gap** issue; it may become a line in [`ROADMAP.md`](ROADMAP.md) |
| A bug in a tool or script | Open an issue with the command, the input description and the output |
| A new tool | Read [Adding a tool](tools/README.md#adding-a-tool), then open a pull request |

## Writing rules

1. **No project content** ([decision 0007](docs/decisions/0007-no-project-content.md)): no deliverable, asset, project,
   client, artwork or person name, and no figure, setting, timeline or quotation specific to a project. A lesson is
   rewritten as a rule that stands on its own.
2. **Every practice carries a maturity level**: **[proven]**, **[extrapolated]** or **[proposed]**. `scripts/check_repo.py`
   checks that the documents that need one have one.
3. **Invent nothing**: a practice that was never applied is [proposed], never [proven].
4. **Method, not aesthetics** ([decision 0002](docs/decisions/0002-method-separate-from-aesthetics.md)): no style is
   prescribed.
5. **One rule, one source**: other documents link to it.
6. **English** for documentation, file names, identifiers, options, branches and labels.
7. **No secret and no personal data**: no token, email address or workstation path.
8. **Relative links** and stable anchors (`<a id="…">`) for sections cited elsewhere.

<a id="after-each-project"></a>

## After each project

1. **Retrospective in the project**: fill in `docs/RETROSPECTIVE.md` ([template](templates/retrospective.md)). It does
   not come here.
2. **Anti-patterns**: each corrected mistake becomes a generic entry in
   [`anti-patterns.md`](docs/quality/anti-patterns.md) (symptom, cost, prevention).
3. **Principles, workflow, guides**: clarify or correct; an [extrapolated] or [proposed] practice applied successfully
   becomes [proven].
4. **Tools**: a script useful to a second project is generalized into [`tools/`](tools/README.md), **with tests on
   synthetic data**.
5. **Defaults**: a lead preference confirmed from one project to the next can go into
   [`collaboration.md`](docs/quality/collaboration.md).
6. **Method decision** if a structural choice changes ([decisions](docs/decisions/README.md)).
7. **Version**: [`CHANGELOG.md`](CHANGELOG.md), then a Git tag.
8. **Confidentiality review**: `python3 scripts/check_repo.py`, with your own deny list (see below).

## Development setup

```bash
git clone https://github.com/maoxor/ai-assisted-visual-production-playbook.git
cd ai-assisted-visual-production-playbook
uv run pytest                    # or: python -m pip install numpy opencv-python-headless pytest && python -m pytest
uv run ruff check .              # lint (configuration in pyproject.toml)
python3 scripts/check_repo.py
```

Optional, for the plugin manifests: `claude plugin validate .`

## Pull requests

- **One branch per contribution**: `docs/<topic>`, `tools/<topic>`, `ci/<topic>`, `fix/<topic>`.
- **Commits** follow `type(scope): description`. Types: `docs`, `feat` (tool, template, skill), `fix`, `test`, `ci`,
  `chore`, `refactor`. Scopes: `principles`, `workflow`, `quality`, `domains`, `tooling`, `decisions`, `templates`,
  `skills`, `hooks`, `tools`, `scripts`, `examples`, `plugin`.
- **Commit body**: why, what changes for a future project, evidence (tests, checks).
- Fill in the pull request template. CI must be green; `main` accepts changes only through pull requests whose checks
  pass.
- **Issue labels**: `lesson-learned`, `method-change`, `gap`.

<a id="versioning"></a>

## Versioning

Inspired by semantic versioning, applied to the method:

- **major**: a principle added, removed or changed in meaning, a decision replaced, or a breaking change in a tool's
  command line;
- **minor**: a step, guide, tool, template or skill added;
- **patch**: clarification, correction, link.

The version appears in `CHANGELOG.md`, `pyproject.toml` and `.claude-plugin/plugin.json`; each release has a
`vX.Y.Z` tag.

## Checking before you propose

```bash
python3 scripts/check_repo.py                                  # links, anchors, maturity, structure, confidentiality
python3 scripts/check_repo.py --deny-list ~/path/terms.txt     # plus your own forbidden terms
uv run pytest
```

Without the option, `check_repo.py` also reads `.git/info/deny-list.txt` if it exists: a local file, never versioned,
one term per line (`#` starts a comment). Put there the names of your projects, clients and colleagues so that they
can never slip into a contribution.

To run these checks automatically before every commit, enable the repository's Git hook once per clone:

```bash
git config core.hooksPath scripts/git-hooks      # runs scripts/check_repo.py, with your deny list, on each commit
```

CI ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)) runs the same checks, without any deny list, on every push
and pull request.
