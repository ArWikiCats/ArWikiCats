"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

import functools
from typing import Mapping, Tuple

from ...helps import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    ministrs_keys,
    all_country_with_nat,
)
from .utils import apply_arabic_article

#: Mapping of suffixes that require adding a prefix around the formatted label.
ENDS_WITH_TABLE: Mapping[str, str] = {
    " civilians": "مدنيو {}",
    " generals": "جنرالات {}",
    " accidents and incidents": "حوادث {}",
}

# ---
ministrs_for_en_is_P17_ar_is_mens = {}
# ---
for ministry_key, ministry_labels in ministrs_keys.items():
    normalized_ministry = ministry_key.lower()
    singular_label = ministry_labels["singular"]
    label = f"وزراء {singular_label} {{}}"
    ministrs_for_en_is_P17_ar_is_mens[f"secretaries-of {normalized_ministry}"] = label
    ministrs_for_en_is_P17_ar_is_mens[f"secretaries of {normalized_ministry}"] = label


@functools.lru_cache(maxsize=None)
@dump_data(1)
def te_army2(category: str) -> str:
    """Resolve the Arabic label for a military-related category.

    Args:
        category: The category name in English.

    Returns:
        The resolved Arabic label or an empty string when no match exists.
    TODO: use FormatData method
    """

    normalized_category = category.lower().strip()

    logger.debug(f"Starting army label resolution, category: {normalized_category}")

    suffix = ""
    women_label = ""

    for country, details in all_country_with_nat.items():
        english_country = details.get("en", "").lower()
        women_label = details.get("female", "")

        if not women_label:
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
                break

    if not suffix or not women_label:
        return ""

    resolved_label = ""

    for suffix, prefix_template in ENDS_WITH_TABLE.items():
        if not suffix.endswith(suffix):
            continue

        base_suffix = suffix[: -len(suffix)].strip()

        suffix_template = ministrs_for_en_is_P17_ar_is_mens.get(base_suffix, "")

        if suffix_template:
            women_with_article = apply_arabic_article(women_label)
            logger.debug(f"Resolved women extended suffix, {suffix=}, {base_suffix=}")
            _label = suffix_template.format(nat=women_with_article)
            resolved_label = prefix_template.format(_label)
            break

    logger.info(f"Finished army label resolution, category: {normalized_category}, label: {resolved_label}")

    return resolved_label


__all__ = [
    "te_army2"
]
