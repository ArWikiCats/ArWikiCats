"""Ethnic labelling helpers."""

from __future__ import annotations

from typing import Dict

from ...helps.log import logger
from ...helps.print_bot import output_test4
from ...ma_lists import Nat_men, Nat_mens, Nat_women, en_is_nat_ar_is_women_2
from .utils import build_cache_key, get_or_set

#: Cache for :func:`ethnic_culture` results keyed by the important parameters.
ETHNIC_CULTURE_CACHE: Dict[str, str] = {}

#: Cache for :func:`ethnic` results keyed by the important parameters.
ETHNIC_CACHE: Dict[str, str] = {}

MALE_TOPIC_TABLE: Dict[str, str] = {
    "history": "تاريخ {}",
    "descent": "أصل {}",
    "cuisine": "مطبخ {}",
    "literature": "أدب {}",
    "law": "قانون {}",
    "wine": "نبيذ {}",
    "diaspora": "شتات {}",
    "traditions": "تراث {}",
    "folklore": "فلكور {}",
    "television": "تلفاز {}",
}


def ethnic_culture(category: str, start: str, suffix: str) -> str:
    """Return the cultural label for ``suffix`` relative to ``start``.

    Args:
        category: Full category name (used only for logging).
        start: The base nationality or country.
        suffix: The trailing segment describing the specific topic.

    Returns:
        The resolved label or an empty string.
    """

    cache_key = build_cache_key(category, start, suffix)
    if cache_key in ETHNIC_CULTURE_CACHE:
        return ETHNIC_CULTURE_CACHE[cache_key]

    def _resolve() -> str:
        logger.info(
            "Resolving ethnic culture",
            extra={"category": category, "start": start, "suffix": suffix},
        )

        if not Nat_women.get(start, "") and not Nat_men.get(start, ""):
            return ""

        topic_label = ""
        group_label = ""
        start_label = ""

        # Try to resolve using women-centric templates first.
        start_women_label = Nat_women.get(start, "")
        if start_women_label:
            for key, template in en_is_nat_ar_is_women_2.items():
                candidate_suffix = f" {key}"
                if suffix.endswith(candidate_suffix):
                    base_key = suffix[: -len(candidate_suffix)].strip()
                    group_label = Nat_women.get(base_key, "")
                    if group_label:
                        topic_label = template
                        start_label = start_women_label
                        break

        # Fallback to male templates when the women-specific search fails.
        if not topic_label:
            start_men_label = Nat_men.get(start, "")
            if start_men_label:
                for key, template in MALE_TOPIC_TABLE.items():
                    candidate_suffix = f" {key}"
                    if suffix.endswith(candidate_suffix):
                        base_key = suffix[: -len(candidate_suffix)].strip()
                        group_label = Nat_men.get(base_key, "")
                        if group_label:
                            topic_label = template
                            start_label = start_men_label
                            break

        if topic_label and group_label and start_label:
            combined = f"{group_label} {start_label}"
            resolved = topic_label.format(combined)
            output_test4(f'<<lightblue>> ethnic_culture resolved label "{resolved}" for "{category}"')
            return resolved

        return ""

    return get_or_set(ETHNIC_CULTURE_CACHE, cache_key, _resolve)


def ethnic(category: str, start: str, suffix: str) -> str:
    """Return the ethnic label for ``category``."""

    cache_key = build_cache_key(category, start, suffix)
    if cache_key in ETHNIC_CACHE:
        return ETHNIC_CACHE[cache_key]

    def _resolve() -> str:
        logger.info(
            "Resolving ethnic label",
            extra={"category": category, "start": start, "suffix": suffix},
        )

        normalized_suffix = suffix
        if suffix.endswith(" people"):
            candidate = suffix[: -len(" people")]
            if Nat_mens.get(candidate, ""):
                normalized_suffix = candidate

        group_label = Nat_mens.get(normalized_suffix, "")
        start_label = Nat_mens.get(start, "")
        if group_label and start_label:
            resolved = f"{group_label} {start_label}"
            output_test4(f'<<lightblue>> ethnic resolved label "{resolved}" for "{category}"')
            return resolved

        return ethnic_culture(category, start, normalized_suffix)

    return get_or_set(ETHNIC_CACHE, cache_key, _resolve)


# Backwards compatibility ----------------------------------------------------------------------
Ethnic_culture = ethnic_culture
Ethnic = ethnic

__all__ = [
    "ethnic",
    "ethnic_culture",
    "Ethnic",
    "Ethnic_culture",
]
