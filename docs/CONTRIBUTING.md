# Contribuer

Merci de contribuer au projet **WoW Calendrier EU FR**.

L'objectif est de maintenir un calendrier fiable, homogène et facile à maintenir.

---

# Avant de commencer

Merci de lire les documents suivants :

- README.md
- docs/editorial-policy.md
- docs/data-format.md

Ils décrivent les conventions utilisées dans tout le projet.

---

# Ajouter un événement

Les événements sont définis dans les fichiers JSON du dossier `data/`.

Avant toute modification :

- vérifier que l'événement n'existe pas déjà ;
- utiliser le modèle fourni ;
- respecter la structure documentée.

---

# Sources

Toute nouvelle information doit être vérifiable.

Ordre de priorité :

1. Blizzard Entertainment
2. Site officiel World of Warcraft
3. Warcraft Wiki

Les sites communautaires ne doivent être utilisés qu'en complément.

---

# Style éditorial

Le calendrier est volontairement concis.

Les descriptions doivent :

- expliquer ce qu'est l'événement ;
- rester courtes ;
- utiliser la terminologie officielle Blizzard ;
- conserver le même style que les autres événements.

Le calendrier n'est pas un guide de jeu.

---

# Champ location

Le champ `location` doit rester court.

Exemples :

```
Reflet-de-Lune
```

```
Hurlevent ou Fossoyeuse
```

```
Différents lieux d'Azeroth
```

Les listes de villes sont à éviter.

---

# Validation

Avant toute Pull Request :

```bash
python scripts/validate.py
```

Puis :

```bash
python scripts/build.py
```

Le fichier `wow-eu.ics` doit être régénéré.

---

# Checklist

Avant d'ouvrir une Pull Request :

- [ ] Données valides
- [ ] Sources vérifiées
- [ ] Terminologie Blizzard
- [ ] Description concise
- [ ] JSON validé
- [ ] Calendrier régénéré

---

# Philosophie

Chaque événement doit permettre au joueur de répondre rapidement aux questions suivantes :

- Quand ?
- Où ?
- De quoi s'agit-il ?

Pour les informations détaillées, les utilisateurs sont invités à consulter les liens officiels présents dans chaque événement.
