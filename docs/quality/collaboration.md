# Collaboration defaults

Default preferences between the lead and the agent. They are **[proven]** and have held from one project to the next
for the authors of this playbook. They are **defaults, not laws**: an explicit project instruction replaces them
([P15](../principles.md#p15)). Keep the ones that suit you, change the others in your instruction register.

| # | Default | Why |
|---|---|---|
| C1 | **The lead's language**, with correct spelling and diacritics, in conversation and documentation | The lead reads everything |
| C2 | **No sub-agents**: the agent does research and work itself ([decision 0003](../decisions/0003-no-subagents.md)) | Traceability of what was read and concluded |
| C3 | **Local by default**: nothing published, uploaded or deployed without approval; no purchase or subscription | Rights, money and data are at stake ([P12](../principles.md#p12)) |
| C4 | **Autonomy on reversible decisions**, without asking again at every step ([P12](../principles.md#p12)) | Asking constantly exhausts the lead |
| C5 | **Show the result**: open renders and pages as soon as they are ready, and check that they opened | The lead judges on the evidence |
| C6 | **Review videos forward, whole piece, latest version** ([P8](../principles.md#p8)) | Judgement in final conditions |
| C7 | **Short status updates**: what works, what remains, the next action | Decisions without chasing |
| C8 | **Keep previous versions**; overwrite nothing | Going back is frequent |
| C9 | **The lead's visual judgement wins** over the agent's measurements | Metrics are not the goal ([P1](../principles.md#p1)) |
| C10 | **Sides named from the viewer's point of view** | Removes left/right ambiguity |
| C11 | **Do not touch other projects' processes** or parallel sessions | Shared machines |
| C12 | **The workstation's Git identity**: commits authored with the identity configured on the machine, never one copied from existing commits | Correct attribution |
| C13 | **No push or merge unless asked**; never work directly on the main branch | The lead controls what is shared |
| C14 | **No AI regeneration of the subject** when a source artwork exists ([decision 0004](../decisions/0004-preserve-the-source.md)) | Fidelity and rights |
| C15 | **Aim for the best references of the domain**, judged on the rendered result and the experience | Avoids timid proposals ([A20](anti-patterns.md#a20)) |

## Snippet ready to copy

To apply these defaults to every project, copy this block into Claude Code's global instructions (`~/.claude/CLAUDE.md`)
or into a project's `CLAUDE.md`, after removing the lines you do not want. The playbook never edits those files
itself.

```markdown
## Working method (playbook: ai-assisted-visual-production-playbook)

- Answer in the user's language, with correct spelling and diacritics.
- Do research and work yourself, without sub-agents.
- Stay local: publish, upload, deploy or buy nothing without explicit approval.
- Decide alone what is reversible; ask for what is irreversible or external.
- "Verified" = command run and result quoted; separate my checks from the user's approval.
- Done = final deliverables exist, open and were checked; a launched computation is not a delivery.
- Judge at final size, normal speed, on the latest version; review videos forward, whole piece.
- One variable at a time; sample before generalizing; cost measured before production.
- Fix the cause, never mask it (global blur, disabled test).
- Keep previous versions; separate outputs; delete nothing without approval.
- Keep a log and an instruction register; short status updates; open the results.
```
