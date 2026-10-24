# Vidéo d'arrière-plan pour le web

Pratiques **[éprouvé]**, sauf mention contraire. Liste de contrôle associée :
[`web-video.md`](../quality/checklists/web-video.md).

## Principe directeur

**La vidéo est un décor : la page doit être utilisable et belle sans elle.** L'affiche (première image) s'affiche
tout de suite et constitue l'élément principal (LCP). La vidéo ne prend sa place que lorsqu'elle peut être lue sans
attente ; en cas d'échec, l'affiche reste.

## Trois familles de défauts, mesurées séparément

1. **Dans les images rendues** (scintillement, bruit) : mesurées sur les images sources avant tout encodage. Un défaut
   présent ici ne relève pas de l'encodage.
2. **Introduits par l'encodage** (blocs, aplats en escalier dans les noirs, microdétails perdus, saut de qualité au
   raccord) : vidéo décodée comparée aux sources image par image (VMAF, XPSNR, CAMBI, accélération temporelle) et revue
   côte à côte.
3. **À la lecture** (décodage, réseau, navigateur, charge de la page) : images perdues (`getVideoPlaybackQuality`),
   régularité et raccord (`requestVideoFrameCallback`), attentes, tâches longues, LCP, CLS, octets téléchargés.

## Exports

- **Variantes par cadrage et par définition réellement affichée** (par exemple 1440p, 1080p et 720p en paysage ;
  1080 et 720 de large en portrait). Réduction en lumière linéaire (Lanczos).
- **Trois codecs, par ordre de préférence** (réglages de départ, à valider par mesure sur chaque projet) :

  | Codec | Pour qui | Point de départ |
  |---|---|---|
  | AV1 10 bits (SVT-AV1) | Chrome, Firefox, Android récents | `-preset 4 -pix_fmt yuv420p10le -svtav1-params tune=0:enable-overlays=1:scd=0:film-grain=0`, CRF autour de 34 |
  | HEVC 10 bits, `hvc1` | Safari et navigateurs iOS | `-preset slow -x265-params aq-mode=3:psy-rd=1.5:psy-rdoq=1.0:no-open-gop=1`, CRF autour de 27 |
  | H.264 8 bits | Repli universel | `-preset slow -profile:v high -x264-params aq-mode=3:aq-strength=0.9:deblock=-1,-1`, CRF autour de 23 |

- **Une seule image-clé par boucle** (`-g` égal au nombre d'images) pour une scène qui scintille : pas de pompage de
  qualité à chaque groupe d'images. Mesurer ensuite le raccord encodé (l'image-clé est souvent un peu plus nette) et
  vérifier qu'il reste invisible.
- **Métadonnées BT.709, plage limitée**, pas d'audio, `+faststart`.
- **Fichiers nommés par empreinte de contenu** (cache « immutable ») et manifeste JSON inséré dans la page.
- **CRF choisis sur la séquence finale**, par un comparatif de qualité perçue (VMAF) et de poids, pas sur un extrait
  provisoire.
- **La stabilisation temporelle allège aussi** : le bruit d'une image à l'autre coûte des bits ; stabiliser avant
  d'encoder réduit le poids à qualité égale.

## Couleur dans les navigateurs Apple

Constat **[éprouvé]** dans WebKit sur macOS : la pile vidéo d'Apple convertit la vidéo avec un gamma d'environ 1,96
au lieu de la courbe sRGB, ce qui éclaircit les demi-teintes, quel que soit le codec ; l'étiquette de transfert est
sans effet. Le flux HEVC, servi seulement aux navigateurs Apple, peut être pré-compensé :

```
v = (sRGB→linéaire(x))^(1/1,961)
ffmpeg -vf "format=rgb48le,lutrgb=r='EXPR':g='EXPR':b='EXPR'"
EXPR = clip(maxval*pow(if(lte(val/maxval,0.04045),(val/maxval)/12.92,pow(((val/maxval)+0.055)/1.055,2.4)),1/1.961),0,maxval)
```

