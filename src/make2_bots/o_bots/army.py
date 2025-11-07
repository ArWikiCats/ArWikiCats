"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

from typing import Dict, Mapping, Tuple

"""Resolve Arabic labels for army-related categories."""

from ...helps.log import logger
from ...ma_lists import All_contry_with_nat, All_contry_with_nat_keys_is_en, military_format_men, military_format_women, military_format_women_without_al, military_format_women_without_al_from_end, sport_formts_en_p17_ar_nat
from .utils import apply_arabic_article, get_or_set

#: Cache storing resolved labels keyed by the normalised category name.
TEST_ARMY_CACHE: Dict[str, str] = {}

#: Mapping of suffixes that require adding a prefix around the formatted label.
ENDS_WITH_TABLE: Mapping[str, str] = {
    " civilians": "مدنيو {}",
    " generals": "جنرالات {}",
    " accidents and incidents": "حوادث {}",
}


def _match_country_prefix(category: str) -> Tuple[str, str, str]:
    """Return the suffix and gendered labels for the matched country prefix."""

    for country, details in All_contry_with_nat.items():
        english_country = details.get("en", "").lower()
        women_label = details.get("women", "")
        men_label = details.get("men", "")

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
                logger.debug("Matched country prefix", extra={"category": category, "prefix": prefix.strip()})
                return suffix, women_label, men_label

    return "", "", ""


def _resolve_women_without_article_prefix(category: str) -> str:
    """Resolve categories that start with a women-only prefix template."""

    for prefix_without_article, template in military_format_women_without_al_from_end.items():
        prefix_with_space = f"{prefix_without_article} "
        if not category.startswith(prefix_with_space):
            continue

        suffix_key = category[len(prefix_with_space) :].strip()
        country_label = All_contry_with_nat_keys_is_en.get(suffix_key, {}).get("women", "")
        if country_label:
            logger.debug(
                "Resolved women without article prefix",
                extra={"prefix": prefix_without_article, "country": suffix_key},
            )
            return template.format(nat=country_label)

    return ""


def _resolve_women_suffix(category_suffix: str, women_label: str) -> str:
    """Resolve categories with a direct women suffix template."""

    if not category_suffix or not women_label:
        return ""

    template = military_format_women_without_al.get(category_suffix, "")
    if template:
        logger.debug("Resolved women suffix", extra={"suffix": category_suffix})
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
            logger.debug(
                "Resolved women extended suffix",
                extra={"base_suffix": base_suffix, "suffix": suffix},
            )
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
        logger.debug("Resolved men suffix", extra={"suffix": category_suffix})
        return template.format(nat=men_with_article)
    return ""


def _resolve_sport_suffix(category_suffix: str, men_label: str) -> str:
    """Resolve sports-related categories that share the same structure as armies."""

    if not category_suffix or not men_label:
        return ""

    template = sport_formts_en_p17_ar_nat.get(category_suffix, "")
    if template:
        men_with_article = apply_arabic_article(men_label)
        logger.debug("Resolved sports suffix", extra={"suffix": category_suffix, "template": template})
        return template.format(nat=men_with_article)
    return ""


def test_army(category: str) -> str:
    """Resolve the Arabic label for a military-related category.

    Args:
        category: The category name in English.

    Returns:
        The resolved Arabic label or an empty string when no match exists.
    """

    normalized_category = category.lower().strip()

    if normalized_category in TEST_ARMY_CACHE:
        cached = TEST_ARMY_CACHE[normalized_category]
        if cached:
            logger.debug(
                "Cache hit for army label",
                extra={"category": normalized_category, "label": cached},
            )
        return cached

    def _resolve() -> str:
        logger.info(
            "Starting army label resolution",
            extra={"category": normalized_category},
        )

        suffix, women_label, men_label = _match_country_prefix(normalized_category)

        if not suffix:
            resolved = _resolve_women_without_article_prefix(normalized_category)
            if resolved:
                return resolved

        # Attempt to resolve using women-focused templates first.
        resolved_label = _resolve_women_suffix(suffix, women_label)
        if resolved_label:
            return resolved_label

        resolved_label = _resolve_women_extended_suffix(suffix, women_label)
        if resolved_label:
            return resolved_label

        # Fall back to men-specific and sport-specific templates.
        resolved_label = _resolve_men_suffix(suffix, men_label)
        if resolved_label:
            return resolved_label

        resolved_label = _resolve_sport_suffix(suffix, men_label)
        if resolved_label:
            return resolved_label

        return ""

    resolved_value = get_or_set(TEST_ARMY_CACHE, normalized_category, _resolve)
    logger.info(
        "Finished army label resolution",
        extra={"category": normalized_category, "label": resolved_value},
    )
    return resolved_value


# Backwards compatibility ----------------------------------------------------------------------
#
# Historically the function was exposed as ``test_Army`` with a capitalised name.  Keep a public
# alias so callers using the old name continue to function while the codebase migrates towards
# PEP 8 compliant identifiers.
test_Army = test_army
__all__ = ["test_army", "test_Army"]
