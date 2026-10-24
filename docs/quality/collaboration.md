# Préférences de collaboration

Préférences par défaut entre la personne qui dirige et l'agent. Elles sont **[éprouvé]** et valables d'un projet à
l'autre ; une consigne explicite du projet les remplace ([P15](../principles.md#p15)).

| # | Préférence |
|---|---|
| C1 | **Langue de la personne qui dirige**, avec une orthographe et des accents corrects, dans les échanges et la documentation |
| C2 | **Pas de sous-agents** : l'agent mène lui-même recherches et travaux ([décision 0003](../decisions/0003-no-subagents.md)) |
| C3 | **Local par défaut** : rien de publié, téléversé ou déployé sans accord ; aucun achat ni abonnement |
| C4 | **Autonomie sur les décisions réversibles**, sans redemander à chaque étape ([P12](../principles.md#p12)) |
| C5 | **Montrer le résultat** : ouvrir rendus et pages dès qu'ils sont prêts, et vérifier l'ouverture |
| C6 | **Vidéos de contrôle en avant, œuvre entière, dernière version** ([P8](../principles.md#p8)) |
| C7 | **Points d'avancement courts** : ce qui marche, ce qui reste, la prochaine action |
| C8 | **Conserver les versions précédentes** ; ne rien écraser |
| C9 | **Le jugement visuel de la personne qui dirige l'emporte** sur les mesures de l'agent |
| C10 | **Côtés désignés du point de vue du spectateur** |
| C11 | **Ne pas toucher aux processus des autres projets** ni aux sessions parallèles |
| C12 | **Identité Git du poste** : commits signés par l'identité configurée sur la machine, jamais par une identité reprise de commits existants |
| C13 | **Pas de push ni de fusion sans demande** ; jamais de travail direct sur la branche principale |
| C14 | **Pas de régénération du sujet par IA** quand une œuvre source existe ([décision 0004](../decisions/0004-preserve-the-source.md)) |
| C15 | **Niveau visé : les meilleures références du domaine**, jugé sur le rendu et l'expérience |

## Extrait prêt à copier

Pour appliquer ces préférences à tous les projets, copier ce bloc dans les instructions globales de Claude Code
(`~/.claude/CLAUDE.md`, ou le dossier de configuration utilisé sur le poste). Le référentiel ne modifie pas ces
fichiers lui-même.

```markdown
## Méthode de travail (référentiel : production-playbook)

- Répondre dans la langue de l'utilisateur, orthographe et accents corrects.
- Mener soi-même les recherches et les travaux, sans sous-agents.
- Rester en local : ne rien publier, téléverser, déployer ni acheter sans accord explicite.
- Décider seul ce qui est réversible ; demander pour l'irréversible et l'extérieur.
- « Vérifié » = commande exécutée et résultat cité ; distinguer mes contrôles de la validation de l'utilisateur.
- Terminé = livrables finaux existants, ouverts et contrôlés ; un calcul lancé n'est pas une livraison.
- Juger à la taille finale, à vitesse normale, sur la dernière version ; vidéos de contrôle en avant, œuvre entière.
- Une variable à la fois ; échantillon avant généralisation ; coût mesuré avant production.
- Corriger la cause, jamais masquer (flou global, test désactivé).
- Conserver les versions précédentes ; séparer les sorties ; ne rien supprimer sans accord.
- Tenir un journal et un registre des consignes ; points d'avancement courts ; ouvrir les résultats.
```
