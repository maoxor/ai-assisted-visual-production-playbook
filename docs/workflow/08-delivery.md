# 8. Livraison

**Objectif.** Remettre des livrables qui existent, s'ouvrent et ont été contrôlés, avec un bilan qui permet de les
utiliser et de les reproduire.

## Ce qui est livré [éprouvé]

- **Les sources reproductibles** : projet et dépendances regroupées, scripts de génération, de calcul et d'export,
  configuration et graines.
- **Les livrables finaux** dans tous les formats cibles, avec leurs **replis** (images fixes, affiches, versions
  dégradées).
- **L'intégration** testée dans l'environnement cible, ou une page de démonstration locale minimale.
- **Les preuves** : captures de contrôle, avant/après, vidéos de revue, page de revue actualisée.
- **Un rapport court** : contrôles réellement exécutés, défauts corrigés, limites restantes
  ([modèle](../../templates/delivery-report.md)).
- **Un README** : ouvrir, modifier, régénérer, exporter ; sources et licences des ressources ajoutées.

## Le bilan final [éprouvé]

Il distingue toujours :

1. **Terminé** : ce qui existe à l'emplacement final.
2. **Testé** : ce qui a été vérifié, comment, avec quels résultats, dans quels environnements (réel ou émulé).
3. **Limites** : ce qui n'a pas pu être fait ou vérifié, avec la raison et la manière de le faire.

Il reprend aussi les choix retenus et leur raison, en une ligne chacun.

<a id="delivery-under-time-pressure"></a>

## Livraison sous contrainte de temps [éprouvé]

Quand la personne qui dirige n'a plus de temps et demande tout de suite ce qui est prêt :

- livrer immédiatement ce qui est **prêt et vérifié**, à un emplacement clair, avec l'extrait d'intégration à copier ;
- dire en une ligne ce qui n'est pas testé ;
- reprendre ensuite les travaux en cours sans casser ce qui a été livré : **mêmes noms de fichiers**, anciennes
  versions archivées à côté, annonce explicite quand de nouveaux fichiers remplacent les anciens.

## Après la livraison

- **Retour d'expérience** : bilan dans le projet ([modèle](../../templates/retrospective.md)), puis report des
  enseignements **génériques** dans ce référentiel ([`CONTRIBUTING.md`](../../CONTRIBUTING.md#after-each-project)).
- **Nettoyage proposé, pas imposé** : les fichiers intermédiaires régénérables peuvent être supprimés, mais on le
  propose au lieu de le faire.

## Critère de fin

La [définition de « terminé »](../quality/README.md#definition-of-done) est satisfaite ; le bilan est rendu ;
l'emplacement des livrables est indiqué ; l'utilisation est expliquée (extrait de code, commande).
