# Claude Code : configuration et usage

## Réglages du poste [éprouvé]

- Langue de réponse fixée sur celle de la personne qui dirige (réglage `language`).
- Modèle le plus capable disponible, effort élevé pour les travaux de production.
- Mode de permissions large sur un poste personnel **seulement si** les règles de prudence sont écrites dans les
  consignes et les hooks : publication, achat, suppression, processus des autres projets.
- Plusieurs sessions peuvent tourner en parallèle sur des projets différents : verrou commun pour les calculs lourds,
  processus des autres sessions intouchables ([machine partagée](README.md#shared-machine)).

## Instructions de projet

| Support | Rôle | Maturité |
|---|---|---|
| `CLAUDE.md` racine, **court** | Carte du dépôt, commandes de vérification, règles impératives, continuité | [éprouvé] |
| `CLAUDE.md` de sous-dossier, `.claude/rules/` | Conventions locales, chargées à la demande | [éprouvé] |
| `AGENTS.md` | Renvoi vers `CLAUDE.md` pour d'autres agents | [éprouvé] |
| Section « Méthode appliquée » qui renvoie à ce référentiel | Rend la méthode active dès la première session, sans répéter les consignes dans chaque demande | [proposé] ([modèle](../../templates/project-claude-md.md)) |

Sans `CLAUDE.md`, les consignes vivent dans les demandes et finissent répétées d'une version à l'autre : le modèle les
rassemble une fois pour toutes.

## Mémoire de l'agent [éprouvé]

- Un fichier par fait, avec un en-tête (`name`, `description`, `type`) et, pour un retour de la personne qui dirige,
  les sections **Why** et **How to apply** ; liens entre mémoires par `[[nom]]`.
- Types : `feedback` (comment travailler), `project` (état, décisions), `reference` (ressource externe), `user`
  (profil).
- **Limite** : la mémoire est propre à un dossier de projet. Les préférences transversales vivent donc dans ce
  référentiel ([préférences de collaboration](../quality/collaboration.md)).

## Skills

| Skill | Rôle | Maturité |
|---|---|---|
| [`work-log`](../../skills/work-log/SKILL.md) | Ouvrir, reprendre et clore un travail long avec son journal | [éprouvé] |
| [`test-first-change`](../../skills/test-first-change/SKILL.md) | Livrer un changement de code : cadrer, test d'abord, vérifier, documenter, committer | [éprouvé] |
| [`visual-iteration`](../../skills/visual-iteration/SKILL.md) | Boucle référence → essai isolé → comparatif → intégration pour un travail visuel | [proposé] |
| Skills de coordination par sous-agents | Recherche déléguée | **Écartés** par défaut ([décision 0003](../decisions/0003-no-subagents.md)) |

<a id="hooks"></a>

## Hooks

Configuration **[éprouvé]** pour un projet logiciel :

- `PreToolUse` sur `Edit|Write` : garde (par exemple, refus de modifier une migration déjà fusionnée).
- `PostToolUse` sur `Edit|Write` : vérification immédiate du fichier modifié.
- `PreToolUse` sur `Bash` : vérifications complètes **avant tout `git commit`**.
- `Stop` : vérifications complètes **à la fin de chaque tour**.
- Permissions : lecture et écriture des `.env` refusées.
- Hooks écrits en scripts portables et **testés en CI** avec des entrées simulées.

Pour un projet de rendu ou de média **[proposé]** :

- refuser l'écriture dans les dossiers d'archive ;
- refuser la modification des dépendances d'une production en cours (comparaison avec l'empreinte de
  [`fingerprint.py`](../../tools/README.md#fingerprintpy)) ;
- refuser l'ajout à Git de fichiers volumineux (rendus, vidéos, scènes binaires).

## Outils de l'agent [éprouvé]

- **Exécution en arrière-plan avec notification** pour les calculs longs, plutôt qu'une attente active.
- **Surveillance par événements** des étapes d'un script long, à condition que le script journalise des lignes
  repérables (`STEP …`).
- **Recherche web** menée directement, en parallélisant les requêtes.
- **Partage privé** (Artifacts, par exemple) pour une galerie ou un rapport, avec l'accord de la personne qui dirige.
- **Pas de sous-agents** par défaut ([décision 0003](../decisions/0003-no-subagents.md)).

## Demandes

Les demandes efficaces suivent une structure stable : objectif, reprise de l'existant, recherche, méthode,
vérifications, livrables, mode d'exécution, critère essentiel. Elle est reprise dans les
[demandes types](../../templates/prompts/README.md).
