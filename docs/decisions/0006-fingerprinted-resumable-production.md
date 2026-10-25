# 0006 — Every long production is resumable and protected by a fingerprint

- **Status**: accepted
- **Date**: 2026-10-25
- **Decided by**: the lead (requirement), the agent (implementation)

## Context

Long productions are often interrupted (version change, late fix, sleep, shared machine). Resuming on the mere presence
of files mixes units computed from different states, which produces wrong deliverables that are hard to detect.

## Decision

- Every production writes the fingerprint of its dependencies (sources, configurations, scripts, software version,
  quality profile) next to its outputs.
- On resume, if the fingerprint differs, the existing outputs are **moved** to `_stale/`, never deleted.
- A unit is done only if its file is complete; units are produced in batches; disk space is checked before every
  batch.
- No dependency is modified during the computation.

## Consequences

- Any change to a dependency during a production stops it at the next batch: that is intended.
- Power supply and sleep settings are part of the prerequisites ([A15](../quality/anti-patterns.md#a15)).

## Verification

Tested tool: [`fingerprint.py`](../../tools/README.md#fingerprintpy) (tests `test_ensure_*` and `test_pending_*`).
