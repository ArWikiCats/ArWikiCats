#!/usr/bin/python3
"""
Usage:
"""

import re
from typing import Literal

from ...helps import getLogger
from ...translations import Jobs_new
from ...utils import check_key_in_tables_return_tuple
from ..legacy_utils import Add_in_table, Keep_it_frist, add_in_to_country
from ..make_bots import (
    Films_O_TT,
    check_key_new_players,
    players_new_keys,
)

logger = getLogger(__name__)

# Constants for prepositions
PREPOSITION_IN: Literal["in"] = "in"
PREPOSITION_AT: Literal["at"] = "at"
ARABIC_PREPOSITION_FI = " في "

# Lookup tables
Table_for_frist_word = {
    "Films_O_TT": Films_O_TT,
    "New_players": players_new_keys,
    "Jobs_new": Jobs_new,
}

ar_lab_before_year_to_add_in = [
    # لإضافة "في" بين البداية والسنة في تصنيفات مثل :
    # tab[Category:1900 rugby union tournaments for national teams] = "تصنيف:بطولات اتحاد رجبي للمنتخبات الوطنية 1900"
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رجبي للمنتخبات الوطنية",
]

country_before_year = [
    "men's road cycling",
    "women's road cycling",
    "track cycling",
    "motorsport",
    "pseudonymous writers",
    "space",
    "disasters",
    "spaceflight",
    "inventions",
    "sports",
    "introductions",
    "discoveries",
    "comics",
    "nuclear history",
    "military history",
    "military alliances",
]


def check_country_in_tables(country: str) -> bool:
    """
    Determine whether a country key is present in the configured lookup sources.

    Returns:
        True if the country is found in any configured lookup table or the special country-before-year list, False otherwise.
    """
    if country in country_before_year:
        logger.debug(f'>> >> X:<<lightpurple>> in_table "{country}" in country_before_year.')
        return True

    in_table, table_name = check_key_in_tables_return_tuple(country, Table_for_frist_word)
    if in_table:
        logger.debug(f'>> >> X:<<lightpurple>> in_table "{country}" in {table_name}.')
        return True

    return False


def add_the_in(
    in_table: bool,
    country: str,
    arlabel: str,
    suf: str,
    in_str: str,
    typeo: str,
    year_labe: str,
    country_label: str,
    cat_test: str,
) -> tuple[bool, str, str]:
    """
    Decide whether to insert the Arabic preposition " في " into a label and produce the updated label and category text.

    Parameters:
        in_table (bool): True if the country/key is found in configured lookup tables affecting insertion rules.
        country (str): Raw country/key identifier used for membership checks.
        arlabel (str): Current Arabic label to be updated.
        suf (str): Suffix or spacer to place between parts of the label (may be empty or a space-like token).
        in_str (str): Detected English preposition token from the original category (e.g., "in", "at"); used to decide removal from cat_test.
        typeo (str): Category type that can inhibit table-based insertion when present in Keep_it_frist.
        year_labe (str): Year-related portion of the label; used to determine whether insertion is appropriate.
        country_label (str): Human-readable country/location label in Arabic to be combined with arlabel.
        cat_test (str): Category test string from which the matched English preposition may be removed.

    Returns:
        tuple:
            add_in_done (bool): `True` if the Arabic preposition was inserted and the category test adjusted, `False` otherwise.
            arlabel (str): The resulting Arabic label after any insertion and normalization.
            cat_test (str): The possibly modified category test string with the original English preposition removed when applicable.
    """
    add_in_done = False
    arlabel2 = arlabel

    if in_table and typeo not in Keep_it_frist:
        # in_tables = country.lower() in New_players
        in_tables = check_key_new_players(country.lower())
        # ---
        logger.info(f"{in_tables=}")
        if not country_label.startswith("حسب") and year_labe:
            if (in_str.strip() == PREPOSITION_IN or in_str.strip() == PREPOSITION_AT) or in_tables:
                country_label = f"{country_label}{ARABIC_PREPOSITION_FI}"
                add_in_done = True
                logger.info(">>> Add في in add_the_in")
                cat_test = cat_test.replace(in_str, "")

        arlabel = country_label + suf + arlabel
        if arlabel.startswith("حسب"):
            arlabel = arlabel2 + suf + country_label
    else:
        if in_str.strip() == PREPOSITION_IN or in_str.strip() == PREPOSITION_AT:
            country_label = f"{ARABIC_PREPOSITION_FI}{country_label}"

            cat_test = cat_test.replace(in_str, "")
            add_in_done = True
            logger.info(">>> Add في in else branch")

        arlabel = arlabel + suf + country_label
        arlabel = re.sub(r"\s+", " ", arlabel)
        arlabel = arlabel.replace(f"{ARABIC_PREPOSITION_FI}{ARABIC_PREPOSITION_FI}", ARABIC_PREPOSITION_FI)
        logger.info(f">3252 {arlabel=}")

    return add_in_done, arlabel, cat_test


