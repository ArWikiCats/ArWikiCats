"""Helpers for normalizing Arabic category titles.

The module exposes the :func:`fixlabel` entry point that performs a sequence of
regular-expression driven transformations. The transformations are heavily
localized for Arabic Wikipedia labels and rely on the constants defined in
:mod:`ArWikiCats.fix.fixlists`.
"""

from __future__ import annotations

import re
from typing import Iterable, Mapping

from ..helps import getLogger

logger = getLogger(__name__)
from .fixlists import (
    ENDING_REPLACEMENTS,
    REPLACEMENTS,
    STARTING_REPLACEMENTS,
    YEAR_CATEGORY_LABELS,
)
from .mv_years import move_years
from .specific_normalizations import apply_category_specific_normalizations

# Pattern for matching years in Arabic text (including BCE dates and century/millennium references)
YEARS_REGEX_AR = (
    r"\d+[−–\-]\d+"
    # r"|\d+\s*(ق[\s\.]م|قبل الميلاد)*"
    r"|(?:عقد|القرن|الألفية)*\s*\d+\s*(ق[\s\.]م|قبل الميلاد)*"
)

categories = [
    "الآلة",
    "البلد",
    "البوابة",
    "الجنسية والمجموعة العرقية",
    "المجموعة العرقية",
    "الجنسية والمهنة",
    "الدين والجنسية",
    "المهنة والجنسية",
    "البلد أو اللغة",
    "النوع الفني",
    "الجنسية",
    "الحرب",
    "الدين",
    "السنة",
    "العقد",
    "القارة",
    "اللغة",
    "المدينة",
    "المنظمة",
    "المهنة",
    "الموقع",
    "النزاع",
    "الولاية",
]

categories_expression = "|".join(categories)
REGEX_COMPATTERN = re.compile(rf" حسب\s({categories_expression}) ({YEARS_REGEX_AR})$")


def add_fee(text: str) -> str:
    """Ensure the preposition ``في`` precedes years in certain categories.

    Args:
        text: The label text that should be inspected.

    Returns:
        A label with normalized year phrasing.
    """

    text = REGEX_COMPATTERN.sub(r" حسب \1 في \2", text)
    return text


def _apply_regex_replacements(text: str, replacements: Mapping[str, str]) -> str:
    """Sequentially apply regex-based replacements to ``text``.

    Args:
        text: The mutable text that should be normalized.
        replacements: Pairs of patterns and replacement strings to apply in
            insertion order.

    Returns:
        The normalized text.
    """

    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text)
    return text


def _apply_prefix_replacements(text: str, replacements: Mapping[str, str]) -> str:
    """Replace matching prefixes using simple string slicing.

    Args:
        text: The text to normalise.
        replacements: Mapping of prefix strings to their normalized versions.

    Returns:
        The updated text.
    """

    for prefix, replacement in replacements.items():
        if text.startswith(prefix):
            text = replacement + text[len(prefix) :]
    return text


def _apply_suffix_replacements(text: str, replacements: Mapping[str, str]) -> str:
    """Replace matching suffixes using simple string slicing.

    Args:
        text: The text to normalise.
        replacements: Mapping of suffix strings to replacement values.

    Returns:
        The updated text with trailing whitespace removed.
    """

    for suffix, replacement in replacements.items():
        if text.endswith(suffix):
            text = text[: -len(suffix)] + replacement
            text = text.strip()
    return text


def _insert_year_preposition(text: str, categories: Iterable[str]) -> str:
    """Insert the preposition ``في`` when a year immediately follows a label.

    Args:
        text: The text to normalise.
        categories: Category names that should receive the additional
            preposition.

    Returns:
        The updated text with consistent year formatting.
    """

    for category in categories:
        pattern = rf"(\s*{re.escape(category)}) (\d+\s*|عقد \d+\s*|القرن \d+\s*)"
        text = re.sub(pattern, r"\g<1> في \g<2>", text)
    return text


