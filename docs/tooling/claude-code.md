# Claude Code: configuration and use

The method is agent-agnostic, but it was developed with Claude Code. This page records how Claude Code is configured
and used. Other agents can use the same files: `AGENTS.md` points to `CLAUDE.md`, and the skills follow the open Agent
Skills format.

## Workstation settings [proven]

- Response language set to the lead's language (`language` setting).
- The most capable model available, high effort for production work.
- A broad permission mode on a personal workstation **only if** the rules of caution are written in the instructions
  and hooks: publication, purchases, deletion, other projects' processes.
- Several sessions can run in parallel on different projects: a common lock for heavy computations, other sessions'
  processes untouchable ([shared machine](README.md#shared-machine)).

## Project instructions

| Medium | Role | Maturity |
|---|---|---|
| Root `CLAUDE.md`, **short** | Repository map, verification commands, mandatory rules, continuity | [proven] |
| Sub-folder `CLAUDE.md`, `.claude/rules/` | Local conventions, loaded on demand | [proven] |
| `AGENTS.md` | Points other agents to `CLAUDE.md` | [proven] |
| An "Applied method" section that refers to this playbook | Makes the method active from the first session, without repeating the instructions in every request | [proposed] ([template](../../templates/project-claude-md.md)) |

Without a `CLAUDE.md`, instructions live in the requests and end up repeated from one version to the next: the
template gathers them once and for all.

## Agent memory [proven]

- One file per fact, with a header (`name`, `description`, `type`) and, for feedback from the lead, the **Why** and
  **How to apply** sections; links between memories with `[[name]]`.
- Types: `feedback` (how to work), `project` (state, decisions), `reference` (external resource), `user` (profile).
- **Limit**: memory is specific to a project folder. Cross-project preferences therefore live in this playbook
  ([collaboration defaults](../quality/collaboration.md)).

## Skills and plugin

| Skill | Role | Maturity |
|---|---|---|
| [`work-log`](../../skills/work-log/SKILL.md) | Open, resume and close a long task with its log | [proven] |
| [`test-first-change`](../../skills/test-first-change/SKILL.md) | Ship a code change: scope, test first, verify, document, commit | [proven] |
| [`visual-iteration`](../../skills/visual-iteration/SKILL.md) | Reference → isolated trial → comparison → integration loop for visual work | [proposed] |
| Sub-agent coordination skills | Delegated research | **Not used** by default ([decision 0003](../decisions/0003-no-subagents.md)) |

The skills ship in two ways: copied into a project by `scripts/new_project.py` (`.claude/skills/`), or installed for
every project through the repository's Claude Code plugin (`.claude-plugin/`, see
[`skills/README.md`](../../skills/README.md#install)). The plugin manifests are checked with `claude plugin validate`.

<a id="hooks"></a>

## Hooks

Configuration **[proven]** for a software project:

- `PreToolUse` on `Edit|Write`: guard (for example, refusing to modify a migration that is already merged).
- `PostToolUse` on `Edit|Write`: immediate check of the modified file.
- `PreToolUse` on `Bash`: full checks **before any `git commit`**.
- `Stop`: full checks **at the end of each turn**.
- Permissions: reading and writing `.env` files denied.
- Hooks written as portable scripts and **tested in CI** with simulated inputs.

For a rendering or media project **[proposed]**:

- refuse writes to archive folders;
- refuse changes to the dependencies of a running production (comparison with the fingerprint of
  [`fingerprint.py`](../../tools/README.md#fingerprintpy));
- refuse adding large files to Git (renders, videos, binary scenes).

## Agent tools [proven]

- **Background execution with notification** for long computations, rather than active waiting.
- **Event-based monitoring** of the steps of a long script, provided the script logs recognizable lines (`STEP …`).
- **Web search** run directly, with queries in parallel.
- **Private sharing** (Artifacts, for example) for a gallery or report, with the lead's approval.
- **No sub-agents** by default ([decision 0003](../decisions/0003-no-subagents.md)).

## Requests

Effective requests follow a stable structure: objective, taking stock of the existing work, research, method, checks,
deliverables, execution mode, key criterion. It is the structure of the
[prompt templates](../../templates/prompts/README.md).
