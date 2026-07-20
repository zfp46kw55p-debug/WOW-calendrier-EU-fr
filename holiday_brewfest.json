# WoW Calendrier EU FR

Calendrier **iCalendar (`.ics`)** des événements de **World of Warcraft Retail – Europe**, en français.

Le dépôt est volontairement simple : les événements sont des objets JSON, le validateur contrôle les données et le générateur produit `wow-eu.ics`. Ajouter ou corriger un événement ne demande aucune modification du code Python.

## Utilisation rapide

Prérequis : **Python 3.10 ou supérieur**, sans dépendance externe.

```bash
python scripts/validate.py
python scripts/build.py
```

Le calendrier généré se trouve à la racine du dépôt :

```text
wow-eu.ics
```

## Ajouter un événement

La méthode la plus simple est l'assistant interactif :

```bash
python scripts/new_event.py micro_holidays.json
```

Il demande les informations utiles, ajoute l'objet au bon fichier et le trie. Il reste ensuite à lancer :

```bash
python scripts/validate.py
python scripts/build.py
```

Il est également possible de copier `templates/event.json` et d'ajouter manuellement l'objet dans un fichier de `data/`.

## Mettre à jour un événement

1. Ouvrir le fichier JSON concerné dans `data/`.
2. Corriger les dates, le texte ou les sources.
3. Ne jamais changer un `uid` déjà publié, sauf nécessité absolue.
4. Exécuter le validateur puis le générateur.

Les dates utilisent le format `YYYYMMDD`. La date `end` est **exclusive** : un événement d'une seule journée commençant le 1er janvier se termine donc le 2 janvier.

## Structure

```text
.
├── config.json                 # Nom, URL et réglages du calendrier
├── data/                       # Source de vérité : événements JSON
├── docs/
│   ├── CONTRIBUTING.md
│   ├── data-format.md
│   └── editorial-policy.md
├── scripts/
│   ├── build.py                # Génération ICS
│   ├── event_data.py           # Chargement et règles communes
│   ├── new_event.py            # Assistant d'ajout
│   └── validate.py             # Contrôles avant génération
├── templates/
│   └── event.json              # Modèle à copier
└── wow-eu.ics
```

Le chargeur lit automatiquement tous les fichiers `*.json` de `data/`, y compris dans de futurs sous-dossiers. Les noms commençant par `_` sont ignorés.

## Documentation

- [Format des données](docs/data-format.md)
- [Politique éditoriale](docs/editorial-policy.md)
- [Guide de contribution](docs/CONTRIBUTING.md)

## Principes

- Données simples et lisibles.
- Aucun cas particulier d'événement dans le code.
- Validation avant chaque génération.
- Sources Blizzard privilégiées, puis sources communautaires reconnues.
- Bibliothèque standard Python uniquement.

## Licence

Le dépôt ne contient actuellement pas encore de fichier de licence. Il convient d'en choisir une avant une publication formelle.
