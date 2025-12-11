"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

import functools
from typing import Mapping, Tuple

from ...helps import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    all_country_with_nat,
    countries_nat_en_key,
    military_format_men,
    military_format_women,
)
from .utils import apply_arabic_article

# الإنجليزية اسم البلد والعربية جنسية مؤنث بدون ألف ولام التعريف
# TODO: move to countries_names_v2.py
military_format_women_without_al_from_end = {
    # Category:Unmanned_aerial_vehicles_of_Jordan > طائرات بدون طيار أردنية
    "unmanned military aircraft-of": "طائرات عسكرية بدون طيار {nat}",
    "unmanned aerial vehicles-of": "طائرات بدون طيار {nat}",
    "unmanned military aircraft of": "طائرات عسكرية بدون طيار {nat}",
    "unmanned aerial vehicles of": "طائرات بدون طيار {nat}",
}

# TODO: move to countries_names_v2.py
military_format_women_without_al = {
    "federal legislation": "تشريعات فيدرالية {nat}",
    "courts": "محاكم {nat}",
    "sports templates": "قوالب رياضة {nat}",
    "political party": "أحزاب سياسية {nat}",
}
#: Mapping of suffixes that require adding a prefix around the formatted label.
ENDS_WITH_TABLE: Mapping[str, str] = {
    " civilians": "مدنيو {}",
    " generals": "جنرالات {}",
    " accidents and incidents": "حوادث {}",
}


def _match_country_prefix(category: str) -> Tuple[str, str, str]:
    """Return the suffix and gendered labels for the matched country prefix."""

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


def _resolve_women_without_article_prefix(category: str) -> str:
    """Resolve categories that start with a women-only prefix template."""

    for prefix_without_article, template in military_format_women_without_al_from_end.items():
        prefix_with_space = f"{prefix_without_article} "
        if not category.startswith(prefix_with_space):
            continue

        suffix_key = category[len(prefix_with_space) :].strip()
        country_label = countries_nat_en_key.get(suffix_key, {}).get("female", "")
        if country_label:
            logger.debug(
                f"Resolved women without article prefix, prefix: {prefix_without_article}, category: {suffix_key}"
            )
            return template.format(nat=country_label)

    return ""


def _resolve_women_suffix(category_suffix: str, women_label: str) -> str:
    """Resolve categories with a direct women suffix template."""

    if not category_suffix or not women_label:
        return ""

    template = military_format_women_without_al.get(category_suffix, "")
    if template:
        logger.debug(f"Resolved women suffix, suffix: {category_suffix}")
        return template.format(nat=women_label)
    return ""


def _resolve_women_extended_suffix(category_suffix: str, women_label: str) -> str:
    """Resolve categories with suffixes that require a surrounding template."""

    if not category_suffix or not women_label:
        return ""

    for suffix, prefix_template in ENDS_WITH_TABLE.items():
        if not category_suffix.endswith(suffix):
            continue

        base_suffix = category_suffix[: -len(suffix)].strip()
        suffix_template = military_format_women.get(base_suffix, "")
        if suffix_template:
            women_with_article = apply_arabic_article(women_label)
            logger.debug(f"Resolved women extended suffix, {suffix=}, {base_suffix=}")
            resolved_label = suffix_template.format(nat=women_with_article)
            return prefix_template.format(resolved_label)

    return ""


def _resolve_men_suffix(category_suffix: str, men_label: str) -> str:
    """Resolve categories that use the male templates."""

    if not category_suffix or not men_label:
        return ""

    template = military_format_men.get(category_suffix, "")
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
    """

    normalized_category = category.lower().strip()

    logger.debug(f"Starting army label resolution, category: {normalized_category}")

    suffix, women_label, men_label = _match_country_prefix(normalized_category)

    if not suffix:
        resolved = _resolve_women_without_article_prefix(normalized_category)
        return resolved or ""

    # Attempt to resolve using women-focused templates first.
    resolved_label = _resolve_women_suffix(suffix, women_label)

    if not resolved_label:
        resolved_label = _resolve_women_extended_suffix(suffix, women_label)

    # Fall back to men-specific and sport-specific templates.
    if not resolved_label:
        resolved_label = _resolve_men_suffix(suffix, men_label)

    if resolved_label:
        logger.info(f"Finished army label resolution, category: {normalized_category}, label: {resolved_label}")

    return resolved_label


__all__ = ["te_army"]
