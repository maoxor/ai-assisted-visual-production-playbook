# Web application: test first, layers, guardrails, Git

Practices **[proven]** on web applications (Python API, React interface), when working **as a team** and **with an
agent**, unless stated otherwise.

## Instructions for the agent: a short hierarchy

| Medium | Content | Loading |
|---|---|---|
| Root `CLAUDE.md` | Repository map, verification commands, mandatory rules, guardrails, continuity. **Short** | Every session |
| Sub-folder `CLAUDE.md` | Local conventions (back end, front end), reference implementations | When working in that folder |
| `.claude/rules/*.md` | Targeted rules: migrations, tests, business rules | On demand, by path |
| `.claude/skills/*/SKILL.md` | **Procedures** ([`test-first-change`](../../skills/test-first-change/SKILL.md), [`work-log`](../../skills/work-log/SKILL.md)) | When the task matches |
| `.claude/settings.json` (hooks) | What must happen **every time**, deterministically | Automatic |
| `AGENTS.md` | Points other tools to `CLAUDE.md` | — |
| `docs/` | Architecture, business invariants with their test, decisions, guides, work logs | Linked from `CLAUDE.md` |

**One rule, one source**: the other documents link to it.

## Mandatory rules

1. **Test first** for any behaviour change: write the test, see it fail for the right reason, fix, see it pass.
2. **Access control in the service layer**; someone else's resource returns a 404.
3. **One-way layers** (routes → service → data access → schemas → models), checked by an executable contract
   (import-linter or equivalent).
4. **Immutable migrations** once on the main branch.
5. **The business source of truth wins**: never infer a rule from the code's behaviour without checking it.
6. **Secrets**: never read, display or commit a `.env`; no default value for a secret.
7. **Git**: never work directly on the main branch; `type(scope): description` commits; no push or merge unless asked.
8. **No mass reformatting**: only modified code follows the file's style.
9. **Keep the architecture in place**: do as the surrounding code does; depart from it only if the alternative is
   better **and** the reason is explained before writing the code.

## Procedure: ship a change, test first

Detailed in the [`test-first-change`](../../skills/test-first-change/SKILL.md) skill:

1. **Scope**: expected behaviour in one sentence, edge cases; read the closest reference implementation; stop and ask
   if a rule is ambiguous.
2. **Test first**, depending on the nature of the change:

   | Change | First test |
   |---|---|
   | Bug | A test that reproduces the bug, failing for the right reason |
   | New rule | Unit tests, nominal and edge cases |
   | Data access | Integration test on a real database |
   | New route | Owner OK, other user 404/403, anonymous 401 |
   | Refactoring | Characterization tests, green **before** touching the code |
   | Critical screen | e2e spec (Playwright, fake API) |

3. **Implement** the minimal change, in the right layer; nothing out of scope (note the other problems).
4. **Verify** by running the commands and quoting their results.
5. **Document in the same commit** what the change makes false: invariants, architecture, `CLAUDE.md`, decisions,
   deployment.
6. **Commit** on a dedicated branch: why, evidence (test failing then green), limitations; review the staged diff (no
   unrelated file, no secret).

## Automatic guardrails

- **Claude Code hooks**: immediate check of the modified file (lint, architecture contract); refusal to modify a
  migration already on the main branch; full checks **at the end of each turn and before any `git commit`**; reading
  `.env` files denied by permissions ([Claude Code](../tooling/claude-code.md#hooks)).
- **The hooks are tested themselves**, with simulated inputs, in CI.
- **CI**: lint, architecture, unit and integration tests (real database), e2e in parallel, migration immutability,
  dependency audit, secret detection (gitleaks, false positives justified one by one).
- **A failing check is fixed at the cause**, never by disabling the test or the rule.

<a id="audit-then-counter-audit"></a>

## Audit, then counter-audit [proven]

An audit of a repository by an agent finds real problems, but it also anchors whoever reads it. A second,
**independent counter-audit** run after the fixes finds what the first one missed or introduced.

1. **Run it separately**: another session (or another person), briefed with the repository and the audit's scope, not
   with its conclusions.
2. **Look for four things**: regressions introduced by the audit's fixes; fixes that treat a symptom instead of the
   cause; problems the audit missed; guardrails for agents (hooks, permissions, instructions) that do not actually
   work.
3. **Check concurrency explicitly**: read-then-write sequences (quotas, counters, limited codes, state transitions)
   fail under simultaneous requests and are rarely found by reading code; reproduce them with parallel requests in a
   test.
4. **Reproduce every finding with a test first**, then fix it at the cause; rank findings by priority and record the
   evidence (test, command) next to each one.
5. **Test the guardrails themselves**: a hook that silently stopped working looks exactly like a hook that never
   fires; mutation tests in CI catch it.

## Git as a traceability tool

- **Commit types**: `fix`, `feat`, `docs`, `chore`, `refactor`, `style`, `test`, `perf`, `ci`; explicit merges.
- **Typical message body**: problem, measurement before, changes, measurement after, evidence from tests, link to the
  workstream's log.
- **One branch per workstream** (`type/short-topic`), the workstream's log versioned in `docs/` (the
  [`work-log`](../../skills/work-log/SKILL.md) skill).
- **Structural decisions** in ADR format ([template](../../templates/decision-record.md)); an accepted decision is
  challenged only by a new decision that replaces it.
- **Git identity**: the one configured on the workstation, never an identity copied from existing commits.

## Art direction of an interface

- The lead judges on the rendered result and the experience, at the level of the best websites and games of the
  domain, never on the number of screens or on technical checks.
- Prototype **in motion** and record it before concluding; share galleries privately.
- Develop only **after explicit approval** of a direction.
- Design an animation choreography (arrival, entrances, hovers, slow motion to judge it), not generic fades.
- Measure performance without waiting to be asked (profiling, Lighthouse, frames per second, comparison with the
  existing version).
- Say what is not tested: iOS simulators and Android emulators are not real devices; Playwright does not reproduce
  every audio activation rule.
