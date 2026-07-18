#!/usr/bin/env python3
"""
WoW Calendrier EU FR
Générateur du fichier wow-eu.ics
"""

import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
OUTPUT = ROOT / "wow-eu.ics"


def escape_ics(value):
    """Échappe les caractères spéciaux RFC5545."""
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace(";", r"\;")
        .replace(",", r"\,")
        .replace("\n", r"\n")
    )


def validate_date(value):
    datetime.strptime(value, "%Y%m%d")


def validate_events(events):
    seen = set()

    for event in events:

        for field in ("uid", "title", "start"):
            if field not in event:
                raise ValueError(
                    f"Champ obligatoire manquant : {field}\n{event}"
                )

        validate_date(event["start"])

        if "end" in event:
            validate_date(event["end"])

        uid = event["uid"]

        if uid in seen:
            raise ValueError(f"UID en double : {uid}")

        seen.add(uid)


def load_events():
    events = []

    for file in sorted(DATA_DIR.glob("*.json")):

        with open(file, encoding="utf-8") as f:

            data = json.load(f)

            if not isinstance(data, list):
                raise ValueError(
                    f"{file.name} doit contenir une liste."
                )

            events.extend(data)

    return events


def write_calendar(events):

    now = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//WoW Calendrier EU FR//Retail//FR",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:WoW Retail EU FR",
        "X-WR-TIMEZONE:Europe/Zurich",
    ]

    for event in events:

        lines.append("BEGIN:VEVENT")
        lines.append(f"UID:{escape_ics(event['uid'])}")
        lines.append(f"DTSTAMP:{now}")
        lines.append(f"SUMMARY:{escape_ics(event['title'])}")
        lines.append(f"DTSTART;VALUE=DATE:{event['start']}")

        if "end" in event:
            lines.append(f"DTEND;VALUE=DATE:{event['end']}")

        if "rrule" in event:
            lines.append(f"RRULE:{event['rrule']}")

        if "description" in event:
            lines.append(
                f"DESCRIPTION:{escape_ics(event['description'])}"
            )

        if "url" in event:
            lines.append(
                f"URL:{escape_ics(event['url'])}"
            )

        if "category" in event:

            category = event["category"]

            if isinstance(category, list):
                category = ",".join(category)

            lines.append(
                f"CATEGORIES:{escape_ics(category)}"
            )

        lines.append("END:VEVENT")

    lines.append("END:VCALENDAR")

    OUTPUT.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(f"{len(events)} événements générés.")


def main():

    events = load_events()

    validate_events(events)

    events.sort(key=lambda e: e["start"])

    write_calendar(events)


if __name__ == "__main__":
    main()
