# Format des données

Tous les événements du calendrier sont définis dans des fichiers JSON situés dans le dossier `data/`.

Chaque fichier contient une **liste d'événements**.

```json
[
    {
        "uid": "wow-brewfest",
        "title": "La fête des Brasseurs",
        "start": "20260920"
    }
]
```

---

# Structure d'un événement

| Champ | Type | Obligatoire | Description |
|-------|------|-------------|-------------|
| uid | string | Oui | Identifiant unique de l'événement. |
| title | string | Oui | Nom affiché dans le calendrier. |
| start | string | Oui | Date de début au format `YYYYMMDD`. |
| end | string | Non | Date de fin (exclusive) au format `YYYYMMDD`. |
| description | string | Non | Description de l'événement. |
| location | string | Non | Lieu de l'événement. |
| url | string | Non | Lien HTTPS vers une source officielle. |
| rrule | string | Non | Règle de récurrence au format iCalendar. |
| category | string ou liste | Non | Catégorie(s) de l'événement. |

---

# Champs obligatoires

## uid

Chaque événement possède un identifiant unique.

Exemple :

```json
{
    "uid": "wow-hallows-end"
}
```

Bonnes pratiques :

- uniquement des lettres minuscules ;
- utiliser des tirets (`-`) comme séparateurs ;
- rester descriptif ;
- ne jamais réutiliser un UID existant.

Exemples :

```
wow-brewfest
wow-darkmoon-faire
wow-pirates-day
```

---

## title

Nom affiché dans le calendrier.

```json
"title": "La fête des Brasseurs"
```

Le titre doit être court, clair et lisible.

---

## start

Date de début.

Format obligatoire :

```
YYYYMMDD
```

Exemple :

```json
"start": "20260920"
```

---

# Champs optionnels

## end

Date de fin.

```json
"end": "20261006"
```

La date de fin doit être postérieure à la date de début.

Conformément à la norme iCalendar, la date de fin est **exclusive**.

---

## description

Texte libre.

Exemple :

```json
"description": "Événement mondial disponible dans toutes les capitales."
```

---

## location

Lieu affiché dans le calendrier.

```json
"location": "Hurlevent"
```

---

## url

Lien vers une source officielle.

```json
"url": "https://worldofwarcraft.blizzard.com/"
```

Seules les URL HTTPS sont acceptées.

---

## rrule

Permet de créer des événements récurrents.

Exemple :

```json
"rrule": "FREQ=YEARLY"
```

La syntaxe utilisée est celle de la norme iCalendar.

---

## category

Une ou plusieurs catégories.

Exemple :

```json
"category": "holiday"
```

ou

```json
"category": [
    "holiday",
    "world-event"
]
```

---

# Exemple complet

```json
{
    "uid": "wow-brewfest",
    "title": "La fête des Brasseurs",
    "start": "20260920",
    "end": "20261006",
    "description": "Événement mondial.",
    "location": "Forgefer",
    "url": "https://worldofwarcraft.blizzard.com/",
    "rrule": "FREQ=YEARLY",
    "category": [
        "holiday",
        "world-event"
    ]
}
```

---

# Validation

Avant chaque génération du calendrier, exécutez :

```bash
python scripts/validate.py
```

Le validateur contrôle notamment :

- la syntaxe JSON ;
- les champs obligatoires ;
- les champs inconnus ;
- les types de données ;
- le format des dates ;
- les UID en double ;
- les URL HTTPS ;
- les catégories.

Aucune erreur ne doit être signalée avant de lancer la génération du calendrier.

---

# Génération

Une fois la validation réussie :

```bash
python scripts/build.py
```

Le fichier `wow-eu.ics` est alors généré à la racine du projet.
