#!/usr/bin/python3
"""
Arabic Label Builder Module
"""

import re
from typing import Tuple

from ....helps.log import logger
from ....translations import (
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    New_P17_Finall,
    pf_keys2,
)
from ... import tmp_bot
from ...countries_formats.t4_2018_jobs import te4_2018_Jobs
from ....new import time_to_arabic
from ...format_bots import (
    Tabl_with_in,
    for_table,
)
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.check_bot import check_key_new_players
from ...media_bots.films_bot import te_films
from ...o_bots import bys
from ...o_bots.popl import make_people_lab
from ...p17_bots import nats_other
from ...sports_bots import team_work
from .. import country2_lab
from ..country_bot import Get_c_t_lab, get_country


def _split_category_by_separator(category: str, separator: str) -> Tuple[str, str]:
    """Split category into type and country parts using the separator.

    Args:
        category: The category string to split
        separator: The delimiter to use for splitting

    Returns:
        Tuple of (category_type, country)
    """
    if separator and separator in category:
        parts = category.split(separator, 1)
        category_type = parts[0]
        country = parts[1] if len(parts) > 1 else ""
    else:
        category_type = category
        country = ""

    return category_type, country.lower()


def _fix_typos_in_type(category_type: str, separator_stripped: str) -> str:
    """Fix known typos in the category type.

    Args:
        category_type: The category type string
        separator_stripped: The stripped separator

    Returns:
        Corrected category type
    """
    if separator_stripped == "in" and category_type.endswith(" playerss"):
        return category_type.replace(" playerss", " players")
    return category_type


def _adjust_separator_position(
    text: str,
    separator_stripped: str,
    is_type: bool
) -> str:
    """Adjust separator position for type or country based on separator value.

    Args:
        text: The text to adjust (either type or country)
        separator_stripped: The stripped separator
        is_type: True if adjusting type, False if adjusting country

    Returns:
        Adjusted text with proper separator positioning
    """
    separator_ends = f" {separator_stripped}"
    separator_starts = f"{separator_stripped} "

    if is_type:
        # Adjustments for type (separator should be at the end)
        if separator_stripped == "of" and not text.endswith(separator_ends):
            return f"{text} of"
        elif separator_stripped == "spies for" and not text.endswith(" spies"):
            return f"{text} spies"
    else:
        # Adjustments for country (separator should be at the start)
        if separator_stripped == "by" and not text.startswith(separator_starts):
            return f"by {text}"
        elif separator_stripped == "for" and not text.startswith(separator_starts):
            return f"for {text}"

    return text


def _apply_regex_extraction(
    category: str,
    separator: str,
    category_type: str,
    country: str
) -> Tuple[str, str, bool]:
    """Apply regex-based extraction when simple split is insufficient.

    Args:
        category: Original category string
        separator: The separator string
        category_type: Currently extracted type
        country: Currently extracted country

    Returns:
        Tuple of (type_regex, country_regex, should_use_regex)
    """
    separator_escaped = re.escape(separator) if separator else ""
    mash_pattern = f"^(.*?)(?:{separator_escaped}?)(.*?)$"

    test_remainder = category.lower()
    type_regex, country_regex = "", ""

    try:
        type_regex = re.sub(mash_pattern, r"\g<1>", category.lower())
        country_regex = re.sub(mash_pattern, r"\g<2>", category.lower())

        # Calculate what's left after removing extracted parts
        test_remainder = re.sub(re.escape(category_type.lower()), "", test_remainder)
        test_remainder = re.sub(re.escape(country.lower()), "", test_remainder)
        test_remainder = test_remainder.strip()

    except Exception as e:
        logger.info(f"<<lightred>>>>>> except test_remainder: {e}")
        return type_regex, country_regex, False

    # Determine if we should use regex results
    separator_stripped = separator.strip()
    should_use_regex = test_remainder and test_remainder != separator_stripped

    return type_regex, country_regex, should_use_regex


def get_type_country(category: str, separator: str) -> Tuple[str, str]:
    """Extract the type and country from a given category string.

    This function takes a category string and a delimiter (separator) to split
    the category into a type and a country. It processes the strings to
    ensure proper formatting and handles specific cases based on the value
    of separator.

    Args:
        category: The category string containing type and country information
        separator: The delimiter used to separate the type and country

    Returns:
        Tuple containing the processed type (str) and country (str)

    Example:
        >>> get_type_country("Military installations in Egypt", "in")
        ("Military installations", "egypt")
    """
    # Step 1: Initial split
    category_type, country = _split_category_by_separator(category, separator)

    # Step 2: Fix known typos
    separator_stripped = separator.strip()
    category_type = _fix_typos_in_type(category_type, separator_stripped)

    # Step 3: Apply initial separator adjustments
    category_type = _adjust_separator_position(category_type, separator_stripped, is_type=True)
    country = _adjust_separator_position(country, separator_stripped, is_type=False)

    logger.info(
        f'>xx>>> category_type: "{category_type.strip()}", '
        f'country: "{country.strip()}", {separator=}'
    )

    # Step 4: Check if regex extraction is needed
    type_regex, country_regex, should_use_regex = _apply_regex_extraction(
        category, separator, category_type, country
    )

    if not should_use_regex:
        logger.info('>>>> Using simple split results')
        return category_type, country

    # Step 5: Use regex results with separator adjustments
    logger.info(
        f'>>>> Using regex extraction: {type_regex=}, '
        f'{separator=}, {country_regex=}'
    )

    # Apply typo fixes to regex results as well
    type_regex = _fix_typos_in_type(type_regex, separator_stripped)

    type_regex = _adjust_separator_position(type_regex, separator_stripped, is_type=True)
    country_regex = _adjust_separator_position(country_regex, separator_stripped, is_type=False)

    logger.info(f'>>>> yementest: {type_regex=}, {country_regex=}')

    return type_regex, country_regex


