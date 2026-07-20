#!/usr/bin/env python3
"""
WoW Calendrier EU FR
Validateur des fichiers JSON du dossier data.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

REQUIRED_FIELDS = ("uid", "title", "start")
OPTIONAL_TEXT_FIELDS = ("id", "description", "location", "url", "rrule")
DATE_FIELDS = ("start", "end")


@dataclass(frozen=True)
class Issue:
    """Erreur ou avertissement détecté pendant la validation."""

    level: str
    file: str
    event_number: int | None
    message: str


def add_issue(
    issues: list[Issue],
    level: str,
    file: Path,
    event_number: int | None,
    message: str,
) -> None:
    """Ajoute une erreur ou un avertissement à la liste des résultats."""
    issues.append(
        Issue(
            level=level,
            file=file.name,
            event_number=event_number,
            message=message,
        )
    )


def is_non_empty_string(value: Any) -> bool:
    """Indique si une valeur est une chaîne non vide."""
    return isinstance(value, str) and bool(value.strip())


def parse_date(
    value: Any,
    field: str,
    file: Path,
    event_number: int,
    issues: list[Issue],
) -> datetime | None:
    """Valide et convertit une date au format YYYYMMDD."""
    if not isinstance(value, str):
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            f'Le champ "{field}" doit être une chaîne au format YYYYMMDD.',
        )
        return None

    if len(value) != 8 or not value.isdigit():
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            f'Le champ "{field}" doit respecter le format YYYYMMDD : {value!r}.',
        )
        return None

    try:
        return datetime.strptime(value, "%Y%m%d")
    except ValueError:
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            f'Date invalide dans le champ "{field}" : {value!r}.',
        )
        return None


def validate_https_url(
    value: Any,
    field: str,
    file: Path,
    event_number: int,
    issues: list[Issue],
) -> None:
    """Vérifie qu'une URL est une URL HTTPS absolue."""
    if not is_non_empty_string(value):
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            f'Le champ "{field}" doit être une URL non vide.',
        )
        return

    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            f'Le champ "{field}" doit contenir une URL HTTPS absolue : {value!r}.',
        )


def validate_category(
    value: Any,
    file: Path,
    event_number: int,
    issues: list[Issue],
) -> None:
    """Vérifie le format d'une catégorie ou d'une liste de catégories."""
    if is_non_empty_string(value):
        return

    if isinstance(value, list):
        if not value:
            add_issue(
                issues,
                "ERROR",
                file,
                event_number,
                'Le champ "category" ne peut pas être une liste vide.',
            )
            return

        for index, category in enumerate(value, start=1):
            if not is_non_empty_string(category):
                add_issue(
                    issues,
                    "ERROR",
                    file,
                    event_number,
                    f'La catégorie no {index} doit être une chaîne non vide.',
                )
        return

    add_issue(
        issues,
        "ERROR",
        file,
        event_number,
        'Le champ "category" doit être une chaîne ou une liste de chaînes.',
    )


def validate_sources(
    value: Any,
    file: Path,
    event_number: int,
    issues: list[Issue],
) -> None:
    """Vérifie la liste optionnelle des sources."""
    if not isinstance(value, list):
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            'Le champ "sources" doit être une liste d’URL HTTPS.',
        )
        return

    if not value:
        add_issue(
            issues,
            "WARNING",
            file,
            event_number,
            'Le champ "sources" est présent mais vide.',
        )
        return

    for index, source in enumerate(value, start=1):
        validate_https_url(
            source,
            f"sources[{index}]",
            file,
            event_number,
            issues,
        )


def validate_rrule(
    value: Any,
    file: Path,
    event_number: int,
    issues: list[Issue],
) -> None:
    """Effectue quelques contrôles simples sur une règle de récurrence."""
    if not is_non_empty_string(value):
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            'Le champ "rrule" doit être une chaîne non vide.',
        )
        return

    if "FREQ=" not in value.upper():
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            f'La règle de récurrence ne contient pas "FREQ=" : {value!r}.',
        )


