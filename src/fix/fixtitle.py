"""Helpers for normalizing Arabic category titles.

The module exposes the :func:`fixlab` entry point that performs a sequence of
regular-expression driven transformations. The transformations are heavily
localized for Arabic Wikipedia labels and rely on the constants defined in
:mod:`src.fix.fixlists`.
"""

from __future__ import annotations

import logging
import re
from typing import Iterable, Mapping

from .fixlists import ENDING_REPLACEMENTS, REPLACEMENTS, STARTING_REPLACEMENTS, YEAR_CATEGORY_LABELS
from .mv_years import YEARS_REGEX, move_years

logger = logging.getLogger(__name__)


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
    """Replace matching suffixes using anchored regular expressions.

    Args:
        text: The text to normalise.
        replacements: Mapping of suffix strings to replacement values.

    Returns:
        The updated text with trailing whitespace removed.
    """

    for suffix, replacement in replacements.items():
        if text.endswith(suffix):
            pattern = re.compile(rf"{re.escape(suffix)}$")
            text = pattern.sub(replacement, text).strip()
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
            second_part = second_part[2:]
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


def _apply_category_specific_normalizations(ar_label: str, en_label: str) -> str:
    """Apply normalizations that depend on the English context string.

    # مسلسلات تلفزيونية > to > مسلسلات تلفازية أنتجها أو أنتجتها ...
    # مبان ومنشآت بواسطة > to > مبان ومنشآت صممها أو خططها ...
    # ألبومات ... بواسطة ... > ألبومات ... ل.....
    # لاعبو كرة بواسطة > لاعبو كرة حسب
    # """

    fix_bys = [
        "أفلام",
        "أعمال",
        "اختراعات",
        "لوحات",
        "شعر",
        "مسرحيات",
        "روايات",
        "كتب",
    ]
    for replacement in fix_bys:
        ar_label = re.sub(f"{replacement} بواسطة ", f"{replacement} ", ar_label)

    ar_label = re.sub(r"وفيات بواسطة ضربات ", "وفيات بضربات ", ar_label)
    ar_label = re.sub(r"ضربات جوية نفذت بواسطة ", "ضربات جويت نفذتها ", ar_label)
    ar_label = re.sub(r"أفلام أنتجت بواسطة ", "أفلام أنتجها ", ar_label)
    ar_label = re.sub(r"كاميرات اخترعت ", "كاميرات عرضت ", ar_label)
    ar_label = re.sub(r"هواتف محمولة اخترعت ", "هواتف محمولة عرضت ", ar_label)
    ar_label = re.sub(r"مركبات اخترعت ", "مركبات عرضت ", ar_label)
    ar_label = re.sub(r"منتجات اخترعت ", "منتجات عرضت ", ar_label)

    # قصص قصيرة 1613 > قصص قصيرة كتبت سنة 1613
    # قصص قصيرة من تأليف إرنست همينغوي > قصص إرنست همينغوي القصيرة
    # قصص قصيرة لأنطون تشيخوف > قصص أنطون تشيخوف القصيرة
    ar_label = re.sub(r"^قصص قصيرة (\d+)$", r"قصص قصيرة كتبت سنة \1", ar_label)

    ar_label = re.sub(r"ردود فعل إلى ", "ردود فعل على ", ar_label)
    ar_label = re.sub(r"مدراء كرة", "مدربو كرة", ar_label)
    ar_label = re.sub(r"متعلقة 2", "متعلقة ب2", ar_label)
    ar_label = re.sub(r"هولوكوستية", "الهولوكوست", ar_label)
    ar_label = re.sub(r"في هولوكوست", "في الهولوكوست", ar_label)
    ar_label = re.sub(r"صدور عظام في الدولة العثمانية", "صدور عظام عثمانيون في", ar_label)
    ar_label = re.sub(r"أعمال بواسطة ", "أعمال ", ar_label)
    ar_label = re.sub(r" في فائزون ", " فائزون ", ar_label)
    ar_label = re.sub(r" في منافسون ", " منافسون ", ar_label)
    ar_label = re.sub(r" على السجل الوطني للأماكن ", " في السجل الوطني للأماكن ", ar_label)
    ar_label = re.sub(r" من قبل البلد", " حسب البلد", ar_label)
    ar_label = re.sub(r"حكم عليهم الموت", "حكم عليهم بالإعدام", ar_label)
    ar_label = re.sub(r"محررون من منشورات", "محررو منشورات", ar_label)
    ar_label = re.sub(r"محررات من منشورات", "محررات منشورات", ar_label)
    ar_label = re.sub(r"قديسون صوفيون", "أولياء صوفيون", ar_label)
    ar_label = re.sub(r"مدربو رياضية", "مدربو رياضة", ar_label)
    ar_label = re.sub(r" من من ", " من ", ar_label)
    ar_label = re.sub(r" حسب حسب ", " حسب ", ar_label)
    ar_label = re.sub(r" حسب بواسطة ", " بواسطة ", ar_label)
    ar_label = re.sub(r" في في ", " في ", ar_label)
    ar_label = re.sub(r" في في ", " في ", ar_label)
    ar_label = re.sub(r" في في ", " في ", ar_label)
    ar_label = re.sub(r"أدينوا ب ", "أدينوا ب", ar_label)
    ar_label = re.sub(r" في من ", " من ", ar_label)
    ar_label = re.sub(r" العسكري القرن ", " العسكري في القرن ", ar_label)
    ar_label = re.sub(r" من في ", " في ", ar_label)
    ar_label = re.sub(r" فورمولا 1 2", " فورمولا 1 في سنة 2", ar_label)
    ar_label = re.sub(r" فورمولا 1 1", " فورمولا 1 في سنة 1", ar_label)
    ar_label = re.sub(r" في حسب ", " حسب ", ar_label)
    ar_label = re.sub(r" من حسب ", " حسب ", ar_label)
    ar_label = re.sub(r" ق\.م ", " ق م ", ar_label)
    # ar_label = re.sub(r"تأسيسات سنة", "تأسيسات", ar_label)

    ar_label = re.sub(r"أحداث رياضية الرياضية", "أحداث رياضية", ar_label)
    ar_label = re.sub(r" من القرن", " في القرن", ar_label)
    ar_label = re.sub(r" من حروب", " في حروب", ar_label)
    ar_label = re.sub(r" من الحروب", " في الحروب", ar_label)
    ar_label = re.sub(r" من حرب", " في حرب", ar_label)
    ar_label = re.sub(r" من الحرب", " في الحرب", ar_label)
    ar_label = re.sub(r" من الثورة", " في الثورة", ar_label)
    ar_label = re.sub(r"مغتربون ال", "مغتربون من ال", ar_label)
    ar_label = re.sub(r"سفراء إلى ", "سفراء لدى ", ar_label)
    ar_label = re.sub(r"أشخاص أصل ", "أشخاص من أصل ", ar_label)
    ar_label = re.sub(r" بدأ عرضها حسب السنة", " حسب سنة بدء العرض", ar_label)
    ar_label = re.sub(r" أنتهت حسب السنة", " حسب سنة انتهاء العرض", ar_label)
    ar_label = re.sub(r" في رياضة في ", " في الرياضة في ", ar_label)

    if "attacks on" in en_label and "هجمات في " in ar_label:
        ar_label = re.sub(r"هجمات في ", "هجمات على ", ar_label)

    return ar_label


