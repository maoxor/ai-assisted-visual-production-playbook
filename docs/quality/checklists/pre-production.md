# Before a long production

## Decision

- [ ] Explicit approval to launch, if the lead reserved that decision.
- [ ] Validation excerpt (shape of the final deliverable, delivery settings) approved, unless explicitly instructed
      otherwise.
- [ ] Instruction register reviewed: **every** requested fix is done ([A2](../anti-patterns.md#a2)).
- [ ] Identified defects fixed; no "we'll see later".

## Content (adapt to the domain)

- [ ] Subject fidelity on the reference state.
- [ ] Protected areas respected over the whole duration (face, interface, text).
- [ ] Generated geometry valid: orientation, closure, self-intersections ([A13](../anti-patterns.md#a13)).
- [ ] Edges and margins at extreme positions.
- [ ] Loop: exact match of the state at the complete period (position and velocity), no duplicated unit.
- [ ] Representative units at final quality, including extreme poses and angles.
- [ ] Rest of the composition unchanged after the last fix (element-by-element comparison).
- [ ] Leftovers absent from the pipeline: signature, logo, text, trial setting.

## Cost and pipeline

- [ ] Cost per unit measured on an idle machine, first unit separated from the steady state
      ([A16](../anti-patterns.md#a16)).
- [ ] Total estimate announced, with its assumptions.
- [ ] Resumable pipeline: fingerprint of dependencies, finished unit = complete file, batches, stale outputs moved
      ([`fingerprint.py`](../../../tools/README.md#fingerprintpy)).
- [ ] Configuration and sources archived before launch.
- [ ] Enough disk space; mains power; sleep prevented ([A15](../anti-patterns.md#a15)).
- [ ] Next steps chained: post-processing, checks, exports, tests.
- [ ] Rule stated: **change nothing** in the dependencies during the computation.
