# 1. Cadrage : comprendre le besoin et l'existant

**Objectif.** Savoir précisément ce qui est attendu, avec quelles ressources et sous quelles contraintes, puis avancer
sur des hypothèses explicites sans attendre des réponses qui ne changent pas la solution.

## Entrées

- La demande, souvent longue et structurée (voir les [demandes types](../../templates/prompts/README.md)).
- Les références : images, maquettes, vidéos, sites, produits.
- Le projet existant : fichiers, instructions locales (`CLAUDE.md`), configuration, scripts, résultats, rapports,
  processus en cours.

## Étapes

1. **Inspecter l'existant réellement disponible** [éprouvé]. Ouvrir les fichiers ; vérifier versions, chemins et
   paramètres dont dépend la suite ; lister les processus actifs. Un compte rendu précédent peut être tronqué : on
   retrouve les valeurs dans les fichiers plutôt que de les deviner.
2. **Vérifier les outils réellement disponibles** [éprouvé] : logiciels et versions, matériel (GPU, mémoire), espace
   disque, accès réseau. Ne jamais supposer qu'une intégration ou une permission existe sans l'avoir vérifiée.
3. **Décomposer la référence** [éprouvé]. Séparer ce qui est visible des hypothèses sur sa fabrication : une image
   seule ne révèle ni son logiciel ni son pipeline. Identifier aussi ce qu'il ne faut **pas** reproduire (incohérences,
   textes d'interface, défauts de la maquette).
4. **Recenser les paramètres qui conditionnent le choix technique** [éprouvé] : sortie précalculée ou interactive,
   résolution, durée, boucle, plateformes cibles, matériel, budget, logiciels accessibles, droits.
5. **Écrire les hypothèses de travail** [éprouvé] et avancer avec elles. Une question n'est posée que si sa réponse
   change réellement la solution.
6. **Isoler les questions bloquantes** [éprouvé]. Exemple type : des droits de diffusion non confirmés n'empêchent pas
   la préparation technique locale ; la question reste ouverte à part, et l'on conserve attributions et signatures
   jusqu'à confirmation.
7. **Reformuler l'objectif et le critère essentiel** [éprouvé]. Une demande contient souvent une phrase qui résume
   tout (par exemple : « même sans effets, le sujet doit paraître vivant »). Ce critère sert à juger chaque itération.
8. **Ouvrir le registre des consignes** [éprouvé] ([P15](../principles.md#p15)) : contraintes durables (local
   seulement, pas de sous-agents, droits) et choix déjà faits.

## Sorties

- Un cadrage court : objectif, critère essentiel, contraintes, hypothèses, questions bloquantes
  ([modèle de brief](../../templates/project-brief.md)).
- Un [registre des consignes](../../templates/instruction-register.md).
- Pour une étude de faisabilité : un diagnostic, un comparatif compact de trois approches au plus, une recommandation
  avec une solution de repli, et la prochaine action à valider.

## Critère de fin

L'objectif tient en une phrase ; le critère essentiel est identifié ; l'existant a été inspecté fichier par fichier ;
les hypothèses sont écrites ; les questions restantes sont réellement bloquantes et la suite peut avancer sans elles.

## Pièges

- **Compte rendu tronqué pris pour la vérité** : retrouver les valeurs dans les fichiers.
- **Tension non signalée dans le cahier des charges** : deux exigences qui se contredisent (par exemple un effet
  physique qui déforme forcément une zone qui doit rester intacte). La signaler tôt et proposer un compromis explicite.
- **Reproduire les défauts de la référence** : elle sert de cible de composition et de matière, pas de vérité sur tout.
- **Imposer une pile complexe sans bénéfice concret** : reconstruction complète, génération par IA ou outillage lourd
  doivent prouver leur apport face à une solution plus simple.
