# Boîte à outils

Scripts Python génériques, sans dépendance à un projet et **testés** sur des séquences synthétiques
([`tests/test_tools.py`](tests/test_tools.py), 20 tests). Ils servent les mécanismes de qualité de la méthode :
mesurer le scintillement, contrôler une boucle, stabiliser, garantir qu'on ne mélange pas les versions, présenter une
revue. Le code (noms, options, messages) est en anglais.

## Installation et tests

Python 3.12 et [uv](https://docs.astral.sh/uv/), sans installation globale :

```bash
uv run --no-project --python 3.12 --with numpy --with opencv-python-headless --with pytest pytest tools/tests -q
# utiliser un outil :
uv run --no-project --python 3.12 --with numpy --with opencv-python-headless \
    python tools/flicker.py --seq <dossier> --label trial
```

`review_video.py` requiert ffmpeg. `fingerprint.py` et `review_page.py` n'utilisent que la bibliothèque standard.

## Outils

<a id="flickerpy"></a>

### `flicker.py`

Mesure les pixels qui s'allument puis s'éteignent, d'après l'accélération temporelle de la luminance, sur une
séquence d'images ou une vidéo décodée : part de pixels scintillants, part de points isolés, carte.

- **Quand** : diagnostic d'une régression de stabilité ; avant/après une correction ; images sources contre vidéos
  encodées, pour savoir où naît le défaut.
- **Apport** : rend mesurable un défaut que l'œil voit mais ne localise pas ; sépare calcul et encodage.
- **Limite** : une variation voulue (clignement, éclair) est comptée ; juger avec la vidéo sous les yeux, à la taille
  et en qualité finales.

<a id="loop_checkpy"></a>

### `loop_check.py`

Contrôle une séquence complète destinée à boucler : nombre d'images, fichiers lisibles, raccord (rapport entre l'écart
dernière → première image et l'écart consécutif moyen), scintillement à travers le raccord. Code de sortie 1 en cas de
problème.

- **Quand** : après chaque production complète, avant l'encodage.
- **Apport** : détecte un saut au raccord, une image manquante ou une image finale dupliquée (écart nul, signe d'une
  pause).
- **Limite** : complète, sans la remplacer, la vérification de l'**état** de la scène à la période.

<a id="stabilizepy"></a>

### `stabilize.py`

Stabilisation temporelle : médiane sur trois images recalées par flux optique dense (OpenCV DIS), **limitée aux
pics** ; un pixel n'est modifié que s'il sort de l'intervalle de ses deux voisins recalés. Aucun flou spatial ; boucle
fermée en option (`--loop`).

- **Quand** : après un rendu dont le scintillement résiduel vient de l'échantillonnage (reflets très intenses, petits
  détails brillants).
- **Apport** : forte réduction du scintillement sans perte de netteté ; vidéos plus légères à qualité égale.
- **Garde-fous** : pixels laissés intacts si le flux est incohérent dans les deux sens (zone sans texture) ou si
  l'écart dépasse `--guard` (occlusion, recalage faux). Les tests le vérifient.
- **Limite** : ce n'est pas un débruiteur ; vérifier à 200 % les zones sensibles (visage, texte).

<a id="fingerprintpy"></a>

### `fingerprint.py`

Empreinte SHA-256 des dépendances d'une production (fichiers, motifs, valeurs comme la version du logiciel ou le
profil). `ensure` déplace dans `_stale/` les sorties d'un autre état, sans jamais les supprimer ; `pending` liste les
unités absentes ou incomplètes (PNG sans bloc IEND).

- **Quand** : avant chaque paquet de production, et pour toute reprise après interruption.
- **Apport** : aucune unité d'un ancien état ne se glisse dans un livrable ; reprise sûre ; historique conservé.
- Intégration dans une boucle de calcul :

  ```python
  from fingerprint import ensure, pending
  deps = ["scenes/main.blend", "config/scene.toml", "scripts/render/job.py", "layers/*.png"]
  ensure("renders/v3/desktop", deps, {"renderer": "5.x", "quality": "final"})
  for batch in split(pending("renders/v3/desktop", 300), 10):
      render(batch)        # un processus par paquet ; vérifier l'espace disque avant chacun
  ```

<a id="review_pagepy"></a>

### `review_page.py`

Génère une page HTML locale, autonome et hors ligne, à partir d'un plan JSON : sections, vidéos en boucle lues en
avant, images, tableaux de mesures. Thème clair ou sombre selon le système ; légendes obligatoires ; fichiers absents
signalés. Option `--open`.

- **Quand** : à chaque étape présentée à la personne qui dirige.
- **Apport** : comparatifs homogènes (même taille, colonnes libellées), rien d'oublié, aucune publication nécessaire.

<a id="review_videopy"></a>

### `review_video.py`

Transforme une ou plusieurs séquences d'images en vidéo de revue H.264 (CRF 14), **en avant**, sur plusieurs tours,
côte à côte à la même hauteur.

- **Quand** : comparatifs avant/après, revue d'une boucle (plusieurs tours pour juger le raccord).
- **Apport** : applique d'office les règles de revue (jamais d'aller-retour, même taille).

## Ajouter un outil

Un script n'entre ici qu'une fois **généralisé** (aucun chemin, nom ou réglage de projet), **testé** sur des données
synthétiques et documenté dans ce fichier avec son usage, son apport et ses limites
([`CONTRIBUTING.md`](../CONTRIBUTING.md#after-each-project)).
