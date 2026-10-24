# Production Playbook

Référentiel de méthode pour **concevoir, produire, itérer, valider et livrer** un travail technique ou créatif, mené
par une personne qui dirige et un agent d'IA (Claude Code) qui exécute, recherche et vérifie.

Il documente **comment réaliser les travaux**, pas les travaux eux-mêmes. Il ne contient aucun livrable, aucune
réalisation, aucun asset et aucune donnée de projet ([décision 0007](docs/decisions/0007-no-project-content.md)). Tout
y est générique et réutilisable, quels que soient le domaine, la technique ou la direction artistique.

## Niveau de maturité des pratiques

Chaque pratique porte un niveau, pour savoir sur quoi l'on peut s'appuyer :

| Niveau | Signification |
|---|---|
| **[éprouvé]** | Appliqué en production réelle, avec un effet constaté. |
| **[extrapolé]** | Dérivé de pratiques éprouvées pour un autre contexte, sans y avoir encore été appliqué. |
| **[proposé]** | Nouveau, destiné à combler un manque. À éprouver. |

Les preuves restent dans les projets concernés : le référentiel ne garde que la règle qui en découle.

## Par où commencer

| Je veux… | Lire |
|---|---|
| Comprendre la philosophie en 10 minutes | [Principes](docs/principles.md) |
| Démarrer un nouveau projet | [`GETTING_STARTED.md`](GETTING_STARTED.md) |
| Suivre le déroulé complet, du besoin à la livraison | [Workflow](docs/workflow/README.md) |
| Adapter la méthode à un autre domaine ou une autre direction artistique | [Adapter](docs/workflow/adapting.md) |
| Savoir quand un travail est « terminé » et comment le juger | [Qualité](docs/quality/README.md) |
| Éviter les erreurs classiques | [Anti-modèles](docs/quality/anti-patterns.md) |
| Utiliser une liste de contrôle | [Listes de contrôle](docs/quality/checklists/README.md) |
| Retrouver les méthodes par technique (rendu 3D, animation 2,5D, vidéo web, application web, IA) | [Domaines](docs/domains/README.md) |
| Configurer Claude Code et choisir ses outils | [Outillage](docs/tooling/README.md) |
| Réutiliser des scripts testés | [`tools/`](tools/README.md) |
| Partir d'un modèle de document ou de demande | [`templates/`](templates/README.md) |
| Installer des skills dans un projet | [`skills/`](skills/README.md) |
| Comprendre une décision structurante | [Décisions](docs/decisions/README.md) |
| Savoir ce qui reste à faire pour renforcer la méthode | [`ROADMAP.md`](ROADMAP.md) |
| Enrichir le référentiel | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Vérifier le vocabulaire | [`GLOSSARY.md`](GLOSSARY.md) |

## La méthode en une page

1. **Cadrer avec des hypothèses explicites.** Reformuler le besoin, inspecter l'existant réel, écrire les hypothèses,
   ne poser que les questions qui changent la solution. → [Cadrage](docs/workflow/01-scoping.md)
2. **Rechercher de façon ciblée, puis s'arrêter.** Sources primaires d'abord, forums comme pistes, chaque affirmation
   étiquetée, arrêt dès qu'un essai est possible. → [Recherche](docs/workflow/02-research.md)
3. **Lever les risques sur un prototype minimal**, avant toute production. → [Prototype](docs/workflow/03-prototyping.md)
4. **Itérer sur des preuves.** Un essai isolé, une variable à la fois, un échantillon avant de généraliser, un
   diagnostic par extinction, un avant/après à conditions identiques. → [Itération](docs/workflow/04-evidence-based-iteration.md)
5. **Laisser la direction artistique à celui qui juge.** Variantes contrastées, rôle de chaque élément, choix écrit.
   → [Direction artistique](docs/workflow/05-art-direction.md)
6. **Produire seulement après avoir mesuré le coût réel.** Production reprenable, protégée par une empreinte,
   versions séparées, rien supprimé. → [Production](docs/workflow/06-production.md)
7. **Valider dans les conditions finales.** Taille finale, vitesse normale, œuvre entière, lecture en avant, dernière
   version. Les mesures complètent le jugement. → [Validation](docs/workflow/07-validation.md)
8. **Livrer des fichiers qui existent, s'ouvrent et ont été contrôlés.** Le bilan sépare terminé, testé et limites.
   → [Livraison](docs/workflow/08-delivery.md)
9. **Rendre la reprise possible sans la conversation.** Journal, versions archivées, registre des consignes.
   → [Continuité](docs/workflow/09-continuity.md)
10. **Montrer plutôt que décrire.** Ouvrir le résultat, faire des points courts, garder l'objectif en tête.
    → [Communication](docs/workflow/10-communication.md)

## Organisation

```
docs/
  principles.md        Pourquoi : seize principes indépendants du projet
  workflow/            Quoi et quand : dix étapes, critères de fin, adaptation
  quality/             Comment juger : définition de « terminé », grille, anti-modèles, listes de contrôle
  domains/             Comment, par technique : guides de domaine
  tooling/             Avec quoi : inventaire, provenance et licences, Claude Code
  decisions/           Décisions structurantes de la méthode (ADR)
templates/             Modèles de documents et de demandes
skills/                Skills Claude Code prêts à installer
tools/                 Scripts Python testés (mesure, contrôle, stabilisation, empreinte, revue)
scripts/               Vérification du référentiel, création d'un projet
```

## Vérification

Le référentiel se vérifie lui-même, en local et dans la CI (`.github/workflows/ci.yml`) :

```bash
python3 scripts/check_repo.py          # liens, ancres, niveaux de maturité, structure, secrets
uv run --no-project --python 3.12 --with numpy --with opencv-python-headless --with pytest pytest tools/tests -q
```

## Ce que ce dépôt n'est pas

- **Pas une archive de projets** : ni réalisations, ni livrables, ni retours d'expérience nominatifs, ni chiffres de
  projet. Chaque projet garde son propre bilan ; seuls les enseignements génériques remontent ici.
- **Pas un catalogue de styles** : aucun choix esthétique n'est prescrit
  ([décision 0002](docs/decisions/0002-method-separate-from-aesthetics.md)).
- **Pas figé** : la méthode est versionnée ([`CHANGELOG.md`](CHANGELOG.md)) et évolue par décisions documentées.
