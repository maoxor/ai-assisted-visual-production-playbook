---
name: test-first-change
description: Ship a fix, a feature or a refactoring of application code: scoping, test first, implementation, quoted checks, documentation, commit. Use before modifying application code.
---

# Ship a change, test first

A short, local change: follow these steps directly. Several steps or sessions: also open a log (the `work-log` skill).

## 1. Scope

- State the expected behaviour in one sentence, with its edge cases.
- Locate the code (`docs/architecture.md` if it exists, then a targeted search) and read the closest reference
  implementation; follow its conventions.
- If a business rule is ambiguous or contradicts the code: stop and ask, do not invent.

## 2. Test first

| Change | First test to write |
|---|---|
| Bug | A test that reproduces the bug; run it, see it fail **for the right reason** |
| New rule or formula | Unit tests of the nominal and edge cases |
| Data access, query, transaction | Integration test on a real database |
| New route | Owner OK, other user 404/403, anonymous 401 |
| Refactoring | Characterization tests of the current behaviour, green BEFORE touching the code |
| Critical screen or journey | e2e spec (fake API) |

## 3. Implement

- The minimal change that makes the test pass, in the right layer; no magic number; access control in the service.
- Then refactor if useful, tests still green. Nothing outside the requested scope: note other problems in the log or
  report them.

## 4. Verify (and quote the results)

The verification commands of the project's `CLAUDE.md`, at least for the part touched. A failing check is fixed at the
cause: never disable a rule or a test.

## 5. Document

Update in the same commit what the change makes false or incomplete: invariants, architecture, `CLAUDE.md`, decisions
(`docs/decisions/`), deployment.

## 6. Commit

- On a dedicated branch, never on the main branch; no push or merge unless asked.
- Message `type(scope): description` (`fix`, `feat`, `refactor`, `test`, `docs`, `chore`, `ci`, `perf`); a body that
  explains the why, the before/after measurement, the evidence (test failing then green) and the limitations.
- `git diff --staged` reviewed: no unrelated file, no secret, no debug file. Git identity: the one configured on the
  workstation.
