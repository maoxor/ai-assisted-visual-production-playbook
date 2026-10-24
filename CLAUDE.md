# Production Playbook

Référentiel de méthode générique : principes, workflow, qualité, guides, outils, modèles, skills. Il ne contient aucun
projet. Documentation en français, accents corrects ; noms (fichiers, identifiants, branches) en anglais.

<!-- Chargé à chaque session : rester court. -->

## Utiliser ce référentiel depuis un autre projet

- Démarrer un projet : `python3 scripts/new_project.py <chemin> --name "<nom>"`, puis
  [`GETTING_STARTED.md`](GETTING_STARTED.md).
- Principes : [`docs/principles.md`](docs/principles.md) ; listes de contrôle :
  [`docs/quality/checklists/`](docs/quality/checklists/README.md).

## Modifier ce référentiel

- Lire [`CONTRIBUTING.md`](CONTRIBUTING.md). Toute pratique porte un niveau : **[éprouvé]**, **[extrapolé]** ou
  **[proposé]**. Ne jamais présenter comme éprouvé ce qui ne l'est pas.
- **Aucun contenu de projet** ([décision 0007](docs/decisions/0007-no-project-content.md)) : ni livrable, ni nom, ni
  chiffre, ni citation ; reformuler en règle générique.
- Méthode ≠ esthétique : aucun style prescrit.
- Aucun secret, aucun asset, aucune donnée personnelle.
- Vérifier avant de conclure, et citer les résultats :
  `python3 scripts/check_repo.py` et
  `uv run --no-project --python 3.12 --with numpy --with opencv-python-headless --with pytest pytest tools/tests -q`.
- Git : branche dédiée, commits `type(portée): description`, pas de push ni de fusion sans demande ; identité Git du
  poste.
