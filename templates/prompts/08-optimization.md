# Réduire le coût de production et de diffusion

```markdown
<Constat : les temps annoncés ne permettent pas d'itérer.> **Résous d'abord ce problème de production avant de
lancer un nouveau calcul long.**

Rappel de l'objectif : <…>. Le livrable de validation est **un véritable extrait de <durée> de la production finale**
(<n> unités consécutives), avec les réglages et le traitement envisagés pour la production complète. Des images fixes
ou un aperçu dégradé ne permettent pas cette validation.

## 1. Identifier les causes réelles du coût
Inspecte toute la chaîne. Vérifie l'utilisation effective du matériel (accélérateur, replis), le coût des éléments
(<transparences, matériaux, géométries, lumières…>), les réglages (<échantillons, suréchantillonnage, rebonds…>), la
mémoire, les temps de compilation, les écritures disque et les reconstructions inutiles. Mesure quelques unités
représentatives, dont une difficile ; distingue démarrage et régime établi ; attribue les dépenses par des tests
isolés. Aucun réglage n'est intouchable : son utilité doit être démontrée visuellement.

## 2. Rechercher
Documentation officielle, dépôts, forums, retours de production comparables, sans sous-agents.

## 3. Comparer des solutions mesurées
Quelques profils cohérents sur les mêmes unités et un court passage exigeant : temps, mémoire, netteté, détails,
stabilité, compatibilité. Explore aussi les changements de méthode (remplacer, simplifier, supprimer l'invisible,
répartir entre calcul et post-traitement). Ne fige pas ce qui doit évoluer ; pas d'interpolation non vérifiée ; pas de
flou global. Tableau court : temps mesurés, gain, différences visibles, recommandation.

## 4. Distinguer calcul et diffusion
Traite séparément : temps de production, poids et transfert, décodage et lecture. Exports adaptés aux tailles
affichées et aux appareils ; comparatif des codecs sur les passages difficiles ; intégration réelle testée (démarrage,
raccords, images perdues, réseau contraint, affiche, repli). Distingue appareils physiques et émulation.

## 5. Produire l'extrait demandé
Choisis le meilleur compromis mesuré ; estimation actualisée pour l'extrait et pour le tout ; produis l'extrait avec
les paramètres de livraison sur un passage qui permet une décision artistique. Livre : extraits lisibles, accès aux
sources, réglages et temps constatés, comparatif qualité / performance, limites, page d'aperçu. Conserve les versions
précédentes. Ne lance pas la production complète avant ma validation de l'extrait ; poursuis de façon autonome
l'analyse, les essais et leur réalisation.
```
