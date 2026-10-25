# 0005 — Judgement in final conditions comes first; measurements complement it

- **Status**: accepted
- **Date**: 2026-10-25
- **Decided by**: the lead

## Context

Measurements taken as evidence have led to bad decisions several times: a motion that was measurable but invisible, a
visibility percentage that said nothing about credibility, a recommendation of restraint contrary to the lead's taste.

## Decision

- Every evaluation happens first in final conditions: display size, normal speed, final processing, whole piece,
  forward playback, latest version ([P8](../principles.md#p8)).
- Every measurement comes with a capture or a video; it serves diagnosis, non-regression and the comparison of
  profiles.
- No threshold is a target. The lead's judgement wins over the agent's measurements.

## Consequences

- The measurement tools ([`flicker.py`](../../tools/README.md#flickerpy), [`loop_check.py`](../../tools/README.md#loop_checkpy))
  also produce maps and are used together with review videos.
- Reports present what is seen first, then what the measurement confirms.

## Verification

[Visual review checklist](../quality/checklists/visual-review.md): the render in final conditions accompanies every
measurement.
