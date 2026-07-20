# Contribuer

Le projet est conçu pour qu'un événement puisse être ajouté ou corrigé sans toucher au code Python.

## Ajouter un événement

Méthode recommandée :

```bash
python scripts/new_event.py micro_holidays.json
```

L'assistant ajoute l'événement et trie le fichier. Une autre possibilité consiste à copier `templates/event.json` et à modifier directement un fichier de `data/`.

## Modifier un événement

Rechercher son `uid` dans `data/`, modifier uniquement les informations nécessaires, puis conserver cet UID. Les changements de dates annuelles peuvent en revanche nécessiter un nouvel objet avec un nouvel UID daté.

## Contrôles obligatoires

Avant tout commit ou Pull Request :

```bash
python scripts/validate.py
python scripts/build.py
```

Le premier contrôle la syntaxe, les champs, les dates, les doublons, les URL et les récurrences. Le second régénère `wow-eu.ics`.

## Qualité éditoriale

- Utiliser le titre français officiel lorsqu'il existe.
- Donner une description courte et utile dans un calendrier.
- Indiquer `end` comme date exclusive.
- Ajouter au moins une source fiable lorsque l'information a été vérifiée.
- Privilégier les sources officielles Blizzard.
- Limiter une Pull Request à un seul sujet cohérent.

La politique complète figure dans `docs/editorial-policy.md` et le schéma des champs dans `docs/data-format.md`.

## Ajouter un nouveau fichier de données

Créer simplement `data/nom_du_groupe.json` contenant :

```json
[]
```

Le générateur le découvrira automatiquement. Aucun registre ni changement dans `build.py` n'est nécessaire.

## Modifier le format

Un nouveau champ ne doit pas être ajouté isolément dans les données. Il faut aussi :

1. expliquer son utilité dans `docs/data-format.md` ;
2. l'ajouter aux règles de `scripts/event_data.py` ;
3. préciser s'il doit être exporté dans `scripts/build.py` ;
4. valider les données existantes.
