"""Shared helpers for the Claude Code hooks of this folder (standard library only).

A PreToolUse hook receives the tool call as JSON on standard input. Exit code 0 lets the call through; exit code 2
blocks it and shows standard error to the agent, which can then explain or adapt. Any unexpected error lets the call
through (exit 0) with a warning: a guard must never lock the agent out because of its own bug.
"""
import json
import os
import sys
from pathlib import Path

FILE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}


def read_event():
    try:
        return json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return {}


def project_dir(event):
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or os.getcwd()).resolve()


def target_file(event):
    """Absolute path of the file a file tool is about to change, or None."""
    if event.get("tool_name") not in FILE_TOOLS:
        return None
    tool_input = event.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not path:
        return None
    path = Path(path)
    if not path.is_absolute():
        path = Path(event.get("cwd") or os.getcwd()) / path
    return path.resolve()


def config_lines(root, name, default):
    """Lines of .claude/hooks/<name> (comments with '#'), or the default list."""
    path = root / ".claude" / "hooks" / name
    if not path.is_file():
        return default
    lines = [line.split("#", 1)[0].strip() for line in path.read_text(encoding="utf-8").splitlines()]
    return [line for line in lines if line]


def block(message):
    print(message, file=sys.stderr)
    sys.exit(2)


def guarded(main):
    """Run a hook's main function; a crash lets the tool call through with a warning."""
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 (a guard must fail open)
        print(f"hook warning ({Path(sys.argv[0]).name}): {exc}", file=sys.stderr)
        sys.exit(0)
