# Rendu 3D précalculé

Pratiques **[éprouvé]** avec Blender (Cycles, GPU, débruitage OIDN), transposables à tout moteur de rendu précalculé,
sauf mention contraire.

## Architecture d'un projet de rendu reproductible

```
config/*.toml                  paramètres nommés : composition, matériaux, mouvement, qualité, encodage
scripts/prep/                  préparation des données (segmentation, profondeur, calques)
scripts/build/                 génère la scène depuis la configuration
scripts/render/                rend une unité ou un paquet
scripts/post/                  réduction à la taille finale, stabilisation
scripts/qa/                    contrôles, comparatifs, pages de revue
scenes/<scene>_<version>.*     scène générée, textures empaquetées
renders/<version>/…            sorties séparées par version (hors de Git)
qa/<version>/…                 journaux, mesures, comparatifs, rapports
archive/<version>/             état complet de chaque version passée
```

- **La scène est générée**, jamais retouchée à la main : une modification durable passe par la configuration, puis par
  la régénération.
- **La version courante** est lue dans la configuration (`project.version`) ; tous les scripts en dérivent leurs
  chemins, ce qui évite de mélanger les sorties.
- **Surcharge sans modifier la configuration** (`build --set 'clé=valeur'`) : c'est la base des variantes et des essais.
- **Le fichier de scène s'ouvre sans exécuter de script** : pilotes d'animation en expressions simples, textures
  empaquetées, contrôleurs exposés comme propriétés nommées.
- **Gestion des couleurs neutre** (« Standard » dans Blender) quand une texture source doit être restituée telle
  quelle : une transformation de vue filmique la modifierait.

<a id="reproducibility"></a>

## Reproductibilité

