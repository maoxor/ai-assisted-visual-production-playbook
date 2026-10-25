# 6. Production: produce the whole reliably

**Objective.** Produce the complete piece with justified settings, in a time that still allows iteration, through a
pipeline that survives interruptions and never mixes versions.

## Prerequisites [proven]

- The identified defects are fixed: hours of computation are not relaunched while they persist.
- Explicit approval to launch has been given, if the lead reserved that decision ([P12](../principles.md#p12)).
- The validation excerpt has been approved, unless explicitly instructed otherwise.
- The [pre-production checklist](../quality/checklists/pre-production.md) has been passed.

<a id="cost-profile"></a>

## Cost profile [proven]

1. **Measure a few representative units, including a difficult one**, separating start-up (loading, compilation,
   preparation) from steady state.
2. **Check real hardware usage**: accelerator actually used, no silent fallback to the CPU, peak memory.
3. **Attribute the cost to elements** with isolated tests, removing one element at a time.
4. **Compare a few consistent profiles** on the same units, in a short table:

   | Profile | Time per unit | Factor | Similarity (SSIM, ꟻLIP) | Sharpness per area | Visual opinion |
   |---|---|---|---|---|---|

5. **Also explore method changes**, not only settings: replace secondary geometry with a texture, remove details
   invisible at final size, split the work between computation and post-processing.
6. **Never freeze** what has to evolve (a reflection, a refraction, dynamic data) and **never replace** computation
   with an unverified interpolation.
7. **Estimate and announce** the total time for the excerpt and for the whole, with its assumptions.

<a id="fingerprint-and-resume"></a>

## Fingerprint and resume [proven]

The [`fingerprint.py`](../../tools/README.md#fingerprintpy) tool implements these rules:

- **Fingerprint**: SHA-256 of everything that determines the result (sources, configurations, layers, computation and
  post-processing scripts, software version, quality profile), written to `VERSION.json` next to the outputs.
- **Safe resume**: if the fingerprint no longer matches, the existing outputs come from another state; they are
  **moved** to `_stale/<date>/`, never deleted, and production starts again from scratch.
- **Finished unit = complete file**: a PNG counts only if its final chunk (IEND) is present.
- **In batches**: one process per batch of N units; an interruption loses at most one batch, and memory is released.
- **Post-processing as you go**: each finished batch is immediately reduced to final size.
- **Disk space checked before every batch.**
- **Timing log**: one line per unit (CSV).
- **Change nothing during the computation**: any change to a dependency changes the fingerprint and stops production at
  the next batch. That is intended.

## Machine and environment [proven]

- **Sleep**: on a laptop, sleep stops the computation. On macOS, `caffeinate -i -s` only works on mains power; on
  battery with the lid closed, the machine sleeps anyway. Launch production from a script that waits for mains power
  (`pmset -g batt`), then runs under `caffeinate` ([A15](../quality/anti-patterns.md#a15)).
- **Shared machine**: never kill processes of another project or session; route heavy computations through a common
  lock ([shared machine](../tooling/README.md#shared-machine)).
- **Orphan processes**: a killed script can leave a child process (render engine, browser) behind; check after every
  stop.
- **Detach and monitor**: launch with `nohup … &` and a log; show the first units without waiting for the end.

## End-of-production chain [proven]

A single script chains every step, each one timestamped in the log:

1. computation of each format;
2. post-processing (stabilization, downscaling), as a closed loop if the piece loops;
3. whole-piece checks;
4. distribution exports;
5. playback or integration tests;
6. review page.

A launched computation is only the first step of delivery ([P3](../principles.md#p3)).

## Exit criterion

The complete piece exists in every format, under a single consistent fingerprint; real timings are recorded; the next
steps (validation, exports) are chained.
