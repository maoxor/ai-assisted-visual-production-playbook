# 0003 — Research and work done by the agent itself, without sub-agents (default)

- **Status**: accepted
- **Date**: 2026-10-25
- **Decided by**: the lead

## Context

The lead wants to keep control and traceability of what is read and concluded, and to avoid second-hand syntheses
produced by delegated agents.

## Decision

- By default, the agent does research, reading and trials itself. It runs tool calls in parallel (several searches in
  the same turn) rather than delegating.
- Skills that coordinate sub-agents are not used, unless explicitly requested.
- This is a **default**: a team that prefers delegation records the opposite instruction in its project's instruction
  register.

## Consequences

- Research is more sequential; this is compensated by parallel queries and by stopping as soon as a trial is possible
  ([P5](../principles.md#p5)).
- An explicit, newer request can lift the rule ([P15](../principles.md#p15)).

## Verification

No automatic check. The rule appears in the global instructions snippet
([collaboration defaults](../quality/collaboration.md)) and in the
[`CLAUDE.md` template](../../templates/project-claude-md.md).
