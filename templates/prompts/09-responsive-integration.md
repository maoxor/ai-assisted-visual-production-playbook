# Intégration responsive : rotation, tablettes, écran partagé

```markdown
Vérifie que notre intégration couvre aussi **la rotation de l'écran sur mobile et l'affichage sur tablette**, en
tenant compte du cadrage, du chargement et des performances.

Définis puis teste le comportement dans chaque situation : téléphone portrait et paysage ; tablette portrait et
paysage ; rotation pendant le chargement ou la lecture ; redimensionnement et écran partagé.

Choisis les variantes selon les dimensions et le rapport d'aspect de la zone affichée, plutôt que sur une distinction
« mobile ou bureau ». Vérifie si les variantes existantes suffisent ou si une variante intermédiaire est réellement
nécessaire.

Préserve la composition : <éléments importants> visibles, espace pour l'interface, pas d'étirement, recadrage
maîtrisé.

Lors d'une rotation : pas d'écran noir, pas de changements répétés de source, pas de téléchargements inutiles ni de
redémarrage perturbant. Si un changement est nécessaire, transition propre en conservant la position <dans la boucle>.

Adapte la définition et le débit aux capacités : un appareil à haute densité ne doit pas recevoir automatiquement le
fichier le plus lourd. Prévois un repli fixe.

Indique précisément ce qui est déjà couvert, ce qui manque et ce qui reste à tester. Tableau des formats, cadrages et
sources retenus ; vérifie fluidité et réactivité avant, pendant et après la rotation. Distingue appareils physiques et
émulation.
```
