# Contribuer

Ce référentiel s'enrichit par **petits ajouts génériques**, pas par réécriture. Git et GitHub servent à tracer quand
et pourquoi chaque règle a changé.

## Règles de rédaction

1. **Aucun contenu de projet** ([décision 0007](docs/decisions/0007-no-project-content.md)) : ni livrable, ni asset,
   ni nom de projet, de client, d'œuvre ou de personne, ni chiffre, réglage, chronologie ou citation propres à un
   projet. Un enseignement est reformulé comme une règle indépendante de son origine.
2. **Niveau de maturité obligatoire** pour toute pratique : **[éprouvé]**, **[extrapolé]** ou **[proposé]**.
   `scripts/check_repo.py` vérifie sa présence dans les documents qui l'exigent.
3. **Ne rien inventer** : une pratique non appliquée est [proposé], jamais [éprouvé].
4. **Méthode ≠ esthétique** ([décision 0002](docs/decisions/0002-method-separate-from-aesthetics.md)) : aucun style
   prescrit.
5. **Une règle, une source** : les autres documents y renvoient par un lien.
6. **Noms en anglais** : fichiers, dossiers, identifiants, options, branches, étiquettes. La documentation est rédigée
   en français, avec les accents corrects.
7. **Aucun secret ni donnée personnelle** : ni jeton, ni adresse électronique, ni chemin de poste.
8. **Liens relatifs** et ancres stables (`<a id="…">` en anglais pour les sections citées ailleurs).

<a id="after-each-project"></a>

## Après chaque projet

1. **Retour d'expérience dans le projet** : remplir `docs/RETROSPECTIVE.md`
   ([modèle](templates/retrospective.md)). Il ne vient pas ici.
2. **Anti-modèles** : chaque erreur corrigée devient une entrée générique de
   [`anti-patterns.md`](docs/quality/anti-patterns.md) (symptôme, coût, prévention).
3. **Principes, workflow, guides** : préciser ou corriger ; une pratique [extrapolé] ou [proposé] appliquée avec succès
   passe à [éprouvé].
4. **Outils** : un script utile à un deuxième projet est généralisé dans [`tools/`](tools/README.md), **avec ses tests
   sur données synthétiques**.
5. **Préférences** : une préférence de la personne qui dirige confirmée d'un projet à l'autre va dans
   [`collaboration.md`](docs/quality/collaboration.md).
6. **Décision de méthode** si un choix structurant change ([décisions](docs/decisions/README.md)).
7. **Version** : [`CHANGELOG.md`](CHANGELOG.md), puis une étiquette Git.
8. **Relecture de confidentialité** : `python3 scripts/check_repo.py`, avec la liste de termes interdits du poste.

## Pendant un projet

- Un enseignement important n'attend pas la fin : issue **« Lesson learned »** (forme générique).
- Une proposition de changement : issue **« Method change »**.
- Une lacune de la méthode : issue **« Gap »**, et une ligne dans [`ROADMAP.md`](ROADMAP.md).

## Git et GitHub

- **Branche** par contribution (`docs/<sujet>`, `tools/<sujet>`, `ci/<sujet>`), puis une demande de fusion avec le
  modèle de description. Fusion sur `main` par la personne qui dirige, ou à sa demande.
- **Commits** `type(portée): description`. Types : `docs`, `feat` (outil, modèle, skill), `fix`, `test`, `ci`,
  `chore`. Portées : `principles`, `workflow`, `quality`, `domains`, `tooling`, `decisions`, `templates`, `skills`,
  `tools`, `scripts`.
- **Corps du commit** : pourquoi, ce qui change pour un futur projet, preuve (tests, vérification).
- **Identité Git** : celle configurée sur le poste.
- **Étiquettes** `vX.Y.Z` à chaque version.
- **Libellés d'issues** : `lesson-learned`, `method-change`, `gap`.

<a id="versioning"></a>

## Versions

Inspiré de semver :

- **majeure** : un principe ajouté, retiré ou changé de sens, ou une décision remplacée ;
- **mineure** : une étape, un guide, un outil, un modèle ou un skill ajoutés ;
- **correctif** : précision, correction, lien.

## Vérifier avant de proposer

```bash
python3 scripts/check_repo.py                                   # liens, ancres, maturité, structure, confidentialité
python3 scripts/check_repo.py --deny-list ~/chemin/termes.txt   # avec une liste de termes interdits du poste
uv run --no-project --python 3.12 --with numpy --with opencv-python-headless --with pytest pytest tools/tests -q
```

Sans option, `check_repo.py` lit aussi `.git/info/deny-list.txt` s'il existe : un fichier local, jamais versionné,
avec un terme par ligne (`#` pour les commentaires).

La CI (`.github/workflows/ci.yml`) exécute les mêmes contrôles, sans liste locale, à chaque push.
