# 0001 — A single, versioned method repository, separate from projects

- **Status**: accepted
- **Date**: 2026-10-25
- **Decided by**: the lead

## Context

The method lived in three scattered places: the lead's requests (long and often repeated), the agent's memories
(specific to each project folder) and each project's logs. Nothing made it possible to pass it on to a new project
without rereading hundreds of pages.

## Decision

- A dedicated repository holds the principles, the workflow, the quality criteria, the domain guides, the tested tools,
  the templates, the skills and the method decisions.
- Every practice carries a maturity level: **[proven]**, **[extrapolated]** or **[proposed]**.
- Projects stay in their own repositories; the playbook receives only their generic lessons
  ([decision 0007](0007-no-project-content.md)).
- The method is versioned in the spirit of semantic versioning ([`CONTRIBUTING.md`](../../CONTRIBUTING.md#versioning)).

## Consequences

- After each project, the generic lessons are brought back here; the detailed report stays in the project.
- The agent's cross-project memories are copied here; project-specific memories stay in the project.
- The repository checks itself: links, anchors, maturity levels, absence of secrets, tool tests.

## Verification

`python3 scripts/check_repo.py` and CI (`.github/workflows/ci.yml`).
