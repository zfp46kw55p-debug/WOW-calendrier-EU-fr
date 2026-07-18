from pathlib import Path
from datetime import datetime, timezone, timedelta
import json

ROOT = Path(__file__).resolve().parents[1]
EVENTS_FILE = ROOT / "data" / "events.json"
OUTPUT_FILE = ROOT / "wow-eu.ics"

def esc(value: str) -> str:
    return (value.replace("\\", "\\\\")
                 .replace("\n", "\\n")
                 .replace(",", "\\,")
                 .replace(";", "\\;"))

def fold(line: str, limit: int = 73):
    if len(line.encode("utf-8")) <= 75:
        return [line]
    out, current = [], ""
    for ch in line:
        candidate = current + ch
        if len(candidate.encode("utf-8")) > limit:
            out.append(current)
            current = " " + ch
        else:
            current = candidate
    if current:
        out.append(current)
    return out

def add(lines, line):
    lines.extend(fold(line))

def event_lines(event, stamp):
    lines = ["BEGIN:VEVENT"]
    add(lines, f"UID:{event['uid']}@wow-calendrier-eu-fr")
    add(lines, f"DTSTAMP:{stamp}")
    add(lines, f"SUMMARY:{esc(event['title'])}")
    add(lines, f"CATEGORIES:{esc(event.get('category', 'WoW'))}")
    description = event['description'] + "\nPriorité : " + event.get('priority','') + "\nSource : " + event.get('source','')
    add(lines, f"DESCRIPTION:{esc(description)}")
    if event.get("source"):
        add(lines, f"URL:{event['source']}")

    kind = event["type"]
    if kind in ("single_all_day", "recurring_all_day"):
        add(lines, f"DTSTART;VALUE=DATE:{event['start'].replace('-', '')}")
        end_dt = datetime.fromisoformat(event["start"]) + timedelta(days=1)
        add(lines, f"DTEND;VALUE=DATE:{end_dt.strftime('%Y%m%d')}")
    elif kind == "date_range":
        add(lines, f"DTSTART;VALUE=DATE:{event['start'].replace('-', '')}")
        add(lines, f"DTEND;VALUE=DATE:{event['end'].replace('-', '')}")
    else:
        raise ValueError(f"Type inconnu: {kind}")

    if event.get("rrule"):
        add(lines, f"RRULE:{event['rrule']}")

    if event.get("alarm_days_before"):
        lines += [
            "BEGIN:VALARM",
            f"TRIGGER:-P{int(event['alarm_days_before'])}D",
            "ACTION:DISPLAY",
            f"DESCRIPTION:{esc(event['title'])}",
            "END:VALARM",
        ]

    lines.append("END:VEVENT")
    return lines

def main():
    events = json.loads(EVENTS_FILE.read_text(encoding="utf-8"))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//WOW calendrier EU FR//Midnight//FR",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:WoW Midnight EU – FR",
        "X-WR-CALDESC:Calendrier communautaire francophone des événements World of Warcraft Retail Europe.",
        "X-WR-TIMEZONE:Europe/Zurich",
    ]
    for event in events:
        lines.extend(event_lines(event, stamp))
    lines.append("END:VCALENDAR")
    OUTPUT_FILE.write_text("\r\n".join(lines) + "\r\n", encoding="utf-8")
    print(f"Généré : {OUTPUT_FILE} ({len(events)} événements)")

if __name__ == "__main__":
    main()
