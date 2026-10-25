# 0007 — The playbook contains no project work or deliverable

- **Status**: accepted
- **Date**: 2026-10-25
- **Decided by**: the lead

## Context

The playbook must document **how to do the work**, without exposing **the work itself**. It must be possible to read,
share or publish it without revealing any production, deliverable, project data or third-party artwork.

## Decision

The playbook contains only: principles, workflow, quality criteria, good practices, procedures, domain guides, generic
and tested tools, templates, skills, method decisions and improvement actions.

It never contains:

- a deliverable, render, image, video, scene or asset;
- code delivered to a client or integrated into a product;
- a project, client, artwork, author or collaborator name;
- a timeline, figure, measurement or setting specific to a project;
- a quotation from a request or conversation;
- a workstation path, account identifier or secret.

Examples are generic. A lesson that comes from a project is rewritten as a rule independent of that project.

## Consequences

- Project reports ([template](../../templates/retrospective.md)) stay in each project; only what is generic comes here.
- Maturity levels replace source citations: the evidence stays in the project.
- A tool enters only once generalized, without dependency on a project, and tested on synthetic data.

## Verification

- `python3 scripts/check_repo.py` rejects secrets, email addresses, workstation paths and media files.
- A workstation-specific **deny list** (project, artwork and person names), never versioned, can be passed with
  `--deny-list` or placed in `.git/info/deny-list.txt`: the script reads it automatically.
- The pull request and issue templates restate the rule.
