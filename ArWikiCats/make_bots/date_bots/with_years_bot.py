#!/usr/bin/python3
"""
!
"""

import functools
import re
from typing import Pattern

from ...helps.log import logger
from ...translations import WORD_AFTER_YEARS, change_numb_to_word, get_from_pf_keys2
from ..format_bots import ar_lab_before_year_to_add_in
from ...ma_bots import country2_lab
from ...ma_bots.ye_ts_bot import translate_general_category
from ..matables_bots.data import Add_in_table
from ..matables_bots.table1_bot import get_KAKO
from ..reg_lines import RE1_compile, RE2_compile, RE33_compile, re_sub_year
from ...new_resolvers.reslove_all import new_resolvers_all

# Precompiled Regex Patterns
REGEX_SUB_YEAR = re.compile(re_sub_year, re.IGNORECASE)

known_bodies = {
    # "term of the Iranian Majlis" : "المجلس الإيراني",
    "iranian majlis": "المجلس الإيراني",
    "united states congress": "الكونغرس الأمريكي",
}

pattern_str = r"^(\d+)(th|nd|st|rd) (%s)$" % "|".join(known_bodies.keys())
_political_terms_pattern = re.compile(pattern_str, re.IGNORECASE)


def _handle_political_terms(category_text: str) -> str:
    """Handles political terms like 'united states congress'."""
    # كونغرس
    # cs = re.match(r"^(\d+)(th|nd|st|rd) united states congress", category_text)
    if match := _political_terms_pattern.match(category_text):
        ordinal_number = match.group(1)
        body_key = match.group(3)
        body_label = known_bodies[body_key]
        ordinal_label = change_numb_to_word.get(ordinal_number, f"الـ{ordinal_number}")
        label = f"{body_label} {ordinal_label}"
        logger.debug(f">>> _handle_political_terms lab ({label}), country: ({category_text})")
        return label
    return ""


def _handle_year_at_start(category_text: str) -> str:
    """Handles cases where the year is at the start of the string."""
    label = ""
    year = REGEX_SUB_YEAR.sub(r"\g<1>", category_text)
    if year == category_text or not year:
        return ""

    remainder = category_text[len(year) :].strip().lower()
    logger.debug(f">>> _handle_year_at_start: {year=}, suffix:{remainder}")

    remainder_label = ""
    if remainder in WORD_AFTER_YEARS:
        remainder_label = WORD_AFTER_YEARS[remainder]

    if not remainder_label:
        remainder_label = (
            new_resolvers_all(remainder) or
            get_from_pf_keys2(remainder) or
            get_KAKO(remainder) or
            translate_general_category(remainder, fix_title=False) or
            country2_lab.get_lab_for_country2(remainder) or
            ""
        )

    if not remainder_label:
        return ""

    separator = " "

    if remainder_label.strip() in ar_lab_before_year_to_add_in:
        logger.debug("ar_lab_before_year_to_add_in Add في to arlabel sus.")
        separator = " في "

    elif remainder in Add_in_table:
        logger.debug("a<<lightblue> > > > > > Add في to suf")
        separator = " في "

    label = remainder_label + separator + year
    logger.debug(f'>>>>>> Try With Years new lab2  "{label}" ')

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
        new_resolvers_all(remainder) or
        translate_general_category(remainder, fix_title=False) or
        country2_lab.get_lab_for_country2(remainder) or
        ""
    )
    if "–present" in formatted_year_label:
        formatted_year_label = formatted_year_label.replace("–present", "–الآن")

    if remainder_label:
        label = f"{remainder_label} {formatted_year_label}"
        logger.debug(f'>>>>>> Try With Years new lab4  "{label}" ')
        return label
    return ""


@functools.lru_cache(maxsize=None)
def Try_With_Years(category_text: str) -> str:
    """Retrieve a formatted label for a given country based on its historical
    context.

    This function processes the input country string to extract relevant
    year information and formats it according to predefined rules. It checks
    for specific patterns in the input string, such as congressional terms
    or year ranges, and returns a corresponding label. If the input does not
    match any known patterns, an empty string is returned. The function also
    caches results for efficiency.

    Args:
        category_text (str): The name of the country or a related term that may include year
            information.

    Returns:
        str: A formatted label that includes the country name and associated year
            information,
        or an empty string if no valid information is found.
    """
    logger.debug(f">>> Try With Years country ({category_text})")
    # pop_final_Without_Years

    label = ""
    category_text = category_text.strip()

    if category_text.isdigit():
        return category_text

    category_text = category_text.replace("−", "-")

    if label := _handle_political_terms(category_text):
        return label

    year_at_start = RE1_compile.match(category_text)
    year_at_end = RE2_compile.match(category_text)
    # Category:American Soccer League (1933–83)
    year_at_end2 = RE33_compile.match(category_text)
    # RE4 = RE4_compile.match(category_text)

    if not year_at_start and not year_at_end and not year_at_end2:  # and not RE4
        return ""

    label = _handle_year_at_start(category_text)

    if not label:
        label = _handle_year_at_end(category_text, RE2_compile, RE33_compile)

    if label:
        logger.debug(f'>>>>>> Try With Years lab2 "{label}" ')

    return label
