#!/usr/bin/python3
"""
Year-based category label processing.

This module handles categories that contain year information, extracting and
formatting them appropriately for Arabic labels.
"""

import functools
import re
from typing import Pattern

from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...translations import WORD_AFTER_YEARS
from ...translations.funcs import get_from_pf_keys2
from ..circular_dependency import general_resolver, sub_general_resolver
from ..common_resolver_chain import get_lab_for_country2
from ..data.mappings import change_numb_to_word
from ..legacy_utils import Add_in_table
from ..make_bots import get_KAKO
from ..utils.regex_hub import REGEX_SUB_YEAR, RE1_compile, RE2_compile, RE33_compile
from .bot_2018 import get_pop_All_18

arabic_labels_preceding_year = [
    # لإضافة "في" بين البداية والسنة في تصنيفات مثل :
    # tab[Category:1900 rugby union tournaments for national teams] = "تصنيف:بطولات اتحاد رجبي للمنتخبات الوطنية 1900"
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رجبي للمنتخبات الوطنية",
]


known_bodies = {
    # "term of the Iranian Majlis" : "المجلس الإيراني",
    "iranian majlis": "المجلس الإيراني",
    "united states congress": "الكونغرس الأمريكي",
}


pattern_str = rf"^(\d+)(th|nd|st|rd) ({'|'.join(known_bodies.keys())})$"
_political_terms_pattern = re.compile(pattern_str, re.IGNORECASE)


def translate_general_category_wrap(category: str) -> str:
    arlabel = (
        ""
        or sub_general_resolver.sub_translate_general_category(category)
        or general_resolver.work_separator_names(category)
    )
    return arlabel


def handle_political_terms(category_text: str) -> str:
    """Handles political terms like 'united states congress'."""
    # كونغرس
    # cs = re.match(r"^(\d+)(th|nd|st|rd) united states congress", category_text)
    match = _political_terms_pattern.match(category_text.lower())
    if not match:
        return ""
    ordinal_number = match.group(1)
    body_key = match.group(3)

    body_label = known_bodies.get(body_key, "")
    if not body_label:
        return ""

    ordinal_label = change_numb_to_word.get(ordinal_number, f"الـ{ordinal_number}")

    label = f"{body_label} {ordinal_label}"
    logger.debug(f">>> _handle_political_terms lab ({label}), country: ({category_text})")
    return label


def _handle_year_at_start(category_text: str) -> str:
    """Handles cases where the year is at the start of the string."""
    label = ""
    year = REGEX_SUB_YEAR.sub(r"\g<1>", category_text)

    if not year:
        logger.debug(f">>> _handle_year_at_start: {year=}, no match")
        return ""

    if year == category_text:
        logger.debug(f">>> _handle_year_at_start: {year=}, no match (year == category_text)")
        return ""

    remainder = category_text[len(year) :].strip().lower()
    logger.debug(f">>> _handle_year_at_start: {year=}, suffix:{remainder}")

    remainder_label = ""
    if remainder in WORD_AFTER_YEARS:
        remainder_label = WORD_AFTER_YEARS[remainder]

    if not remainder_label:
        remainder_label = (
            ""
            or all_new_resolvers(remainder)
            or get_from_pf_keys2(remainder)
            or translate_general_category_wrap(remainder)
            or get_lab_for_country2(remainder)
            or get_pop_All_18(remainder)
            or get_KAKO(remainder)
            or ""
        )

    if not remainder_label:
        return ""

    separator = " "

    if remainder_label.strip() in arabic_labels_preceding_year:
        logger.debug("arabic_labels_preceding_year Add في to arlabel sus.")
        separator = " في "

    elif remainder in Add_in_table:
        logger.debug("a<<lightblue> > > > > > Add في to suf")
        separator = " في "

    label = remainder_label + separator + year

    logger.info_if_or_debug(f"<<yellow>> end _handle_year_at_start: {category_text=}, {label=}", label)
    return label


