# Anti-modèles

Erreurs classiques d'une collaboration entre une personne qui dirige et un agent, chacune avec son symptôme, son coût
et sa prévention. Toutes sont **[éprouvé]** : elles ont été commises puis corrigées en conditions réelles. Les plus
coûteuses viennent en premier.

Format : **symptôme** → **coût** → **prévention**.

---

<a id="a1"></a>

### A1. Présenter des images fixes quand on attend du mouvement

- **Symptôme.** La validation porte sur une œuvre animée, et l'agent présente des images.
- **Coût.** Relances répétées, perte de confiance.
- **Prévention.** Le livrable de validation a la forme du livrable final : un vrai extrait continu, avec les réglages
  de livraison. Les images fixes complètent une vidéo, elles ne la remplacent pas ([P8](../principles.md#p8)).

<a id="a2"></a>

### A2. Oublier une correction demandée

- **Symptôme.** Une demande figurait dans un long message, souvent à côté d'un ordre de lancement, et n'a pas été
  traitée.
- **Coût.** Production à relancer, frustration.
- **Prévention.** Registre des consignes ; avant tout lancement long et avant chaque bilan, reprendre chaque demande
  avec son état ([P15](../principles.md#p15)).

<a id="a3"></a>

### A3. Laisser un élément résiduel dans les livrables

- **Symptôme.** Une signature, un logo, une mention provisoire (« démo », « droits non confirmés ») ou un réglage
  d'essai reste dans un livrable ou dans la page d'intégration, parfois après qu'une consigne a changé.
- **Coût.** Défaut visible découvert par la personne qui dirige.
- **Prévention.**
  - Un contrôle des éléments résiduels figure dans toute liste de livraison. On cherche **où** un élément est ajouté
    (calcul, post-traitement, page), pas seulement s'il est visible ([liste livraison](checklists/delivery.md)).
  - Un ajout de ce type est désactivable par la configuration, et son absence est vérifiée sur toutes les unités.
  - Quand une consigne change, on cherche **toutes** ses traces : textes, mentions, réglages.

<a id="a4"></a>

### A4. Laisser le coût de production dériver jusqu'à empêcher l'itération

- **Symptôme.** Les réglages s'accumulent (échantillons, suréchantillonnage, micro-détails invisibles) jusqu'à des
  heures de calcul pour quelques secondes.
- **Coût.** Plus aucune itération possible dans le délai.
- **Prévention.** Le coût par unité est suivi à chaque itération ; toute hausse se justifie visuellement ; un profil
  de coût précède la production ([P13](../principles.md#p13)).

<a id="a5"></a>

### A5. Présenter un changement imperceptible

- **Symptôme.** « Je ne vois aucune différence » : les détails modifiés sont trop petits pour la taille d'affichage.
- **Prévention.** Avant de présenter, vérifier soi-même, à la taille finale et à vitesse normale, que la différence se
  voit ; travailler à une échelle perceptible.

<a id="a6"></a>

### A6. Comparer à une ancienne version au lieu de la dernière

- **Symptôme.** Les tableaux et messages prennent une version passée pour étalon.
- **Prévention.** Valeurs absolues sur la version actuelle, avant et après la correction. Une version passée sert
  d'étalon seulement sur demande. Une solution mesurée sur un état ancien est revalidée sur l'état actuel.

<a id="a7"></a>

### A7. Vidéos de contrôle en aller-retour

- **Symptôme.** Les comparatifs jouent 0 → n → 0, ce qui masque le vrai mouvement et le raccord.
- **Prévention.** Lecture en avant seulement, en boucle, sur l'œuvre entière
  ([`review_video.py`](../../tools/README.md#review_videopy)).

<a id="a8"></a>

### A8. Déléguer à des sous-agents contre la préférence de la personne qui dirige

- **Symptôme.** L'agent répartit la recherche entre des sous-agents alors que la personne qui dirige veut qu'il la
  mène lui-même.
- **Prévention.** Recherche menée par l'agent, en parallélisant les appels d'outils
  ([décision 0003](../decisions/0003-no-subagents.md)).

<a id="a9"></a>

### A9. Paramètre sans effet pris pour une correction

- **Symptôme.** Un paramètre est réglé depuis plusieurs versions pour corriger un défaut, mais il n'agit pas dans les
  conditions du projet (par exemple un réglage spéculaire sur une surface entièrement transmissive).
- **Prévention.** Vérifier le sens et l'effet de chaque paramètre **dans le moteur et la version utilisés** : mesurer
  le résultat, ne pas se contenter de régler la valeur.

<a id="a10"></a>

### A10. Erreur de configuration silencieuse

- **Symptôme.** Une clé se retrouve dans la mauvaise section après une modification structurelle (l'ordre des tables
  TOML, par exemple), et plusieurs essais sont faits sans elle.
- **Prévention.** Après toute modification structurelle de la configuration, diff sémantique avec la version archivée :
  seuls des changements voulus doivent apparaître.

<a id="a11"></a>

### A11. Graine non déterministe

- **Symptôme.** Un même élément procédural diffère d'une construction à l'autre, parce que sa graine vient d'une
  fonction instable (`hash()` de Python change à chaque processus) ou de l'ordre d'itération.
- **Prévention.** Toute graine dérive d'une valeur stable (nom, numéro, CRC32 d'une chaîne) ; un test de
  reconstruction vérifie l'identité au bit près.

<a id="a12"></a>

### A12. Défendre sa recommandation artistique contre le choix de la personne qui dirige

- **Symptôme.** L'agent recommande un traitement sobre, mesures à l'appui, alors que la personne qui dirige préfère la
  version riche.
- **Prévention.** Proposer des variantes contrastées, présenter les mesures comme contrôle et non comme argument ; le
  choix final appartient à la personne qui dirige.

<a id="a13"></a>

### A13. Montrer une version qui portait un défaut non détecté

- **Symptôme.** Une géométrie générée a des normales retournées ou n'est pas fermée ; le défaut est découvert après la
  présentation.
- **Prévention.** Contrôle automatique de validité de toute géométrie générée (orientation par le volume signé,
  fermeture, intersections). Un défaut découvert après coup se signale toujours, avec un avant/après de la correction.

<a id="a14"></a>

### A14. Juger la stabilité sur des aperçus dégradés

- **Symptôme.** Des aperçus peu échantillonnés exagèrent fortement le scintillement et faussent la décision.
- **Prévention.** Bruit et scintillement se jugent en qualité finale, à la taille finale. Les aperçus servent au
  mouvement et à la composition.

<a id="a15"></a>

### A15. Laisser la machine se mettre en veille pendant un calcul long

- **Symptôme.** Un portable passe sur batterie, capot fermé, et un calcul de quelques minutes prend des heures.
- **Prévention.** Avant un calcul long, vérifier alimentation, mise en veille et espace disque ; lancer via un script
  qui attend le secteur ; choisir une chaîne reprenable ([production](../workflow/06-production.md)).

<a id="a16"></a>

### A16. Prendre une première mesure de temps aberrante pour la vérité

- **Symptôme.** La première unité inclut la préparation (chargement, compilation) ou la machine est occupée ; le temps
  annoncé est faux.
- **Prévention.** Refaire toute mesure surprenante, croiser sur une machine libre, distinguer la première unité du
  régime établi.

<a id="a17"></a>

### A17. Laisser un malentendu sur une consigne ambiguë

- **Symptôme.** Une consigne admettait deux lectures (orientation d'une face ou sens d'un relief, par exemple) et
  l'agent a traité la mauvaise.
- **Prévention.** Écrire ce que l'on a compris, traiter la lecture la plus probable, signaler l'autre dans le bilan.

<a id="a18"></a>

### A18. Recopier tels quels des contrôles devenus inadaptés

- **Symptôme.** Après un changement de périmètre (un sujet statique devient animé, par exemple), les contrôles hérités
  produisent des faux positifs ou ne contrôlent plus rien d'utile.
- **Prévention.** À chaque changement de périmètre, relire les contrôles hérités et les adapter.

<a id="a19"></a>

### A19. Annoncer ouvert un fichier ou une page qui ne l'est pas

- **Symptôme.** « La page ne s'est pas ouverte. »
- **Prévention.** Vérifier que l'ouverture a réussi (processus, fenêtre, URL) ; sinon, donner le chemin exact.

<a id="a20"></a>

### A20. Proposer des directions artistiques sans ambition

- **Symptôme.** Plusieurs séries de propositions sont rejetées parce qu'elles reprennent l'existant au lieu de viser
  les meilleures références du domaine (espaces, mouvement, réponses aux actions, vraie 3D quand elle sert).
- **Prévention.** Fixer la barre sur les meilleures références du domaine ; prototyper en mouvement et filmer avant de
  conclure.

---

## Ajouter un anti-modèle

Dès qu'une erreur est corrigée dans un projet : ouvrir une issue « Lesson learned », puis ajouter l'entrée ici sous
forme **générique**, sans nom de projet ni détail de livrable ([`CONTRIBUTING.md`](../../CONTRIBUTING.md)). Une erreur
qui se répète devient une règle dans un principe, une étape du workflow ou une liste de contrôle.