def get_type_lab(separator: str, type_value: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters.

    Args:
        separator (str): The separator/delimiter (separator).
        type_value (str): The type part of the category.

    Returns:
        Tuple[str, bool]: The label and a boolean indicating if 'in' should be appended.
    """
    normalized_preposition = separator.strip()
    type_lower = type_value.lower()

    label = ""
    if type_lower == "women" and normalized_preposition == "from":
        label = "نساء"
        logger.info(f'>> >> >> Make {label=}.')

    elif type_lower == "women of":
        label = "نساء من"
        logger.info(f'>> >> >> Make {label=}.')

    should_append_in_label = True
    type_lower_with_preposition = type_lower.strip()

    if not type_lower_with_preposition.endswith(f" {normalized_preposition}"):
        type_lower_with_preposition = f"{type_lower.strip()} {normalized_preposition}"

    if not label:
        label = Tabl_with_in.get(type_lower_with_preposition, "")
        if label:
            should_append_in_label = False
            logger.info(f'<<<< {type_lower_with_preposition=}, {label=}')

    if not label:
        label = New_P17_Finall.get(type_lower, "")
        if label:
            logger.debug(f'<< {type_lower_with_preposition=}, {label=}')

    if label == "" and type_lower.startswith("the "):
        type_lower_no_article = type_lower[len("the ") :]
        label = New_P17_Finall.get(type_lower_no_article, "")
        if label:
            logger.debug(f'<<< {type_lower_with_preposition=}, {label=}')

    if label == "" and type_lower.strip().endswith(" people"):
        label = make_people_lab(type_lower)

    if not label:
        label = RELIGIOUS_KEYS_PP.get(type_lower, {}).get("males", "")
    if not label:
        label = New_female_keys.get(type_lower, "")
    if not label:
        label = te_films(type_lower)
    if not label:
        label = nats_other.find_nat_others(type_lower)
    if not label:
        label = team_work.Get_team_work_Club(type_lower)

    if not label:
        label = tmp_bot.Work_Templates(type_lower)

    if not label:
        label = Get_c_t_lab(type_lower, normalized_preposition, lab_type="type_label")

    if not label:
        label = te4_2018_Jobs(type_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(type_lower)

    logger.info(f"?????? get_type_lab: {type_lower=}, {label=}")

    label = " ".join(label.strip().split())

    return label, should_append_in_label


def get_con_lab(separator: str, country: str, start_get_country2: bool = False) -> str:
    """Retrieve the corresponding label for a given country.

    Args:
        separator (str): The separator/delimiter.
        country (str): The country part of the category.
        start_get_country2 (bool): Whether to use the secondary country lookup.

    Returns:
        str: The Arabic label for the country.
    """
    separator = separator.strip()
    country_lower = country.strip().lower()
    label = ""
    country_lower_no_dash = country_lower.replace("-", " ")

    if not label:
        label = New_P17_Finall.get(country_lower, "")
    if not label:
        label = pf_keys2.get(country_lower, "")
    if not label:
        label = get_pop_All_18(country_lower, "")

    if not label and "-" in country_lower:
        label = get_pop_All_18(country_lower_no_dash, "")
        if not label:
            label = New_female_keys.get(country_lower_no_dash, "")

    if label == "" and "kingdom-of" in country_lower:
        label = get_pop_All_18(country_lower.replace("kingdom-of", "kingdom of"), "")

    if label == "" and country_lower.startswith("by "):
        label = bys.make_by_label(country_lower)

    if label == "" and " by " in country_lower:
        label = bys.get_by_label(country_lower)

    if separator.lower() == "for":
        label = for_table.get(country_lower, "")

    if label == "" and country_lower.strip().startswith("in "):
        cco2 = country_lower.strip()[len("in ") :].strip()
        cco2_ = get_country(cco2)
        if not cco2_:
            cco2_ = country2_lab.get_lab_for_country2(cco2)
        if cco2_:
            label = f"في {cco2_}"

    if not label:
        label = time_to_arabic.convert_time_to_arabic(country_lower)
    if not label:
        label = te_films(country)
    if not label:
        label = nats_other.find_nat_others(country)
    if not label:
        label = team_work.Get_team_work_Club(country.strip())

    if not label:
        label = Get_c_t_lab(country_lower, separator, start_get_country2=start_get_country2)

    if not label:
        label = tmp_bot.Work_Templates(country_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(country_lower)

    logger.info(f"?????? get_con_lab: {country_lower=}, {label=}")

    return label or ""


__all__ = [
    "get_type_lab",
    "get_con_lab",
    "get_type_country",
]
