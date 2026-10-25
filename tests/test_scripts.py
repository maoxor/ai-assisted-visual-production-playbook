"""Tests of the repository scripts: project scaffolder and repository checks.

  uv run pytest tests/test_scripts.py
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import new_project  # noqa: E402

SKIPPED = shutil.ignore_patterns(".git", ".venv", "__pycache__", ".pytest_cache", "outputs")


# -- new_project.py --------------------------------------------------------------------------------------------------

def test_new_project_creates_the_skeleton(tmp_path):
    target, report = new_project.create(tmp_path / "demo", "Demo project")
    for rel in ["CLAUDE.md", "AGENTS.md", ".gitignore", "docs/BRIEF.md", "docs/instruction-register.md",
                "docs/work-logs/_template.md", "docs/DELIVERY_REPORT.md", "archive/_template-README.md",
                ".claude/skills/work-log/SKILL.md", ".claude/skills/visual-iteration/SKILL.md",
                "tools/fingerprint.py", "tools/README.md", ".claude/settings.json",
                ".claude/hooks/guard_archive.py", ".claude/hooks/_common.py"]:
        assert (target / rel).is_file(), rel
    assert (target / "config").is_dir() and (target / "outputs").is_dir()
    assert all(line.startswith("created") for line in report)
    assert "# Demo project" in (target / "CLAUDE.md").read_text(encoding="utf-8")
    assert "<project name>" not in (target / "docs/BRIEF.md").read_text(encoding="utf-8")
    assert "YYYY-MM-DD" not in (target / "docs/BRIEF.md").read_text(encoding="utf-8").split("\n")[2]


def test_new_project_never_overwrites(tmp_path):
    target, _ = new_project.create(tmp_path / "demo", "Demo")
    brief = target / "docs/BRIEF.md"
    brief.write_text("my own brief\n", encoding="utf-8")
    _, report = new_project.create(target, "Demo")
    assert brief.read_text(encoding="utf-8") == "my own brief\n"
    assert all(line.startswith("kept") for line in report)


def test_new_project_without_tools_or_hooks(tmp_path):
    target, _ = new_project.create(tmp_path / "demo", "Demo", tools=False, hooks=False)
    assert not (target / "tools").exists()
    assert not (target / ".claude/hooks").exists() and not (target / ".claude/settings.json").exists()
    assert (target / ".claude/skills/test-first-change/SKILL.md").is_file()


def test_installed_hook_blocks_archive_edits_in_the_new_project(tmp_path):
    target, _ = new_project.create(tmp_path / "demo", "Demo")
    event = json.dumps({"tool_name": "Edit", "tool_input": {"file_path": str(target / "archive" / "v1.md")}})
    r = subprocess.run([sys.executable, str(target / ".claude/hooks/guard_archive.py")], input=event, text=True,
                       capture_output=True, env={**os.environ, "CLAUDE_PROJECT_DIR": str(target)})
    assert r.returncode == 2


def test_copied_tool_runs_in_the_new_project(tmp_path):
    target, _ = new_project.create(tmp_path / "demo", "Demo")
    r = subprocess.run([sys.executable, str(target / "tools/fingerprint.py"), "compute", "--dep",
                        str(target / "docs/BRIEF.md")], capture_output=True, text=True)
    assert r.returncode == 0 and '"fingerprint"' in r.stdout


# -- check_repo.py ---------------------------------------------------------------------------------------------------

def copy_repo(tmp_path):
    dst = tmp_path / "repo"
    shutil.copytree(ROOT, dst, ignore=SKIPPED)
    return dst


def run_check(repo, *args):
    return subprocess.run([sys.executable, str(repo / "scripts/check_repo.py"), *args], capture_output=True,
                          text=True, cwd=repo)


def test_check_repo_passes_on_this_repository(tmp_path):
    r = run_check(copy_repo(tmp_path))
    assert r.returncode == 0, r.stdout


def test_check_repo_detects_problems(tmp_path):
    repo = copy_repo(tmp_path)
    address = "someone" + "@" + "example.com"                      # built here so this file passes the check
    (repo / "docs/extra.md").write_text("[broken](missing.md) and [anchor](principles.md#nope)\n"
                                        f"contact: {address}\n", encoding="utf-8")
    (repo / "docs/workflow/README.md").write_text("# Workflow without maturity level\n", encoding="utf-8")
    (repo / "frame.png").write_bytes(b"\x89PNG")
    r = run_check(repo)
    assert r.returncode == 1
    for expected in ["broken link -> missing.md", "missing anchor -> principles.md#nope", "email address",
                     "docs/workflow/README.md: no maturity level", "frame.png: media or binary asset"]:
        assert expected in r.stdout, expected


def test_check_repo_deny_list_and_versions(tmp_path):
    repo = copy_repo(tmp_path)
    (repo / "docs/extra.md").write_text("This mentions Secretproject by name.\n", encoding="utf-8")
    terms = tmp_path / "terms.txt"
    terms.write_text("# local terms\nsecretproject\n", encoding="utf-8")
    pyproject = repo / "pyproject.toml"
    pyproject.write_text(pyproject.read_text(encoding="utf-8").replace('version = "', 'version = "9', 1),
                         encoding="utf-8")
    r = run_check(repo, "--deny-list", str(terms))
    assert r.returncode == 1
    assert "deny-listed term (secretproject)" in r.stdout
    assert "inconsistent versions" in r.stdout


def test_check_repo_rejects_personal_commit_addresses(tmp_path):
    repo = copy_repo(tmp_path)
    env = {**os.environ, "GIT_AUTHOR_NAME": "x", "GIT_COMMITTER_NAME": "x",
           "GIT_AUTHOR_EMAIL": "1+x@users.noreply.github.com", "GIT_COMMITTER_EMAIL": "1+x@users.noreply.github.com"}
    for cmd in (["git", "init", "-q"], ["git", "add", "-A"], ["git", "commit", "-q", "-m", "ok"]):
        subprocess.run(cmd, cwd=repo, check=True, env=env)
    assert run_check(repo).returncode == 0
    (repo / "docs" / "extra.md").write_text("more\n", encoding="utf-8")
    personal = {**env, "GIT_AUTHOR_EMAIL": "someone" + "@" + "example.com"}
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True, env=personal)
    subprocess.run(["git", "commit", "-q", "-m", "leak"], cwd=repo, check=True, env=personal)
    r = run_check(repo)
    assert r.returncode == 1 and "is not a noreply address" in r.stdout and "example.com" in r.stdout
