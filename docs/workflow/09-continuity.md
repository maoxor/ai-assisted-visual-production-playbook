# 9. Continuity: resume without the conversation

**Objective.** Allow anyone to resume the work exactly where it stands without rereading the conversation: another
session, another person, or yourself after an interruption or a context compaction.

## What carries continuity

| Medium | Content | Maturity |
|---|---|---|
| **Experiment log** | Numbered entries: trial, finding, kept or rejected, reason; grouped by iteration with the request that triggered it ([template](../../templates/experiment-log.md)) | [proven] |
| **Work log** | Status, decisions, checks run, next actions, open questions ([template](../../templates/work-log.md), [`work-log`](../../skills/work-log/SKILL.md) skill) | [proven] |
| **Archived versions** | Complete state before each new version, with a `README` saying what and why ([template](../../templates/archived-version-readme.md)) | [proven] |
| **Archived configurations** | Configuration in force copied before every significant change | [proven] |
| **Instruction register** | Durable constraints, active and replaced instructions, requests and their status ([template](../../templates/instruction-register.md)) | [proven] |
| **Agent memory** | The lead's durable preferences: a rule, its reason, how to apply it | [proven] |
| **Git history** | Atomic commits whose message explains the why and the evidence | [proven] |

## Resume (always first) [proven]

1. Real state: `git status` and `git log` if there is a repository; active processes; running computations; disk
   space.
2. Read the most recent log and the instruction register.
3. **Verify before continuing**: rerun the checks listed in the log; a box ticked without evidence has to be checked
   again. If the log contradicts the files, the files win and the log is corrected.
4. Cleanly stop the tasks that have become obsolete (production of an outdated version, its automatic finalization),
   keeping their useful results and without touching other work.
5. Resume at "Next actions".

The [resume checklist](../quality/checklists/session-resume.md) details these points.

## Open a new version [proven]

1. Archive the current version: sources, configurations, scripts, `README`, fingerprints.
2. Create an identifiable version, read by every script from the configuration (for example `project.version`), from
   which they derive their paths.
3. Separate its outputs: computations, caches, reports.
4. Keep what works; change the architecture only where the new objective requires it.

## Keep it up to date

At each completed step: status, decisions and reasons, checks run with their results, next actions. Separate
*verified*, *hypothesis* and *to do*. The log stays concise: details live in the files, the tests and the commit
messages.

## Close

Set the status to "done" and write the report. What must last goes elsewhere: project decisions, rules in its
`CLAUDE.md`, generic lessons in this playbook. **The log is a trace, not a source of rules.**

## Agent memory, project or playbook?

| Goes into the project's memory or documents | Goes into this playbook |
|---|---|
| A preference specific to one project (an aesthetic choice) | A preference valid for every project (review videos played forward) |
| Status of ongoing work, figures, measurements | Method, principle, generic lesson |
| Path, identifier, artefact, deliverable | Template, tool, reusable procedure |

Cross-project preferences are gathered in the [collaboration defaults](../quality/collaboration.md).
