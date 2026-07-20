#!/usr/bin/env python3
"""Ajoute simplement un événement dans un fichier JSON existant ou nouveau."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from event_data import DATA_DIR, DataError, ROOT, validate_event


def ask(label: str, required: bool = False) -> str:
    while True:
        value = input(f"{label}{' *' if required else ''} : ").strip()
        if value or not required:
            return value
        print("Ce champ est obligatoire.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Ajouter un événement au calendrier.")
    parser.add_argument(
        "file",
        nargs="?",
        help="Fichier cible dans data/ (ex. micro_holidays.json)",
    )
    args = parser.parse_args()

    target_name = args.file or ask("Fichier cible dans data/", required=True)
    target = DATA_DIR / target_name
    if target.suffix.lower() != ".json":
        target = target.with_suffix(".json")
    try:
        target.resolve().relative_to(DATA_DIR.resolve())
    except ValueError:
        print("Le fichier cible doit rester dans le dossier data/.", file=sys.stderr)
        return 1

    event: dict[str, object] = {
        "uid": ask("UID unique", required=True),
        "title": ask("Titre", required=True),
        "start": ask("Début (YYYYMMDD)", required=True),
    }

    end = ask("Fin exclusive (YYYYMMDD, laisser vide pour 1 jour)")
    if end:
        event["end"] = end

    event["category"] = ask("Catégorie", required=True)

    for field, label in (
        ("description", "Description"),
        ("location", "Lieu"),
        ("url", "URL affichée"),
        ("rrule", "Règle RRULE"),
    ):
        value = ask(label)
        if value:
            event[field] = value

    source = ask("Source HTTPS de vérification")
    if source:
        event["sources"] = [source]

    errors = validate_event(event)
    if errors:
        print("L'événement n'a pas été ajouté :", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if target.exists():
        try:
            data = json.loads(target.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            print(f"JSON invalide dans {target}: {exc}", file=sys.stderr)
            return 1
        if not isinstance(data, list):
            print(f"{target} ne contient pas une liste JSON.", file=sys.stderr)
            return 1
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        data = []

    data.append(event)
    data.sort(key=lambda item: (item.get("start", ""), item.get("title", "").casefold()))
    target.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"✓ Événement ajouté dans {target.relative_to(ROOT)}.")
    print("Étape suivante : python scripts/validate.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
