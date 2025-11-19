#!/usr/bin/python3
"""Helper utilities for resolving film- and media-related categories."""

import functools
from typing import Dict

from ...translations import en_is_nat_ar_is_women
from ...translations import (
    Films_key_CAO,
    Films_key_For_nat,
    Films_key_CAO_new_format,
    television_keys_female,
    Films_key_333,
)
from ...translations import (Nat_women, Nat_mens)
from ...helps.print_bot import output_test4

@functools.lru_cache(maxsize=None)
def get_Films_key_CAO(country_identifier: str) -> str:
    """Resolve labels for composite television keys used in film lookups."""

    output_test4(f'<<lightblue>> get_Films_key_CAO : country_identifier "{country_identifier}" ')
    normalized_identifier = country_identifier.lower().strip()
    resolved_label = ""
    for suffix, suffix_translation in television_keys_female.items():
        if normalized_identifier.endswith(suffix.lower()):
            prefix = normalized_identifier[: -len(suffix)].strip()
            output_test4(f'<<lightblue>> prefix:"{prefix}", endswith:"{suffix}" ')
            prefix_label = Films_key_333.get(prefix.strip(), "")
            if prefix_label:
                output_test4(f'<<lightblue>> get_Films_key_CAO : prefix "{prefix}" ')
                if "{}" in prefix_label:
                    resolved_label = prefix_label.format(tyty=suffix_translation)
                else:
                    resolved_label = f"{suffix_translation} {prefix_label}"
                output_test4(
                    f'<<lightblue>> get_Films_key_CAO: new resolved_label "{resolved_label}" '
                )

    return resolved_label


@functools.lru_cache(maxsize=None)
def Films(category: str, country_start: str, country_code: str, reference_category: str = "") -> str:
    """Resolve the Arabic label for a given film category."""

    country_label = ""
    if country_code:
        country_name = Nat_mens[country_start] if country_code == "people" else Nat_women[country_start]
        country_code_label = en_is_nat_ar_is_women.get(country_code.strip(), "")
        if country_code_label:
            country_label = country_code_label.format(country_name)
            output_test4(
                f'<<lightblue>> bot_te_4:Films: new country_label  "{country_label}" '
            )
        if not country_label:
            country_code_label = Films_key_CAO.get(country_code, get_Films_key_CAO(country_code))
            if country_code_label:
                country_label = f"{country_code_label} {country_name}"
                if country_code in Films_key_CAO_new_format:
                    country_label = Films_key_CAO_new_format[country_code].format(country_name)
                output_test4(
                    f'<<lightblue>> bot_te_4:Films: new country_label "{country_label}" , country_code:{country_code} '
                )
        if not country_label:
            country_code_label = Films_key_For_nat.get(country_code, "")
            if country_code_label:
                country_label = country_code_label.format(country_name)
                output_test4(
                    f'<<lightblue>> Films_key_For_nat:Films: new country_label  "{country_label}" '
                )

    if not country_label:
        category_label = Films_key_CAO.get(category, "")
        if category_label:
            country_label = category_label
            output_test4(f'<<lightblue>> test Films: country_label "{country_label}" ')

    if not country_label:
        country_label = get_Films_key_CAO(category)
        if country_label:
            output_test4(f'<<lightblue>> test Films: new country_label "{country_label}" ')

    return country_label
