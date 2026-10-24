# Vidéo pour une page web

Détails et justifications : [guide vidéo web](../../domains/web-background-video.md).

## Exports

- [ ] Variantes par **cadrage** et par **définition réellement affichée**, pas seulement « mobile / bureau ».
- [ ] Codecs : un format efficace (AV1), un format pour Apple (HEVC, pré-compensé si nécessaire), un repli universel
      (H.264).
- [ ] Débits ou CRF choisis sur un comparatif mesuré (VMAF ou autre) sur les passages difficiles, **sur la séquence
      finale**.
- [ ] Une seule image-clé par boucle si la scène scintille, ou un choix justifié.
- [ ] Métadonnées couleur cohérentes ; rendu des couleurs vérifié dans WebKit.
- [ ] Noirs sans aplats en escalier ; microdétails et mouvements préservés (revue côte à côte).
- [ ] Raccord de boucle encodé mesuré : pas de saut visible au retour à la première image.
- [ ] Chaque fichier décodé en entier (nombre d'images attendu).
- [ ] Affiches (première image) dans les formats modernes et en repli ; poids dans le budget.

## Intégration

- [ ] La page est utilisable et belle **sans** la vidéo ; l'affiche est l'élément principal (LCP).
- [ ] Vidéo chargée après les ressources prioritaires ; démarrage seulement si la lecture peut se faire sans attente.
- [ ] `muted`, `playsinline`, `loop` ; lecture automatique refusée → affiche, puis lecture au premier geste.
- [ ] `prefers-reduced-motion` → image fixe, aucune vidéo téléchargée.
- [ ] Bouton pause (WCAG 2.2.2 : animation de plus de 5 s) ; choix mémorisé.
- [ ] Pause hors de l'écran et onglet masqué ; reprise au retour.
- [ ] Rotation, redimensionnement, écran partagé : pas d'écran noir, une seule nouvelle requête, position dans la
      boucle conservée, pas d'aller-retour de variante.
- [ ] Appareils tactiles plafonnés à une définition raisonnable ; pas de fichier le plus lourd par défaut.
- [ ] Serveur de test avec **requêtes partielles** (sinon Safari et iOS refusent le MP4).
- [ ] Échecs (vidéo introuvable, codec refusé) : l'affiche reste, aucune erreur de script.

## Tests

- [ ] Matrice réel / émulé écrite ; ce qui n'est pas testable est listé.
- [ ] Images perdues, intervalles aux raccords, attentes, tâches longues, CLS, octets téléchargés : mesurés dans chaque
      moteur.
- [ ] **Chaque codec livré lu au moins une fois** par un moteur, y compris le repli (forcer le codec si nécessaire).
- [ ] Tests refaits sur les **exports définitifs**, pas seulement sur des exports provisoires.
- [ ] Résultats sous charge distingués d'une machine libre ; perte attribuée à l'environnement seulement avec une
      preuve (un A/B sur d'anciens exports, par exemple).
