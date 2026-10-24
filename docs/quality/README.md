# Qualité : comment juger, quand s'arrêter

Ce dossier rend explicites les **critères d'évaluation** et les **mécanismes** qui permettent d'atteindre puis de
maintenir un niveau de qualité élevé.

| Document | Rôle |
|---|---|
| Ce fichier | Définition de « terminé », grille d'évaluation, mécanismes de qualité |
| [`checklists/`](checklists/README.md) | Listes de contrôle par moment : reprise, revue visuelle, avant production, vidéo web, livraison |
| [`anti-patterns.md`](anti-patterns.md) | Erreurs classiques, avec leur prévention |
| [`collaboration.md`](collaboration.md) | Préférences de collaboration par défaut entre la personne qui dirige et l'agent |

<a id="definition-of-done"></a>

## Définition de « terminé » [éprouvé]

Un travail est terminé quand **toutes** les conditions suivantes sont vraies :

1. Les livrables existent à leur emplacement définitif, dans tous les formats demandés, replis compris.
2. Ils **s'ouvrent ou se lisent** dans leur environnement cible : fichier décodé en entier, lecture vérifiée dans le
   navigateur ou l'outil.
3. Les contrôles prévus ont été **exécutés** et leurs résultats sont cités.
4. Chaque demande de l'itération a un état : fait, essai écarté (raison) ou manquant ([P15](../principles.md#p15)).
5. Aucun élément résiduel ne subsiste : signature, logo, texte provisoire, fichier de debug, réglage d'essai.
6. Les sources permettent de **régénérer** le résultat (configuration, graines, scripts, versions).
7. La version précédente est **conservée**.
8. Le bilan distingue *terminé*, *testé* (réel ou émulé) et *limites*.
9. Les enseignements génériques sont reportés dans ce référentiel, ou notés comme à reporter.

Ne sont **pas** terminés : une commande lancée, un calcul en cours, un prototype, un plan, une scène reconstruite sans
rendu final, un export non lu.

## Grille d'évaluation [éprouvé]

Pour juger une proposition ou une itération, dans l'ordre de priorité : l'apparence et le mouvement d'abord, les
mesures ensuite.

| # | Critère | Question | Comment le vérifier |
|---|---|---|---|
| 1 | **Intention** | Le résultat sert-il l'objectif et le critère essentiel du cadrage ? | Relire le cadrage ; regarder le résultat à la taille finale |
| 2 | **Sujet** | Le sujet reste-t-il le centre ? Son identité est-elle préservée ? | Comparaison avec la source ; vue sans effets |
| 3 | **Perceptibilité** | Chaque amélioration se voit-elle dans les conditions finales, à vitesse normale ? | Vidéo côte à côte, avant/après, œuvre entière |
| 4 | **Cohérence** | Les éléments appartiennent-ils au même monde (plans, lumières, matières, rythmes) ? | Vue d'ensemble ; recherche des éléments qui paraissent rapportés |
| 5 | **Richesse sans confusion** | La matière est-elle riche sans brouiller les zones de lecture ? | Gros plans des zones sensibles ; contrôle fonctionnel (lisibilité) |
| 6 | **Variété intentionnelle** | Évite-t-on la répétition mécanique (mosaïque, oscillations identiques, motifs réguliers) ? | Inspection en mouvement ; comparaison des éléments entre eux |
| 7 | **Propreté** | Y a-t-il des artefacts (scintillement, bords, trous, halos, texture qui glisse, résidus) ? | Contrôles automatiques et inspection à 100 % et 200 % |
| 8 | **Stabilité** | Le résultat tient-il en mouvement et au raccord de boucle ? | Plusieurs tours de boucle ; mesure du scintillement |
| 9 | **Coût** | Le coût (production, poids, lecture) est-il connu et justifié ? | Profil de coût, poids, tests de lecture |
| 10 | **Reproductibilité** | Peut-on régénérer exactement ce résultat ? | Empreinte, configuration archivée, graines |

Pour une **direction artistique**, seuls les critères 1 à 6 sont décisifs, et le jugement de la personne qui dirige
l'emporte ([direction artistique](../workflow/05-art-direction.md)).

## Mécanismes qui produisent la qualité

| Mécanisme | Contribution | Où |
|---|---|---|
| Référence de l'état actuel avant tout essai | Rend l'effet de chaque changement mesurable | [Itération](../workflow/04-evidence-based-iteration.md) |
| Une variable à la fois, diagnostic par extinction | Trouve la vraie cause ; évite les corrections qui se masquent | [Itération](../workflow/04-evidence-based-iteration.md) |
| Échantillon avant généralisation | Itérations rapides ; coût vérifié avant multiplication | [P7](../principles.md#p7) |
| Comparatif à cadrage, taille et vitesse identiques | Décision visuelle juste, sans biais de présentation | [Validation](../workflow/07-validation.md) |
| Variantes contrastées et contre-essai | Révèle la préférence réelle de la personne qui dirige | [Direction artistique](../workflow/05-art-direction.md) |
| Configuration déclarative, régénération | Aucune retouche perdue ; essais combinables | [P11](../principles.md#p11) |
| Empreinte des dépendances | Aucun mélange de versions ; reprise sûre | [Production](../workflow/06-production.md#fingerprint-and-resume) |
| Contrôles de non-régression | Une correction locale ne casse pas l'ensemble | [Itération](../workflow/04-evidence-based-iteration.md) |
| Profil de coût | Cycle d'itération praticable ; réglages justifiés | [Production](../workflow/06-production.md#cost-profile) |
| Journal numéroté | Mémoire des impasses ; reprise fiable | [Continuité](../workflow/09-continuity.md) |
| Registre des consignes | Aucune demande oubliée ; consignes à jour | [P15](../principles.md#p15) |
| Bilan terminé / testé / limites | Confiance ; décisions éclairées | [Livraison](../workflow/08-delivery.md) |
| Garde-fous automatiques (hooks, CI) | Contrôles qui ne dépendent pas de la bonne volonté de l'agent | [Claude Code](../tooling/claude-code.md#hooks) |
