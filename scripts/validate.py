#!/usr/bin/env python3
"""
WoW Calendrier EU FR
Validation des fichiers JSON
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"


def validate_date(value):
    """Valide une date au format YYYYMMDD."""
    return datetime.strptime(value, "%Y%m%d")


def is_https_url(value):
    """Vérifie qu'une URL utilise HTTPS."""
    url = urlparse(value)
    return url.scheme == "https" and bool(url.netloc)


def load_events():
    """Charge tous les fichiers JSON du dossier data."""

    events = []

    for file in sorted(DATA_DIR.glob("*.json")):

        try:

            with open(file, encoding="utf-8") as f:
                data = json.load(f)

        except json.JSONDecodeError as e:

            print(
                f"ERREUR : {file.name}\n"
                f"JSON invalide (ligne {e.lineno}, colonne {e.colno})\n"
            )

            continue

        if not isinstance(data, list):

            print(
                f"ERREUR : {file.name}\n"
                "Le fichier doit contenir une liste.\n"
            )

            continue

        for index, event in enumerate(data, start=1):

            events.append(
                {
                    "file": file.name,
                    "index": index,
                    "event": event,
                }
            )

    return events
def validate_events(events):
    """Vérifie les événements."""

    errors = 0

    seen_uid = set()
    seen_id = set()

    required = ("uid", "title", "start", "category")

    for item in events:

        file = item["file"]
        index = item["index"]
        event = item["event"]

        # Champs obligatoires
        for field in required:

            if field not in event:

                print(
                    f"ERREUR : {file} (événement {index})\n"
                    f"Champ obligatoire manquant : {field}\n"
                )

                errors += 1

        # Impossible d'aller plus loin
        if any(field not in event for field in required):
            continue

        # Date de début
        try:

            start = validate_date(event["start"])

        except ValueError:

            print(
                f"ERREUR : {file} (événement {index})\n"
                f"Date invalide : {event['start']}\n"
            )

            errors += 1
            continue

        # Date de fin
        if "end" in event:

            try:

                end = validate_date(event["end"])

                if end <= start:

                    print(
                        f"ERREUR : {file} (événement {index})\n"
                        "La date de fin doit être postérieure à la date de début.\n"
                    )

                    errors += 1

            except ValueError:

                print(
                    f"ERREUR : {file} (événement {index})\n"
                    f"Date invalide : {event['end']}\n"
                )

                errors += 1

        # UID
        uid = event["uid"]

        if uid in seen_uid:

            print(
                f"ERREUR : {file} (événement {index})\n"
                f"UID en double : {uid}\n"
            )

            errors += 1

        else:
            seen_uid.add(uid)

        # ID (optionnel)
        if "id" in event:

            identifier = event["id"]

            if identifier in seen_id:

                print(
                    f"ERREUR : {file} (événement {index})\n"
                    f"ID en double : {identifier}\n"
                )

                errors += 1

            else:
                seen_id.add(identifier)

        # URL
        if "url" in event:

            if not is_https_url(event["url"]):

                print(
                    f"ERREUR : {file} (événement {index})\n"
                    f"URL invalide : {event['url']}\n"
                )

                errors += 1

    return errors
def main():

    print("WoW Calendrier EU FR")
    print("Validation des données\n")

    events = load_events()

    if not events:

        print("Aucun événement trouvé.")
        return 1

    errors = validate_events(events)

    print("----------------------------------------")
    print(f"{len(events)} événements contrôlés")

    if errors:

        print(f"{errors} erreur(s) détectée(s).")
        return 1

    print("Aucune erreur détectée.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
