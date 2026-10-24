# 10. Communication

**Objectif.** Que la personne qui dirige voie, à chaque moment, ce qu'il faut pour décider, sans avoir à relancer.

## Montrer [éprouvé]

- **Ouvrir le résultat** (vidéo, page, image) dès qu'il est prêt, puis **vérifier qu'il s'est effectivement ouvert** ;
  sinon, donner le chemin exact ([A19](../quality/anti-patterns.md#a19)).
- **Montrer ce qui a été demandé** : si l'on attend l'œuvre animée, des images fixes ne suffisent pas
  ([A1](../quality/anti-patterns.md#a1)).
- **Montrer tôt** : un rendu court ou partiel vaut mieux qu'une attente silencieuse ; l'ouverture d'une page peut être
  programmée dès que les premiers résultats sont prêts.
- **Une page de revue locale** rassemble les vidéos, comparatifs et mesures d'une étape
  ([`review_page.py`](../../tools/README.md#review_pagepy)).
- **Publier en privé seulement**, et seulement avec l'accord de la personne qui dirige ; une œuvre tierce ne quitte
  pas la machine sans accord.

## Points d'avancement [éprouvé]

Un point contient :

1. **Ce qui fonctionne** (vérifié).
2. **Ce qui reste à corriger.**
3. **La prochaine action**, et le temps estimé si un calcul est en cours.
4. **Ce qui attend la personne qui dirige**, le cas échéant (décision, validation).

Il est **court** ([modèle](../../templates/status-update.md)). Pendant les longues tâches, on l'envoie **sans attendre
la demande**.

## Répondre à la question posée [éprouvé]

| Question | Réponse attendue |
|---|---|
| « Combien de temps, et pourquoi ? » | Un chiffre, ses hypothèses, la cause principale |
| « Ça sert à quoi ? » | Le rôle de l'étape en une ou deux phrases, et ce qui se passerait sans elle |
| « Est-ce que ça marchera parfaitement ? » | Oui ou non, la preuve, la limite |
| « Qu'as-tu choisi et pourquoi ? » | Le choix, les raisons, les alternatives écartées |

## Rester aligné sur l'objectif [éprouvé]

Quand la personne qui dirige demande de rappeler l'objectif du projet, elle vérifie que l'agent ne s'est pas égaré.
L'objectif et le critère essentiel du cadrage doivent pouvoir être reformulés à tout moment ; on les relit avant chaque
bilan.

## Forme [éprouvé]

- La langue de la personne qui dirige, avec une orthographe et des accents corrects.
- Valeurs absolues sur la **dernière version** ; les versions passées seulement si elles sont demandées.
- Côtés désignés du point de vue du spectateur, et dits explicitement (« à droite de l'image »).
- Tableaux courts pour les comparatifs : profil, mesure, différence visible, recommandation.
- Reconnaître un oubli ou un défaut sans détour, puis montrer la correction.
