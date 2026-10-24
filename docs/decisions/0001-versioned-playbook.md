# 0001 — Un référentiel de méthode unique, versionné, séparé des projets

- **Statut** : acceptée
- **Date** : 2026-10-25
- **Décidée par** : la personne qui dirige

## Contexte

La méthode vivait à trois endroits dispersés : les demandes de la personne qui dirige (longues et souvent répétées),
les mémoires de l'agent (propres à chaque dossier de projet) et les journaux de chaque projet. Rien ne permettait de la
transmettre à un nouveau projet sans relire des centaines de pages.

## Décision

- Un dépôt dédié contient les principes, le workflow, les critères de qualité, les guides de domaine, les outils
  testés, les modèles, les skills et les décisions de méthode.
- Chaque pratique porte un niveau de maturité : **[éprouvé]**, **[extrapolé]** ou **[proposé]**.
- Les projets restent dans leurs propres dépôts ; le référentiel n'en reçoit que les enseignements génériques
  ([décision 0007](0007-no-project-content.md)).
- La méthode est versionnée sur le modèle de semver ([`CONTRIBUTING.md`](../../CONTRIBUTING.md#versioning)).

## Conséquences

- Après chaque projet, les enseignements génériques sont reportés ici ; le bilan détaillé reste dans le projet.
- Les mémoires transversales de l'agent sont recopiées ici ; les mémoires propres à un projet restent dans le projet.
- Le dépôt se vérifie lui-même : liens, ancres, niveaux de maturité, absence de secrets, tests des outils.

## Vérification

`python3 scripts/check_repo.py` et la CI (`.github/workflows/ci.yml`).
