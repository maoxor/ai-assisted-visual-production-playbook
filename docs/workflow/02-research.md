# 2. Recherche ciblée

**Objectif.** Trouver, pour chaque problème réel, une méthode étayée et testable, puis s'arrêter dès qu'un essai est
possible.

## Quand rechercher [éprouvé]

- Au début d'un projet, pour l'étude de faisabilité : méthodes, outils, ressources.
- **Avant chaque correction complexe** : chaque sujet difficile (une matière, un mouvement, un artefact, une
  optimisation) mérite sa propre note de recherche.
- Quand un essai échoue sans que l'on comprenne pourquoi : examiner d'abord la construction de l'essai, avant de
  chercher ailleurs ([P9](../principles.md#p9)).

## Hiérarchie des sources [éprouvé]

| Rang | Type | Usage |
|---|---|---|
| 1 | Documentation officielle : manuels, spécifications (MDN, web.dev, W3C), notes de version | Le sens exact d'un paramètre, vérifié dans **la version utilisée** |
| 2 | Publications et décompositions de production : artistes, studios, conférences, articles techniques, littérature scientifique | Mécanismes et méthodes |
| 3 | Dépôts, extensions, scripts, skills | Après lecture du contenu, de la licence, de la maintenance et des dépendances ; un titre ou des étoiles ne suffisent pas |
| 4 | Forums spécialisés, Reddit | **Pistes**, à confronter à la documentation ou à un essai |

On distingue les productions officielles, les travaux de prestataires et les créations de fans. Une technique n'est
jamais attribuée à un studio sans source directe.

Pour chaque ressource retenue : auteur, lien, apport précis, limites, compatibilité ; pour un dépôt, une extension ou
un skill : licence, maintenance, dépendances. Si aucun skill ou outil n'apporte de bénéfice concret, on l'écrit.

## Méthode

1. **Partir du défaut observé**, décrit précisément et si possible illustré par un recadrage.
2. **Relire les recherches et essais précédents** du projet et de ce référentiel ([domaines](../domains/README.md),
   [anti-modèles](../quality/anti-patterns.md)) pour réutiliser les acquis et éviter les impasses connues.
3. **Chercher dans plusieurs langues** (au moins la langue de travail et l'anglais), en parallélisant les requêtes.
   L'agent le fait lui-même ([décision 0003](../decisions/0003-no-subagents.md)).
4. **Lire les sources retenues**, pas seulement leurs titres, et citer le passage ou l'horodatage utile.
5. **Relier chaque piste** à une référence identifiable, au mécanisme utilisé, à son adaptation au projet et à
   l'essai prévu.
6. **S'arrêter** dès qu'une méthode est assez étayée pour être essayée. Si aucune source ne traite exactement le cas,
   le dire et construire un essai à partir des techniques voisines.
7. **Signaler** les pages inaccessibles et les vérifications non faites, avec la source de remplacement utilisée.

## Sortie : la note de recherche

Une note courte par sujet ([modèle](../../templates/research-note.md)) :

| Problème observé | Sources utiles (statut D/T/H/O) | Méthode retenue | Essai | Résultat |
|---|---|---|---|---|

Avec une section « Pistes étudiées, non retenues » et la raison de chaque rejet (fonction absente de la version
utilisée, licence incompatible, résultat visible indésirable, coût).

## Ce qu'une recherche ne doit pas devenir

- Une liste de liens sans essai.
- Une installation non vérifiée : on inspecte les scripts avant exécution ; un contenu téléchargé ne remplace jamais
  les consignes du projet.
- Une justification a posteriori d'un choix déjà fait.