def validate_event(
    event: Any,
    file: Path,
    event_number: int,
    issues: list[Issue],
) -> dict[str, Any] | None:
    """Valide la structure et le contenu d'un événement."""
    if not isinstance(event, dict):
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            "Chaque événement doit être un objet JSON.",
        )
        return None

    for field in REQUIRED_FIELDS:
        if field not in event:
            add_issue(
                issues,
                "ERROR",
                file,
                event_number,
                f'Champ obligatoire manquant : "{field}".',
            )
        elif not is_non_empty_string(event[field]):
            add_issue(
                issues,
                "ERROR",
                file,
                event_number,
                f'Le champ "{field}" doit être une chaîne non vide.',
            )

    if "category" in event:
        validate_category(event["category"], file, event_number, issues)
    else:
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            'Champ obligatoire manquant : "category".',
        )

    for field in OPTIONAL_TEXT_FIELDS:
        if field in event and not is_non_empty_string(event[field]):
            add_issue(
                issues,
                "ERROR",
                file,
                event_number,
                f'Le champ optionnel "{field}" doit être une chaîne non vide.',
            )

    parsed_dates: dict[str, datetime | None] = {}
    for field in DATE_FIELDS:
        if field in event:
            parsed_dates[field] = parse_date(
                event[field],
                field,
                file,
                event_number,
                issues,
            )

    start = parsed_dates.get("start")
    end = parsed_dates.get("end")
    if start is not None and end is not None and end <= start:
        add_issue(
            issues,
            "ERROR",
            file,
            event_number,
            (
                f'La date "end" ({event["end"]}) doit être postérieure '
                f'à "start" ({event["start"]}). '
                "Dans un fichier ICS, DTEND est exclusif."
            ),
        )

    if "url" in event:
        validate_https_url(event["url"], "url", file, event_number, issues)

    if "sources" in event:
        validate_sources(event["sources"], file, event_number, issues)

    if "rrule" in event:
        validate_rrule(event["rrule"], file, event_number, issues)

    if "description" not in event:
        add_issue(
            issues,
            "WARNING",
            file,
            event_number,
            'Description absente.',
        )

    return event


def load_and_validate_files(
    issues: list[Issue],
) -> tuple[list[tuple[Path, int, dict[str, Any]]], int]:
    """Charge les fichiers JSON et valide leur structure générale."""
    json_files = sorted(DATA_DIR.glob("*.json"))

    if not DATA_DIR.is_dir():
        add_issue(
            issues,
            "ERROR",
            DATA_DIR,
            None,
            f"Dossier de données introuvable : {DATA_DIR}",
        )
        return [], 0

    if not json_files:
        add_issue(
            issues,
            "ERROR",
            DATA_DIR,
            None,
            f"Aucun fichier JSON trouvé dans {DATA_DIR}.",
        )
        return [], 0

    events: list[tuple[Path, int, dict[str, Any]]] = []

    for file in json_files:
        try:
            with file.open(encoding="utf-8") as stream:
                data = json.load(stream)
        except json.JSONDecodeError as exc:
            add_issue(
                issues,
                "ERROR",
                file,
                None,
                (
                    f"JSON invalide à la ligne {exc.lineno}, "
                    f"colonne {exc.colno} : {exc.msg}."
                ),
            )
            continue
        except OSError as exc:
            add_issue(
                issues,
                "ERROR",
                file,
                None,
                f"Impossible de lire le fichier : {exc}.",
            )
            continue

        if not isinstance(data, list):
            add_issue(
                issues,
                "ERROR",
                file,
                None,
                "La racine du fichier doit être une liste JSON.",
            )
            continue

        for event_number, raw_event in enumerate(data, start=1):
            event = validate_event(
                raw_event,
                file,
                event_number,
                issues,
            )
            if event is not None:
                events.append((file, event_number, event))

    return events, len(json_files)


def validate_unique_values(
    events: list[tuple[Path, int, dict[str, Any]]],
    field: str,
    issues: list[Issue],
) -> None:
    """Recherche les doublons d'un champ dans l'ensemble des fichiers."""
    seen: dict[str, tuple[Path, int]] = {}

    for file, event_number, event in events:
        value = event.get(field)
        if not is_non_empty_string(value):
            continue

        if value in seen:
            first_file, first_event_number = seen[value]
            add_issue(
                issues,
                "ERROR",
                file,
                event_number,
                (
                    f'{field.upper()} en double : {value!r}. '
                    f"Déjà utilisé dans {first_file.name}, "
                    f"événement no {first_event_number}."
                ),
            )
        else:
            seen[value] = (file, event_number)


def print_header() -> None:
    """Affiche l'en-tête du validateur."""
    print("─" * 54)
    print(" WoW Calendrier EU FR - Validation des données")
    print("─" * 54)


def print_issues(issues: list[Issue]) -> None:
    """Affiche les erreurs et avertissements."""
    for issue in issues:
        location = issue.file
        if issue.event_number is not None:
            location += f" — événement no {issue.event_number}"

        symbol = "✗" if issue.level == "ERROR" else "⚠"
        print(f"{symbol} {issue.level:<7} {location}")
        print(f"           {issue.message}")


def main() -> int:
    """Point d'entrée du script."""
    print_header()

    issues: list[Issue] = []
    events, file_count = load_and_validate_files(issues)

    validate_unique_values(events, "uid", issues)
    validate_unique_values(events, "id", issues)

    errors = [issue for issue in issues if issue.level == "ERROR"]
    warnings = [issue for issue in issues if issue.level == "WARNING"]

    if issues:
        print()
        print_issues(issues)

    print()
    print("─" * 54)
    print(f"Fichiers JSON : {file_count}")
    print(f"Événements    : {len(events)}")
    print(f"Erreurs       : {len(errors)}")
    print(f"Avertissements: {len(warnings)}")
    print("─" * 54)

    if errors:
        print("✗ Validation échouée.")
        return 1

    print("✓ Toutes les données sont valides.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
