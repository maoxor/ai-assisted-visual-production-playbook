# <nom du projet>

<Une ou deux phrases : ce que produit le projet, pour qui.> Langue de travail : <langue>.

<!-- Fichier chargé à chaque session : rester court. Détails dans docs/. -->

## Carte

| Chemin | Contenu |
|---|---|
| `config/` | Paramètres nommés (source de vérité) ; régénérer après modification |
| `scripts/` | Génération, production, contrôles, exports |
| `docs/BRIEF.md` | Objectif, critère essentiel, contraintes, hypothèses |
| `docs/instruction-register.md` | Consignes durables, actives, remplacées ; demandes et leur état |
| `docs/experiments/` | Journal numéroté des essais |
| `docs/work-logs/` | Journaux des travaux longs |
| `docs/decisions/` | Décisions structurantes |
| `archive/` | Versions précédentes (jamais modifiées) |

## Vérifier (avant de conclure une tâche)

```bash
<commandes de contrôle du projet>
```

Ne jamais déclarer un travail vérifié sans avoir lancé ces commandes : citer leur résultat.

## Méthode appliquée

Référentiel : `production-playbook` (principes, workflow, listes de contrôle). En bref :

1. **Reprendre d'abord** : état réel (processus, `git status`), journal, registre des consignes ; les fichiers font
   foi.
2. **Une variable à la fois**, sur un **échantillon** ; référence de l'état actuel avant chaque essai ; diagnostic par
   extinction si la cause est inconnue.
3. **Juger dans les conditions finales** : <taille, vitesse, traitement final, plateforme>. Vidéos de contrôle en
   avant, œuvre entière, dernière version. Mesures en complément, jamais comme preuve.
4. **Corriger la cause**, jamais masquer (flou global, test désactivé, amplitude réduite).
5. **Coût mesuré** avant toute production longue ; production reprenable avec empreinte des dépendances.
6. **Ne rien perdre** : archiver avant de changer, sorties séparées par version, ne rien supprimer (déplacer).
7. **Terminé** = livrables finaux existants, ouverts et contrôlés ; bilan terminé / testé / limites ; chaque demande
   avec son état.
8. **Montrer** : ouvrir les résultats ; points courts (ce qui marche, ce qui reste, prochaine action).

Traduction de la méthode pour ce projet :

- Unité de production : <…>
- Conditions finales : <…>
- Échantillon qui porte le risque principal : <…>
- Familles de contrôles retenues : <…>
- Coûts à séparer : <…>

## Règles impératives

- Décisions réversibles : les prendre sans redemander. Publication, envoi de données à un service externe, achat,
  suppression, production longue réservée : accord explicite.
- Ne jamais toucher aux processus d'autres projets ou sessions ; calculs lourds via le verrou commun s'il existe.
- Ressource ajoutée : provenance, licence, version, rôle, empreinte consignés.
- Secrets : jamais lus, affichés ni commités.
- Git : branche dédiée, commits `type(portée): description` (pourquoi, preuve, limites), pas de push ni de fusion sans
  demande ; identité Git du poste.

## Spécifique au projet

- Formats et conditions finales : <…>
- Zones protégées, à préserver : <…>
- Direction artistique validée : <renvoi vers docs/decisions/…>
