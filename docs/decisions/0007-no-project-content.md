# 0007 — Le référentiel ne contient aucun travail ni livrable de projet

- **Statut** : acceptée
- **Date** : 2026-10-25
- **Décidée par** : la personne qui dirige

## Contexte

Le référentiel doit documenter **comment réaliser les travaux**, sans exposer **les travaux eux-mêmes**. Il doit
pouvoir être consulté, partagé ou publié sans révéler de réalisation, de livrable, de donnée de projet ni d'œuvre
tierce.

## Décision

Le référentiel contient uniquement : principes, workflow, critères de qualité, bonnes pratiques, procédures, guides de
domaine, outils génériques et testés, modèles, skills, décisions de méthode et actions d'amélioration.

Il ne contient jamais :

- de livrable, de rendu, d'image, de vidéo, de scène ou d'asset ;
- de code livré à un client ou intégré dans un produit ;
- de nom de projet, de client, d'œuvre, d'auteur ou de collaborateur ;
- de chronologie, de chiffre, de mesure ou de réglage propre à un projet ;
- de citation de demande ou de conversation ;
- de chemin de poste, d'identifiant de compte ni de secret.

Les exemples sont génériques. Un enseignement venu d'un projet est reformulé comme une règle indépendante de ce projet.

## Conséquences

- Les bilans de projet ([modèle](../../templates/retrospective.md)) restent dans chaque projet ; seul ce qui est
  générique remonte ici.
- Les niveaux de maturité remplacent les citations de sources : la preuve reste dans le projet.
- Un outil n'entre ici qu'une fois généralisé, sans dépendance à un projet, et testé sur des données synthétiques.

## Vérification

- `python3 scripts/check_repo.py` refuse les secrets, adresses électroniques, chemins de poste et fichiers média.
- Une **liste de termes interdits** propre au poste (noms de projets, d'œuvres, de personnes), jamais versionnée,
  peut être fournie avec `--deny-list` ou placée dans `.git/info/deny-list.txt` : le script la lit automatiquement.
- Le modèle de demande de fusion et les modèles d'issues rappellent la règle.
