# Format des données

Tous les événements du projet sont décrits dans des fichiers **JSON** situés dans le dossier `data/`.

Chaque fichier contient un tableau JSON (`array`) d'un ou plusieurs événements.

---

# Structure d'un événement

Chaque événement utilise la structure suivante :

```json
{
  "id": "holiday_brewfest",
  "uid": "holiday_brewfest_2026",
  "title": "🍺 Fête des Brasseurs",
  "start": "20260920",
  "end": "20261007",
  "category": "holiday",
  "location": "Forgefer ou Orgrimmar",
  "description": "Participez aux festivités brassicoles, affrontez Coren Navrebière et récoltez des jetons de la fête des Brasseurs.",
  "url": "https://…",
  "sources": [
    "https://…",
    "https://…"
  ]
}
```

---

# Champs

| Champ | Obligatoire | Description |
|--------|:-----------:|-------------|
| `id` | Oui | Identifiant unique de l'événement. |
| `uid` | Oui | Identifiant unique utilisé dans le calendrier ICS. |
| `title` | Oui | Nom de l'événement précédé d'un emoji. |
| `start` | Oui | Date de début au format `YYYYMMDD`. |
| `end` | Oui | Date de fin au format `YYYYMMDD`. |
| `category` | Oui | Catégorie de l'événement. |
| `location` | Non | Principal lieu de l'événement. |
| `description` | Non | Courte description de l'événement. |
| `url` | Non | Lien principal vers une source officielle. |
| `sources` | Non | Liste des sources utilisées pour documenter l'événement. |

---

# Le champ `location`

Le champ `location` doit rester volontairement court.

Il représente le principal point de départ de l'événement.

Trois cas sont utilisés.

## Type A — Lieu unique

```text
Reflet-de-Lune
```

## Type B — Deux lieux principaux

```text
Hurlevent ou Fossoyeuse
```

```text
Forgefer ou Orgrimmar
```

## Type C — Événement réparti

```text
Différents lieux d'Azeroth
```

Le champ `location` ne doit pas devenir une liste exhaustive de villes.

---

# Le champ `description`

La description présente :

- ce qu'est l'événement ;
- les activités principales ;
- les principales récompenses.

Elle doit rester concise.

Le calendrier n'a pas vocation à remplacer un guide de jeu.

---

# Le champ `sources`

Les sources sont classées selon l'ordre de priorité suivant :

1. Blizzard Entertainment
2. Site officiel World of Warcraft
3. Warcraft Wiki

Les sites communautaires peuvent être utilisés uniquement lorsqu'une information n'est pas disponible dans les sources officielles.

---

# Conventions

Le projet applique les conventions suivantes :

- UTF-8
- JSON valide
- identifiants uniques
- terminologie officielle Blizzard
- descriptions homogènes
- calendrier compatible RFC 5545

---

# Validation

Avant toute génération du calendrier :

```bash
python scripts/validate.py
```

Puis :

```bash
python scripts/build.py
```

Les données invalides bloquent la génération du fichier ICS.

---

# Évolution du modèle

Le modèle de données est volontairement stable.

L'ajout d'un nouveau champ doit rester exceptionnel afin de préserver la compatibilité avec les scripts de validation et de génération.
