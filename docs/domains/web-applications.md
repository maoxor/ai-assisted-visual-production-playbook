# Application web : test d'abord, couches, garde-fous, Git

Pratiques **[éprouvé]** sur des applications web (API Python, interface React), quand on travaille **à plusieurs** et
**avec un agent**, sauf mention contraire.

## Instructions pour l'agent : une hiérarchie courte

| Support | Contenu | Chargement |
|---|---|---|
| `CLAUDE.md` racine | Carte du dépôt, commandes de vérification, règles impératives, garde-fous, continuité. **Court** | À chaque session |
| `CLAUDE.md` de sous-dossier | Conventions locales (back, front), implémentations de référence | Quand on travaille dans ce dossier |
| `.claude/rules/*.md` | Règles ciblées : migrations, tests, règles métier | À la demande, par chemin |
| `.claude/skills/*/SKILL.md` | **Procédures** ([`test-first-change`](../../skills/test-first-change/SKILL.md), [`work-log`](../../skills/work-log/SKILL.md)) | Quand la tâche correspond |
| `.claude/settings.json` (hooks) | Ce qui doit arriver **à chaque fois**, de façon déterministe | Automatique |
| `AGENTS.md` | Renvoi vers `CLAUDE.md`, pour les autres outils | — |
| `docs/` | Architecture, invariants métier avec leur test, décisions, guides, journaux de chantier | Lien depuis `CLAUDE.md` |

**Une règle, une source** : les autres documents y renvoient.

## Règles impératives

1. **Test d'abord** pour tout changement de comportement : écrire le test, le voir échouer pour la bonne raison,
   corriger, le voir passer.
2. **Contrôle d'accès dans la couche service** ; la ressource d'autrui renvoie une 404.
3. **Couches à sens unique** (routes → service → accès aux données → schémas → modèles), vérifiées par un contrat
   exécutable (import-linter ou équivalent).
4. **Migrations immuables** une fois sur la branche principale.
5. **La source de vérité métier fait foi** : ne jamais déduire une règle du comportement du code sans la vérifier.
6. **Secrets** : jamais de `.env` lu, affiché ni commité ; aucune valeur par défaut pour un secret.
7. **Git** : jamais de travail direct sur la branche principale ; commits `type(portée): description` ; ni push ni
   fusion sans demande.
8. **Pas de reformatage de masse** : seul le code modifié suit le style du fichier.
9. **Garder l'architecture en place** : faire comme le voisinage ; s'en écarter seulement si l'autre solution est
   meilleure **et** que la raison est expliquée avant d'écrire le code.

## Procédure : livrer un changement, test d'abord

Détaillée dans le skill [`test-first-change`](../../skills/test-first-change/SKILL.md) :

1. **Cadrer** : comportement attendu en une phrase, cas limites ; lire l'implémentation de référence la plus proche ;
   s'arrêter et demander si une règle est ambiguë.
2. **Test d'abord**, selon la nature du changement :

   | Changement | Premier test |
   |---|---|
   | Bug | Test qui reproduit le bug, en échec pour la bonne raison |
   | Nouvelle règle | Tests unitaires, cas nominaux et limites |
   | Accès aux données | Test d'intégration sur une vraie base |
   | Nouvelle route | Propriétaire OK, autre utilisateur 404/403, non connecté 401 |
   | Refactorisation | Tests de caractérisation, verts **avant** de toucher au code |
   | Écran critique | Spec e2e (Playwright, fausse API) |

3. **Implémenter** le changement minimal, dans la bonne couche ; rien hors périmètre (noter les autres problèmes).
4. **Vérifier** en lançant les commandes et en citant leurs résultats.
5. **Documenter dans le même commit** ce que le changement rend faux : invariants, architecture, `CLAUDE.md`,
   décisions, déploiement.
6. **Committer** sur une branche dédiée : pourquoi, preuve (test en échec puis vert), limites ; relire le diff indexé
   (aucun fichier hors sujet, aucun secret).

## Garde-fous automatiques

- **Hooks Claude Code** : vérification immédiate du fichier modifié (lint, contrat d'architecture) ; refus de modifier
  une migration de la branche principale ; vérifications complètes **à la fin de chaque tour et avant tout
  `git commit`** ; lecture des `.env` refusée par les permissions ([Claude Code](../tooling/claude-code.md#hooks)).
- **Les hooks sont eux-mêmes testés**, avec des entrées simulées, en CI.
- **CI** : lint, architecture, tests unitaires et d'intégration (vraie base), e2e en parallèle, immuabilité des
  migrations, audit des dépendances, détection de secrets (gitleaks, faux positifs justifiés un par un).
- **Un contrôle en échec se corrige à la cause**, jamais en désactivant le test ou la règle.

## Git comme outil de traçabilité

- **Types de commits** : `fix`, `feat`, `docs`, `chore`, `refactor`, `style`, `test`, `perf`, `ci` ; fusions
  explicites.
- **Corps de message type** : problème, mesure avant, changements, mesure après, preuve par test, renvoi au journal du
  chantier.
- **Branche par chantier** (`type/sujet-court`), journal du chantier versionné dans `docs/` (skill
  [`work-log`](../../skills/work-log/SKILL.md)).
- **Décisions structurantes** au format ADR ([modèle](../../templates/decision-record.md)) ; une décision acceptée ne se
  remet en cause que par une nouvelle décision qui la remplace.
- **Identité Git** : celle configurée sur le poste, jamais une identité reprise des commits existants.

## Direction artistique d'une interface

- La personne qui dirige juge sur le rendu et l'expérience, au niveau des meilleurs sites et jeux du domaine, jamais
  sur le nombre d'écrans ou les contrôles techniques.
- Prototyper **en mouvement** et filmer avant de conclure ; partager les galeries en privé.
- Ne développer qu'**après validation explicite** d'une direction.
- Concevoir une chorégraphie d'animation (arrivée, entrées, survols, ralenti pour la juger), pas des fondus génériques.
- Mesurer la performance sans attendre la demande (profilage, Lighthouse, images par seconde, comparaison avec
  l'existant).
- Dire ce qui n'est pas testé : simulateurs iOS et émulateurs Android ne sont pas des appareils réels ; Playwright ne
  reproduit pas toutes les règles d'activation du son.
