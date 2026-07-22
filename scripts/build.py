#!/usr/bin/env python3
"""Génère le calendrier wow-eu.ics à partir des fichiers JSON."""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from typing import Iterable

from event_data import (
    DataError,
    ROOT,
    categories,
    is_datetime_value,
    load_config,
    load_events,
    validate_event,
)


def escape_ics(value: object) -> str:
    """Échappe une valeur texte selon RFC 5545."""
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace(";", r"\;")
        .replace(",", r"\,")
        .replace("\r\n", r"\n")
        .replace("\n", r"\n")
        .replace("\r", r"\n")
    )


def fold_line(line: str, limit: int = 75) -> list[str]:
    """Plie une ligne ICS sans couper un caractère UTF-8."""
    chunks: list[str] = []
    remaining = line
    first = True
    while len(remaining.encode("utf-8")) > limit:
        prefix = "" if first else " "
        available = limit - len(prefix.encode("utf-8"))
        cut = 0
        used = 0
        for index, char in enumerate(remaining):
            size = len(char.encode("utf-8"))
            if used + size > available:
                break
            used += size
            cut = index + 1
        chunks.append(prefix + remaining[:cut])
        remaining = remaining[cut:]
        first = False
    chunks.append(("" if first else " ") + remaining)
    return chunks


def append(lines: list[str], line: str) -> None:
    """Ajoute une ligne ICS en appliquant le pliage RFC 5545."""
    lines.extend(fold_line(line))


def append_temporal(lines: list[str], property_name: str, value: object) -> None:
    """Ajoute DTSTART ou DTEND selon qu'il s'agit d'une date ou d'un horaire UTC."""
    if is_datetime_value(value):
        append(lines, f"{property_name}:{value}")
    else:
        append(lines, f"{property_name};VALUE=DATE:{value}")


def event_lines(event: dict[str, object], stamp: str) -> Iterable[str]:
    """Construit les lignes iCalendar d'un événement validé."""
    lines: list[str] = ["BEGIN:VEVENT"]
    append(lines, f"UID:{escape_ics(event['uid'])}")
    append(lines, f"DTSTAMP:{stamp}")
    append(lines, f"SUMMARY:{escape_ics(event['title'])}")
    append_temporal(lines, "DTSTART", event["start"])

    if "end" in event:
        append_temporal(lines, "DTEND", event["end"])
    if "rrule" in event:
        append(lines, f"RRULE:{event['rrule']}")
    if "description" in event:
        append(lines, f"DESCRIPTION:{escape_ics(event['description'])}")
    if "location" in event:
        append(lines, f"LOCATION:{escape_ics(event['location'])}")
    if "url" in event:
        append(lines, f"URL:{escape_ics(event['url'])}")

    category_text = ",".join(escape_ics(item) for item in categories(event["category"]))
    append(lines, f"CATEGORIES:{category_text}")
    lines.extend(["STATUS:CONFIRMED", "TRANSP:TRANSPARENT", "END:VEVENT"])
    return lines


def main() -> int:
    try:
        config = load_config()
        loaded = load_events()

        errors: list[str] = []
        for item in loaded:
            for message in validate_event(item.data):
                errors.append(
                    f"{item.file.relative_to(ROOT)}, événement no {item.number} : {message}"
                )
        if errors:
            raise DataError("\n".join(errors))

        events = sorted(
            (item.data for item in loaded),
            key=lambda event: (str(event["start"]), str(event["title"]).casefold()),
        )

        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        lines = [
            "BEGIN:VCALENDAR",
            "VERSION:2.0",
            f"PRODID:{config['prodid']}",
            "CALSCALE:GREGORIAN",
            "METHOD:PUBLISH",
            f"X-WR-CALNAME:{escape_ics(config['calendar_name'])}",
            f"X-WR-CALDESC:{escape_ics(config['calendar_description'])}",
            f"X-WR-TIMEZONE:{escape_ics(config['timezone'])}",
            f"URL:{config['calendar_url']}",
        ]

        for event in events:
            lines.extend(event_lines(event, stamp))
        lines.append("END:VCALENDAR")

        output = ROOT / config["output_file"]
        output.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8", newline="")
        print(f"✓ {len(events)} événements générés dans {output.relative_to(ROOT)}.")
        return 0
    except DataError as exc:
        print(f"✗ Génération impossible :\n{exc}", file=sys.stderr)
        print("Exécutez d'abord : python scripts/validate.py", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