def fix_it(ar_label: str, en_label: str) -> str:
    """Normalize an Arabic label based on heuristics and English context.

    Args:
        ar_label: The Arabic label that requires normalization.
        en_label: The English text associated with the label. The string is
            inspected for hints that determine specific Arabic replacements.

    Returns:
        A normalised Arabic label.
    """

    ar_label = re.sub(r"\s+", " ", ar_label)
    ar_label = re.sub(r"\{\}", "", ar_label)
    if ar_label.endswith(" في"):
        ar_label = ar_label[: -len(" في")]

    normalized_en = en_label.replace("_", " ").lower()

    if match := re.match(r".*(\d\d\d\d)\-(\d\d).*", ar_label, flags=re.IGNORECASE):
        start_year = match.group(1)
        end_year = match.group(2)
        ar_label = re.sub(f"{start_year}-{end_year}", f"{start_year}–{end_year}", ar_label)
        logger.debug("Replaced hyphen with en dash in range %s-%s", start_year, end_year)

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
    ar_label = _apply_category_specific_normalizations(ar_label, normalized_en)
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
    ar_label = ar_label.replace("  ", " ")
    ar_label = re.sub(r"^شغب (\d+)", r"شغب في \g<1>", ar_label)
    ar_label = re.sub(r"قوائممتعلقة", "قوائم متعلقة", ar_label)
    ar_label = re.sub(r" في أصل ", " من أصل ", ar_label)
    ar_label = _normalize_conflict_phrases(ar_label)
    ar_label = ar_label.strip()
    return ar_label


def add_fee(text: str) -> str:
    """Ensure the preposition ``في`` precedes years in certain categories.

    Args:
        text: The label text that should be inspected.

    Returns:
        A label with normalized year phrasing.
    """

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
    text = re.sub(rf" حسب\s({categories_expression}) ({YEARS_REGEX})$", r" حسب \1 في \2", text)
    return text


def fixlab(label_old: str, out: bool = False, en: str = "") -> str:
    """Return a normalized Arabic label suitable for publication.

    Args:
        label_old: The original, possibly denormalized, Arabic label.
        out: When ``True`` emit an informational log when a label changes.
        en: Optional English context string that influences certain fixes.

    Returns:
        The normalized label string. An empty string indicates that the label
        was rejected by one of the validation steps.
    """

    letters_regex = "[abcdefghijklmnopqrstuvwxyz]"
    if re.sub(letters_regex, "", label_old, flags=re.IGNORECASE) != label_old:
        return ""

    if "مشاعر معادية للإسرائيليون" in label_old:
        return ""

    label_old = label_old.strip()
    label_old = re.sub(r"_", " ", label_old)
    label_old = re.sub(r"تصنيف\:\s*", "", label_old)
    label_old = re.sub(r"تصنيف:", "", label_old)

    ar_label = fix_it(label_old, en)
    ar_label = add_fee(ar_label)
    ar_label = move_years(ar_label)

    if label_old != ar_label and out:
        logger.info('fixtitle: label_old before:"%s", after:"%s"', label_old, ar_label)

    return ar_label


__all__ = [
    "add_fee",
    "fix_it",
    "fixlab",
]