def _apply_basic_normalizations(ar_label: str) -> str:
    """Apply the shared replacements that most labels require."""

    normalized = _apply_regex_replacements(ar_label, REPLACEMENTS)
    normalized = _insert_year_preposition(normalized, YEAR_CATEGORY_LABELS)
    normalized = _apply_prefix_replacements(normalized, STARTING_REPLACEMENTS)
    normalized = normalized.strip()
    normalized = _apply_suffix_replacements(normalized, ENDING_REPLACEMENTS)
    normalized = normalized.replace("نصب تذكارية لال", "نصب تذكارية لل")
    normalized = _apply_suffix_replacements(normalized, ENDING_REPLACEMENTS)
    return normalized


def _normalize_conflict_phrases(text: str) -> str:
    """Normalize phrases describing conflicts or geographic relations."""

    if match := re.match(r"^(الغزو \w+|\w+ الغزو \w+) في (\w+.*?)$", text):
        first_part = match.group(1)
        second_part = match.group(2)
        if second_part.startswith("ال"):
            second_part = second_part[1:]
        text = f"{first_part} ل{second_part}"
    return text


def _normalize_sub_regions(text: str) -> str:
    """Normalize sub-region terminology for a number of countries."""

    if any(country in text for country in ("اليابان", "يابانيون", "يابانيات")):
        text = re.sub(r"حسب الولاية", "حسب المحافظة", text)
    if "سريلانكي" in text or "سريلانكا" in text:
        text = re.sub(r"الإقليم", "المقاطعة", text)
        text = re.sub(r"أقاليم", "مقاطعات", text)
    if "تركيا" in text:
        text = re.sub(r"مديريات", "أقضية", text)
    if "جزائر" in text:
        text = re.sub(r"المقاطعة", "الإقليم", text)
        text = re.sub(r"مقاطعات", "أقاليم", text)
        text = re.sub(r"مديريات", "دوائر", text)
        text = re.sub(r"المديرية", "الدائرة", text)
    return text


def fix_it(ar_label: str, en_label: str) -> str:
    """Normalize an Arabic label based on heuristics and English context.

    Args:
        ar_label: The Arabic label that requires normalization.
        en_label: The English text associated with the label. The string is
            inspected for hints that determine specific Arabic replacements.

    Returns:
        A normalised Arabic label.
    """

    normalized_en = en_label.replace("_", " ").lower()

    ar_label = re.sub(r"\s+", " ", ar_label)
    ar_label = re.sub(r"\{\}", "", ar_label)

    # santa fe province
    if ar_label.endswith(" في") and " fe " not in f" {normalized_en.strip()} ":
        ar_label = ar_label[: -len(" في")]
        logger.debug(f"Removed stray 'في' from end of label: {ar_label}")

    if match := re.match(r".*(\d\d\d\d)\-(\d\d).*", ar_label, flags=re.IGNORECASE):
        start_year = match.group(1)
        end_year = match.group(2)
        ar_label = re.sub(f"{start_year}-{end_year}", f"{start_year}–{end_year}", ar_label)
        logger.debug(f"Replaced hyphen with en dash in range {start_year}-{end_year}")

    if re.sub(r"^\–\d+", "", ar_label) != ar_label:
        return ""

    ar_label = ar_label.strip()
    ar_label = _apply_basic_normalizations(ar_label)
    ar_label = re.sub(r"كأس العالم لكرة القدم (\d)", r"كأس العالم \g<1>", ar_label)
    ar_label = re.sub(r",", "،", ar_label)
    ar_label = re.sub(r"^(.*) تصفيات مؤهلة إلى (.*)$", r"تصفيات \g<1> مؤهلة إلى \g<2>", ar_label)
    ar_label = re.sub(r"تأسيسات (\d+.*)$", r"تأسيسات سنة \g<1>", ar_label)
    ar_label = re.sub(r"انحلالات (\d+.*)$", r"انحلالات سنة \g<1>", ar_label)
    ar_label = re.sub(r" من حسب ", " حسب ", ar_label)
    # ar_label = re.sub(r"لاعبو في " , "لاعبو ", ar_label)
    # ar_label = re.sub(r"لاعبو من " , "لاعبو " , ar_label)
    ar_label = apply_category_specific_normalizations(ar_label, normalized_en)
    ar_label = ar_label.strip()

    # if ar_label.endswith("أنتهت في"):
    # ar_label = re.sub(r"أنتهت في$" , "أنتهت" , ar_label ).strip()

    ar_label = _apply_basic_normalizations(ar_label)

    if "مبنية على" not in ar_label:
        ar_label = re.sub(r" على أفلام$", " في الأفلام", ar_label)

    ar_label = _normalize_sub_regions(ar_label)
    ar_label = ar_label.replace("(توضيح)", "")
    ar_label = ar_label.replace(" تأسست في ", " أسست في ")
    ar_label = ar_label.replace("ب201", "بسنة 201")
    ar_label = ar_label.replace("ب202", "بسنة 202")
    ar_label = ar_label.replace("على المريخ", "في المريخ")

    ar_label = " ".join(ar_label.strip().split())

    ar_label = re.sub(r"^شغب (\d+)", r"شغب في \g<1>", ar_label)
    ar_label = re.sub(r"قوائممتعلقة", "قوائم متعلقة", ar_label)
    ar_label = re.sub(r" في أصل ", " من أصل ", ar_label)
    ar_label = re.sub(r"حلقات قوائم", "قوائم حلقات", ar_label)
    ar_label = _normalize_conflict_phrases(ar_label)

    # if "لاعبو " and "سيدات" in label_old: fix it to لاعبات (use all())

    # if all(x in ar_label for x in ["لاعبو ", "سيدات"]): ar_label = ar_label.replace("لاعبو ", "لاعبات ")

    ar_label = ar_label.strip()
    return ar_label


