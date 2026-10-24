# 9. Continuité : reprendre sans la conversation

**Objectif.** Permettre à n'importe qui de reprendre le travail exactement où il en est, sans relire la conversation :
une autre session, une autre personne, ou soi-même après une interruption ou une compaction du contexte.

## Les supports de la continuité

| Support | Contenu | Maturité |
|---|---|---|
| **Journal d'essais** | Entrées numérotées : essai, constat, retenu ou écarté, raison ; regroupées par itération avec la demande qui l'a déclenchée ([modèle](../../templates/experiment-log.md)) | [éprouvé] |
| **Journal de chantier** | État, décisions, validations exécutées, prochaines actions, questions ouvertes ([modèle](../../templates/work-log.md), skill [`work-log`](../../skills/work-log/SKILL.md)) | [éprouvé] |
| **Versions archivées** | État complet avant chaque nouvelle version, avec un `README` qui dit quoi et pourquoi ([modèle](../../templates/archived-version-readme.md)) | [éprouvé] |
| **Configurations archivées** | Configuration en vigueur copiée avant chaque changement important | [éprouvé] |
| **Registre des consignes** | Contraintes durables, consignes actives et remplacées, demandes et leur état ([modèle](../../templates/instruction-register.md)) | [éprouvé] |
| **Mémoire de l'agent** | Préférences durables de la personne qui dirige : une règle, sa raison, comment l'appliquer | [éprouvé] |
| **Historique Git** | Commits atomiques dont le message explique le pourquoi et la preuve | [éprouvé] |

## Reprendre (toujours en premier) [éprouvé]

1. État réel : `git status` et `git log` s'il y a un dépôt ; processus actifs ; calculs en cours ; espace disque.
2. Lire le journal le plus récent et le registre des consignes.
3. **Vérifier avant de continuer** : relancer les contrôles du journal ; une case cochée sans preuve est à revérifier.
   Si le journal contredit les fichiers, les fichiers font foi et l'on corrige le journal.
4. Arrêter proprement les tâches devenues obsolètes (production d'une version dépassée, finalisation automatique
   associée), en conservant leurs résultats utiles et sans toucher aux autres travaux.
5. Reprendre à « Prochaines actions ».

La [liste de reprise](../quality/checklists/session-resume.md) détaille ces points.

## Ouvrir une nouvelle version [éprouvé]

1. Archiver la version actuelle : sources, configurations, scripts, `README`, empreintes.
2. Créer une version identifiable, lue par tous les scripts depuis la configuration (par exemple
   `project.version`), d'où ils dérivent leurs chemins.
3. Séparer ses sorties : calculs, caches, rapports.
4. Conserver ce qui fonctionne ; ne faire évoluer l'architecture que là où le nouvel objectif l'exige.

## Tenir à jour

À chaque étape terminée : statut, décisions et raisons, validations exécutées avec leurs résultats, prochaines
actions. On distingue *vérifié*, *hypothèse* et *à faire*. Le journal reste concis : le détail vit dans les fichiers,
les tests et les messages de commit.

## Clore

On passe le statut à « terminé » et l'on rédige le bilan. Ce qui doit durer est reporté ailleurs : décisions du
projet, règles dans son `CLAUDE.md`, enseignements génériques dans ce référentiel. **Le journal est une trace, pas une
source de règles.**

## Mémoire de l'agent, projet ou référentiel ?

| Va dans la mémoire ou les documents du projet | Va dans ce référentiel |
|---|---|
| Préférence propre à un projet (un choix esthétique) | Préférence valable pour tous les projets (vidéos de contrôle lues en avant) |
| État d'un travail en cours, chiffres, mesures | Méthode, principe, enseignement générique |
| Chemin, identifiant, artefact, livrable | Modèle, outil, procédure réutilisable |

Les préférences transversales sont regroupées dans [les préférences de collaboration](../quality/collaboration.md).
