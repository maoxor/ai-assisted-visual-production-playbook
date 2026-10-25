# Agent skills

Procedures that an agent loads when a task matches their description. They follow the
[Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) format (`<name>/SKILL.md` with a `name` and a
`description`), so Claude Code and other compatible agents can use them. They rely on the
[templates](../templates/README.md), which `scripts/new_project.py` installs in the project's `docs/` folder.

| Skill | Use | Maturity |
|---|---|---|
| [`work-log`](work-log/SKILL.md) | Open, resume or close a long task with its log | [proven] |
| [`test-first-change`](test-first-change/SKILL.md) | Ship a code change, test first | [proven] |
| [`visual-iteration`](visual-iteration/SKILL.md) | Improve a visual result through isolated trials and comparisons | [proposed] |

<a id="install"></a>

## Install

**For one project** (the skills travel with the repository):

```bash
python3 scripts/new_project.py <path> --name "<name>"     # copies them to <path>/.claude/skills/
# or copy a single skill:
mkdir -p <project>/.claude/skills && cp -R skills/work-log <project>/.claude/skills/
```

**For every project, as a Claude Code plugin** (the repository is also a plugin marketplace):

```text
/plugin marketplace add maoxor/ai-assisted-visual-production-playbook
/plugin install visual-production@visual-production-playbook
```

The skills then appear as `visual-production:work-log`, `visual-production:test-first-change` and
`visual-production:visual-iteration`. From a local clone, `/plugin marketplace add ./ai-assisted-visual-production-playbook`
works the same way. The manifests (`.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`) are checked with
`claude plugin validate .` in CI, and installation from GitHub with the two commands above has been verified.

## Adapt

Adapt the verification commands to the project. A skill stays short: the details go into the templates and the
project's `CLAUDE.md`. When the project has no `docs/` templates (plugin installation), the skills fall back on the
templates of this repository.
