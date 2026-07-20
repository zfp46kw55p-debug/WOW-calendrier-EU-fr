# WoW Calendrier EU FR

Un calendrier **iCalendar (ICS)** regroupant les événements de **World of Warcraft – Europe (Français)**.

Le projet permet de générer un fichier `.ics` pouvant être importé dans la plupart des applications de calendrier (Google Calendar, Outlook, Thunderbird, Apple Calendar, etc.).

L'objectif est de fournir un calendrier :

- fiable ;
- simple ;
- facilement maintenable ;
- basé sur des données structurées au format JSON.

---

## Fonctionnalités

- Génération d'un calendrier au format **ICS**
- Données stockées dans des fichiers **JSON**
- Validation automatique des données avant génération
- Aucune dépendance externe (bibliothèque standard Python uniquement)
- Compatible avec les principaux logiciels de calendrier

---

## Structure du projet

```
.
├── data/                  # Données des événements
├── docs/
│   └── data-format.md     # Documentation du format JSON
├── scripts/
│   ├── build.py           # Génération du calendrier
│   └── validate.py        # Validation des données
├── wow-eu.ics             # Calendrier généré
├── README.md
└── CONTRIBUTING.md
```

---

## Prérequis

- Python 3.10 ou supérieur
- Aucune dépendance externe

---

## Installation

Clonez le dépôt :

```bash
git clone https://github.com/<utilisateur>/WOW-calendrier-EU-fr.git

cd WOW-calendrier-EU-fr
```

---

## Vérification des données

Avant toute génération, vérifiez les fichiers JSON :

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

---

## Génération du calendrier

Une fois la validation réussie :

```bash
python scripts/build.py
```

Le calendrier est généré dans le fichier :

```
wow-eu.ics
```

---

## Utilisation

Le fichier `wow-eu.ics` peut être importé dans :

- Google Calendar
- Microsoft Outlook
- Mozilla Thunderbird
- Apple Calendar
- tout logiciel compatible iCalendar (.ics)

---

## Données

Les événements sont décrits dans les fichiers JSON du dossier `data/`.

La spécification complète du format est disponible ici :

```
docs/data-format.md
```

---

## Contribuer

Les contributions sont les bienvenues.

Avant de proposer une modification, consultez :

```
CONTRIBUTING.md
```

---

## Philosophie du projet

Le projet privilégie :

- la simplicité ;
- la lisibilité ;
- l'absence de dépendances externes ;
- un code facile à maintenir ;
- des données vérifiées avant chaque génération.

---

## Feuille de route

Les évolutions envisagées comprennent notamment :

- amélioration continue des données ;
- automatisation des contrôles via GitHub Actions ;
- enrichissement de la documentation ;
- ajout de nouveaux événements liés à World of Warcraft.

---

## Licence

Ce projet est distribué sous licence **MIT** (à adapter selon la licence choisie).

---

## Remerciements

Merci à toutes les personnes qui contribuent à maintenir un calendrier World of Warcraft fiable et à jour pour la communauté francophone.
