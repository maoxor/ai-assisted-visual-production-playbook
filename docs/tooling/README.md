# Outillage : rôle, usage, contribution à la qualité

Outils employés avec la méthode, leur rôle et ce qu'ils apportent à la qualité. Vérifier les versions disponibles au
début de chaque projet : celles indiquées ici sont des repères, pas des exigences.

| Document | Contenu |
|---|---|
| Ce fichier | Inventaire, provenance et licences, machine partagée |
| [`claude-code.md`](claude-code.md) | Configuration et usage de Claude Code : instructions, mémoire, skills, hooks, permissions |
| [`../../tools/`](../../tools/README.md) | Scripts réutilisables et testés |
| [`../../skills/`](../../skills/README.md) | Skills prêts à installer |

## Inventaire [éprouvé]

| Outil | Rôle | Quand | Contribution à la qualité |
|---|---|---|---|
| **Claude Code** | Agent : recherche, code, essais, contrôles, documentation | Tout le projet | Exécute et vérifie ; tient journaux et mémoire |
| **Blender** (version LTS) | Génération de scène par script Python, rendu Cycles sur GPU, débruitage OIDN | Construction, essais, production | Matériaux physiques, réfraction réelle de l'état animé, reproductible par script |
| **Python** et **uv** | Préparation, contrôles, post-traitement, encodage, tests ; environnement figé (`uv.lock`) | Partout | Reproductibilité ; outils de mesure sur mesure |
| **numpy, OpenCV, Pillow, scikit-image** | Mesures d'image, flux optique (DIS), réduction de taille | Contrôles, stabilisation | Mesures objectives en complément de l'œil |
| **ꟻLIP** (`flip-evaluator`) | Différence perceptuelle entre images | Fidélité | Plus proche de la perception que le PSNR |
| **PyTorch, transformers** | Inférence locale de modèles de segmentation et de profondeur | Préparation | Masques et profondeur sans régénérer l'image |
| **ffmpeg** (libsvtav1, libx265, libx264, libvmaf) | Encodage, vidéos de revue, VMAF, XPSNR | Revue, exports | Exports mesurés ; comparatifs côte à côte |
| **Playwright** (Chrome, WebKit, Firefox) | Tests de page : lecture, images perdues, rotation, émulations | Intégration | Lecture réelle mesurée ; réel et émulé distingués |
| **pytest, Vitest, ruff, ESLint, import-linter** | Tests et contrats d'architecture | Développement | Non-régression automatique |
| **GitHub Actions** | CI : lint, tests, e2e, migrations, audit, secrets | Chaque push | Contrôles indépendants de l'agent |
| **gitleaks** | Détection de secrets | CI | Aucun secret publié |
| **Simulateurs iOS (Xcode), émulateurs Android** | Tests mobiles proches du réel | Intégration mobile | Comportements Safari iOS et Chrome Android |
| **caffeinate, pmset, nohup** (macOS) | Empêcher la veille, attendre le secteur, détacher les calculs | Production longue | Calculs qui survivent aux interruptions |

<a id="provenance-and-licensing"></a>

## Provenance et licences [éprouvé]

Avant d'ajouter un outil, un modèle, une texture, un dépôt, un MCP ou un skill :

1. **Provenance** : source officielle, version stable, dépendances maintenues.
2. **Licence** compatible avec l'usage prévu, vérifiée sur la variante exacte.
3. **Compatibilité** avec la machine (architecture, GPU, mémoire).
4. **Utilité concrète** démontrée : un MCP, un skill ou un modèle ne s'ajoute que s'il apporte un gain mesurable ; des
   scripts suffisent souvent.
5. **Inspection des scripts** avant exécution.
6. **Consignation** : version ou commit, source, licence, rôle, empreintes (manifeste de provenance, `SHA256SUMS`,
   tableau du README).

Ce qui a été **envisagé puis écarté** se note aussi, avec la raison (fonction absente de la version utilisée, licence
non commerciale, bénéfice nul).

<a id="shared-machine"></a>

## Machine partagée [éprouvé]

Quand plusieurs projets ou sessions partagent la même machine :

- ne **jamais** tuer les processus d'un autre projet ou d'une autre session ;
- faire passer les calculs lourds d'apprentissage automatique par un **verrou commun** (par exemple `flock` sur un
  fichier partagé), car plusieurs inférences simultanées peuvent épuiser la mémoire et arrêter la machine ;
- avant de conclure qu'un calcul est lent, vérifier qui tient le verrou et la charge (`uptime`) ; signaler les mesures
  faites sous charge ;
- après l'arrêt d'un script, vérifier qu'aucun processus enfant (moteur de rendu, navigateur) n'est resté orphelin.
