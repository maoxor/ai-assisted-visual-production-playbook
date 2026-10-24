# 3. Prototype minimal

**Objectif.** Vérifier sur le plus petit cas possible que les risques principaux sont maîtrisables, avant d'investir
dans la production.

## Principe [éprouvé]

Le prototype contient **un exemplaire de chaque élément risqué**, et rien d'autre. Pour une scène composée, par
exemple : le sujet, un élément d'effet devant lui, un élément de premier plan et un court mouvement de caméra. Pour une
application : une route de bout en bout, avec ses tests.

Il est décidé dès l'étude de faisabilité et réalisé avant l'œuvre complète.

## Ce que le prototype doit prouver

Pour chaque risque, on prévoit un contrôle **qui peut échouer** :

| Risque type | Contrôle |
|---|---|
| Fidélité au sujet ou à la source | Rendu de l'état de repos comparé à la source, à gestion des couleurs équivalente (PSNR, ꟻLIP, différence visuelle) |
| Localité d'un effet | Déplacer l'effet en plusieurs positions et mesurer l'écart hors de son emprise |
| Superpositions | Empiler les éléments transparents ou les couches ; aucune zone noire, aucun artefact |
| Bruit et stabilité | Scène figée rendue avec plusieurs graines ; écart-type dans les zones sensibles |
| Raccord de boucle | État de la scène à la période comparé à l'état initial |
| Bords révélés | Marges aux positions extrêmes de la caméra ou de la mise en page |
| Coût | Temps par unité en qualité finale |

## Variantes à comparer dès le prototype [éprouvé]

Quand deux techniques sont possibles (effet physique ou compositing, par exemple), on les compare sur le prototype et
l'on retient celle qui respecte le mieux le cahier des charges.

## Critère de fin

Chaque risque identifié au cadrage a un résultat mesuré et une capture ; le coût par unité est connu ; les risques non
levés sont écrits avec la manière de les traiter.

## Piège [éprouvé]

Un prototype qui « marche » ne valide pas la production : plus d'éléments, un traitement final et un sujet animé font
apparaître des défauts absents du prototype. Les contrôles du prototype sont **adaptés** au nouveau périmètre, pas
recopiés : une comparaison pixel à pixel avec la source ne vaut que pour l'état de repos, et une variation temporelle
voulue n'est pas du scintillement ([A18](../quality/anti-patterns.md#a18)).
