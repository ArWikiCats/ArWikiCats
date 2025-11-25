"""Ethnic labelling helpers."""

from __future__ import annotations

import functools
from typing import Dict

from ...helps.log import logger
from ..jobs_bots.get_helps import get_con_3
from ...translations import Nat_men, Nat_mens, Nat_women, en_is_nat_ar_is_women_2

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


@functools.lru_cache(maxsize=None)
def ethnic_culture(category: str, start: str, suffix: str) -> str:
    """Return the cultural label for ``suffix`` relative to ``start``.

    Args:
        category: Full category name (used only for logging).
        start: The base nationality or country.
        suffix: The trailing segment describing the specific topic.

    Returns:
        The resolved label or an empty string.
    """

    if not Nat_women.get(start, "") and not Nat_men.get(start, ""):
        return ""

    logger.info(f"Resolving ethnic culture, category={category}, start={start}, suffix={suffix}")

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
        logger.debug(f'<<lightblue>> ethnic_culture resolved label "{resolved}" for "{category}"')
        return resolved

    return ""


@functools.lru_cache(maxsize=None)
def ethnic(category: str, start: str, suffix: str) -> str:
    """Return the ethnic label for ``category``."""

    logger.info(f"Resolving ethnic label, category={category}, start={start}, suffix={suffix}")

    group_label = Nat_mens.get(suffix, "")
    start_label = Nat_mens.get(start, "")
    if group_label and start_label:
        resolved = f"{group_label} {start_label}"
        logger.debug(f'<<lightblue>> ethnic resolved label "{resolved}" for "{category}"')
        return resolved

    return ""


@functools.lru_cache(maxsize=None)
def ethnic_label(category: str, nat: str="", suffix: str="") -> str:
    if not suffix or not nat:
        suffix, nat = get_con_3(category, "nat")

    normalized_suffix = suffix
    if suffix.endswith(" people"):
        candidate = suffix[: -len(" people")]
        if Nat_mens.get(candidate, ""):
            normalized_suffix = candidate

    result = ethnic(category, nat, normalized_suffix)

    if not result:
        result = ethnic_culture(category, nat, normalized_suffix)

    return result


__all__ = [
    "ethnic",
    "ethnic_label",
    "ethnic_culture",
]
