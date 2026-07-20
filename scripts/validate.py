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
