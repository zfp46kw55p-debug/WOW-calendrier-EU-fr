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


def load_events():
    events = []

    for file in sorted(DATA_DIR.glob("*.json")):
        with open(file, encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):
                events.extend(data)
            else:
                raise ValueError(f"{file.name} doit contenir une liste.")

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

        lines.append(f"UID:{event['uid']}")
        lines.append(f"DTSTAMP:{now}")

        lines.append(f"SUMMARY:{event['title']}")

        lines.append(f"DTSTART;VALUE=DATE:{event['start']}")

        if "end" in event:
            lines.append(f"DTEND;VALUE=DATE:{event['end']}")

        if "rrule" in event:
            lines.append(f"RRULE:{event['rrule']}")

        if "description" in event:
            lines.append(
                f"DESCRIPTION:{event['description']}"
            )

        if "url" in event:
            lines.append(f"URL:{event['url']}")

        if "category" in event:
            lines.append(
                f"CATEGORIES:{event['category']}"
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

    events.sort(key=lambda e: e["start"])

    write_calendar(events)


if __name__ == "__main__":
    main()
