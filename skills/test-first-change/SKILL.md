---
name: test-first-change
description: Livrer une correction, une évolution ou une refactorisation de code applicatif : cadrage, test d'abord, implémentation, vérifications citées, documentation, commit. À utiliser avant de modifier du code applicatif.
---

# Livrer un changement, test d'abord

Changement court et local : suivre ces étapes directement. Plusieurs étapes ou plusieurs sessions : ouvrir aussi un
journal (skill `work-log`).

## 1. Cadrer

- Formuler le comportement attendu en une phrase, avec ses cas limites.
- Situer le code (`docs/architecture.md` s'il existe, puis recherche ciblée) et lire l'implémentation de référence la
  plus proche ; en reprendre les conventions.
- Si une règle métier est ambiguë ou contredit le code : s'arrêter et demander, ne pas inventer.

## 2. Test d'abord

| Changement | Premier test à écrire |
|---|---|
| Bug | Test qui reproduit le bug ; l'exécuter, constater l'échec **pour la bonne raison** |
| Nouvelle règle ou formule | Tests unitaires des cas nominaux et limites |
| Accès aux données, requête, transaction | Test d'intégration sur une vraie base |
| Nouvelle route | Propriétaire OK, autre utilisateur 404/403, non connecté 401 |
| Refactorisation | Tests de caractérisation du comportement actuel, verts AVANT de toucher au code |
| Écran ou parcours critique | Spec e2e (fausse API) |

## 3. Implémenter

- Le changement minimal qui fait passer le test, dans la bonne couche ; pas de nombre magique ; contrôle d'accès dans
  le service.
- Puis refactoriser si utile, tests toujours verts. Rien hors du périmètre demandé : noter les autres problèmes dans le
  journal ou les signaler.

## 4. Vérifier (et citer les résultats)

Les commandes de vérification du `CLAUDE.md` du projet, au minimum pour la partie touchée. Un contrôle en échec se
corrige à la cause : ne jamais désactiver une règle ni un test.

## 5. Documenter

Mettre à jour dans le même commit ce que le changement rend faux ou incomplet : invariants, architecture, `CLAUDE.md`,
décisions (`docs/decisions/`), déploiement.

## 6. Committer

- Sur une branche dédiée, jamais sur la branche principale ; pas de push ni de fusion sans demande.
- Message `type(portée): description` (`fix`, `feat`, `refactor`, `test`, `docs`, `chore`, `ci`, `perf`) ; corps qui
  explique le pourquoi, la mesure avant/après, la preuve (test en échec puis vert) et les limites.
- `git diff --staged` relu : aucun fichier hors sujet, aucun secret, aucun fichier de debug. Identité Git : celle
  configurée sur le poste.
