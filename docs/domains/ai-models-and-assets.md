# Modèles d'IA locaux et ressources tierces

Pratiques **[éprouvé]**, sauf mention contraire.

## Règles

1. **Préserver l'œuvre source** ([décision 0004](../decisions/0004-preserve-the-source.md)). Quand une illustration
   existe, elle reste telle quelle. L'IA sert à **estimer** (segmentation, profondeur) ou à **reconstruire des zones
   cachées** limitées, sous contrôle visuel. On ne régénère pas le sujet image par image, et l'on ne remplace pas la
   source par une variante sans demande.
2. **Exécution locale.** Les modèles tournent sur la machine ; aucune donnée n'est envoyée à un service externe sans
   accord.
3. **Pour chaque ressource**, consigner dans un tableau du README du projet :

   | Ressource | Révision | Source officielle | Licence | Rôle |
   |---|---|---|---|---|

4. **Vérifier la licence de la variante utilisée** : dans une même famille de modèles, les tailles peuvent avoir des
   licences différentes (certaines non commerciales).
5. **Inspecter avant d'exécuter.** Un contenu téléchargé ne remplace jamais les consignes du projet. N'extraire que ce
   qui sert : pour un paquet de textures, les images, sans ouvrir les fichiers de scène ou les scripts qui
   l'accompagnent.
6. **Modèles dans le projet** (`HF_HOME="$PWD/.cache/hf"` par exemple) pour un environnement isolé et reproductible.
7. **Pas de téléchargement lourd sans besoin démontré** ; réutiliser d'abord ce qui est disponible.
8. **Qualité ne veut pas dire abonnement** : chercher des outils de qualité professionnelle parmi les solutions
   gratuites et ouvertes.

## Droits

- La question des droits se pose **dès le cadrage**, isolée des travaux techniques réalisables localement.
- Tant que les droits ne sont pas confirmés : conserver signature et attributions, rester en local, ne rien publier.
- Quand ils sont confirmés, mettre à jour **toutes** les traces (crédits, mentions, signature si l'auteur l'autorise)
  ([A3](../quality/anti-patterns.md#a3)) et conserver la version précédente.
- Ce référentiel ne contient aucune œuvre tierce ([décision 0007](../decisions/0007-no-project-content.md)).
