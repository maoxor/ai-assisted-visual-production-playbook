---
name: work-log
description: Open, resume or close a long task (several steps or sessions) with its log in docs/work-logs/. Use at the start of a multi-step task, when resuming after an interruption or a context compaction, and at the end of the work.
---

# Long task and reliable resume

A workstream is a branch (if there is a Git repository) and a log `docs/work-logs/YYYY-MM-DD-topic.md` (template:
`docs/work-logs/_template.md`, or `templates/work-log.md` of the ai-assisted-visual-production-playbook repository if
the project has none). The log, `git log` and the instruction register (`docs/instruction-register.md`) must be enough
to resume without the conversation history.

## Resume (always first)

1. Real state: `git status`, `git branch --show-current`, `git log --oneline -15`; active processes (computations,
   servers); disk space. Never touch other projects' processes.
2. Read the workstream's log (the most recent in `docs/work-logs/`, or the branch's) and the instruction register.
3. Check the real state before continuing: rerun the checks in the log's "Validation" section; a box ticked without
   evidence has to be verified again.
4. Resume at "Next actions". If the log contradicts the files, the files win: correct the log.

## Open

1. A dedicated branch from the main branch (`type/short-topic`); archive the current state if the project has no Git.
2. Copy the template; fill in objective, key criterion, scope, initial baseline (measured results of the checks before
   any change).
3. Split the plan into verifiable steps, each with its exit criterion.
4. Report the request's instructions in the register (active, replaced).

## Keep it up to date (at each completed step, before each commit)

- Status, decisions taken (and why), commits, checks run with their results, next actions.
- Separate **verified** (command run, result quoted), **hypothesis** and **to do**; separate my checks from the
  user's approval.
- Stay concise: details live in the files, the tests and the commit messages.

## Close

- Status "done"; report: delivered, verified (real or emulated), limitations; every request with its status.
- Move what must last elsewhere (decisions, `CLAUDE.md`, and the generic lessons in the method playbook): the log is a
  trace, not a source of rules.
