# Principes de qualité

Ces seize principes valent quels que soient le projet, la technique et la direction artistique. Ils expliquent
**pourquoi** le [workflow](workflow/README.md) est construit ainsi. Quand une étape doit être adaptée à un domaine,
l'étape change, le principe reste.

Tous les principes sont **[éprouvé]**, sauf mention contraire.

---

<a id="p1"></a>

## P1. Le résultat perçu fait foi ; les mesures l'éclairent sans le prouver

**Énoncé.** Un travail se juge sur ce que verra le destinataire : l'image à sa taille d'affichage, le mouvement à
vitesse normale, l'expérience dans son environnement réel. Les métriques (SSIM, VMAF, contraste, pourcentages) servent
au diagnostic et à la non-régression. Elles ne prouvent jamais une réussite et ne deviennent pas des objectifs.

**Pourquoi.** Une variation mesurable n'est pas forcément visible. Une métrique devenue objectif se fait optimiser au
détriment de ce qu'elle représentait.

**Comment.** Chaque mesure est accompagnée de la capture ou de la vidéo à inspecter. On écrit d'abord ce que l'on
voit, puis ce que la mesure confirme ou nuance. Les seuils restent indicatifs ; quand ils viennent d'une autre source,
on le dit.

**Anti-modèle.** Réduire un traitement parce qu'une mesure baisse alors que la personne qui dirige préfère la version
riche ([A12](quality/anti-patterns.md#a12)).

---

<a id="p2"></a>

## P2. « Vérifié » veut dire exécuté et cité ; nos contrôles ne valent pas validation

**Énoncé.** Un contrôle n'est déclaré fait qu'après avoir été exécuté, avec son résultat cité (commande, chiffre,
fichier). On distingue toujours *ce que l'agent a vérifié*, *ce que la personne qui dirige a validé* et *ce qui n'a pas
pu être vérifié*.

**Pourquoi.** Un compte rendu peut être tronqué, une case cochée sans preuve, une hypothèse prise pour un fait. La
confiance repose sur la traçabilité.

**Comment.** Les journaux portent la mention « Ces observations sont les miennes ; elles ne valent pas validation ».
Les rapports listent les contrôles réellement exécutés. Ce qui est émulé ou non testable est signalé comme tel.

---

<a id="p3"></a>

## P3. Terminé signifie : les fichiers finaux existent, s'ouvrent et ont été contrôlés

**Énoncé.** Une commande lancée, un calcul en cours, un prototype ou un plan ne sont pas une livraison. Le travail est
terminé quand les livrables existent à leur emplacement définitif, se lisent dans leur environnement cible et ont
passé les contrôles prévus.

**Pourquoi.** L'écart entre « lancé » et « livré » concentre les défauts : unité manquante, fichier illisible dans la
cible, élément résiduel oublié. Il donne aussi la fausse impression d'avoir fini.

**Comment.** La [définition de « terminé »](quality/README.md#definition-of-done) sert de liste de sortie. Le bilan
sépare *terminé*, *testé* et *limites*.

---

<a id="p4"></a>

## P4. Séparer ce qui est documenté, testé, supposé et observé

**Énoncé.** Dans une recherche ou un diagnostic, chaque affirmation porte son statut : **D** documenté (source citée),
**T** testé dans le projet, **H** hypothèse, **O** observation sur nos résultats. Une technique n'est jamais attribuée à
un studio ou à un auteur sans source directe.

**Pourquoi.** Sinon, une supposition devient un fait, un conseil de forum devient une règle, et l'erreur se propage
d'itération en itération.

**Comment.** Les notes de recherche suivent le [modèle](../templates/research-note.md). Les pages inaccessibles sont
signalées.

---

<a id="p5"></a>

## P5. Une recherche ciblée sert une décision, puis s'arrête

**Énoncé.** On recherche pour résoudre un problème précis ou trancher un choix technique. Les sources primaires passent
d'abord ; les forums sont des pistes à vérifier par un essai. On réutilise les recherches précédentes et l'on passe à
l'essai dès qu'une méthode est assez étayée.

**Pourquoi.** Une recherche sans fin retarde la preuve ; une liste de liens ne fait rien avancer ; ignorer les essais
passés fait refaire les mêmes impasses.

**Comment.** Voir [la recherche](workflow/02-research.md). L'agent mène la recherche lui-même, en parallélisant les
requêtes ([décision 0003](decisions/0003-no-subagents.md)).

---

<a id="p6"></a>

## P6. Une variable à la fois ; isoler pour comprendre

**Énoncé.** Un essai modifie une seule chose. Un défaut se diagnostique **par extinction** : on neutralise une cause
possible à la fois (une source de lumière, un matériau peint en noir, un module désactivé, un élément caché) jusqu'à
ce que le défaut disparaisse. Les corrections sont rangées en familles désactivables.

**Pourquoi.** Plusieurs changements simultanés rendent l'effet de chacun illisible : une correction peut en masquer
une autre ou introduire une régression invisible.

**Comment.** Voir [l'itération sur preuves](workflow/04-evidence-based-iteration.md) et la
[technique d'extinction](domains/offline-3d-rendering.md#diagnosis-by-elimination).

---

<a id="p7"></a>

## P7. L'échantillon d'abord, la généralisation ensuite

**Énoncé.** Une méthode nouvelle se met au point sur **un échantillon représentatif** : un élément, un extrait de
quelques secondes, une image difficile, un écran critique. On vérifie le résultat *et* le coût, puis on étend par lots
mesurés. La production complète ne démarre qu'avec l'accord explicite de la personne qui dirige.

**Pourquoi.** Itérer sur le tout coûte des heures par essai. Un défaut généralisé se corrige partout, et un coût
multiplié par cent éléments peut rendre la production impraticable.

**Comment.** [Prototype minimal](workflow/03-prototyping.md), puis échantillon, puis extrait de validation au format
final, puis production.

---

<a id="p8"></a>

## P8. Juger dans les conditions finales

**Énoncé.** On évalue :
- à la **taille finale d'affichage** ;
- à **vitesse normale** ;
- dans le **traitement final** (flou de profondeur de champ, réduction, encodage, build de production) ;
- sur l'**œuvre entière** ;
- en **lecture en avant**, jamais en aller-retour ;
- sur la **dernière version**, pas sur une version passée prise comme étalon.

Le ralenti, l'amplification, les vues de diagnostic et les gros plans servent à comprendre : ils ne valident rien.

**Pourquoi.** Un détail invisible à la taille finale ne compte pas ; un défaut visible seulement en mouvement passe
inaperçu sur une image fixe ; une boucle en aller-retour masque le raccord ; comparer à une ancienne version brouille la
décision.

**Comment.** Toute vidéo de contrôle montre l'œuvre entière, en avant, à la taille finale ; les gros plans viennent
en plus. Les tableaux donnent des valeurs absolues sur la version actuelle.

---

<a id="p9"></a>

## P9. Corriger la cause, pas le symptôme

**Énoncé.** Un défaut se corrige là où il naît. On ne le masque pas par un flou global, une baisse d'amplitude, un
débruitage qui efface les détails, la désactivation d'un test ou un recadrage.

**Pourquoi.** Le symptôme masqué revient ailleurs, et l'on perd la qualité que l'on voulait préserver.

**Comment.** On cherche à quelle étape le défaut apparaît (génération, rendu, débruitage, redimensionnement,
encodage, lecture, code, données) et l'on corrige à cette étape. Un compromis assumé est montré précisément.

---

<a id="p10"></a>

## P10. Ne rien perdre : versions identifiables, archives, sorties séparées

**Énoncé.**
- Chaque version est identifiable.
- Avant tout changement important, l'état courant est archivé.
- Les sorties de versions différentes ne se mélangent jamais.
- Un résultat n'est réutilisé que s'il correspond exactement à l'état actuel, ce que vérifie une empreinte des
  dépendances.
- Rien n'est supprimé : l'obsolète est déplacé.

**Pourquoi.** Revenir à un état antérieur est fréquent ; mélanger les sorties de deux états produit des livrables faux
et difficiles à détecter ; une comparaison avant/après exige l'avant.

**Comment.** Voir [la production](workflow/06-production.md#fingerprint-and-resume) et l'outil
[`fingerprint.py`](../tools/README.md#fingerprintpy).

---

<a id="p11"></a>

## P11. Reproductible par construction

**Énoncé.**
- Les paramètres vivent dans une configuration déclarative, aux noms explicites.
- La génération procédurale dérive d'une graine stable.
- Les dépendances, modèles et révisions sont figés.
- Toute ressource ajoutée porte sa provenance, sa licence et son empreinte.
- On régénère plutôt que de retoucher à la main.

**Pourquoi.** Une retouche manuelle est perdue à la régénération suivante ; une graine instable rend deux
constructions différentes ; une ressource sans licence vérifiée bloque une diffusion.

**Comment.** Voir [la reproductibilité en rendu](domains/offline-3d-rendering.md#reproducibility) et
[la provenance des ressources](tooling/README.md#provenance-and-licensing).

---

<a id="p12"></a>

## P12. Autonomie sur le réversible, accord pour l'irréversible et l'extérieur

**Énoncé.** Les décisions techniques et artistiques **réversibles** se prennent sans redemander, à partir de la
référence et des consignes. Exigent un accord explicite :
- les publications, les achats, les abonnements ;
- l'envoi de données ou d'assets vers un service externe ;
- les suppressions ;
- les changements système destructifs ;
- le lancement d'une production longue quand la personne qui dirige se l'est réservé.

Quand un blocage exige vraiment une intervention, on pose une question précise et l'on poursuit les tâches
indépendantes.

**Pourquoi.** Redemander à chaque étape épuise la personne qui dirige ; agir seul sur l'irréversible peut coûter des
droits, de l'argent ou des données.

---

<a id="p13"></a>

## P13. Mesurer le coût réel avant de produire, et séparer les coûts

**Énoncé.** Avant une production longue, on mesure le coût réel sur des unités représentatives, dont une difficile ;
on distingue démarrage et régime établi ; on attribue chaque dépense à sa cause par des tests isolés. On sépare des
coûts qui ne se confondent pas : temps de production, poids du livrable, coût de lecture ou d'exécution, maintenance.
Aucun réglage n'est intouchable : son utilité doit être démontrée.

**Pourquoi.** Un effet cher à calculer peut être bon marché à diffuser, et inversement. Un coût par unité qui dérive
finit par empêcher toute itération.

**Comment.** Voir [le profil de coût](workflow/06-production.md#cost-profile).

---

<a id="p14"></a>

## P14. Montrer, et rester aligné sur l'objectif

**Énoncé.**
- On montre le résultat (ouvrir la vidéo, la page, l'image) au lieu de le décrire, et l'on vérifie qu'il s'est ouvert.
- Les points d'avancement sont courts : ce qui fonctionne, ce qui reste, la prochaine action.
- On répond à la question posée.
- On sait reformuler à tout moment l'objectif et le critère essentiel du projet.

**Pourquoi.** La personne qui dirige juge sur pièce. Une explication sans résultat, une page qui ne s'ouvre pas ou une
réponse à côté obligent à relancer et érodent la confiance.

**Comment.** Voir [la communication](workflow/10-communication.md).

---

<a id="p15"></a>

## P15. La consigne la plus récente et explicite l'emporte ; tenir le registre des consignes

**Énoncé.** Les consignes évoluent : une demande peut en remplacer explicitement une autre. On tient un **registre
des consignes actives**, avec leur date et ce qu'elles remplacent. Avant de présenter une itération comme terminée, on
vérifie que chacune de ses demandes a été traitée.

**Pourquoi.** Une ancienne consigne appliquée par inertie contredit la direction actuelle. Une demande oubliée au
milieu d'une longue liste est le défaut le plus frustrant pour la personne qui dirige.

**Comment.** Un [registre](../templates/instruction-register.md), relu à chaque reprise et avant chaque bilan. Le
bilan reprend chaque demande avec l'un des états : *fait*, *essai écarté (raison)* ou *manquant*. Quand une consigne
change, on cherche **toutes** ses traces (textes, mentions, réglages).

---

<a id="p16"></a>

## P16. Chaque élément a un rôle ; le sujet reste le centre

**Énoncé.** Dans une composition, chaque élément important reçoit un **rôle** : attirer le regard, fragmenter,
donner de la profondeur, ménager une zone de lecture. Les effets accompagnent le sujet sans le concurrencer. Les
mouvements sont coordonnés sans être synchronisés, sans agitation permanente. Ce principe porte sur la **méthode** de
composition : les rôles eux-mêmes et le dosage sont des décisions propres à chaque projet, prises par la personne qui
dirige.

**Pourquoi.** Un effet sans rôle dilue l'attention ; des oscillations identiques partout produisent un mouvement
mécanique.

---

## Ce qui ne relève pas des principes

Les principes ne disent rien du style, des formats ni des outils d'un projet. Ces choix sont des entrées de chaque
projet et se consignent dans ses propres décisions
([décision 0002](decisions/0002-method-separate-from-aesthetics.md)).
