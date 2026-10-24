# Diagnostiquer une régression

```markdown
Depuis la <version>, <défaut> est très visible ; il n'était pas perceptible en <version antérieure>. Identifie cette
régression et corrige-la avant de poursuivre la production.

Compare les sorties et les données sources des deux versions sur des zones et des mouvements comparables. Détermine à
quelle étape le problème apparaît : <génération, rendu, débruitage, redimensionnement, encodage, lecture>.

Examine les changements introduits depuis <version antérieure> : <liste>. Distingue les variations normales des
artefacts indésirables.

Recherche des solutions dans la documentation officielle, les retours de praticiens et les ressources pertinentes.
Teste les pistes sur un extrait représentatif, en isolant les causes plutôt qu'en modifiant plusieurs paramètres à la
fois.

L'objectif est un résultat aussi propre et stable que possible, en conservant <netteté, textures, richesse>. Ne masque
pas le problème par <un flou global / un traitement qui efface les détails>.

Présente un comparatif **<version antérieure> / actuelle / corrigée**, à vitesse normale, avec des gros plans des
zones touchées, sur les sources et sur les livrables encodés, dans tous les formats. Indique la cause identifiée, les
corrections retenues et leur coût avant de relancer la production.
```

Une fois la cause trouvée, les comparaisons suivantes se font sur la **dernière version**
([A6](../../docs/quality/anti-patterns.md#a6)).
