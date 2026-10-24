# 7. Validation dans les conditions finales

**Objectif.** S'assurer que l'œuvre complète, et non un extrait ou un prototype, tient dans les conditions de
diffusion réelles, et rendre visible ce qui n'a pas pu être vérifié.

## Deux niveaux [éprouvé]

| Niveau | Qui | Forme |
|---|---|---|
| **Contrôles** | L'agent | Commandes exécutées, résultats cités, captures et vidéos à inspecter |
| **Validation** | La personne qui dirige | Décision explicite après avoir vu le résultat |

Les deux ne se confondent jamais dans un bilan ([P2](../principles.md#p2)).

## Familles de contrôles [éprouvé]

Le détail par moment est dans les [listes de contrôle](../quality/checklists/README.md).

1. **Fidélité** : le sujet, sans effets, comparé à la source, à cadrage et gestion des couleurs équivalents.
2. **Localité des effets** : un effet n'agit que là où il doit agir ; on le vérifie en isolant les autres effets.
3. **Superpositions** : aucune zone noire, aucun contour parasite, aucun artefact quand plusieurs éléments se
   superposent.
4. **Bords et marges** : aucun bord visible aux positions extrêmes, ni directement ni par reflet ou réfraction.
5. **Animation** : aucun saut, aucune rupture de vitesse, aucun étirement ni glissement de texture ; mouvement
   perceptible à vitesse normale.
6. **Boucle** : contrôlée sur la **période complète**, sans dernière image dupliquée (pause), avec un raccord du même
   ordre que l'écart entre deux images consécutives. Un extrait court ne valide pas une boucle longue.
7. **Stabilité temporelle** : scintillement mesuré à la taille finale, sur les images sources puis sur les vidéos
   encodées ; une variation voulue n'est pas comptée.
8. **Encodage** : détails préservés, noirs sans aplats en escalier, raccord de boucle sans saut de qualité.
9. **Lecture ou exécution réelle** : dans les navigateurs, appareils ou environnements cibles ; on sépare le réel de
   l'émulé.
10. **Éléments résiduels** : signature, logo, texte provisoire, filigrane, élément de debug ; contrôle explicite sur
    **tous** les livrables ([A3](../quality/anti-patterns.md#a3)).
11. **Demandes de l'itération** : chacune reprise avec son état ([P15](../principles.md#p15)).

## Extrait de validation [éprouvé]

Avant l'œuvre complète, on produit un **véritable extrait de la production finale** : une suite continue d'unités
(quelques secondes consécutives pour une vidéo), avec les réglages et le traitement de livraison, sur un passage qui
contient les mouvements et effets importants. Des images fixes, quelques unités répétées ou un aperçu dégradé **ne
permettent pas** cette validation ([A1](../quality/anti-patterns.md#a1)). On livre l'extrait au format final, l'accès
aux sources (pour distinguer défaut de calcul et défaut de compression) et les temps réellement constatés.

## Vidéos de contrôle [éprouvé]

- **En avant, en boucle, jamais en aller-retour** ([A7](../quality/anti-patterns.md#a7)).
- **Œuvre entière animée**, en plus des gros plans.
- **Côte à côte libellé**, à taille et vitesse identiques.
- **Dernière version** ; les versions passées seulement sur demande.
- **Plusieurs tours de boucle** pour juger le raccord.
- **Montrer tôt** : un rendu court ou partiel vaut mieux qu'une longue attente.

Outils : [`review_video.py`](../../tools/README.md#review_videopy) et
[`review_page.py`](../../tools/README.md#review_pagepy).

## Critère de fin

Contrôles de l'œuvre complète exécutés et cités ; vidéos de revue produites et ouvertes ; lecture réelle vérifiée dans
les environnements accessibles ; vérifications impossibles listées ; validation de la personne qui dirige demandée, ou
consignée si elle a été donnée.
