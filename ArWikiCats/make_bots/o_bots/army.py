"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

import functools
from typing import Mapping, Tuple

from ...helps import logger
from ...helps.jsonl_dump import dump_data
from ...translations import (
    all_country_with_nat,
    ministrs_for_en_is_P17_ar_is_mens,
    ministrs_for_military_format_men,
    ministrs_for_military_format_women,
)
from .utils import apply_arabic_article

#: Mapping of suffixes that require adding a prefix around the formatted label.
ENDS_WITH_TABLE: Mapping[str, str] = {
    " civilians": "مدنيو {}",
    " generals": "جنرالات {}",
    " accidents and incidents": "حوادث {}",
}

military_format_women = {
    "air force": "القوات الجوية {nat}",
    "airlines": "الخطوط الجوية {nat}",
    "armed forces": "القوات المسلحة {nat}",
    "army aviation": "طيران القوات المسلحة {nat}",
    "army": "القوات المسلحة {nat}",
    "case law": "السوابق القضائية {nat}",
    "communications": "الاتصالات {nat}",
    "diplomacy": "الدبلوماسية {nat}",
    "federal election candidates": "مرشحو الانتخابات الفيدرالية {nat}",
    "federal election": "الانتخابات الفيدرالية {nat}",
    "federal elections": "الانتخابات الفيدرالية {nat}",
    "football club": "أندية كرة القدم {nat}",
    "football manager history": "تاريخ مدربي كرة القدم {nat}",
    "football manager": "مدربي كرة القدم {nat}",
    "football": "كرة القدم {nat}",
    "general election candidates": "مرشحو الانتخابات العامة {nat}",
    "general election": "الانتخابات العامة {nat}",
    "general elections": "الانتخابات العامة {nat}",
    "legislature election": "الانتخابات التشريعية {nat}",
    "legislature elections": "الانتخابات التشريعية {nat}",
    "local election": "الانتخابات المحلية {nat}",
    "local elections": "الانتخابات المحلية {nat}",
    "national navy": "القوات البحرية الوطنية {nat}",
    "naval forces": "القوات البحرية {nat}",
    "navy": "القوات البحرية {nat}",
    "presidential candidates": "مرشحو الرئاسة {nat}",
    "presidential election": "انتخابات الرئاسة {nat}",
    "presidential elections": "انتخابات الرئاسة {nat}",
    "presidential electors": "ناخبو الرئاسة {nat}",
    "presidential primaries": "الانتخابات الرئاسية التمهيدية {nat}",
    # "presidential primaries": "انتخابات رئاسية تمهيدية {nat}",
    "presidential-elections": "انتخابات الرئاسة {nat}",
    "presidential-primaries": "الانتخابات الرئاسية التمهيدية {nat}",
    "state legislative": "المجالس التشريعية للولايات {nat}",
    "state lower house": "المجالس الدنيا للولايات {nat}",
    "state upper house": "المجالس العليا للولايات {nat}",
    "supreme court": "المحكمة العليا {nat}",
}  # Category:United_States_Coast_Guard_Aviation

military_format_men = {
    "congressional delegation": "وفود الكونغرس {nat}",
    "congressional delegations": "وفود الكونغرس {nat}",
    "parliament": "البرلمان {nat}",
    "congress": "الكونغرس {nat}",
    "house of commons": "مجلس العموم {nat}",
    "house-of-commons": "مجلس العموم {nat}",
    "senate election": "انتخابات مجلس الشيوخ {nat}",
    "senate elections": "انتخابات مجلس الشيوخ {nat}",
    "premier division": "الدوري {nat} الممتاز",
    "coast guard": "خفر السواحل {nat}",
    "fa cup": "كأس الاتحاد {nat}",  # Category:Iraq FA Cup
    "federation cup": "كأس الاتحاد {nat}",  # Category:Bangladesh Federation Cup
    "marine corps personnel": "أفراد سلاح مشاة البحرية {nat}",
    "army personnel": "أفراد الجيش {nat}",
    "coast guard aviation": "طيران خفر السواحل {nat}",
    "abortion law": "قانون الإجهاض {nat}",
    "labour law": "قانون العمل {nat}",  # Category:French_labour_law
    "professional league": "دوري المحترفين {nat}",
    "first division league": "الدوري {nat} الدرجة الأولى",
    "second division": "الدوري {nat} الدرجة الثانية",
    "second division league": "الدوري {nat} الدرجة الثانية",
    "third division league": "الدوري {nat} الدرجة الثالثة",
    "forth division league": "الدوري {nat} الدرجة الرابعة",
}


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

    for suffix, prefix_template in ENDS_WITH_TABLE.items():
        if not category_suffix.endswith(suffix):
            continue

        base_suffix = category_suffix[: -len(suffix)].strip()

        suffix_template = (
            military_format_women.get(base_suffix, "") or
            ministrs_for_military_format_women.get(base_suffix, "") or
            ministrs_for_en_is_P17_ar_is_mens.get(base_suffix, "")
        )

        if suffix_template:
            women_with_article = apply_arabic_article(women_label)
            logger.debug(f"Resolved women extended suffix, {suffix=}, {base_suffix=}")
            resolved_label = suffix_template.format(nat=women_with_article)
            return prefix_template.format(resolved_label)

    return ""


def _resolve_men_suffix(category_suffix: str, men_label: str) -> str:
    """
    Resolve categories that use the male templates.
    TODO: use FormatData method
    """

    if not category_suffix or not men_label:
        return ""

    template = (
        military_format_men.get(category_suffix, "") or
        ministrs_for_military_format_men.get(category_suffix, "")
    )
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
        # resolved = _resolve_women_without_article_prefix(normalized_category)
        return ""

    resolved_label = _resolve_women_extended_suffix(suffix, women_label)

    # Fall back to men-specific and sport-specific templates.
    if not resolved_label:
        resolved_label = _resolve_men_suffix(suffix, men_label)

    if resolved_label:
        logger.info(f"Finished army label resolution, category: {normalized_category}, label: {resolved_label}")

    return resolved_label


__all__ = ["te_army"]
