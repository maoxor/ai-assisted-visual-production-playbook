"""Create the skeleton of a new project that applies the playbook, never overwriting an existing file.

  python3 scripts/new_project.py ~/dev/my-project --name "My project"
  python3 scripts/new_project.py ~/dev/my-project --name "My project" --no-tools

Copies: agent instructions (CLAUDE.md, AGENTS.md), document templates (docs/), skills (.claude/skills/), toolkit
(tools/), config/ and outputs/ folders and a .gitignore. An existing file is kept as is and reported. Does not run
"git init": that is the project lead's choice (recommended, see GETTING_STARTED.md).
Standard library only.
"""
import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

PLAYBOOK = Path(__file__).resolve().parents[1]
TEMPLATES = PLAYBOOK / "templates"
COPIES = {
    "CLAUDE.md": TEMPLATES / "project-claude-md.md",
    "docs/BRIEF.md": TEMPLATES / "project-brief.md",
    "docs/instruction-register.md": TEMPLATES / "instruction-register.md",
    "docs/experiments/_template.md": TEMPLATES / "experiment-log.md",
    "docs/research/_template.md": TEMPLATES / "research-note.md",
    "docs/work-logs/_template.md": TEMPLATES / "work-log.md",
    "docs/decisions/_template.md": TEMPLATES / "decision-record.md",
    "docs/DELIVERY_REPORT.md": TEMPLATES / "delivery-report.md",
    "docs/RETROSPECTIVE.md": TEMPLATES / "retrospective.md",
    "docs/status-update.md": TEMPLATES / "status-update.md",
    "archive/_template-README.md": TEMPLATES / "archived-version-readme.md",
}
DATED = {"docs/BRIEF.md", "docs/instruction-register.md"}
SKILLS = ["work-log", "test-first-change", "visual-iteration"]
TOOLS = ["flicker.py", "loop_check.py", "stabilize.py", "fingerprint.py", "review_page.py", "review_video.py"]
GITIGNORE = """# Large, regenerable outputs stay out of Git (version sources, configuration and scripts)
outputs/
renders/
.venv/
__pycache__/
.DS_Store
*.blend1
"""
AGENTS = """# Instructions pour les agents

Les instructions du projet sont dans [`CLAUDE.md`](CLAUDE.md). Elles s'appliquent à tout agent, quel que soit l'outil.
"""
TOOLS_README = """# Tools

Copied from the production-playbook repository (`tools/`, where their documentation and tests live).
Update them from the playbook rather than editing them here; a generic improvement goes back to the playbook.
"""


def write(dest, content, report):
    if dest.exists():
        report.append(f"kept      {dest}")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, Path):
        shutil.copy2(content, dest)
    else:
        dest.write_text(content, encoding="utf-8")
    report.append(f"created   {dest}")


def create(target, name, tools=True):
    target = Path(target).expanduser().resolve()
    report = []
    today = date.today().isoformat()
    for rel, src in COPIES.items():
        text = src.read_text(encoding="utf-8").replace("<nom du projet>", name)
        if rel in DATED:
            text = text.replace("YYYY-MM-DD", today, 1)
        write(target / rel, text, report)
    write(target / "AGENTS.md", AGENTS, report)
    write(target / ".gitignore", GITIGNORE, report)
    for s in SKILLS:
        write(target / ".claude/skills" / s / "SKILL.md", PLAYBOOK / "skills" / s / "SKILL.md", report)
    if tools:
        for t in TOOLS:
            write(target / "tools" / t, PLAYBOOK / "tools" / t, report)
        write(target / "tools/README.md", TOOLS_README, report)
    for d in ("config", "outputs"):
        (target / d).mkdir(parents=True, exist_ok=True)
    return target, report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("target", help="folder of the new project (created if missing)")
    ap.add_argument("--name", required=True, help="project name")
    ap.add_argument("--no-tools", action="store_true", help="do not copy the toolkit")
    a = ap.parse_args(argv)
    target, report = create(a.target, a.name, not a.no_tools)
    print("\n".join(report))
    print(f"\nProject ready: {target}\nNext: fill in docs/BRIEF.md and complete CLAUDE.md (see the playbook's "
          "GETTING_STARTED.md). Git: run 'git init' if wanted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
