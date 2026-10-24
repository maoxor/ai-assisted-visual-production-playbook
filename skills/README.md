# Skills Claude Code

Procédures prêtes à copier dans un projet (`<projet>/.claude/skills/<nom>/SKILL.md`). Claude Code les charge quand la
tâche correspond à leur description. Elles s'appuient sur les [modèles](../templates/README.md), installés en même
temps dans `docs/`.

| Skill | Usage | Maturité |
|---|---|---|
| [`work-log`](work-log/SKILL.md) | Ouvrir, reprendre ou clore un travail long avec son journal | [éprouvé] |
| [`test-first-change`](test-first-change/SKILL.md) | Livrer un changement de code, test d'abord | [éprouvé] |
| [`visual-iteration`](visual-iteration/SKILL.md) | Améliorer un résultat visuel par essais isolés et comparatifs | [proposé] |

Installation : `python3 scripts/new_project.py <chemin> --name "<nom>"` copie ces skills et les modèles
([`GETTING_STARTED.md`](../GETTING_STARTED.md)).

Adapter les commandes de vérification au projet. Un skill reste court : le détail va dans les modèles et dans le
`CLAUDE.md` du projet.
