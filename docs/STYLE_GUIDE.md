# Guide de style

Ce document définit les conventions de rédaction et de format utilisées dans le projet **WoW Calendrier EU FR**.

Toutes les nouvelles données doivent respecter ces règles.

---

# Structure JSON

Les propriétés sont toujours présentées dans cet ordre :

```json
{
  "id": "",
  "uid": "",
  "title": "",
  "start": "",
  "end": "",
  "category": "",
  "location": "",
  "description": "",
  "url": "",
  "sources": []
}
```

---

# id

- minuscules uniquement
- snake_case
- stable dans le temps
- basé sur le nom anglais officiel lorsque cela est pertinent

Exemple :

```
holiday_darkmoon_faire

micro_holiday_glowcap_festival

weekly_timewalking
```

---

# uid

Le champ uid est unique.

Convention :

```
<id>_<année>
```

Exemple :

```
holiday_darkmoon_faire_2026
```

---

# title

Le titre :

- utilise toujours le nom officiel français ;
- commence par un emoji ;
- ne contient aucun commentaire supplémentaire.

Exemples :

```
🎣 Concours de pêche de Strangleronce

🦖 Paléon'Goro

🎈 Festival des montgolfières
```

---

# start

Format :

```
YYYYMMDD
```

Toujours basé sur le calendrier européen.

---

# end

Même format.

La date de fin est exclusive conformément à la norme iCalendar.

---

# category

Valeurs actuellement utilisées :

```
holiday

micro_holiday

weekly_event

fishing_event

world_boss

season

history

special_event
```

Les nouvelles catégories doivent rester exceptionnelles.

---

# location

Le lieu correspond uniquement au lieu principal.

Éviter les listes.

Bon exemple :

```
Ancien Silithus
```

Moins bon exemple :

```
Silithus, Tanaris, Kalimdor
```

---

# description

Objectif :

présenter l'événement.

Pas expliquer comment le réussir.

Longueur :

une ou deux phrases.

La première phrase commence de préférence par un verbe.

Exemples :

```
Affrontez...

Découvrez...

Rejoignez...

Célébrez...

Embarquez...
```

Ne jamais écrire :

```
Cette année...

Nouveau...

Actuellement...
```

---

# url

Ordre de préférence :

1. Blizzard France
2. Wowhead France
3. Blizzard anglais
4. Wowhead anglais

---

# sources

Toujours une liste JSON.

Une source minimum.

Deux lorsque cela est possible.

Exemple :

```json
"sources": [
  "...",
  "..."
]
```

---

# Emoji

Chaque événement possède un emoji unique lorsque cela est possible.

L'objectif est d'améliorer la lisibilité dans les applications de calendrier.

Exemple :

🎣 pêche

🎉 fête

⚔️ combat

🦖 dinosaures

🎈 montgolfière

👕 vêtements

🪲 scarabée

---

# Langue

Tout le contenu est rédigé en français.

Les noms anglais peuvent apparaître uniquement :

- dans les identifiants ;
- dans les URLs ;
- dans les sources.

---

# Objectif

Les fichiers doivent être :

- homogènes ;
- lisibles ;
- faciles à maintenir ;
- simples à relire lors des mises à jour annuelles.
