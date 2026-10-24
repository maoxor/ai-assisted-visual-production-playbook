# 0006 — Toute production longue est reprenable et protégée par une empreinte

- **Statut** : acceptée
- **Date** : 2026-10-25
- **Décidée par** : la personne qui dirige (exigence), l'agent (mise en œuvre)

## Contexte

Les productions longues sont souvent interrompues (changement de version, correction tardive, mise en veille, machine
partagée). Reprendre sur la seule présence des fichiers mélange des unités calculées à partir d'états différents, ce
qui produit des livrables faux et difficiles à détecter.

## Décision

- Chaque production écrit l'empreinte de ses dépendances (sources, configurations, scripts, version du logiciel,
  profil de qualité) à côté de ses sorties.
- À la reprise, si l'empreinte diffère, les sorties existantes sont **déplacées** dans `_stale/`, jamais supprimées.
- Une unité n'est faite que si son fichier est complet ; les unités sont produites par paquets ; l'espace disque est
  vérifié avant chaque paquet.
- Pendant le calcul, on ne modifie aucune dépendance.

## Conséquences

- Toute modification d'une dépendance pendant une production l'arrête au paquet suivant : c'est voulu.
- L'alimentation et la mise en veille de la machine font partie des préalables ([A15](../quality/anti-patterns.md#a15)).

## Vérification

Outil testé : [`fingerprint.py`](../../tools/README.md#fingerprintpy) (tests `test_ensure_*` et `test_pending_*`).