- Toute la géométrie procédurale dérive d'**une graine de projet** ; chaque élément a sa sous-graine, dérivée d'une
  valeur stable (nom, numéro, CRC32), **jamais** de `hash()` ([A11](../quality/anti-patterns.md#a11)).
- **La numérotation sert de graine** : ajouter un élément ne doit pas renuméroter les autres ; les numéros existants
  sont réservés.
- Un élément de référence peut être **figé** (sa géométrie relue depuis la référence), puis vérifié identique au bit
  près.
- Révisions des modèles d'IA et versions des dépendances figées (fichier de verrouillage, manifeste des modèles).
- Chaque ressource externe a sa provenance, sa licence et ses empreintes (`SHA256SUMS`, manifeste de provenance).

## Banc d'essai

- **Recadrages en qualité finale** sur la scène chargée : bien plus rapide que l'image entière, suffisant pour juger
  une matière.
- **Modifications nommées** appliquées à une copie en mémoire ; la scène de référence n'est jamais modifiée par un
  essai.
- **Planches** générées automatiquement : colonnes libellées, même cadrage.
- **Variantes nommées** sauvegardées à part, promues ensuite comme scène principale par copie (l'ancienne étant
  conservée).
- **Court mouvement de caméra** sur image figée (petite ellipse, quelques dizaines de positions) pour voir si les
  reflets révèlent le relief ; mesure associée : écart-type temporel dans l'élément.
- **Vue de trois quarts** en matière neutre, avec une caméra partagée entre variantes, pour comprendre les volumes.

<a id="diagnosis-by-elimination"></a>

## Diagnostic par extinction

Méthode pour tout défaut lumineux d'origine inconnue :

1. Rendre la zone en qualité finale : c'est la référence.
2. Neutraliser **une** cause possible à la fois :
   - une source de lumière ou une partie de l'environnement ;
   - une surface peinte en noir ;
   - un élément caché ;
   - un type de rayon coupé (transmission, réflexion) ;
   - une face passée en réfraction pure.
3. La cause est celle dont la neutralisation fait disparaître le défaut.
4. Corriger **localement** (réglage par élément) plutôt que globalement si la cause sert ailleurs.

Les défauts typiques ainsi résolus : liserés continus sur des arêtes, bandes claires élargies par le flou de
profondeur de champ, plages grises dues au reflet d'une source sur une surface courbe, stries renvoyées par des
facettes inclinées, dominantes colorées venues d'une source secondaire.

## Matériaux transparents

- **Vérifier dans le moteur le sens de chaque paramètre** : la transmission du shader n'est pas la lumière
  effectivement transmise. Un petit banc de calibration mesure ce qui passe réellement ; certains paramètres sont sans
  effet dans certaines conditions ([A9](../quality/anti-patterns.md#a9)).
- **Un verre sombre devant un fond sombre ne montre que ses reflets** : pour qu'il garde une information de surface,
  lui donner quelque chose à refléter (lumières localisées, grains brillants, fissures internes).
- **Les arêtes fines et intermittentes viennent de l'éclairage** (sources étroites, technique dite *white-line*) et
  d'un micro-chanfrein, pas d'un épaississement ; un plancher d'intensité produit un cadre continu.
- **La liaison de lumière** (*light linking*) donne à un élément un éclairage propre qui n'éclaire rien d'autre.
- **Épaisseur et relief se découplent** : exprimer le relief en fraction de la taille de la face, pas de l'épaisseur,
  sinon amincir aplatit tout.
- **Teinte spéculaire sur diélectrique** : elle tend vers le blanc aux incidences rasantes ; un reflet coloré à tous
  les angles demande un mélange spéculaire masqué.
- **La profondeur de champ décide de ce qui se voit** : à grande ouverture, les détails brillants deviennent des
  pastilles floues ; il faut choisir l'ouverture d'après la référence.
- **Contrôles de géométrie automatiques** : orientation par le volume signé, fermeture (arêtes non manifold), côté des
  faces, auto-intersections ([A13](../quality/anti-patterns.md#a13)).

## Scintillement : diagnostic et traitement

**Mesure.** Accélération temporelle de la luminance, A(t) = I(t+1) − 2·I(t) + I(t−1) ; on compte les pixels qui
s'allument puis s'éteignent, à la taille finale, sur les images sources puis sur les vidéos encodées
([`flicker.py`](../../tools/README.md#flickerpy)).

**Mécanisme typique.** Un pixel d'intensité moyenne à l'écran est la moyenne de quelques reflets très intenses (des
dizaines ou centaines de fois le blanc d'affichage). Seuls quelques échantillons sur des centaines les touchent, et ce
nombre change d'une image à l'autre. Le débruiteur traite chaque image séparément : il ne peut rien.

**Localiser l'étape.** Comparer rendu, débruitage, réduction de taille, encodage et lecture. Si l'encodage ne
scintille pas plus que les images sources, le défaut naît au rendu.

**Leviers, du plus fidèle au plus destructif :**

| Levier | Effet | Coût ou perte |
|---|---|---|
| Plafond d'échantillons relevé (seuil adaptatif inchangé) | Réduit le scintillement des arêtes ; image moyenne identique | Temps multiplié sur la zone |
| **Stabilisation temporelle compensée en mouvement, limitée aux pics** | Forte réduction ; vidéos plus légères | Quelques dixièmes de seconde par image ; aucun flou spatial |
| Rendu suréchantillonné (200 %) | Réduction modérée | Temps ×4 |
| Graine fixe | Faible | Le bruit restant reste figé à l'écran |
| Écrêtage, sources moins intenses | Efficace | Ternit et amincit les traits voulus : relève de la direction artistique |
| Débruitage temporel, moyenne d'images | À éviter | Traînées sur les reflets ; détails effacés |

Combinaison recommandée : un plafond raisonnable, puis la stabilisation
([`stabilize.py`](../../tools/README.md#stabilizepy)), validée par une mesure avant/après et une inspection à 200 %.

## Coût de rendu

- **Mesurer avant d'optimiser.** Quand l'échantillonnage sur le GPU domine (cas fréquent), seuls comptent le nombre de
  pixels, le nombre d'échantillons et le coût d'un échantillon (rebonds dans les matériaux transparents, complexité
  des matériaux).
- **Leviers habituels**, à mesurer un par un :
  - plancher d'échantillons adaptatifs abaissé (souvent sans perte) ;
  - seuil adaptatif relevé (surveiller les zones sombres) ;
  - plafond d'échantillons abaissé ;
  - détails invisibles à la taille finale supprimés ;
  - suréchantillonnage réduit (perte de netteté à mesurer) ;
  - rebonds limités à ce qui est visible.
- **Suréchantillonner puis réduire** (125 à 150 %, réduction Lanczos en lumière linéaire) peut donner une netteté que
  le débruitage seul n'atteint pas ; le gain se démontre à chaque projet.
- **Coût de construction** à suivre aussi : nombre de faces, mémoire au pic, temps de construction.
- La **première image** d'un processus inclut la préparation de la scène : elle ne compte pas dans le régime établi.

## Boucle parfaite

- Tous les mouvements sont **périodiques sur la période exacte**, avec raccord en position **et** en vitesse.
- **Pas d'image terminale dupliquée** : l'image N n'est pas rendue, puisque c'est l'image 0.
- Contrôle de la scène : l'état à la période est égal à l'état initial (transformations et déformations à écart nul).
- Contrôle des images : l'écart dernière → première image est du même ordre que l'écart moyen entre deux images
  consécutives ([`loop_check.py`](../../tools/README.md#loop_checkpy)).
- Stabilisation **en boucle fermée** : l'image 0 a pour voisine la dernière image.
