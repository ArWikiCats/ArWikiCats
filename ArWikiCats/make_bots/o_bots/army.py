"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

import functools
from typing import Tuple

from ...helps import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    all_country_with_nat,
    ministrs_keys,
)
from .utils import apply_arabic_article


ministrs_format_men = {}
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    al_label = ministry_labels["al"]

    ministrs_format_men[f"assistant secretaries of {normalized_ministry}"] = f"مساعدو وزير {al_label} {{nat}}"
    ministrs_format_men[f"deputy secretaries of {normalized_ministry}"] = f"نواب وزير {al_label} {{nat}} للشؤون المتخصصة"

ministrs_format_women = {}
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    al_label = ministry_labels["al"]

    ministrs_format_women[f"department of {normalized_ministry} agencies"] = (
        f"وكالات وزارة {al_label} {{nat}}"
    )
    ministrs_format_women[f"department of {normalized_ministry} facilities"] = (
        f"مرافق وزارة {al_label} {{nat}}"
    )
    ministrs_format_women[f"department of {normalized_ministry} national laboratories"] = (
        f"مختبرات وزارة {al_label} {{nat}}"
    )
    ministrs_format_women[f"department of {normalized_ministry} national laboratories personnel"] = (
        f"موظفو مختبرات وزارة {al_label} {{nat}}"
    )
    ministrs_format_women[f"department of {normalized_ministry} officials"] = (
        f"مسؤولو وزارة {al_label} {{nat}}"
    )
    ministrs_format_women[f"department of {normalized_ministry}"] = (
        f"وزارة {al_label} {{nat}}"
    )


def _match_country_prefix(category: str) -> Tuple[str, str, str]:
    """
    Return the suffix and gendered labels for the matched country prefix.
    TODO: use FormatData method
    """

    for country, details in all_country_with_nat.items():
        english_country = details.get("en", "").lower()
        women_label = details.get("female", "")
        men_label = details.get("male", "")

        if not (women_label or men_label):
            continue

        english_prefix = f"{english_country} " if english_country else ""
        localised_prefix = f"{country.lower()} "

        english_without_article = english_country
        if english_without_article.startswith("the "):
            english_without_article = english_without_article[len("the ") :]
        english_without_article_prefix = f"{english_without_article} " if english_without_article else ""

        for prefix in filter(None, [english_prefix, english_without_article_prefix, localised_prefix]):
            if category.startswith(prefix):
                suffix = category[len(prefix) :].strip()
                logger.debug(f"Matched country prefix, {category=}, {prefix=}")
                return suffix, women_label, men_label

    return "", "", ""


def _resolve_women_extended_suffix(category_suffix: str, women_label: str) -> str:
    """
    Resolve categories with suffixes that require a surrounding template.
    TODO: use FormatData method
    """

    if not category_suffix or not women_label:
        return ""

    suffix_template = ministrs_format_women.get(category_suffix, "")

    resolved_label = ""
    if suffix_template:
        women_with_article = apply_arabic_article(women_label)
        resolved_label = suffix_template.format(nat=women_with_article)

    logger.debug(f"Resolved women extended suffix, {category_suffix=}, {resolved_label=}")
    return resolved_label


def _resolve_men_suffix(category_suffix: str, men_label: str) -> str:
    """
    Resolve categories that use the male templates.
    TODO: use FormatData method
    """

    if not category_suffix or not men_label:
        return ""
    category_suffix = category_suffix.replace("secretaries-of", "secretaries of")

    template = ministrs_format_men.get(category_suffix, "")

    if template:
        men_with_article = apply_arabic_article(men_label)
        logger.debug(f"Resolved men suffix, suffix: {category_suffix}")
        return template.format(nat=men_with_article)
    return ""


@functools.lru_cache(maxsize=None)
@dump_data(1)
def te_army(category: str) -> str:
    """Resolve the Arabic label for a military-related category.

    Args:
        category: The category name in English.

    Returns:
        The resolved Arabic label or an empty string when no match exists.
    TODO: use FormatData method
    """

    normalized_category = category.lower().strip()

    logger.debug(f"Starting army label resolution, category: {normalized_category}")

    suffix, women_label, men_label = _match_country_prefix(normalized_category)

    if not suffix:
        return ""

    resolved_label = _resolve_women_extended_suffix(suffix, women_label) or _resolve_men_suffix(suffix, men_label)

    logger.info(f"Finished army label resolution, category: {normalized_category}, label: {resolved_label}")

    return resolved_label


__all__ = ["te_army"]
