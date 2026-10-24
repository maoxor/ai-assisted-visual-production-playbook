# Feuille de route

Actions à entreprendre pour renforcer la méthode. Chaque action terminée est retirée par un commit qui dit comment,
et le niveau de maturité concerné est mis à jour.

## Éprouver ce qui est proposé ou extrapolé

| Action | Pourquoi | Critère de fin |
|---|---|---|
| Appliquer la méthode à un projet de **motion design**, de **jeu ou temps réel**, ou de **document** | Ces colonnes de [l'adaptation](docs/workflow/adapting.md) sont [extrapolé] | Une colonne passe à [éprouvé], avec les ajustements reportés |
| Utiliser le skill [`visual-iteration`](skills/visual-iteration/SKILL.md) sur un vrai travail visuel | Rédigé à partir de pratiques éprouvées, jamais utilisé tel quel | Skill corrigé d'après l'usage ; maturité [éprouvé] |
| Créer un vrai projet avec [`new_project.py`](scripts/new_project.py) | Testé seulement dans des dossiers temporaires et en CI | Squelette ajusté d'après l'usage réel |
| Utiliser la section « Méthode appliquée » du [modèle de `CLAUDE.md`](templates/project-claude-md.md) dès la première session | [proposé] | Effet constaté sur la répétition des consignes |

## Combler des manques

| Action | Pourquoi | Critère de fin |
|---|---|---|
| Écrire et tester les **hooks pour projets de rendu** (archives en lecture seule, dépendances d'une production en cours, fichiers volumineux) | Décrits dans [Claude Code](docs/tooling/claude-code.md#hooks), jamais écrits | Hooks dans `skills/` ou `tools/`, avec leurs tests en CI |
| Définir une **procédure de test sur appareils physiques** (téléphones, tablettes) | Les tests de lecture vidéo n'ont été faits qu'en émulation | Procédure ajoutée au [guide vidéo web](docs/domains/web-background-video.md) et à la liste de contrôle |
| Vérifier la **compensation de couleur Apple** sur iPhone et iPad réels | Constat fait seulement sous macOS | Résultat consigné dans le guide vidéo web |
| Généraliser un **banc de tests de lecture vidéo** (Playwright) dans `tools/` | Le banc reste à construire à chaque projet | Outil générique testé |
| Généraliser un **banc d'essai à modifications nommées** pour Blender | Le principe est décrit, pas outillé | Outil générique testé sur une scène synthétique |
| Documenter le **temps humain et le budget** dans le cadrage | Aucun repère d'estimation dans la méthode | Section ajoutée au [brief](templates/project-brief.md) |
| Décrire les **rôles à plusieurs personnes** (collaborateurs, relecteurs) | La méthode décrit un duo personne qui dirige / agent | Section ajoutée aux préférences de collaboration |

## Outillage du référentiel

| Action | Pourquoi | Critère de fin |
|---|---|---|
| Ajouter un **hook pre-commit local** qui lance `check_repo.py` avec la liste de termes interdits | La CI ne connaît pas la liste locale | Hook documenté dans `CONTRIBUTING.md` |
| Ajouter une **licence** si le dépôt devient public | Dépôt privé à sa création | Fichier `LICENSE` choisi par la personne qui dirige |
