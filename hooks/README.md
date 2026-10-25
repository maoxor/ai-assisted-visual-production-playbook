# Hooks for rendering and media projects

Three Claude Code `PreToolUse` hooks that turn rules of the method into guards that do not depend on the agent's
goodwill ([quality mechanisms](../docs/quality/README.md#mechanisms-that-produce-quality)). Maturity: **[proposed]**:
written and tested with simulated events in CI, not yet used in a real production.

| Hook | Refuses | Rule enforced |
|---|---|---|
| [`guard_archive.py`](guard_archive.py) | Editing a file inside an archive folder (default `archive/`) | Archived versions are never modified ([P10](../docs/principles.md#p10)) |
| [`guard_production.py`](guard_production.py) | Editing a dependency of a production in progress | Change nothing during the computation ([decision 0006](../docs/decisions/0006-fingerprinted-resumable-production.md)) |
| [`guard_large_files.py`](guard_large_files.py) | A `git commit` that adds media or large files (default: > 5 MB, or `.mp4 .mov .mkv .webm .exr .blend .psd .zip …`) | Outputs stay out of Git; sources, configuration and scripts go in |

## Install

`scripts/new_project.py` installs them in a new project (`--no-hooks` to skip): the scripts go to `.claude/hooks/` and
[`settings.json`](settings.json) to `.claude/settings.json` (an existing settings file is kept: merge the `hooks`
section by hand). By hand:

```bash
mkdir -p <project>/.claude/hooks
cp hooks/*.py <project>/.claude/hooks/
cp hooks/settings.json <project>/.claude/settings.json      # or merge its "hooks" section into yours
```

Requirements: `python3` (3.9 or later, standard library only) in the `PATH` of the shell that Claude Code uses for
hooks; `git` for `guard_large_files.py`. On Windows, replace `python3` with `python` in `settings.json` if needed.

## How they work

Claude Code sends each tool call to the hook as JSON on standard input. **Exit code 2 blocks the call** and shows the
message to the agent, which can explain or adapt; exit code 0 lets it through. A hook that crashes lets the call
through with a warning: a guard must never lock the agent out because of its own bug.

- **`guard_archive.py`** checks the path of `Edit`, `Write`, `MultiEdit` and `NotebookEdit` calls against the
  protected folders.
- **`guard_production.py`** looks for output folders holding both `VERSION.json` (written by
  [`fingerprint.py ensure`](../tools/README.md#fingerprintpy)) and `RUNNING` (written by `fingerprint.py run -- <command>`
  or by `fingerprint.running()` around a render loop). If the `RUNNING` process is alive, the files listed in
  `VERSION.json` are read-only for the agent. A marker left by a dead process is ignored. Fingerprint paths are relative
  to the project: call `fingerprint.py` from the project root.
- **`guard_large_files.py`** runs on `Bash` calls whose command contains `git commit`, and inspects the files already
  staged plus those a `git add` or `git commit -a` in the same command is about to stage.

## Configure

Optional files in the project's `.claude/hooks/` folder (one entry per line, `#` for comments):

| File | Content | Default |
|---|---|---|
| `protected-paths.txt` | Folders where edits are refused | `archive/` |
| `production-roots.txt` | Folders searched for running productions | `renders/`, `outputs/` |
| `large-files.txt` | `max_mb=<size>`, extensions to refuse (`.exr`), exceptions (`allow=<path or glob>`) | `max_mb=5` and the media extensions |

## Limits

- Shell commands are not parsed for file writes (`cp`, `mv`, redirections): the guards cover the agent's file tools
  and `git commit`. Permissions (`permissions.deny` in `settings.json`) can add coarse shell restrictions.
- `guard_large_files.py` anticipates what `git add <paths>`, `git add -A` or `git commit -a` in the same command line
  will stage; staging done in other ways (a script that calls `git add`) is seen only once it has happened. Keep a
  `.gitignore` that excludes outputs (installed by `new_project.py`).
- Tests: [`tests/test_hooks.py`](../tests/test_hooks.py) (simulated events, temporary Git repositories).