def _handle_year_at_end(
    category_text: str,
    compiled_year_pattern: Pattern[str],
    compiled_range_pattern: Pattern[str],
) -> str:
    """
    Create an Arabic label when a year or year-range appears at the end of a category string.

    Parameters:
        category_text (str): The category text to analyze; trailing year or year-range is expected.
        compiled_year_pattern (Pattern[str]): Regex that extracts a trailing year-like substring from the input.
        compiled_range_pattern (Pattern[str]): Regex that extracts a trailing year-range substring (used to refine the year label).

    Returns:
        str: A combined label of the resolved remainder and the formatted year (e.g., "<remainder_label> <year_label>"), or an empty string if no valid remainder label or year extraction is found. The function normalizes "–present" to "–الآن" in the year portion.
    """
    year_at_end_label = compiled_year_pattern.sub(r"\g<1>", category_text.strip())

    range_match = compiled_range_pattern.match(category_text)

    if range_match:
        year_at_end_label = compiled_range_pattern.sub(r"\g<1>", category_text.strip())
        year_at_end_label = compiled_range_pattern.sub(r"\g<1>", category_text.strip())

    # if RE4:
    # year2 = "موسم " + RE4_compile.sub(r"\g<1>", country.strip())

    if year_at_end_label == category_text or not year_at_end_label:
        return ""

    formatted_year_label = year_at_end_label
    logger.debug(f">>> _handle_year_at_end: year2:{year_at_end_label}")
    remainder = category_text[: -len(year_at_end_label)]

    remainder_label = (
        ""
        or all_new_resolvers(remainder)
        or translate_general_category_wrap(remainder)
        or get_lab_for_country2(remainder)
        or get_pop_All_18(remainder)
        or get_KAKO(remainder)
        or ""
    )
    if not remainder_label:
        return ""
    if "–present" in formatted_year_label:
        formatted_year_label = formatted_year_label.replace("–present", "–الآن")

    label = f"{remainder_label} {formatted_year_label}"
    logger.debug(f'>>>>>> Try With Years new lab4  "{label}" ')

    logger.info_if_or_debug(f"<<yellow>> end _handle_year_at_end: {category_text=}, {label=}", label)
    return label


@functools.lru_cache(maxsize=10000)
def Try_With_Years(category: str) -> str:
    """
    Produce an Arabic label combining detected year information with the resolved category remainder.

    Detects year patterns at the start or end of the category or specific political-term patterns, and composes a label that pairs the resolved remainder with the normalized year (or year-range). Returns an empty string when no applicable year pattern is found.

    Parameters:
        category (str): Category text that may contain a year or year-range (e.g., "1990 United States Congress", "American Soccer League (1933–83)").

    Returns:
        str: The formatted Arabic label including the resolved remainder and year, or an empty string if no year pattern is applicable.
    """
    logger.debug(f"<<yellow>> start Try_With_Years: {category=}")
    # pop_final_Without_Years

    label = ""
    category = category.strip()

    if category.isdigit():
        return category

    category = category.replace("−", "-")

    if label := handle_political_terms(category):
        return label

    year_at_start = RE1_compile.match(category)
    year_at_end = RE2_compile.match(category)
    # Category:American Soccer League (1933–83)
    year_at_end2 = RE33_compile.match(category)
    # RE4 = RE4_compile.match(category)

    if not year_at_start and not year_at_end and not year_at_end2:  # and not RE4
        logger.info(f" end Try_With_Years: {category=} no match year patterns")
        return ""

    label = _handle_year_at_start(category) or _handle_year_at_end(category, RE2_compile, RE33_compile) or ""
    logger.info_if_or_debug(f"<<yellow>> end Try_With_Years: {category=}, {label=}", label)
    return label


def wrap_try_with_years(category_r) -> str:
    """
    Parse a category name that may start with a year and return its Arabic label.

    Parameters:
        category_r (str): Raw category name; may include a leading "Category:" prefix and mixed case.

    Returns:
        str: The generated Arabic label when a year-based pattern is recognized, or an empty string if no suitable year-based label is found.
    """
    cat3 = category_r.lower().replace("category:", "").strip()

    logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

    # TODO: THIS NEED REVIEW
    # Reject strings that contain common English prepositions
    blocked = ("in", "of", "from", "by", "at")
    if any(f" {word} " in cat3.lower() for word in blocked):
        return ""

    category_lab = ""
    if re.sub(r"^\d", "", cat3) != cat3:
        category_lab = Try_With_Years(cat3)

    return category_lab