def cleanse_category_label(category_lab):
    """
    Fixes a known formatting issue in Arabic category labels.

    Parameters:
        category_lab (str): The category label to cleanse.

    Returns:
        str: The cleansed category label with specific formatting corrections applied.
    """
    category_lab = re.sub(r"سانتا-في", "سانتا في", category_lab)
    return category_lab


def fixlabel(label_old: str, en: str = "") -> str:
    """Return a normalized Arabic label suitable for publication.

    Args:
        label_old: The original, possibly denormalized, Arabic label.
        out: When ``True`` emit an informational log when a label changes.
        en: Optional English context string that influences certain fixes.

    Returns:
        The normalized label string. An empty string indicates that the label
        was rejected by one of the validation steps.
    """
    logger.debug(f"fixlabel: Starting with label_old: {label_old=}| {en=}")
    original_label = label_old
    letters_regex = "[a-z]"
    if re.sub(letters_regex, "", label_old, flags=re.IGNORECASE) != label_old:
        return ""

    skip_labels = [
        "مراكز سياسية",
        "مشاعر معادية للإسرائيليون",
    ]

    if any(label in label_old for label in skip_labels):
        return ""

    if "لاعبات" in label_old and "مغتربون" in label_old:
        return ""

    label_old = label_old.strip()
    label_old = label_old.replace("_", " ")
    label_old = re.sub(r"تصنيف\:\s*", "", label_old)
    label_old = re.sub(r"تصنيف:", "", label_old)

    ar_label = label_old
    ar_label = fix_it(ar_label, en)
    ar_label = add_fee(ar_label)
    ar_label = move_years(ar_label)

    if "لاعبو" in ar_label and ("women's" in en or "womens" in en or "سيدات" in ar_label or "نسائية" in ar_label):
        ar_label = ar_label.replace("لاعبو", "لاعبات")

    if original_label != ar_label:
        logger.info(f'fixtitle: original_label:"{original_label}", after:"{ar_label}"')

    return ar_label


__all__ = [
    "add_fee",
    "fix_it",
    "fixlabel",
]
