# 0004 — Préserver l'œuvre source ; l'IA estime, elle ne régénère pas

- **Statut** : acceptée
- **Date** : 2026-10-25
- **Décidée par** : la personne qui dirige

## Contexte

Un projet peut partir d'une œuvre existante (illustration, photographie, rendu d'un tiers). La régénérer par IA
trahit son identité, ses détails et souvent les droits de son auteur.

## Décision

- Quand une œuvre source existe, elle est restituée telle quelle à l'état de repos, et la fidélité est contrôlée.
- L'IA sert à **estimer** (segmentation, profondeur) et éventuellement à **reconstruire des zones cachées** limitées,
  sous contrôle visuel. Elle ne remplace jamais le sujet.
- Les modèles s'exécutent localement, avec révision et licence consignées.

## Conséquences

- Les animations se construisent par déformation contrôlée (calques projetés, champs à ancres), avec des amplitudes
  limitées à ce que la vue supporte ([animation 2,5D](../domains/2-5d-animation.md)).
- La fidélité devient un contrôle systématique : l'état de repos est comparé à la source.

## Vérification

Contrôle de fidélité dans la [liste avant production](../quality/checklists/pre-production.md).
