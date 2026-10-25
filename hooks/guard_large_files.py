"""PreToolUse hook on Bash: refuse a git commit that would add large or media files to the repository.

Renders, videos, binary scenes and other heavy outputs stay out of Git; sources, configuration and scripts go in.
Checked when the command runs `git commit`: the files already staged, plus those that a `git add` or `git commit -a`
in the same command line is about to stage (the hook runs before the whole command). Limits, one per line in
.claude/hooks/large-files.txt: `max_mb=<size>` (default 5) and extensions to refuse, e.g. `.exr` (default: .mp4 .mov
.mkv .webm .exr .blend .blend1 .psd .zip .tar .gz). Allowed exceptions: lines `allow=<path or glob>`.
"""
import fnmatch
import re
import shlex
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import block, config_lines, guarded, project_dir, read_event  # noqa: E402

DEFAULT_EXTENSIONS = [".mp4", ".mov", ".mkv", ".webm", ".exr", ".blend", ".blend1", ".psd", ".zip", ".tar", ".gz"]


def settings(root):
    lines = config_lines(root, "large-files.txt", [])
    max_mb = next((float(line.split("=", 1)[1]) for line in lines if line.startswith("max_mb=")), 5.0)
    extensions = [line.lower() for line in lines if line.startswith(".")] or DEFAULT_EXTENSIONS
    allowed = [line.split("=", 1)[1] for line in lines if line.startswith("allow=")]
    return max_mb, extensions, allowed


def git_lines(root, *args):
    r = subprocess.run(["git", *args, "-z"], cwd=root, capture_output=True, text=True)
    return [n for n in r.stdout.split("\0") if n] if r.returncode == 0 else []


def about_to_stage(root, command):
    """Files that `git add …` or `git commit -a` in this command line will stage."""
    changed = git_lines(root, "diff", "--name-only", "--diff-filter=AM")
    untracked = git_lines(root, "ls-files", "--others", "--exclude-standard")
    found = set()
    for part in re.split(r"&&|\|\||;|\|", command):
        try:
            words = shlex.split(part)
        except ValueError:
            words = part.split()
        for i in range(len(words) - 1):
            if words[i] != "git":
                continue
            rest = words[i + 1:]
            while rest[:1] == ["-C"] and len(rest) > 2:
                rest = rest[2:]
            if rest[:1] == ["add"]:
                args = rest[1:]
                paths = [a for a in args if not a.startswith("-")]
                if any(a in ("-A", "--all", "-u", "--update") for a in args) or not paths or "." in paths:
                    found.update(changed + ([] if "-u" in args or "--update" in args else untracked))
                else:
                    for name in changed + untracked:
                        if any(name == q.rstrip("/") or name.startswith(q.rstrip("/") + "/") or fnmatch.fnmatch(name, q)
                               for q in paths):
                            found.add(name)
            elif rest[:1] == ["commit"] and any(a in ("-a", "--all") or (a.startswith("-") and not a.startswith("--")
                                                                          and "a" in a[1:]) for a in rest[1:]):
                found.update(changed)
    return found


def main():
    event = read_event()
    if event.get("tool_name") != "Bash":
        return
    command = (event.get("tool_input") or {}).get("command", "")
    if not re.search(r"(^|[;&|(]\s*|\s)git(\s+-C\s+\S+)?\s+commit\b", command):
        return
    root = project_dir(event)
    if subprocess.run(["git", "rev-parse", "--git-dir"], cwd=root, capture_output=True).returncode != 0:
        return
    candidates = set(git_lines(root, "diff", "--cached", "--name-only", "--diff-filter=AM"))
    candidates |= about_to_stage(root, command)
    max_mb, extensions, allowed = settings(root)
    refused = []
    for name in sorted(candidates):
        if any(fnmatch.fnmatch(name, a) for a in allowed):
            continue
        path = root / name
        size_mb = path.stat().st_size / 1e6 if path.is_file() else 0.0
        if Path(name).suffix.lower() in extensions:
            refused.append(f"{name} (media or binary extension)")
        elif size_mb > max_mb:
            refused.append(f"{name} ({size_mb:.1f} MB > {max_mb:g} MB)")
    if refused:
        block("Blocked: this commit would add large or media files to Git:\n  " + "\n  ".join(refused) +
              "\nKeep outputs out of Git (add them to .gitignore and unstage them with `git restore --staged`), "
              "or allow a file explicitly in .claude/hooks/large-files.txt (`allow=<path>`).")


if __name__ == "__main__":
    guarded(main)
