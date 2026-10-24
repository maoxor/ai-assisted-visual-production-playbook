# Démarrer un nouveau projet

Ce guide se suit dans l'ordre, du premier jour à la fin du projet. Il ne présuppose ni la technique ni la direction
artistique.

## 0. Avant tout (10 minutes)

1. Lire les [principes](docs/principles.md), en particulier P1 à P3, P7, P8 et P15.
2. Lire les [anti-modèles](docs/quality/anti-patterns.md) : ce sont les erreurs à ne pas refaire.
3. Lire les [préférences de collaboration](docs/quality/collaboration.md).

## 1. Créer le squelette du projet

```bash
python3 scripts/new_project.py ~/dev/my-project --name "My project"
```

Le script crée, **sans rien écraser** :

```
my-project/
  CLAUDE.md                        instructions de l'agent, avec la méthode appliquée (à compléter)
  AGENTS.md                        renvoi vers CLAUDE.md
  docs/BRIEF.md                    cadrage
  docs/instruction-register.md     consignes durables, actives, remplacées ; demandes et leur état
  docs/experiments/_template.md    journal numéroté des essais
  docs/research/_template.md       note de recherche
  docs/work-logs/_template.md      journal de travail long
  docs/decisions/_template.md      décision structurante
  docs/DELIVERY_REPORT.md          rapport de livraison
  docs/RETROSPECTIVE.md            retour d'expérience (reste dans le projet)
  docs/status-update.md            modèle de point d'avancement
  archive/_template-README.md      README de version archivée
  .claude/skills/                  work-log, test-first-change, visual-iteration
  tools/                           boîte à outils (option --no-tools pour s'en passer)
  config/  outputs/                paramètres, sorties séparées
  .gitignore                       sorties volumineuses exclues
```

Puis `git init` dans le projet (recommandé : [P10](docs/principles.md#p10)).

## 2. Cadrer ([cadrage](docs/workflow/01-scoping.md))

- Remplir `docs/BRIEF.md` : objectif, **critère essentiel**, références (et ce qu'il ne faut pas en reproduire),
  livrables et conditions finales, contraintes, hypothèses, tensions, questions bloquantes.
- Remplir `docs/instruction-register.md` avec les contraintes durables.
- Compléter `CLAUDE.md` : carte, commandes de vérification, conditions finales.
- Pour une étude, partir de la [demande de faisabilité](templates/prompts/01-feasibility-study.md).

## 3. Traduire la méthode dans le domaine ([adapter](docs/workflow/adapting.md))

Dans `CLAUDE.md`, section « Méthode appliquée », écrire :

- l'**unité de production** et les **conditions finales** (où l'on juge) ;
- l'**échantillon** qui porte le risque principal ;
- les **familles de contrôles** traduites (fidélité, localité, superpositions, bords, animation, boucle, stabilité,
  encodage ou performance, éléments résiduels) ;
- les **coûts à séparer**.

## 4. Rechercher, prototyper, itérer

- [Recherche ciblée](docs/workflow/02-research.md) → `docs/research/<sujet>.md`, avec la légende D/T/H/O.
- [Prototype minimal](docs/workflow/03-prototyping.md) : un exemplaire de chaque élément risqué ; un contrôle qui
  peut échouer pour chaque risque ; coût par unité mesuré.
- [Itération sur preuves](docs/workflow/04-evidence-based-iteration.md) : skill `visual-iteration` ; journal
  numéroté ; [revue visuelle](docs/quality/checklists/visual-review.md) avant chaque présentation ; page de revue
  (`tools/review_page.py`).
- [Direction artistique](docs/workflow/05-art-direction.md) : variantes contrastées avec un contre-essai, vue annotée,
  aperçu en mouvement, choix écrit.

## 5. Produire, valider, livrer

- [Avant production](docs/quality/checklists/pre-production.md) : accord, extrait validé, registre relu, coût mesuré,
  chaîne reprenable (`tools/fingerprint.py`).
- [Validation](docs/workflow/07-validation.md) sur l'œuvre complète, dans les conditions finales
  (`tools/loop_check.py`, `tools/flicker.py`, `tools/review_video.py`).
- [Livraison](docs/quality/checklists/delivery.md) : définition de « terminé », rapport `docs/DELIVERY_REPORT.md`.

## 6. Pendant tout le projet

- **Reprise** : [liste](docs/quality/checklists/session-resume.md) au début de chaque session.
- **Communication** : ouvrir les résultats ; [points courts](templates/status-update.md).
- **Ne rien perdre** : archiver avant chaque nouvelle version ([modèle](templates/archived-version-readme.md)).

## 7. À la fin : enrichir le référentiel

Remplir `docs/RETROSPECTIVE.md` **dans le projet**, puis reporter ici les seuls enseignements génériques
([`CONTRIBUTING.md`](CONTRIBUTING.md#after-each-project)).
