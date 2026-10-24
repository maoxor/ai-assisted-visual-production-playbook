# Modèles

Modèles prêts à copier dans un projet. `python3 scripts/new_project.py <chemin> --name "<nom>"` les installe
automatiquement ([`GETTING_STARTED.md`](../GETTING_STARTED.md)).

| Modèle | Usage | Emplacement dans le projet |
|---|---|---|
| [`project-brief.md`](project-brief.md) | Cadrage : objectif, critère essentiel, contraintes, hypothèses | `docs/BRIEF.md` |
| [`project-claude-md.md`](project-claude-md.md) | Instructions de l'agent pour le projet, avec la méthode appliquée | `CLAUDE.md` |
| [`instruction-register.md`](instruction-register.md) | Consignes durables, actives, remplacées ; demandes et leur état | `docs/instruction-register.md` |
| [`experiment-log.md`](experiment-log.md) | Journal numéroté des essais d'une version | `docs/experiments/<version>.md` |
| [`research-note.md`](research-note.md) | Problème, sources (D/T/H/O), méthode, essai, résultat | `docs/research/<sujet>.md` |
| [`work-log.md`](work-log.md) | Journal d'un travail long (branche, plan, validations, prochaines actions) | `docs/work-logs/<date>-<sujet>.md` |
| [`decision-record.md`](decision-record.md) | Décision structurante (ADR) | `docs/decisions/NNNN-<titre>.md` |
| [`status-update.md`](status-update.md) | Point d'avancement court | Message |
| [`delivery-report.md`](delivery-report.md) | Bilan de fin : terminé, testé, limites | `docs/DELIVERY_REPORT.md` |
| [`retrospective.md`](retrospective.md) | Retour d'expérience de fin de projet, qui reste dans le projet | `docs/RETROSPECTIVE.md` |
| [`archived-version-readme.md`](archived-version-readme.md) | `README` d'une version archivée | `archive/<version>/README.md` |
| [`prompts/`](prompts/README.md) | Demandes types adressées à l'agent | Message |
