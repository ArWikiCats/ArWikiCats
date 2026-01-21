#!/usr/bin/python3
"""
Year-based category label processing.

This module handles categories that contain year information, extracting and
formatting them appropriately for Arabic labels.
"""

import functools
import re
from typing import Pattern

from ..helps import logger
from ..legacy_bots.common_resolver_chain import get_lab_for_country2
from ..new_resolvers import all_new_resolvers
from ..translations import WORD_AFTER_YEARS, get_from_pf_keys2
from .ma_bots import general_resolver
from .make_bots.reg_lines import RE1_compile, RE2_compile, RE33_compile, re_sub_year
from .matables_bots.data import Add_in_table
from .political_terms import handle_political_terms

# Precompiled Regex Patterns
REGEX_SUB_YEAR = re.compile(re_sub_year, re.IGNORECASE)

arabic_labels_preceding_year = [
    # لإضافة "في" بين البداية والسنة في تصنيفات مثل :
    # tab[Category:1900 rugby union tournaments for national teams] = "تصنيف:بطولات اتحاد رجبي للمنتخبات الوطنية 1900"
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رجبي للمنتخبات الوطنية",
]


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
            or general_resolver.translate_general_category(remainder, fix_title=False)
            or get_lab_for_country2(remainder)
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
    """Handles cases where the year is at the end of the string."""
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
        or general_resolver.translate_general_category(remainder, fix_title=False)
        or get_lab_for_country2(remainder)
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


@functools.lru_cache(maxsize=None)
def Try_With_Years(category: str) -> str:
    """
    Extracts and formats a year-aware Arabic label from a category string.

    Processes the input category to detect year patterns (year at start, year or year-range at end, or specific political-term patterns) and returns a composed label combining the resolved remainder and the year when a match is found.

    Parameters:
        category (str): Category text that may contain a year or year-range (e.g., "1990 United States Congress", "American Soccer League (1933–83)").

    Returns:
        str: The formatted label that includes the resolved remainder and year information, or an empty string if no applicable year pattern is detected.
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
