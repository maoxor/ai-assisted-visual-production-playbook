# 6. Production : produire le tout de façon fiable

**Objectif.** Produire l'œuvre complète avec des réglages justifiés, dans un temps qui permet d'itérer, par une chaîne
qui survit aux interruptions et ne mélange jamais les versions.

## Préalables [éprouvé]

- Les défauts identifiés sont corrigés : on ne relance pas des heures de calcul tant qu'ils persistent.
- L'accord explicite de lancer a été donné, si la personne qui dirige se l'est réservé ([P12](../principles.md#p12)).
- L'extrait de validation a été validé, sauf instruction contraire explicite.
- La [liste avant production](../quality/checklists/pre-production.md) est passée.

<a id="cost-profile"></a>

## Profil de coût [éprouvé]

1. **Mesurer quelques unités représentatives, dont une difficile**, en séparant démarrage (chargement, compilation,
   préparation) et régime établi.
2. **Vérifier l'utilisation réelle du matériel** : accélérateur effectivement utilisé, absence de repli sur le
   processeur, mémoire au pic.
3. **Attribuer le coût aux éléments** par des tests isolés, en retirant un élément à la fois.
4. **Comparer quelques profils cohérents** sur les mêmes unités, avec un tableau court :

   | Profil | Temps par unité | Facteur | Ressemblance (SSIM, ꟻLIP) | Netteté par zone | Avis visuel |
   |---|---|---|---|---|---|

5. **Explorer aussi les changements de méthode**, pas seulement les réglages : remplacer une géométrie secondaire par
   une texture, supprimer les détails invisibles à la taille finale, répartir le travail entre calcul et
   post-traitement.
6. **Ne jamais figer** ce qui doit évoluer (un reflet, une réfraction, une donnée dynamique) et **ne jamais remplacer**
   le calcul par une interpolation non vérifiée.
7. **Estimer et annoncer** le temps total pour l'extrait et pour le tout, avec ses hypothèses.

<a id="fingerprint-and-resume"></a>

## Empreinte et reprise [éprouvé]

L'outil [`fingerprint.py`](../../tools/README.md#fingerprintpy) met en œuvre ces règles :

- **Empreinte** : SHA-256 de tout ce qui détermine le résultat (sources, configurations, calques, scripts de calcul et
  de post-traitement, version du logiciel, profil de qualité), écrite dans `VERSION.json` à côté des sorties.
- **Reprise sûre** : si l'empreinte ne correspond plus, les sorties existantes viennent d'un autre état ; elles sont
  **déplacées** dans `_stale/<date>/`, jamais supprimées, et la production repart de zéro.
- **Unité terminée = fichier complet** : un PNG n'est compté que si son bloc final (IEND) est présent.
- **Par paquets** : un processus par paquet de N unités ; une interruption ne perd qu'un paquet et la mémoire est
  libérée.
- **Post-traitement au fil de l'eau** : chaque paquet terminé est aussitôt réduit à la taille finale.
- **Espace disque vérifié avant chaque paquet.**
- **Journal des temps** : une ligne par unité (CSV).
- **Ne rien modifier pendant le calcul** : toute modification d'une dépendance change l'empreinte et arrête la
  production au paquet suivant. C'est voulu.

## Machine et environnement [éprouvé]

- **Veille** : sur un portable, la mise en veille arrête le calcul. Sur macOS, `caffeinate -i -s` n'agit que sur
  secteur ; sur batterie, capot fermé, la machine dort quand même. Lancer la production depuis un script qui attend
  le secteur (`pmset -g batt`), puis s'exécute sous `caffeinate` ([A15](../quality/anti-patterns.md#a15)).
- **Machine partagée** : ne jamais tuer les processus d'un autre projet ou d'une autre session ; faire passer les
  calculs lourds par un verrou commun ([machine partagée](../tooling/README.md#shared-machine)).
- **Processus orphelins** : un script tué peut laisser un processus enfant (moteur de rendu, navigateur) ; vérifier
  après chaque arrêt.
- **Détacher et surveiller** : lancer avec `nohup … &` et un journal ; montrer les premières unités sans attendre la
  fin.

## Enchaînement de fin de production [éprouvé]

Un seul script enchaîne toutes les étapes, chacune horodatée dans le journal :

1. calcul de chaque format ;
2. post-traitement (stabilisation, réduction), en boucle fermée si l'œuvre boucle ;
3. contrôles de l'œuvre complète ;
4. exports de diffusion ;
5. tests de lecture ou d'intégration ;
6. page de revue.

Le calcul lancé n'est que la première étape de la livraison ([P3](../principles.md#p3)).

## Critère de fin

L'œuvre complète existe dans chaque format, sous une empreinte unique et cohérente ; les temps réels sont consignés ;
les étapes suivantes (validation, exports) sont enchaînées.
