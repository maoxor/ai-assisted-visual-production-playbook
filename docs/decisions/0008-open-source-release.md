# 0008 — Open-source release: explicit name, English, MIT licence, plugin

- **Status**: accepted
- **Date**: 2026-10-25
- **Decided by**: the lead (objective: an open-source project useful to as many people as possible, with an explicit
  name and English names); the agent (name, language of the documentation, licence and packaging, as reversible
  decisions delegated by the lead)

## Context

The playbook was written for its authors: a generic name, documentation in one non-English language, no licence, no
reproducible installation, tools usable only by copying files. An outsider could read it but could hardly understand
its purpose at a glance, install it, verify it or reuse it.

## Options considered

| Option | Advantages | Drawbacks |
|---|---|---|
| Keep the generic name | No change | Says nothing about the domain or the agent |
| `ai-assisted-visual-production-playbook` | States who (AI-assisted), what (visual production) and the form (playbook) | Long |
| Documentation in two languages | Wider reach | Double maintenance, divergence |
| Documentation in English only | Reach; a single source per rule | The authors' working language is not English |

## Decision

- **Name**: `ai-assisted-visual-production-playbook`; the Claude Code plugin is `visual-production`, published by the
  `visual-production-playbook` marketplace.
- **Language**: English for documentation, code, file names, identifiers, branches and labels. Projects keep their own
  working language (C1 of the [collaboration defaults](../quality/collaboration.md)).
- **Licence**: MIT for the whole repository; the content of `templates/` and `skills/` may additionally be copied into
  projects without attribution (MIT No Attribution).
- **Reproducibility**: `pyproject.toml` and `uv.lock` pin the tools' dependencies; CI runs on Linux, macOS and
  Windows; `examples/demo.py` reproduces every tool's behaviour on synthetic data.
- **Packaging**: the skills are also distributed as a Claude Code plugin (`.claude-plugin/`).
- **Publication itself** (switching the repository to public) remains an explicit decision of the lead
  ([P12](../principles.md#p12)).

## Consequences

- The version is kept consistent in `CHANGELOG.md`, `pyproject.toml` and `.claude-plugin/plugin.json`.
- Maturity levels become [proven], [extrapolated], [proposed]; `check_repo.py` checks the English markers.
- Contributions are accepted under the MIT licence ([`CONTRIBUTING.md`](../../CONTRIBUTING.md)).

## Verification

CI ([`.github/workflows/ci.yml`](../../.github/workflows/ci.yml)): repository checks, tests on three operating systems,
demo, project creation, plugin manifest validation.
