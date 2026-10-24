---
name: visual-iteration
description: Améliorer un résultat visuel ou animé (rendu, animation, interface, vidéo) par une boucle référence → essai isolé → comparatif → intégration, jugée dans les conditions finales. À utiliser pour toute correction ou exploration visuelle avant une production longue.
---

# Itération visuelle sur preuves

## 1. Préparer

- Relire la demande et le registre des consignes (`docs/instruction-register.md`) ; lister chaque point demandé.
- Choisir un **échantillon** représentatif (un élément, un extrait de quelques secondes, une image difficile). Ne pas
  toucher au reste tant que l'échantillon n'est pas validé.
- Produire la **référence de l'état actuel** avec les réglages de l'essai (même cadrage, même qualité). Si elle est
  reconstruite, vérifier qu'elle redonne le même résultat.

## 2. Comprendre la cause

- Si la cause n'est pas évidente : **diagnostic par extinction** — neutraliser une cause possible à la fois (source de
  lumière, matériau en noir, élément caché, effet coupé) jusqu'à la disparition du défaut.
- Localiser l'étape où naît le défaut (génération, rendu, débruitage, réduction, encodage, lecture) et y corriger.
- Vérifier le sens et l'effet réel de chaque paramètre dans l'outil utilisé : mesurer, ne pas supposer.

## 3. Essayer

- **Une variable par essai**, nommée (`e1`, `e2`…), appliquée à une copie : la référence n'est jamais modifiée.
- Comparer plusieurs amplitudes ou dosages plutôt qu'une seule valeur.
- Si un essai échoue : examiner sa construction, pas seulement son intensité.

## 4. Comparer dans les conditions finales

- Côte à côte libellé, **même cadrage, même taille, même vitesse** : référence / avant / après, ou essai actuel /
  nouvel essai.
- Taille finale d'affichage **et** gros plans ; vue de diagnostic **et** traitement final (flou, encodage).
- Œuvre entière animée, **lecture en avant**, en boucle ; tous les formats.
- **Dernière version** comme base. Vérifier soi-même que la différence se voit avant de présenter.
- Mesures en complément (et le coût : temps, poids), jamais comme preuve à elles seules.

## 5. Intégrer

- Contrôles de non-régression (reste inchangé, zones protégées, géométrie valide).
- Archiver la configuration en vigueur, intégrer dans la configuration, régénérer.
- Journal (`docs/experiments/`) : n°, essai, constat, retenu ou écarté et pourquoi.

## 6. Présenter

- Ouvrir le comparatif pour l'utilisateur et vérifier l'ouverture ; point court : ce qui marche, ce qui reste, la
  prochaine action.
- Chaque point demandé avec son état : fait, essai écarté (raison), manquant.
- Distinguer mes contrôles de sa validation ; ne pas généraliser ni lancer la production sans son accord.
