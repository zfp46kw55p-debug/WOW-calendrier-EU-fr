#!/usr/bin/env python3
"""Outils communs de chargement et de validation des données événementielles."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CONFIG_FILE = ROOT / "config.json"

DATE_FORMAT = "%Y%m%d"
DATETIME_UTC_FORMAT = "%Y%m%dT%H%M%SZ"
DATE_PATTERN = re.compile(r"^\d{8}$")
DATETIME_UTC_PATTERN = re.compile(r"^\d{8}T\d{6}Z$")

REQUIRED_FIELDS = ("uid", "title", "start", "category")
ALLOWED_FIELDS = {
    "id",
    "uid",
    "title",
    "start",
    "end",
    "description",
    "location",
    "url",
    "sources",
    "rrule",
    "category",
}
UID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._@-]*$")
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")


class DataError(ValueError):
    """Erreur de données avec un message directement affichable."""


@dataclass(frozen=True)
class LoadedEvent:
    """Événement chargé avec sa provenance."""

    file: Path
    number: int
    data: dict[str, Any]


@dataclass(frozen=True)
class ParsedTemporal:
    """Valeur temporelle analysée avec son type iCalendar."""

    value: datetime
    has_time: bool


def json_files(data_dir: Path = DATA_DIR) -> list[Path]:
    """Retourne tous les JSON de données, y compris dans des sous-dossiers.

    Les fichiers ou dossiers dont le nom commence par « _ » sont ignorés.
    Cela permet de conserver des modèles dans le dépôt sans les générer.
    """
    if not data_dir.is_dir():
        raise DataError(f"Dossier de données introuvable : {data_dir}")

    files = [
        path
        for path in data_dir.rglob("*.json")
        if not any(part.startswith("_") for part in path.relative_to(data_dir).parts)
    ]
    return sorted(files, key=lambda path: path.as_posix().lower())


def load_config(path: Path = CONFIG_FILE) -> dict[str, str]:
    """Charge et vérifie la configuration générale du calendrier."""
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise DataError(f"Fichier de configuration introuvable : {path}") from exc
    except json.JSONDecodeError as exc:
        raise DataError(
            f"JSON invalide dans {path.name}, ligne {exc.lineno}, colonne {exc.colno} : {exc.msg}."
        ) from exc

    required = {
        "calendar_name",
        "calendar_description",
        "calendar_url",
        "output_file",
        "prodid",
        "timezone",
    }
    missing = sorted(required - set(config))
    if missing:
        raise DataError(f"Champs manquants dans {path.name} : {', '.join(missing)}")

    for field in required:
        if not isinstance(config[field], str) or not config[field].strip():
            raise DataError(f'Le champ "{field}" de {path.name} doit être une chaîne non vide.')

    return config


def load_events(data_dir: Path = DATA_DIR) -> list[LoadedEvent]:
    """Charge tous les événements de tous les fichiers JSON."""
    files = json_files(data_dir)
    if not files:
        raise DataError(f"Aucun fichier JSON trouvé dans {data_dir}.")

    loaded: list[LoadedEvent] = []
    for file in files:
        try:
            content = json.loads(file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise DataError(
                f"JSON invalide dans {file.relative_to(ROOT)}, ligne {exc.lineno}, "
                f"colonne {exc.colno} : {exc.msg}."
            ) from exc
        except OSError as exc:
            raise DataError(f"Impossible de lire {file.relative_to(ROOT)} : {exc}") from exc

        if not isinstance(content, list):
            raise DataError(f"{file.relative_to(ROOT)} doit contenir une liste JSON.")

        for number, event in enumerate(content, start=1):
            if not isinstance(event, dict):
                raise DataError(
                    f"{file.relative_to(ROOT)}, événement no {number} : "
                    "chaque événement doit être un objet JSON."
                )
            loaded.append(LoadedEvent(file=file, number=number, data=event))

    return loaded


def parse_temporal(value: Any, field: str) -> ParsedTemporal:
    """Convertit une date ou une date-heure UTC et indique son type.

    Formats acceptés :
    - YYYYMMDD pour un événement sur une journée entière ;
    - YYYYMMDDTHHMMSSZ pour un événement horaire exprimé en UTC.
    """
    if not isinstance(value, str):
        raise DataError(
            f'Le champ "{field}" doit respecter le format YYYYMMDD '
            "ou YYYYMMDDTHHMMSSZ."
        )

    if DATE_PATTERN.fullmatch(value):
        format_string = DATE_FORMAT
        has_time = False
    elif DATETIME_UTC_PATTERN.fullmatch(value):
        format_string = DATETIME_UTC_FORMAT
        has_time = True
    else:
        raise DataError(
            f'Le champ "{field}" doit respecter le format YYYYMMDD '
            "ou YYYYMMDDTHHMMSSZ."
        )

    try:
        parsed = datetime.strptime(value, format_string)
    except ValueError as exc:
        raise DataError(f'Date invalide dans le champ "{field}" : {value!r}.') from exc

    return ParsedTemporal(value=parsed, has_time=has_time)


def parse_date(value: Any, field: str) -> datetime:
    """Convertit une date ou date-heure valide en ``datetime``.

    Cette fonction est conservée pour compatibilité avec les autres scripts.
    """
    return parse_temporal(value, field).value


def is_datetime_value(value: Any) -> bool:
    """Indique si la valeur utilise le format UTC YYYYMMDDTHHMMSSZ."""
    return isinstance(value, str) and bool(DATETIME_UTC_PATTERN.fullmatch(value))


def is_https_url(value: Any) -> bool:
    """Indique si la valeur est une URL HTTPS absolue."""
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def categories(value: Any) -> list[str]:
    """Normalise une catégorie ou une liste de catégories."""
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    if isinstance(value, list) and value and all(
        isinstance(item, str) and item.strip() for item in value
    ):
        return [item.strip() for item in value]
    raise DataError('Le champ "category" doit être une chaîne ou une liste non vide de chaînes.')


def validate_event(event: dict[str, Any]) -> list[str]:
    """Retourne la liste des erreurs d'un événement."""
    errors: list[str] = []

    unknown = sorted(set(event) - ALLOWED_FIELDS)
    if unknown:
        errors.append(f"Champs inconnus : {', '.join(unknown)}.")

    for field in REQUIRED_FIELDS:
        if field not in event:
            errors.append(f'Champ obligatoire manquant : "{field}".')

    for field in ("uid", "title", "description", "location", "url", "rrule", "id"):
        if field in event and (not isinstance(event[field], str) or not event[field].strip()):
            errors.append(f'Le champ "{field}" doit être une chaîne non vide.')

    uid = event.get("uid")
    if isinstance(uid, str) and uid and not UID_PATTERN.fullmatch(uid):
        errors.append(
            'Le champ "uid" contient des caractères non recommandés. '
            "Utilisez lettres, chiffres, tirets, points, underscores ou @."
        )

    event_id = event.get("id")
    if isinstance(event_id, str) and event_id and not ID_PATTERN.fullmatch(event_id):
        errors.append('Le champ "id" doit être en minuscules, sans espaces (kebab-case ou snake_case).')

    start: ParsedTemporal | None = None
    end: ParsedTemporal | None = None

    if "start" in event:
        try:
            start = parse_temporal(event["start"], "start")
        except DataError as exc:
            errors.append(str(exc))

    if "end" in event:
        try:
            end = parse_temporal(event["end"], "end")
        except DataError as exc:
            errors.append(str(exc))

    if start is not None and end is not None:
        if start.has_time != end.has_time:
            errors.append(
                'Les champs "start" et "end" doivent utiliser le même format : '
                "tous deux YYYYMMDD ou tous deux YYYYMMDDTHHMMSSZ."
            )
        elif end.value <= start.value:
            errors.append(
                'La date "end" doit être postérieure à "start". '
                "Dans iCalendar, DTEND est exclusif."
            )

    if "category" in event:
        try:
            categories(event["category"])
        except DataError as exc:
            errors.append(str(exc))

    if "url" in event and not is_https_url(event["url"]):
        errors.append('Le champ "url" doit contenir une URL HTTPS absolue.')

    if "sources" in event:
        sources = event["sources"]
        if not isinstance(sources, list) or not sources:
            errors.append('Le champ "sources" doit être une liste non vide d’URL HTTPS.')
        else:
            for index, source in enumerate(sources, start=1):
                if not is_https_url(source):
                    errors.append(f'La source no {index} doit être une URL HTTPS absolue.')

    rrule = event.get("rrule")
    if isinstance(rrule, str) and rrule:
        normalized_rrule = rrule.upper()
        if normalized_rrule.startswith("RRULE:"):
            errors.append(
                'Le champ "rrule" doit contenir uniquement la règle, sans le préfixe "RRULE:".'
            )
        elif "FREQ=" not in normalized_rrule:
            errors.append('Le champ "rrule" doit contenir une règle incluant "FREQ=".')

    return errors


def duplicate_values(events: Iterable[LoadedEvent], field: str) -> list[tuple[str, LoadedEvent, LoadedEvent]]:
    """Retourne les doublons d'un champ avec les deux emplacements concernés."""
    seen: dict[str, LoadedEvent] = {}
    duplicates: list[tuple[str, LoadedEvent, LoadedEvent]] = []
    for loaded in events:
        value = loaded.data.get(field)
        if not isinstance(value, str) or not value.strip():
            continue
        if value in seen:
            duplicates.append((value, seen[value], loaded))
        else:
            seen[value] = loaded
    return duplicates
