# Adapter la méthode à un autre projet

La méthode a été éprouvée sur du **rendu 3D précalculé destiné au web** et sur des **applications web**. Ce document
montre comment chaque concept générique se traduit dans d'autres contextes. Les colonnes au-delà de ces deux types sont
**[extrapolé]** : elles n'ont pas encore été appliquées.

## Ce qui ne change jamais

Les [principes](../principles.md), la boucle d'[itération sur preuves](04-evidence-based-iteration.md), la distinction
entre contrôles et validation, la [définition de « terminé »](../quality/README.md#definition-of-done), la continuité
(journal, versions, registre) et la séparation entre méthode et esthétique.

## La traduction des concepts

| Concept générique | Rendu précalculé, vidéo web [éprouvé] | Application web [éprouvé] | Motion design, animation 2D [extrapolé] | Jeu ou temps réel [extrapolé] | Document, présentation, identité [extrapolé] |
|---|---|---|---|---|---|
| Unité de production | Image d'une séquence | Fonctionnalité, écran | Plan, séquence | Scène, niveau, effet | Page, diapositive, déclinaison |
| Conditions finales | Taille d'affichage, vitesse normale, traitement final, vidéo encodée lue dans le navigateur | Navigateurs et appareils réels, données réelles, CI | Sortie finale, son, écran cible | Matériel cible, fréquence d'images, build de production | Format imprimé ou écran réel, export final |
| Échantillon | Un élément, un extrait de quelques secondes, une image difficile | Un parcours, un écran critique | Un plan clé | Une pièce, un effet, une scène de test | Une page type, une diapositive dense |
| Prototype minimal | Sujet, un élément d'effet, un premier plan, un mouvement de caméra | Une route de bout en bout, testée | Animatique | Tranche verticale | Maquette d'une page avec contenu réel |
| Extinction (diagnostic) | Éteindre une lumière, peindre une surface en noir, cacher un élément | Désactiver un module, bissection Git, doublures | Masquer un calque | Désactiver un système, une passe de rendu | Retirer un style, une police |
| Empreinte et reprise | SHA-256 des sources et scripts dans `VERSION.json` | Commits, CI, migrations immuables | Versions de projet, rendus nommés | Builds versionnés, assets hachés | Versions exportées nommées |
| Non-régression | Composition élément par élément, trajectoires, scintillement | Tests unitaires, d'intégration, e2e, contrat d'architecture | Comparaison image par image | Tests automatisés, captures de référence | Comparaison visuelle des pages |
| Métriques complémentaires | SSIM, VMAF, scintillement, contraste WCAG, temps par image | Couverture, LCP, CLS, temps de réponse | Cadence, contrastes | Temps par image (ms), mémoire | Contraste, lisibilité, poids |
| Coûts à séparer | Calcul, poids, décodage, fluidité de la page | Développement, build, performance, maintenance | Rendu, poids, lecture | Production, mémoire, temps par image, téléchargement | Production, impression, poids |

## Démarche pour adapter le workflow

1. **Nommer l'unité de production et les conditions finales** du nouveau projet : sans elles, on ne sait pas où
   juger.
2. **Choisir l'échantillon** qui porte le risque principal.
3. **Traduire les familles de contrôles** de [la validation](07-validation.md). Exemple : la « localité des effets »
   devient « un changement de style ne touche que les composants visés ».
4. **Choisir les métriques complémentaires** et noter ce qu'elles ne prouvent pas ([P1](../principles.md#p1)).
5. **Identifier les coûts à séparer** ([P13](../principles.md#p13)).
6. **Écrire ces choix dans le `CLAUDE.md` du projet** ([modèle](../../templates/project-claude-md.md)), section
   « Méthode appliquée ».
7. **Après le projet**, reporter ici ce qui a marché et ce qui a manqué : une colonne [extrapolé] devient [éprouvé]
   ([`CONTRIBUTING.md`](../../CONTRIBUTING.md)).

## Changer de direction artistique

La direction artistique est une **entrée** du processus, jamais une sortie de ce référentiel.

- On repart des références et de l'intention du nouveau projet ; aucun choix esthétique antérieur n'est repris par
  défaut.
- On garde les **mécanismes** : analyse de la référence par recadrages équivalents, rôles des éléments, variantes
  contrastées avec contre-essai, vue annotée, aperçu en mouvement, choix écrit.
- Les leçons d'un projet sont des observations, pas des interdits généraux : un filtre, une matière ou une métaphore
  écartés une fois restent possibles ailleurs.

## Changer de technologie

La méthode ne dépend d'aucun logiciel. Pour une autre pile :

- remplacer les outils de [l'outillage](../tooling/README.md) par leurs équivalents, en justifiant chaque ajout
  (provenance, licence, maintenance, bénéfice concret) ;
- conserver la configuration déclarative, les graines stables et les versions figées ([P11](../principles.md#p11)) ;
- reconstituer un banc d'essai qui applique des modifications nommées à une copie de l'état de référence.

## Contraintes différentes

| Contrainte | Adaptation |
|---|---|
| Délai très court | Garder le cadrage et la définition de « terminé » ; une source primaire par sujet ; un seul échantillon ; livrer ce qui est vérifié et dire ce qui ne l'est pas ([livraison sous contrainte](08-delivery.md#delivery-under-time-pressure)) |
| Machine modeste | Profil de coût dès le prototype ; échantillons plus petits ; pour une vidéo, privilégier la stabilisation et la réduction de taille au suréchantillonnage |
| Travail à plusieurs | Git obligatoire, branches et journaux de chantier, décisions écrites, CI ([applications web](../domains/web-applications.md)) |
| Diffusion publique et droits | Provenance et licence de chaque ressource ; question des droits isolée dès le cadrage ; rien de publié sans accord |
