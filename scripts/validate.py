#!/usr/bin/env python3
"""Valide tous les fichiers JSON du dossier data."""

from __future__ import annotations

import sys

from event_data import (
    DataError,
    ROOT,
    duplicate_values,
    json_files,
    load_config,
    load_events,
    validate_event,
)


def main() -> int:
    print("─" * 64)
    print(" WoW Calendrier EU FR — Validation des données")
    print("─" * 64)

    try:
        load_config()
        events = load_events()
        files = json_files()
    except DataError as exc:
        print(f"✗ ERROR   {exc}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    for loaded in events:
        location = f"{loaded.file.relative_to(ROOT)} — événement no {loaded.number}"
        for message in validate_event(loaded.data):
            errors.append(f"{location}\n           {message}")
        if "description" not in loaded.data:
            warnings.append(f"{location}\n           Description absente.")

    for field in ("uid", "id"):
        for value, first, second in duplicate_values(events, field):
            errors.append(
                f"{second.file.relative_to(ROOT)} — événement no {second.number}\n"
                f"           {field.upper()} en double : {value!r}. Déjà utilisé dans "
                f"{first.file.relative_to(ROOT)}, événement no {first.number}."
            )

    if errors:
        print()
        for error in errors:
            print(f"✗ ERROR   {error}")

    if warnings:
        print()
        for warning in warnings:
            print(f"⚠ WARNING {warning}")

    print()
    print("─" * 64)
    print(f"Fichiers JSON : {len(files)}")
    print(f"Événements    : {len(events)}")
    print(f"Erreurs       : {len(errors)}")
    print(f"Avertissements: {len(warnings)}")
    print("─" * 64)

    if errors:
        print("✗ Validation échouée.")
        return 1

    print("✓ Toutes les données sont valides.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
