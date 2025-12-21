#!/usr/bin/python3
"""
TODO: replace it with bys_new.py
"""
import functools
from ...helps import dump_data
from ...translations import FILM_PRODUCTION_COMPANY, People_key, SPORTS_KEYS_FOR_LABEL


@functools.lru_cache(maxsize=1)
def _extend_By_table() -> dict[str, str]:
    """
    Extend the By table dictionary with sports teams, people, and production companies.

    Returns:
        dict[str, str]: Mapping of English "by X" strings to Arabic translations.
    """
    result = {}

    # Add sports team mappings
    for sport_key, sport_label in SPORTS_KEYS_FOR_LABEL.items():
        english_key = f"by {sport_key.lower()} team"
        result[english_key] = f"حسب فريق {sport_label}"

    # Add people mappings
    for person_key, person_label in People_key.items():
        english_key = f"by {person_key.lower()}"
        result[english_key] = f"بواسطة {person_label}"

    # Add film production company mappings
    for company_key, company_label in FILM_PRODUCTION_COMPANY.items():
        english_key = f"by {company_key.lower()}"
        result[english_key] = f"بواسطة {company_label}"

    return result


@dump_data(1)
def by_table_extended_get(text):
    data = _extend_By_table()
    return data.get(text, "")


__all__ = [
    "by_table_extended_get",
]
