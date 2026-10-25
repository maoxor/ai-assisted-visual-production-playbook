"""Tests of the rendering-project hooks with simulated Claude Code events (JSON on standard input).

  uv run pytest tests/test_hooks.py
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
HOOKS = ROOT / "hooks"
sys.path.insert(0, str(ROOT / "tools"))

import fingerprint  # noqa: E402


def run_hook(name, event, project):
    env = {**os.environ, "CLAUDE_PROJECT_DIR": str(project)}
    return subprocess.run([sys.executable, str(HOOKS / name)], input=json.dumps(event), capture_output=True,
                          text=True, env=env)


def edit(path, tool="Edit"):
    key = "notebook_path" if tool == "NotebookEdit" else "file_path"
    return {"tool_name": tool, "tool_input": {key: str(path)}}


# -- guard_archive.py ------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("tool", ["Edit", "Write", "MultiEdit", "NotebookEdit"])
def test_archive_edit_is_blocked(tmp_path, tool):
    r = run_hook("guard_archive.py", edit(tmp_path / "archive" / "v1" / "config.toml", tool), tmp_path)
    assert r.returncode == 2 and "protected folder" in r.stderr


def test_edit_outside_archive_passes(tmp_path):
    for path in [tmp_path / "config" / "scene.toml", tmp_path / "archived-notes.md"]:
        assert run_hook("guard_archive.py", edit(path), tmp_path).returncode == 0


def test_relative_path_and_custom_protected_folders(tmp_path):
    (tmp_path / ".claude" / "hooks").mkdir(parents=True)
    (tmp_path / ".claude" / "hooks" / "protected-paths.txt").write_text("# frozen\nassets/source/\n")
    event = {"tool_name": "Write", "tool_input": {"file_path": "assets/source/plate.txt"}, "cwd": str(tmp_path)}
    assert run_hook("guard_archive.py", event, tmp_path).returncode == 2
    assert run_hook("guard_archive.py", edit(tmp_path / "archive" / "x.md"), tmp_path).returncode == 0


def test_other_tools_and_bad_input_pass(tmp_path):
    assert run_hook("guard_archive.py", {"tool_name": "Read", "tool_input": {"file_path": "archive/a"}},
                    tmp_path).returncode == 0
    r = subprocess.run([sys.executable, str(HOOKS / "guard_archive.py")], input="not json", capture_output=True,
                       text=True)
    assert r.returncode == 0


# -- guard_production.py ---------------------------------------------------------------------------------------------

def production(tmp_path):
    dep = tmp_path / "config" / "scene.toml"
    dep.parent.mkdir(parents=True)
    dep.write_text("samples = 512\n")
    outputs = tmp_path / "renders" / "v1" / "desktop"
    cwd = os.getcwd()
    os.chdir(tmp_path)                                   # fingerprint records paths as given: relative to the project
    try:
        fingerprint.ensure(outputs.relative_to(tmp_path), ["config/scene.toml"])
    finally:
        os.chdir(cwd)
    return dep, outputs


def test_dependency_of_running_production_is_blocked(tmp_path):
    dep, outputs = production(tmp_path)
    with fingerprint.running(outputs):
        r = run_hook("guard_production.py", edit(dep), tmp_path)
        assert r.returncode == 2 and "renders/v1/desktop" in r.stderr.replace("\\", "/")
        other = tmp_path / "config" / "other.toml"
        assert run_hook("guard_production.py", edit(other), tmp_path).returncode == 0
    assert run_hook("guard_production.py", edit(dep), tmp_path).returncode == 0        # production finished


def test_stale_running_marker_is_ignored(tmp_path):
    dep, outputs = production(tmp_path)
    (outputs / "RUNNING").write_text(json.dumps({"pid": 2 ** 22 + 12345}))           # no such process
    assert run_hook("guard_production.py", edit(dep), tmp_path).returncode == 0


def test_fingerprint_run_marks_and_clears(tmp_path):
    outputs = tmp_path / "out"
    probe = "import pathlib, sys; sys.exit(0 if pathlib.Path(sys.argv[1]).exists() else 5)"
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "fingerprint.py"), "run", "--outputs", str(outputs),
                        "--", sys.executable, "-c", probe, str(outputs / "RUNNING")])
    assert r.returncode == 0 and not (outputs / "RUNNING").exists()


# -- guard_large_files.py --------------------------------------------------------------------------------------------

def git_repo(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    return tmp_path


def stage(repo, name, size):
    path = repo / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"\0" * size)
    subprocess.run(["git", "add", name], cwd=repo, check=True)


def commit(message="x"):
    return {"tool_name": "Bash", "tool_input": {"command": f'git add -A && git commit -m "{message}"'}}


def test_commit_with_media_or_large_file_is_blocked(tmp_path):
    repo = git_repo(tmp_path)
    stage(repo, "renders/frame.exr", 10)
    stage(repo, "data/big.bin", 6_000_000)
    stage(repo, "config/scene.toml", 100)
    r = run_hook("guard_large_files.py", commit(), repo)
    assert r.returncode == 2
    assert "renders/frame.exr" in r.stderr and "data/big.bin" in r.stderr and "scene.toml" not in r.stderr


def test_small_source_commit_passes_and_other_commands_are_ignored(tmp_path):
    repo = git_repo(tmp_path)
    stage(repo, "scripts/render.py", 2_000)
    assert run_hook("guard_large_files.py", commit(), repo).returncode == 0
    stage(repo, "renders/frame.exr", 10)
    assert run_hook("guard_large_files.py", {"tool_name": "Bash", "tool_input": {"command": "git status"}},
                    repo).returncode == 0


def test_files_added_by_the_same_command_are_checked(tmp_path):
    repo = git_repo(tmp_path)
    (repo / ".gitignore").write_text("outputs/\n")
    (repo / "outputs").mkdir()
    (repo / "outputs" / "ignored.mp4").write_bytes(b"x")                 # ignored: never staged
    (repo / "scripts").mkdir()
    (repo / "scripts" / "build.py").write_text("print(1)\n")
    assert run_hook("guard_large_files.py", commit(), repo).returncode == 0
    (repo / "renders").mkdir()
    (repo / "renders" / "take.mov").write_bytes(b"x")                    # not staged yet: added by the command
    r = run_hook("guard_large_files.py", commit(), repo)
    assert r.returncode == 2 and "renders/take.mov" in r.stderr
    narrow = {"tool_name": "Bash", "tool_input": {"command": "git add scripts && git commit -m x"}}
    assert run_hook("guard_large_files.py", narrow, repo).returncode == 0  # the .mov is not part of this commit


def test_large_file_settings_and_allow_list(tmp_path):
    repo = git_repo(tmp_path)
    (repo / ".claude" / "hooks").mkdir(parents=True)
    (repo / ".claude" / "hooks" / "large-files.txt").write_text("max_mb=1\n.exr\nallow=assets/poster.exr\n")
    stage(repo, "assets/poster.exr", 10)
    assert run_hook("guard_large_files.py", commit(), repo).returncode == 0
    stage(repo, "data/medium.bin", 2_000_000)
    assert run_hook("guard_large_files.py", commit(), repo).returncode == 2


def test_settings_template_points_to_existing_hooks():
    settings = json.loads((HOOKS / "settings.json").read_text())
    commands = [h["command"] for group in settings["hooks"]["PreToolUse"] for h in group["hooks"]]
    for command in commands:
        name = command.rsplit("/", 1)[1].rstrip('"')
        assert (HOOKS / name).is_file(), name
