#!/usr/bin/python3
"""
!
"""

import functools
import re
from typing import Pattern

from ..helps import logger
from ..new_resolvers.reslove_all import new_resolvers_all
from ..time_resolvers.time_to_arabic import convert_time_to_arabic
from ..translations import WORD_AFTER_YEARS, change_numb_to_word, get_from_pf_keys2
from . import sport_lab_suffixes, team_work
from .films_and_others_bot import te_films
from .ma_bots.ye_ts_bot import translate_general_category
from .make_bots.bot_2018 import get_pop_All_18
from .make_bots.reg_lines import RE1_compile, RE2_compile, RE33_compile, re_sub_year
from .matables_bots.data import Add_in_table
from .matables_bots.table1_bot import get_KAKO
from .o_bots import parties_bot, univer
from .o_bots.peoples_resolver import work_peoples

# Precompiled Regex Patterns
REGEX_SUB_YEAR = re.compile(re_sub_year, re.IGNORECASE)

known_bodies = {
    # "term of the Iranian Majlis" : "المجلس الإيراني",
    "iranian majlis": "المجلس الإيراني",
    "united states congress": "الكونغرس الأمريكي",
}


arabic_labels_preceding_year = [
    # لإضافة "في" بين البداية والسنة في تصنيفات مثل :
    # tab[Category:1900 rugby union tournaments for national teams] = "تصنيف:بطولات اتحاد رجبي للمنتخبات الوطنية 1900"
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رجبي للمنتخبات الوطنية",
]

pattern_str = r"^(\d+)(th|nd|st|rd) (%s)$" % "|".join(known_bodies.keys())
_political_terms_pattern = re.compile(pattern_str, re.IGNORECASE)


@functools.lru_cache(maxsize=10000)
def wrap_lab_for_country2(country: str) -> str:
    """
    Retrieve laboratory information for a specified country.
    """

    country2 = country.lower().strip()

    resolved_label = (
        new_resolvers_all(country2)
        or get_from_pf_keys2(country2)
        or get_pop_All_18(country2)
        or te_films(country2)
        or sport_lab_suffixes.get_teams_new(country2)
        or parties_bot.get_parties_lab(country2)
        or team_work.Get_team_work_Club(country2)
        or univer.te_universities(country2)
        or work_peoples(country2)
        or get_KAKO(country2)
        or convert_time_to_arabic(country2)
        or get_pop_All_18(country2)
        or ""
    )
    logger.info(f'>> wrap_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label


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
            new_resolvers_all(remainder)
            or get_from_pf_keys2(remainder)
            or get_KAKO(remainder)
            or translate_general_category(remainder, fix_title=False)
            or wrap_lab_for_country2(remainder)
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
        new_resolvers_all(remainder)
        or translate_general_category(remainder, fix_title=False)
        or wrap_lab_for_country2(remainder)
        or ""
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


def Try_With_Years2(category_r) -> str:
    """ """
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
