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
    pop_of_without_in,
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

separators_lists_raw = [
    "in",
    "from",
    "at",
    "by",
    "of",
]


def separator_lists_fixing(type_label: str, separator_stripped: str, type_lower: str) -> str:
    """
    {"type_label": "منشآت عسكرية", "separator_stripped": "in", "type_lower": "military installations", "output": "منشآت عسكرية في"}
    """
    if separator_stripped in separators_lists_raw:
        if separator_stripped == "in" or " in" in type_lower:
            if type_lower in pop_of_without_in:
                logger.info(f'>>-- Skip aAdd في to {type_label=}, "{type_lower}"')
            else:
                if " في" not in type_label and " in" in type_lower:
                    logger.info(f'>>-- aAdd في to type_label:in"{type_label}", for "{type_lower}"')
                    type_label = type_label + " في"
                elif separator_stripped == "in" and " in" in type_lower:
                    logger.info(f'>>>> aAdd في to type_label:in"{type_label}", for "{type_lower}"')
                    type_label = type_label + " في"

        elif (separator_stripped == "at" or " at" in type_lower) and (" في" not in type_label):
            logger.info('>>>> Add في to type_label:at"%s"' % type_label)
            type_label = type_label + " في"

    return type_label


def get_type_country(category: str, separator: str) -> Tuple[str, str]:
    """Extract the type and country from a given category string.

    This function takes a category string and a delimiter (separator) to split
    the category into a type and a country. It processes the strings to
    ensure proper formatting and handles specific cases based on the value
    of separator. The function also performs some cleanup on the extracted
    strings to remove any unwanted characters or formatting issues.

    Args:
        category (str): The category string containing type and country information.
        separator (str): The delimiter used to separate the type and country in the category
            string.

    Returns:
        tuple: A tuple containing the processed type (str) and country (str).

    """
    category_type, country = "", ""
    if separator and separator in category:
        parts = category.split(separator, 1)
        category_type = parts[0]
        country = parts[1] if len(parts) > 1 else ""
    else:
        category_type = category

    country = country.lower()

    # Attempt to clean up using regex
    # Escape separator to prevent regex errors if it contains special chars
    separator_escaped = re.escape(separator) if separator else ""
    mash_pattern = f"^(.*?)(?:{separator_escaped}?)(.*?)$"

    test_remainder = category.lower()
    type_regex, country_regex = "", ""

    try:
        type_regex = re.sub(mash_pattern, r"\g<1>", category.lower())
        country_regex = re.sub(mash_pattern, r"\g<2>", category.lower())

        # Remove extracted parts from the test string to see what's left
        test_remainder = re.sub(re.escape(category_type.lower()), "", test_remainder)
        test_remainder = re.sub(re.escape(country.lower()), "", test_remainder)

    except Exception as e:
        logger.info(f"<<lightred>>>>>> except test_remainder: {e}")

    test_remainder = test_remainder.strip()
    separator_stripped = separator.strip()

    # Adjustments based on separator
    if separator_stripped == "in" and category_type.endswith(" playerss"):
        category_type = category_type.replace(" playerss", " players")

    separator_ends = f" {separator_stripped}"
    separator_starts = f"{separator_stripped} "

    if separator_stripped == "of" and not category_type.endswith(separator_ends):
        category_type = f"{category_type} of"
    elif separator_stripped == "spies for" and not category_type.endswith(" spies"):
        category_type = f"{category_type} spies"

    elif separator_stripped == "by" and not country.startswith(separator_starts):
        country = f"by {country}"
    elif separator_stripped == "for" and not country.startswith(separator_starts):
        country = f"for {country}"

    logger.info(f'>xx>>> category_type: "{category_type.strip()}", country: "{country.strip()}", {separator=} ')

    if not test_remainder or test_remainder == separator_stripped:
        logger.info(f'>>>> {test_remainder=} == separator')
        return category_type, country

    logger.info(
        f'>>>> test_remainder != "", {type_regex=}, {separator=}, {country_regex=} '
    )

    if separator_stripped == "of" and not type_regex.endswith(separator_ends):
        type_regex = f"{type_regex} of"

    elif separator_stripped == "by" and not country_regex.startswith(separator_starts):
        country_regex = f"by {country_regex}"

    elif separator_stripped == "for" and not country_regex.startswith(separator_starts):
        country_regex = f"for {country_regex}"

    category_type = type_regex
    country = country_regex

    logger.info(f'>>>> yementest: {type_regex=}, {country_regex=}')

    return category_type, country


def get_type_lab(preposition: str, type_value: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters.

    Args:
        preposition (str): The preposition/delimiter (separator).
        type_value (str): The type part of the category.

    Returns:
        Tuple[str, bool]: The label and a boolean indicating if 'in' should be appended.
    """
    normalized_preposition = preposition.strip()
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


def get_con_lab(preposition: str, country: str, start_get_country2: bool = False) -> str:
    """Retrieve the corresponding label for a given country.

    Args:
        preposition (str): The preposition/delimiter.
        country (str): The country part of the category.
        start_get_country2 (bool): Whether to use the secondary country lookup.

    Returns:
        str: The Arabic label for the country.
    """
    preposition = preposition.strip()
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

    if preposition.lower() == "for":
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
        label = Get_c_t_lab(country_lower, preposition, start_get_country2=start_get_country2)

    if not label:
        label = tmp_bot.Work_Templates(country_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(country_lower)

    logger.info(f"?????? get_con_lab: {country_lower=}, {label=}")

    return label or ""


def add_in_tab(type_label: str, type_lower: str, separator_stripped: str) -> str:
    """Add 'من' (from) to the label if conditions are met.

    Args:
        type_label (str): The current Arabic label for the type.
        type_lower (str): The lowercase type string.
        separator_stripped (str): The stripped delimiter.

    Returns:
        str: The modified type label.
    """
    ty_in18 = get_pop_All_18(type_lower)

    if separator_stripped == "from":
        if not type_label.strip().endswith(" من"):
            logger.info(f">>>> nAdd من to type_label '{type_label}' line:44")
            type_label = f"{type_label} من "
        return type_label

    if not ty_in18 or not type_lower.endswith(" of") or " في" in type_label:
        return type_label

    type_lower_prefix = type_lower[: -len(" of")]
    in_tables = check_key_new_players(type_lower)
    in_tables2 = check_key_new_players(type_lower_prefix)

    if in_tables or in_tables2:
        logger.info(f">>>> nAdd من to type_label '{type_label}' line:59")
        type_label = f"{type_label} من "

    return type_label


__all__ = [
    "add_in_tab",
    "get_type_lab",
    "get_con_lab",
    "get_type_country",
    "separator_lists_fixing",
]
