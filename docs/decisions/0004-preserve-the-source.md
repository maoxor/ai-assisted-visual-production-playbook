# 0004 — Preserve the source artwork; AI estimates, it does not regenerate

- **Status**: accepted
- **Date**: 2026-10-25
- **Decided by**: the lead

## Context

A project may start from an existing artwork (illustration, photograph, third-party render). Regenerating it with AI
betrays its identity, its details and often its author's rights.

## Decision

- When a source artwork exists, it is reproduced as is in the rest state, and fidelity is checked.
- AI is used to **estimate** (segmentation, depth) and possibly to **rebuild limited hidden areas**, under visual
  control. It never replaces the subject.
- Models run locally, with their revision and licence recorded.

## Consequences

- Animations are built by controlled deformation (projected layers, anchored fields), with amplitudes limited to what
  the view supports ([2.5D animation](../domains/2-5d-animation.md)).
- Fidelity becomes a systematic check: the rest state is compared with the source.

## Verification

Fidelity check in the [pre-production checklist](../quality/checklists/pre-production.md).
