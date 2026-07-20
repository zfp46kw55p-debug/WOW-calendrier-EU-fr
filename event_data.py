# Format des données

Tous les événements sont enregistrés dans des fichiers JSON du dossier `data/`. Chaque fichier contient une **liste**, même lorsqu'il n'y a encore aucun événement :

```json
[]
```

Le générateur lit automatiquement tous les `*.json` de `data/` et de ses sous-dossiers. Un nom commençant par `_` est ignoré.

## Exemple minimal

```json
[
  {
    "uid": "weekly-reset-eu",
    "title": "Réinitialisation hebdomadaire",
    "start": "20260722",
    "rrule": "FREQ=WEEKLY;BYDAY=WE",
    "category": "Réinitialisation"
  }
]
```

## Exemple complet

```json
[
  {
    "id": "holiday-brewfest",
    "uid": "holiday-brewfest-2026",
    "title": "🍺 Fête des Brasseurs",
    "start": "20260920",
    "end": "20261007",
    "category": [
      "Fête mondiale",
      "Fête des Brasseurs"
    ],
    "description": "Participez aux festivités brassicoles et obtenez des récompenses saisonnières.",
    "location": "Dornogal, Forgefer et Orgrimmar",
    "url": "https://worldofwarcraft.blizzard.com/",
    "sources": [
      "https://worldofwarcraft.blizzard.com/"
    ]
  }
]
```

## Champs

| Champ | Type | Obligatoire | Usage |
|---|---|:---:|---|
| `uid` | chaîne | oui | Identifiant iCalendar unique et stable. |
| `title` | chaîne | oui | Titre affiché dans le calendrier. |
| `start` | chaîne | oui | Date de début au format `YYYYMMDD`. |
| `category` | chaîne ou liste | oui | Catégorie(s) exportée(s) dans l'ICS. |
| `end` | chaîne | non | Date de fin **exclusive**, format `YYYYMMDD`. |
| `id` | chaîne | non | Identifiant interne stable, en minuscules sans espaces. |
| `description` | chaîne | non | Description affichée dans le calendrier. |
| `location` | chaîne | non | Lieu dans le jeu. |
| `url` | chaîne HTTPS | non | Lien principal affiché dans le calendrier. |
| `sources` | liste d'URL HTTPS | non | Sources de vérification, non exportées dans l'ICS. |
| `rrule` | chaîne | non | Règle de récurrence iCalendar contenant `FREQ=`. |

Aucun autre champ n'est accepté sans adaptation préalable du validateur et de la documentation.

## Règles importantes

### UID

Le `uid` doit être unique dans tout le dépôt. Pour un événement daté, inclure l'année ou la date évite les collisions :

```json
"uid": "darkmoon-20260104"
```

Pour une récurrence permanente, conserver un UID stable :

```json
"uid": "weekly-reset-eu"
```

Un UID déjà publié ne doit pas être renommé sans nécessité, car les applications de calendrier pourraient créer un doublon.

### Dates

Les dates sont écrites sans séparateur :

```json
"start": "20260920"
```

`end` est exclusive. Pour un événement visible du 20 septembre au 6 octobre inclus :

```json
"start": "20260920",
"end": "20261007"
```

Pour un événement d'une seule journée, `end` peut être omise.

### Sources

`sources` sert à documenter la vérification sans surcharger l'événement ICS. Privilégier Blizzard, puis Warcraft Wiki, Wowhead ou Icy Veins lorsque la source officielle ne suffit pas.

## Ajouter un événement

Assistant recommandé :

```bash
python scripts/new_event.py nom_du_fichier.json
```

Ajout manuel : copier `templates/event.json`, compléter les champs et insérer l'objet dans la liste du fichier concerné.

## Vérification et génération

```bash
python scripts/validate.py
python scripts/build.py
```
