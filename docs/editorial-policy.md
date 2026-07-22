# Politique éditoriale

## Objectif

Le projet **WoW Calendrier EU FR** a pour objectif de fournir un calendrier iCalendar (.ics) des événements de **World of Warcraft Retail Europe**, entièrement en français.

Chaque événement doit être :

- exact ;
- homogène ;
- facilement maintenable ;
- fondé sur des sources vérifiables.

Le calendrier n'a pas vocation à remplacer un guide de jeu. Il présente uniquement les informations essentielles permettant au joueur d'identifier rapidement un événement.

---

# Principes éditoriaux

Chaque événement doit répondre à trois questions :

- Quand a lieu l'événement ?
- Où commence-t-il ?
- De quoi s'agit-il ?

Les descriptions doivent rester concises et privilégier les informations les plus utiles.

Les stratégies de jeu, les listes exhaustives de récompenses ou les explications détaillées n'ont pas leur place dans ce projet.

---

# Terminologie

Lorsque Blizzard publie une terminologie officielle en français, celle-ci est toujours privilégiée.

Cela concerne notamment :

- le nom des événements ;
- les noms des PNJ ;
- les monnaies d'événement ;
- les objets ;
- les hauts faits ;
- les lieux.

La casse (majuscules et minuscules) est reproduite telle qu'elle apparaît dans les publications officielles.

---

# Sources

Les informations sont vérifiées dans l'ordre de priorité suivant :

1. Blizzard Entertainment
2. Site officiel World of Warcraft
3. Warcraft Wiki

Les sites communautaires (Wowhead, Icy Veins, etc.) peuvent être utilisés pour compléter une information absente des sources officielles, mais ne doivent pas s'y substituer.

Toute information importante doit pouvoir être vérifiée.

---

# Structure des événements

Chaque événement comprend les champs suivants :

- id
- uid
- title
- start
- end
- category
- location
- description
- url
- sources

Le format détaillé est documenté dans :

```
docs/data-format.md
```

---

# Champ « location »

Le champ `location` représente le principal point de départ de l'événement.

Il doit rester court.

Trois cas sont utilisés.

## Type A — Lieu unique

Exemple :

```
Reflet-de-Lune
```

## Type B — Deux lieux principaux

Exemple :

```
Hurlevent ou Fossoyeuse
```

ou

```
Forgefer ou Orgrimmar
```

## Type C — Événement réparti

Lorsque l'événement se déroule dans de nombreux lieux sans qu'un point de départ unique ne soit pertinent :

```
Différents lieux d'Azeroth
```

Le champ `location` ne doit pas devenir une liste exhaustive de villes.

---

# Description

La description doit être courte et informative.

Elle présente :

- l'événement ;
- les activités principales ;
- les principales récompenses.

Elle ne doit pas devenir un guide de jeu.

Les formulations promotionnelles sont évitées.

Exemples :

- récompenses exclusives
- contenu exceptionnel
- incroyable événement

sauf lorsqu'elles sont reprises explicitement d'une communication officielle de Blizzard.

---

# Style rédactionnel

Les descriptions utilisent un ton neutre.

Exemples :

- Participez…
- Célébrez…
- Honorez…
- Accueillez…
- Partez…

Le style doit rester homogène dans l'ensemble du projet.

Toutes les descriptions doivent donner l'impression d'avoir été rédigées par une seule personne.

---

# Évolution du jeu

World of Warcraft évolue régulièrement.

Lorsqu'une nouvelle extension ajoute un nouveau hub principal ou modifie un événement, les données sont mises à jour tout en conservant les principes éditoriaux du projet.

La structure des événements doit rester stable d'une extension à l'autre.

---

# Contrôle qualité

Avant toute publication :

- les données sont validées automatiquement ;
- les identifiants sont uniques ;
- les dates sont vérifiées ;
- les sources sont contrôlées ;
- le calendrier ICS est régénéré.

Les Pull Requests doivent respecter cette politique éditoriale.

---

# Philosophie

La qualité du projet repose davantage sur la cohérence que sur la quantité d'informations.

Chaque événement doit permettre au joueur de comprendre immédiatement :

- quand l'événement a lieu ;
- où le trouver ;
- pourquoi il existe.

Pour les informations détaillées, les utilisateurs sont invités à consulter les sources officielles référencées dans chaque événement.
