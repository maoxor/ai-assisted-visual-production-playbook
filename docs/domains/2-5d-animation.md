# Animation 2,5D d'un sujet à partir d'une image unique

Pratiques **[éprouvé]**, sauf mention contraire.

## Objectif et limite fondamentale

Donner vie à une illustration existante (respiration, micro-expressions, éléments secondaires) **sans régénérer le
sujet** et sans trahir son identité, son anatomie, ses proportions ni ses détails
([décision 0004](../decisions/0004-preserve-the-source.md)). La vue est unique : on n'invente pas une rotation qui
révélerait un profil absent ; les amplitudes restent dans ce que la vue peut supporter.

## Méthode : calques projetés depuis la caméra

1. **Découper ce qui doit bouger, et seulement cela** : la plaque (corps et fond), la tête, les éléments secondaires.
   Chaque découpe ajoutée doit apporter un bénéfice.
2. **Masques précis**, surtout sur les contours sombres et les raccords : segmentation assistée par points, puis
   correction manuelle.
3. **Profondeur relative** estimée par un modèle local pour donner un relief à chaque calque (vérifier la licence de
   la variante utilisée : [guide IA](ai-models-and-assets.md)).
4. **Maillages placés sur les rayons de la caméra de repos** : au repos, la caméra voit exactement l'image source.
   Quand le sujet bouge, la texture reste attachée à la géométrie, sans glisser, et les effets placés devant (verre,
   reflets) réagissent à l'état animé.
5. **Reconstruire seulement les zones cachées qui seront révélées**, par reflet de la texture voisine ou par copie
   d'exemplaires ; résoudre les bords pour que l'état de repos recompose la source.
6. **Contrôleurs nommés** et multiplicateurs par famille de mouvement : 0 donne l'état de repos, 1 le réglage normal, 3
   l'exagération pour le diagnostic.

## Déformer sans étirer : champs à ancres

- Une zone se déplace **d'un bloc** grâce à des noyaux à plateau, sans étirement ; l'étirement local est mesuré et
  plafonné.
- Des **ancres** (déplacement nul sur une zone ou une ligne) fixent ce qui ne doit pas bouger : centre et volume des
  lèvres, arête du nez, attaches.
- **Corriger la construction, pas l'amplitude** : si une zone « gonfle », c'est souvent qu'un mouvement voisin déplace
  ses bords ; des ancres règlent le problème sans réduire l'amplitude.
- **Quand la géométrie ne peut pas aller plus loin, utiliser l'ombre** : une ouverture (narine, pli) qui ne peut pas
  s'agrandir sans étirer la peau devient lisible par l'assombrissement de son sillon.
- **Plis animés** : sur une texture autoéclairée, seule la couleur peut porter l'approfondissement d'un pli ; des
  cartes de plis se creusent avec le poids du mouvement.

## Rythme et hiérarchie du mouvement

- **Le torse porte le souffle** ; le cou, la base du visage et les épaules suivent avec des **décalages** et des
  **amplitudes** différents ; la tête suit moins, pour rester posée.
- **Courbe de respiration dessinée par phases** plutôt qu'une sinusoïde : inspiration active, maintien, expiration à
  rappel élastique, pause. Plusieurs respirations de durées et d'amplitudes différentes dans la boucle, avec raccord
  exact.
- **Canaux précalculés par élément**, une clé par image : chaque élément lit sa propre courbe.
- **Micro-expressions ponctuelles**, réparties dans la boucle, jamais simultanées ni répétées à chaque respiration.
- **Pas d'agitation permanente** : la pause à chaque cycle est essentielle.
- **Comparer plusieurs rythmes dans l'œuvre complète** et choisir sur la présence, à vitesse normale.

## Éléments graphiques animés (tracés, signes, inscriptions)

1. **Isoler** la couche d'encre (alpha et couleur prémultipliée) pour que l'état de repos restitue la source à
   l'identique ; reconstruire le support dessous, teinte recalée sur le voisinage.
2. **Vectoriser** : squelette, puis traits orientés dans le sens d'écriture.
3. **Animer la forme**, pas seulement la lumière : la lumière accompagne, elle ne remplace pas le changement de forme.
4. **Comparer plusieurs directions** (réécriture le long des traits, recomposition) et retenir celle dont **chaque
   état intermédiaire est un dessin net**.
5. **Structurer la séquence** : intention, transformation, tenue, retour ; comparer plusieurs rythmes à la taille
   finale.
6. **Précalculer** dans un atlas lu aux coordonnées de la surface, pour que l'élément reste attaché pendant les
   mouvements ; les reflets montrent la même animation.

## Contrôles

- **Gros plan sans effets, caméra fixe**, sur toute la boucle, à vitesse normale : réel, figé, exagéré ×3, ralenti.
- **Audit du rig** : ce que le rig anime réellement ; vérifier déformations et matériaux animés, pas seulement les
  matrices des objets.
- **Flux optique par zone** et planches repos / pic / différence, mouvement par mouvement.
- **Zones protégées** suivies sur leur position animée, pas sur des coordonnées fixes.
- **Perceptibilité** : le mouvement se lit à vitesse normale et à la taille finale ; le ralenti ne sert qu'au
  diagnostic.

## Ce qui échoue souvent

| Essai | Pourquoi |
|---|---|
| Rotation marquée de la tête | Révèle un profil absent de la source |
| Grande déformation géométrique d'une ouverture | Étire la peau ; préférer l'ombre |
| Frémissement permanent d'éléments secondaires | Agitation qui détourne l'attention du sujet |
| Lueur interne décorative | Tache lumineuse sans rôle |
| Recomposition libre d'un tracé | États intermédiaires confus |
