# Contribuer au WoW Calendrier EU FR

Merci de votre intérêt pour ce projet !

L'objectif est de proposer un calendrier World of Warcraft (Europe – Français) fiable, précis et facile à maintenir. Avant de proposer une modification, merci de prendre connaissance des recommandations suivantes.

---

# Prérequis

Le projet nécessite uniquement :

- Python 3.10 ou supérieur
- Aucune dépendance externe

---

# Structure du projet

```
.
├── data/                  # Données des événements (JSON)
├── docs/
│   └── data-format.md     # Documentation du format des données
├── scripts/
│   ├── build.py           # Génération du calendrier ICS
│   └── validate.py        # Validation des fichiers JSON
├── wow-eu.ics             # Calendrier généré
├── README.md
└── CONTRIBUTING.md
```

---

# Workflow recommandé

Après avoir cloné le dépôt :

```bash
git clone https://github.com/<utilisateur>/WOW-calendrier-EU-fr.git

cd WOW-calendrier-EU-fr

python scripts/validate.py

python scripts/build.py
```

Si aucune erreur n'est signalée, vous pouvez créer votre Pull Request.

---

# Ajouter ou modifier un événement

Tous les événements sont définis dans les fichiers JSON du dossier `data/`.

Chaque événement doit respecter le format décrit dans :

```
docs/data-format.md
```

Les champs obligatoires sont :

- `uid`
- `title`
- `start`

Les autres champs sont optionnels.

---

# Validation

Avant toute Pull Request, exécutez :

```bash
python scripts/validate.py
```

Le validateur vérifie notamment :

- la syntaxe JSON ;
- les champs obligatoires ;
- les champs inconnus ;
- les types de données ;
- le format des dates ;
- les UID en double ;
- les URL HTTPS ;
- les catégories.

Aucune erreur ne doit être signalée.

---

# Génération du calendrier

Une fois les données validées :

```bash
python scripts/build.py
```

Le fichier `wow-eu.ics` est alors généré.

---

# Style du projet

Le projet privilégie un code simple et facile à maintenir.

Merci de respecter les principes suivants :

- utiliser uniquement la bibliothèque standard Python ;
- privilégier les fonctions simples ;
- éviter les dépendances externes ;
- écrire un code clair et lisible ;
- conserver un style cohérent avec le reste du projet.

---

# Qualité des données

Les données constituent le cœur du projet.

Avant de proposer un nouvel événement, vérifiez systématiquement :

- les dates ;
- le titre ;
- les descriptions ;
- les liens Internet.

Lorsque cela est possible, privilégiez toujours les sources officielles de Blizzard.

---

# Pull Requests

Merci de limiter chaque Pull Request à un seul sujet.

Exemples :

- correction d'une date ;
- ajout d'un événement ;
- amélioration de la documentation ;
- amélioration des scripts.

Évitez de regrouper plusieurs modifications indépendantes dans une même Pull Request.

---

# Avant de créer une Pull Request

Vérifiez les points suivants :

- [ ] Les fichiers JSON sont valides.
- [ ] `python scripts/validate.py` ne retourne aucune erreur.
- [ ] `python scripts/build.py` génère correctement le calendrier.
- [ ] Les informations ajoutées ont été vérifiées.
- [ ] La Pull Request traite un seul sujet.

---

Merci pour votre contribution !