Toujours mesurer l'écart à l'écran (capture de la page comparée à l'affiche) avant et après compensation. Non vérifié
sur iPhone ou iPad physiques : à retester à chaque projet.

## Budgets de départ

Plafonds à confronter à la qualité obtenue, à ajuster avec justification.

| Budget | Valeur | Justification |
|---|---|---|
| Affiche mobile (AVIF) | 90 à 150 Ko | 4G lente : LCP ≤ 2,5 s |
| Affiche bureau (AVIF) | 150 à 300 Ko | Réseau fixe |
| Poids initial hors vidéo | ≤ 250 Ko mobile, ≤ 400 Ko bureau | La vidéo n'est demandée qu'après `load` |
| Script du fond | ≤ 6 Ko compressé, sans bibliothèque | Capacités natives du navigateur |
| Débit 720p | ≤ 1,5 Mb/s | Lecture progressive en 4G ordinaire |
| Débit 1080p | ≤ 3 Mb/s | Appareils plus confortables |
| Débit 1440p | ≤ 5 Mb/s | Écrans denses, réseau fixe |
| Fluidité | 0 image perdue sur 3 tours (bureau, décodage matériel) ; ≤ 1 % en mobile émulé | Absence de saccade |
| Coût pour la page | Aucune tâche longue due au fond, CLS = 0 | La vidéo ne bloque rien |

## Intégration

- Choisir la variante selon le **rapport d'aspect de la zone affichée**, avec une zone neutre (entre 0,9 et 1,1) pour
  éviter les allers-retours en écran partagé, et selon une **densité plafonnée** (les appareils tactiles limités à
  1080p, par exemple).
- Choisir le codec par `canPlayType` et Media Capabilities ; servir le flux pré-compensé aux seuls navigateurs Apple.
- Charger après les ressources prioritaires ; démarrer seulement si le chargement devance la lecture.
- `muted playsinline loop` ; lecture automatique refusée → affiche, puis lecture au premier geste.
- `prefers-reduced-motion` → image fixe, aucune vidéo téléchargée.
- **Bouton pause** (WCAG 2.2.2), choix mémorisé.
- Pause hors de la vue (IntersectionObserver) et onglet masqué (Page Visibility).
- **Rotation** : la vidéo en cours continue, recadrée, pendant que la nouvelle variante se charge ; celle-ci reprend à
  la même position de la boucle, puis un fondu croisé court fait la transition. Une seule nouvelle requête ; jamais de
  rétrogradation sur simple redimensionnement.
- **Ne pas se fier à `navigator.connection.downlink`** : sans historique, certains navigateurs annoncent un débit bas
  par défaut et font rétrograder à tort.
- Exposer l'état du moteur dans des attributs `data-*` (variante, codec, état de lecture, raison d'un repli) et prévoir
  un mode `?debug` (variante, codec, images perdues, blocages, tours de boucle).

## Tests

- **Serveur local à requêtes partielles** (`Range`) : avec `python -m http.server`, Safari et iOS refusent le MP4.
  Une option d'écoute sur le réseau local permet de tester un téléphone réel sans rien publier.
- **Banc Playwright** : Chrome installé (décodage matériel réel), WebKit et Firefox ; émulations iPhone et Android ;
  réseau limité ; mouvement réduit ; lecture refusée ; vidéo introuvable ; défilement ; onglet masqué ; rotation ; CLS ;
  trois tours de boucle mesurés image par image.
- **Matrice réel / émulé** écrite. Ne sont pas testables sans matériel : téléphones et tablettes réels, Windows, réseaux
  mobiles réels.
- **Chaque codec livré lu au moins une fois** : le repli n'est souvent choisi par aucun moteur du banc ; le forcer
  (`?codec=h264`) pour le lire réellement.
- **Sous charge**, un moteur peut perdre beaucoup d'images ; avant d'accuser les fichiers, refaire le test sur machine
  libre ou en A/B avec d'anciens exports.
- **Tester les exports définitifs** : poids et comportement des exports provisoires ne sont pas représentatifs.
