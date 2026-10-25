"""PreToolUse hook: refuse edits inside archive folders (archived versions are never modified).

Protected folders, relative to the project: one per line in .claude/hooks/protected-paths.txt; default: archive/.
Matching file tools: Edit, Write, MultiEdit, NotebookEdit. Shell commands are not inspected (see hooks/README.md).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import block, config_lines, guarded, project_dir, read_event, target_file  # noqa: E402


def main():
    event = read_event()
    path = target_file(event)
    if path is None:
        return
    root = project_dir(event)
    for folder in config_lines(root, "protected-paths.txt", ["archive/"]):
        protected = (root / folder).resolve()
        if path == protected or protected in path.parents:
            block(f"Blocked: {path.relative_to(root)} is inside the protected folder '{folder}'. Archived versions "
                  f"are never modified (playbook P10): copy the file into the current version instead.")


if __name__ == "__main__":
    guarded(main)
