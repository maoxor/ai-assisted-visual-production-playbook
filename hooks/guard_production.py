"""PreToolUse hook: refuse edits to a dependency of a production in progress.

A production is in progress when an output folder holds both VERSION.json (written by tools/fingerprint.py ensure)
and RUNNING (written by tools/fingerprint.py run, or by fingerprint.running() in a render loop) whose process is
alive. Editing one of the files listed in VERSION.json would change the fingerprint and stop the production at the
next batch, or mix states: the edit is refused until the production ends.

Output roots searched, relative to the project: one per line in .claude/hooks/production-roots.txt; default: renders/
and outputs/. A RUNNING file whose process no longer exists is ignored (stale marker).
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import block, config_lines, guarded, project_dir, read_event, target_file  # noqa: E402


def alive(pid):
    """True if a process with this id is running. Never sends a signal on Windows, where os.kill terminates."""
    try:
        pid = int(pid)
    except (ValueError, TypeError):
        return False
    if sys.platform == "win32":
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.OpenProcess(0x1000, False, pid)        # PROCESS_QUERY_LIMITED_INFORMATION
        if not handle:
            return False
        code = ctypes.c_ulong()
        ok = kernel32.GetExitCodeProcess(handle, ctypes.byref(code))
        kernel32.CloseHandle(handle)
        return bool(ok) and code.value == 259                    # STILL_ACTIVE
    try:
        os.kill(pid, 0)                                          # signal 0: existence check only (POSIX)
    except PermissionError:
        return True                                              # exists, owned by another user
    except (OSError, OverflowError):
        return False
    return True


def running_productions(root):
    for folder in config_lines(root, "production-roots.txt", ["renders/", "outputs/"]):
        base = root / folder
        if not base.is_dir():
            continue
        for marker in base.rglob("RUNNING"):
            version = marker.parent / "VERSION.json"
            if not version.is_file():
                continue
            try:
                pid = json.loads(marker.read_text(encoding="utf-8")).get("pid")
            except (json.JSONDecodeError, OSError):
                pid = None
            if alive(pid):
                yield marker.parent, json.loads(version.read_text(encoding="utf-8")).get("files", {})


def main():
    event = read_event()
    path = target_file(event)
    if path is None:
        return
    root = project_dir(event)
    for outputs, files in running_productions(root):
        for dep in files:
            dep_path = Path(dep) if Path(dep).is_absolute() else root / dep
            if dep_path.resolve() == path:
                block(f"Blocked: {path.relative_to(root)} is a dependency of the production running in "
                      f"{outputs.relative_to(root)} (see its VERSION.json). Changing it would stop or corrupt the "
                      f"production (playbook decision 0006): wait for the end, or stop the production first.")


if __name__ == "__main__":
    guarded(main)
