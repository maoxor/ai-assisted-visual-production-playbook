# Avant une production longue

## Décision

- [ ] Accord explicite de lancer, si la personne qui dirige se l'est réservé.
- [ ] Extrait de validation (forme du livrable final, réglages de livraison) validé, sauf instruction contraire
      explicite.
- [ ] Registre des consignes relu : **toutes** les corrections demandées sont faites
      ([A2](../anti-patterns.md#a2)).
- [ ] Défauts identifiés corrigés ; aucun « on verra après ».

## Contenu (adapter au domaine)

- [ ] Fidélité du sujet sur l'état de référence.
- [ ] Zones protégées respectées sur toute la durée (visage, interface, texte).
- [ ] Géométrie générée valide : orientation, fermeture, auto-intersections ([A13](../anti-patterns.md#a13)).
- [ ] Bords et marges aux positions extrêmes.
- [ ] Boucle : raccord exact de l'état à la période complète (position et vitesse), sans unité dupliquée.
- [ ] Unités représentatives en qualité finale, dont les poses et angles extrêmes.
- [ ] Reste de la composition inchangé après la dernière correction (comparaison élément par élément).
- [ ] Éléments résiduels absents de la chaîne : signature, logo, texte, réglage d'essai.

## Coût et chaîne

- [ ] Coût par unité mesuré sur une machine libre, première unité distinguée du régime établi
      ([A16](../anti-patterns.md#a16)).
- [ ] Estimation totale annoncée, avec ses hypothèses.
- [ ] Chaîne reprenable : empreinte des dépendances, unité terminée = fichier complet, paquets, obsolètes déplacés
      ([`fingerprint.py`](../../../tools/README.md#fingerprintpy)).
- [ ] Configuration et sources archivées avant le lancement.
- [ ] Espace disque suffisant ; alimentation secteur ; mise en veille empêchée ([A15](../anti-patterns.md#a15)).
- [ ] Étapes suivantes enchaînées : post-traitement, contrôles, exports, tests.
- [ ] Consigne posée : **ne rien modifier** des dépendances pendant le calcul.
