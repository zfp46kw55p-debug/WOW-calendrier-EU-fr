# WoW Calendrier EU FR

Un calendrier **iCalendar (.ics)** des événements de **World of Warcraft Retail Europe**, entièrement en français.

Le projet fournit un calendrier prêt à importer dans Outlook, Google Calendar, Apple Calendar, Thunderbird et toute application compatible avec le format **iCalendar (RFC 5545)**.

Toutes les données sont maintenues dans des fichiers JSON simples, validées automatiquement puis converties en un calendrier ICS unique.

---

## Pourquoi ce projet ?

Ce projet est né du constat qu'il n'existait pas de calendrier francophone réunissant les principaux événements de **World of Warcraft Retail Europe** dans un format :

- simple à utiliser ;
- documenté ;
- facilement maintenable ;
- basé sur des sources officielles.

Contrairement à un guide de jeu, ce calendrier fournit uniquement les informations essentielles :

- le nom de l'événement ;
- sa période ;
- son principal lieu de déroulement ;
- une courte description ;
- un lien vers les sources officielles.

---

# Fonctionnalités

- calendrier iCalendar (.ics)
- événements Retail Europe
- entièrement en français
- terminologie officielle Blizzard
- descriptions courtes et homogènes
- génération automatique
- validation automatique des données
- structure entièrement basée sur des fichiers JSON

---

# Compatibilité

Le calendrier est compatible avec toute application prenant en charge le format iCalendar, notamment :

- Microsoft Outlook
- Google Calendar
- Apple Calendar
- Mozilla Thunderbird
- toute application compatible RFC 5545

---

# Structure du projet

```
.
├── data/
│   ├── holiday_*.json
│   ├── micro_holiday_*.json
│   ├── bonus_event_*.json
│   └── ...
│
├── docs/
│   ├── editorial-policy.md
│   ├── CONTRIBUTING.md
│   └── data-format.md
│
├── scripts/
│   ├── build.py
│   ├── validate.py
│   ├── event_data.py
│   └── new_event.py
│
└── wow-eu.ics
```

---

# Génération

Validation des données :

```bash
python scripts/validate.py
```

Génération du calendrier :

```bash
python scripts/build.py
```

Le fichier généré est :

```
wow-eu.ics
```

---

# Qualité des données

Toutes les données sont vérifiées avant leur intégration.

Les principales règles sont :

- identifiants uniques ;
- UID uniques ;
- dates valides ;
- structure JSON homogène ;
- terminologie officielle Blizzard lorsque disponible ;
- descriptions concises ;
- sources documentées.

Les conventions éditoriales sont détaillées dans :

```
docs/editorial-policy.md
```

---

# Sources

Les informations sont vérifiées en privilégiant les sources suivantes :

1. Blizzard Entertainment
2. Site officiel World of Warcraft
3. Warcraft Wiki

Des sources complémentaires peuvent être utilisées lorsqu'une information n'est pas disponible dans les publications officielles.

---

# Contribution

Les contributions sont les bienvenues.

Avant toute modification, merci de consulter :

- `docs/CONTRIBUTING.md`
- `docs/editorial-policy.md`
- `docs/data-format.md`

Les Pull Requests sont automatiquement validées avant la génération du calendrier.

---

# Philosophie

Le calendrier a pour objectif de répondre rapidement aux questions suivantes :

- Quand a lieu l'événement ?
- Où commence-t-il ?
- De quoi s'agit-il ?

Il n'a pas vocation à remplacer un guide de jeu.

---

# Licence

Voir le fichier `LICENSE`.
