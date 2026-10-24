---
name: work-log
description: Ouvrir, reprendre ou clore un travail long (plusieurs étapes ou sessions) avec son journal dans docs/work-logs/. À utiliser au début d'une tâche en plusieurs étapes, à la reprise après une interruption ou une compaction du contexte, et à la fin du travail.
---

# Travail long et reprise fiable

Un chantier, c'est une branche (s'il y a un dépôt Git) et un journal `docs/work-logs/YYYY-MM-DD-sujet.md` (modèle :
`docs/work-logs/_template.md`). Le journal, `git log` et le registre des consignes (`docs/instruction-register.md`)
doivent suffire à reprendre sans l'historique de la conversation.

## Reprendre (toujours en premier)

1. État réel : `git status`, `git branch --show-current`, `git log --oneline -15` ; processus actifs (calculs,
   serveurs) ; espace disque. Ne jamais toucher aux processus d'autres projets.
2. Lire le journal du chantier (le plus récent de `docs/work-logs/`, ou celui de la branche) et le registre des
   consignes.
3. Vérifier l'état réel avant de continuer : relancer les contrôles de « Validation » du journal ; une case cochée
   sans preuve est à revérifier.
4. Reprendre à « Prochaines actions ». Si le journal contredit les fichiers, les fichiers font foi : corriger le
   journal.

## Ouvrir

1. Branche dédiée depuis la branche principale (`type/sujet-court`) ; archiver l'état courant si le projet n'a pas de
   Git.
2. Copier `docs/work-logs/_template.md` ; remplir objectif, critère essentiel, périmètre, référence initiale
   (résultats mesurés des contrôles avant toute modification).
3. Découper le plan en étapes vérifiables, chacune avec son critère de fin.
4. Reporter dans le registre les consignes de la demande (actives, remplacées).

## Tenir à jour (à chaque étape terminée, avant chaque commit)

- Statut, décisions prises (et pourquoi), commits, validations exécutées avec leurs résultats, prochaines actions.
- Distinguer **vérifié** (commande lancée, résultat cité), **hypothèse** et **à faire** ; distinguer mes contrôles
  de la validation de l'utilisateur.
- Rester concis : le détail vit dans les fichiers, les tests et les messages de commit.

## Clore

- Statut « terminé » ; bilan : livré, vérifié (réel ou émulé), limites ; chaque demande avec son état.
- Reporter ce qui doit durer ailleurs (décisions, `CLAUDE.md`, et les enseignements génériques dans le référentiel de
  méthode) : le journal est une trace, pas une source de règles.