def added_in_new(
    country: str,
    arlabel: str,
    suf: str,
    year_labe: str,
    country_label: str,
    add_in: bool,
    arlabel2: str,
) -> tuple[str, bool, bool]:
    """
    Decide whether to insert the Arabic preposition "في" between a country label and a year-related label and build the resulting Arabic label.

    This function sets `suf` to " في " when the country requires a linking preposition (determined by the country label form, membership in configured tables, or presence in a new-players list). If `suf` is still empty and the year label equals `arlabel2`, it may also insert " في " for specific country-label patterns (entries listed in `ar_lab_before_year_to_add_in` or labels starting with "أعضاء " that do not contain " حسب "). The final `arlabel` is constructed as `country_label + suf + arlabel2`.

    Parameters:
        country: Country key used for table membership checks.
        arlabel: Current Arabic label (unused for logic but part of the calling context).
        suf: Current suffix/preposition string (may be modified to " في ").
        year_labe: Year-related label used to compare against `arlabel2`.
        country_label: Human-readable Arabic country/location label to prepend.
        add_in: Flag indicating whether a preposition addition is still allowed; may be cleared by this function.
        arlabel2: The label part that typically represents the year or right-hand segment to be joined.

    Returns:
        tuple[str, bool, bool]:
            arlabel: Updated Arabic label resulting from concatenating `country_label`, `suf`, and `arlabel2`.
            add_in: Updated flag; cleared (`false`) if this call performed the insertion that consumes the addition permission.
            add_in_done: `true` if this function added " في ", `false` otherwise.
    """
    logger.info("a<<lightblue>>>>>> Add year before")

    to_check_them_tuble = {
        "Add_in_table": Add_in_table,
        "add_in_to_country": add_in_to_country,
        "Films_O_TT": Films_O_TT,
    }

    co_in_tables, tab_name = check_key_in_tables_return_tuple(country, to_check_them_tuble)
    # co_in_tables = country in Add_in_table or country in add_in_to_country or country in Films_O_TT

    # ANY CHANGES IN FOLOWING LINE MAY BRAKE THE CODE !

    if (suf.strip() == "" and country_label.startswith("ال")) or co_in_tables or check_key_new_players(country.lower()):
        suf = ARABIC_PREPOSITION_FI
        logger.info("a<<lightblue>>>>>> Add في to suf")

    logger.info(f"a<<lightblue>>>>>> {country_label=}, {suf=}:, {arlabel2=}")

    add_in_done = False

    if suf.strip() == "" and year_labe.strip() == arlabel2.strip():
        if add_in and country_label.strip() in ar_lab_before_year_to_add_in:
            logger.info("ar_lab_before_year_to_add_in Add في to arlabel")
            suf = ARABIC_PREPOSITION_FI
            add_in = False
            add_in_done = True

        elif country_label.strip().startswith("أعضاء ") and country_label.find(" حسب ") == -1:
            logger.info(">354 Add في to arlabel")
            suf = ARABIC_PREPOSITION_FI
            add_in = False
            add_in_done = True

    arlabel = country_label + suf + arlabel2

    logger.info("a<<lightblue>>>3265>>>arlabel = country_label + suf +  arlabel2")
    logger.info(f"a<<lightblue>>>3265>>>{arlabel}")

    return arlabel, add_in, add_in_done


def new_func_mk2(
    category: str,
    cat_test: str,
    year: str,
    typeo: str,
    in_str: str,
    country: str,
    arlabel: str,
    year_labe: str,
    suf: str,
    add_in: bool,
    country_label: str,
    add_in_done: bool,
) -> tuple[str, str]:
    """Process and modify category-related labels based on various conditions.

    This function takes multiple parameters related to categories and
    modifies the `cat_test` and `arlabel` based on the presence of the
    country in predefined tables, the type of input, and other conditions.
    It also handles specific formatting for the labels and manages the
    addition of certain phrases based on the context. The function performs
    checks against lists of countries and predefined rules to determine how
    to construct the final output labels.

    Args:
        category (str): The category to be processed.
        cat_test (str): The test string for the category.
        year (str): The year associated with the category.
        typeo (str): The type of input being processed.
        in_str (str): A string indicating location (e.g., "in", "at").
        country (str): The country name to be checked.
        arlabel (str): The Arabic label to be modified.
        year_labe (str): The label for the year.
        suf (str): A suffix to be added to the label.
        add_in (bool): A flag indicating whether to add a specific input.
        country_label (str): A resolved label associated with the country.
        add_in_done (bool): A flag indicating whether the addition has been completed.

    Returns:
        tuple: A tuple containing the modified `cat_test` and `arlabel`.
    """

    cat_test = cat_test.replace(country, "")

    arlabel = " ".join(arlabel.strip().split())
    suf = f" {suf.strip()} " if suf else " "
    arlabel2 = arlabel

    logger.info(f"{country=}, {add_in_done=}, {add_in=}")
    # ---------------------
    # phase 1
    # ---------------------
    in_table = check_country_in_tables(country)

    logger.info(f"> new_func_mk2(): {country=}, {in_table=}, {arlabel=}")

    add_in_done, arlabel, cat_test = add_the_in(
        in_table, country, arlabel, suf, in_str, typeo, year_labe, country_label, cat_test
    )

    logger.info(f"> new_func_mk2(): {year_labe=}, {arlabel=}")

    # ---------------------
    # phase 2
    # ---------------------
    # print(xx)
    if not add_in_done:
        if typeo == "" and in_str == "" and country and year:
            arlabel, add_in, add_in_done = added_in_new(
                country, arlabel, suf, year_labe, country_label, add_in, arlabel2
            )

    arlabel = " ".join(arlabel.strip().split())

    logger.info("------- ")
    logger.info(f"a<<lightblue>>>>>> p:{country_label}, {year_labe=}, {category=}")
    logger.info(f"a<<lightblue>>>>>> {arlabel=}")

    logger.info("------- end > new_func_mk2() < --------")
    return cat_test, arlabel
