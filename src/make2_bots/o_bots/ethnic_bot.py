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
    # ---
    contry = start
    topic_key = ""
    con_3_lab = ""
    topic_label = ""
    contry_lab = ""
    # ---
    if Nat_women.get(contry, "") == "" and Nat_men.get(contry, "") == "":
        return contry_lab
    # ---
    _culture_table = {
        "culture": "ثقافة {}",
    }
    # ---
    if not topic_key and not topic_label:
        contry_L = Nat_women.get(contry, "")
        for x, x_lab in en_is_nat_ar_is_women_2.items():
            if not topic_label:
                xx = f" {x}"
                if suffix.endswith(xx):
                    topic_key = x
                    suffix = suffix[: -len(xx)]
                    topic_label = x_lab
                    con_3_lab = Nat_women.get(suffix, "")
    # ---
    # ---
    if topic_key == "" and topic_label == "":
        contry_L = Nat_men.get(contry, "")
        for x, xlab in MALE_TOPIC_TABLE.items():
            if not topic_label:
                xx = f" {x}"
                if suffix.endswith(xx):
                    topic_key = x
                    suffix = suffix[: -len(xx)]
                    topic_label = xlab
                    con_3_lab = Nat_men.get(suffix, "")
    # ---history
    if topic_key and topic_label:
        if con_3_lab:
            rz = f"{con_3_lab} {contry_L}"
            contry_lab = topic_label.format(rz)
            output_test4(f'<<lightblue>> test ethnic_culture: new contry_lab  "{contry_lab}" ')
    # ---
    ETHNIC_CULTURE_CACHE[cache_key] = contry_lab
    # ---
    return contry_lab


def ethnic(category: str, start: str, suffix: str) -> str:
    """Return the ethnic label for ``category``."""

    cache_key = build_cache_key(category, start, suffix)
    if cache_key in ETHNIC_CACHE:
        return ETHNIC_CACHE[cache_key]
    # ---
    contry = start
    contry_lab = ""
    # ---
    if suffix.endswith(" people"):
        con_nat = suffix[: -len(" people")]
        if Nat_mens.get(con_nat):
            suffix = suffix[: -len(" people")]
    # ---
    con_3_lab = Nat_mens.get(suffix, "")
    if con_3_lab:
        if Nat_mens.get(contry, "") != "":
            contry_lab = f"{con_3_lab} {Nat_mens.get(contry, '')}"
            output_test4(f'<<lightblue>> test ethnic: new contry_lab  "{contry_lab}" ')
    # ---
    if not contry_lab:
        contry_lab = ethnic_culture(category, start, suffix)
    # ---
    ETHNIC_CACHE[cache_key] = contry_lab
    # ---
    return contry_lab


__all__ = [
    "ethnic",
    "ethnic_culture",
]
