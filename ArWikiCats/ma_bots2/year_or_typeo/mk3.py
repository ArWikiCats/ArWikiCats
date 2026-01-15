#!/usr/bin/python3
"""
Usage:
"""

import re

from ...helps import logger
from ...make_bots.matables_bots.bot import (
    Films_O_TT,
    Table_for_frist_word,
)
from ...make_bots.matables_bots.check_bot import check_key_new_players
from ...make_bots.matables_bots.data import Add_in_table, Keep_it_frist, add_in_to_country
from ...utils import check_key_in_tables_return_tuple

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


ar_label_before_year_to_add_in = [
    # لإضافة "في" بين البداية والسنة في تصنيفات مثل :
    # tab[Category:1900 rugby union tournaments for national teams] = "تصنيف:بطولات اتحاد رجبي للمنتخبات الوطنية 1900"
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رجبي للمنتخبات الوطنية",
]


def check_country_in_tables(country: str) -> bool:
    """Return True when the country appears in any configured lookup table."""
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
    In: str,
    typeo: str,
    year_labe: str,
    country_label: str,
    cat_test: str,
) -> tuple[bool, str, str]:
    """
    Insert location prepositions into labels when table rules require them.
    """
    Add_In_Done = False
    arlabel2 = arlabel

    if in_table and typeo not in Keep_it_frist:
        # in_tables = country.lower() in New_players
        in_tables = check_key_new_players(country.lower())
        # ---
        logger.info(f"{in_tables=}")
        if not country_label.startswith("حسب") and year_labe:
            if (In.strip() == "in" or In.strip() == "at") or in_tables:
                country_label = f"{country_label} في "
                Add_In_Done = True
                logger.info(">>> Add في line: 49")
                cat_test = cat_test.replace(In, "")

        arlabel = country_label + suf + arlabel
        if arlabel.startswith("حسب"):
            arlabel = arlabel2 + suf + country_label
    else:
        if In.strip() == "in" or In.strip() == "at":
            country_label = f"في {country_label}"

            cat_test = cat_test.replace(In, "")
            Add_In_Done = True
            logger.info(">>> Add في line: 59")

        arlabel = arlabel + suf + country_label
        arlabel = re.sub(r"\s+", " ", arlabel)
        arlabel = arlabel.replace(" في في ", " في ")
        logger.info(f">3252 {arlabel=}")

        # if (typeo == '" and In == "') and (country and year != ""):
    return Add_In_Done, arlabel, cat_test


def added_in_new(
    country: str, arlabel: str, suf: str, year_labe: str, country_label: str, Add_In: bool, arlabel2: str
) -> tuple[str, bool, bool]:
    """Handle cases where a year prefix needs a linking preposition."""
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
        suf = " في "
        logger.info("a<<lightblue>>>>>> Add في to suf")

    logger.info(f"a<<lightblue>>>>>> {country_label=}, {suf=}:, {arlabel2=}")

    Add_In_Done = False

    if suf.strip() == "" and year_labe.strip() == arlabel2.strip():
        if Add_In and country_label.strip() in ar_label_before_year_to_add_in:
            logger.info("ar_label_before_year_to_add_in Add في to arlabel")
            suf = " في "
            Add_In = False
            Add_In_Done = True

        elif country_label.strip().startswith("أعضاء ") and country_label.find(" حسب ") == -1:
            logger.info(">354 Add في to arlabel")
            suf = " في "
            Add_In = False
            Add_In_Done = True

    arlabel = country_label + suf + arlabel2

    logger.info("a<<lightblue>>>3265>>>arlabel = country_label + suf +  arlabel2")
    logger.info(f"a<<lightblue>>>3265>>>{arlabel}")

    return arlabel, Add_In, Add_In_Done


def new_func_mk2(
    category: str,
    cat_test: str,
    year: str,
    typeo: str,
    In: str,
    country: str,
    arlabel: str,
    year_labe: str,
    suf: str,
    Add_In: bool,
    country_label: str,
    Add_In_Done: bool,
) -> tuple[str, str]:
    """
    Modify category test and Arabic label according to country, year, and placement rules.
    
    Processes the inputs to remove the country from `cat_test` and to construct or adjust `arlabel` by applying table-driven and context-sensitive rules for inserting linking phrases (e.g., location prepositions) and normalizing whitespace.
    
    Parameters:
        category (str): The category being processed.
        cat_test (str): The category test string; the function will remove occurrences of `country`.
        year (str): The year associated with the category; used to decide year-related insertions.
        typeo (str): A type discriminator that influences placement rules.
        In (str): Location indicator (commonly "in" or "at") that may trigger insertion of linking phrases.
        country (str): Country or domain name to check against lookup tables.
        arlabel (str): The Arabic label to be adjusted and normalized.
        year_labe (str): The year label token used when deciding year-prefix handling.
        suf (str): Suffix text to place between country label and `arlabel` when applicable.
        Add_In (bool): Input flag indicating whether a linking phrase addition is allowed.
        country_label (str): Resolved human-readable label for the country used when composing `arlabel`.
        Add_In_Done (bool): Flag indicating whether a linking insertion has already been performed.
    
    Returns:
        tuple (cat_test, arlabel): Modified `cat_test` with `country` removed and the possibly-updated, whitespace-normalized Arabic label.
    """
    cat_test = cat_test.replace(country, "")

    return cat_test, ""
    arlabel = " ".join(arlabel.strip().split())
    suf = f" {suf.strip()} " if suf else " "
    arlabel2 = arlabel

    logger.info(f"{country=}, {Add_In_Done=}, {Add_In=}")
    # ---------------------
    # phase 1
    # ---------------------
    in_table = check_country_in_tables(country)

    logger.info(f"> new_func_mk2(): {country=}, {in_table=}, {arlabel=}")

    Add_In_Done, arlabel, cat_test = add_the_in(
        in_table, country, arlabel, suf, In, typeo, year_labe, country_label, cat_test
    )

    logger.info(f"> new_func_mk2(): {year_labe=}, {arlabel=}")

    # ---------------------
    # phase 2
    # ---------------------
    # print(xx)
    if not Add_In_Done:
        if typeo == "" and In == "" and country and year:
            arlabel, Add_In, Add_In_Done = added_in_new(
                country, arlabel, suf, year_labe, country_label, Add_In, arlabel2
            )

    arlabel = " ".join(arlabel.strip().split())

    logger.info("------- ")
    logger.info(f"a<<lightblue>>>>>> p:{country_label}, {year_labe=}, {category=}")
    logger.info(f"a<<lightblue>>>>>> {arlabel=}")

    logger.info("------- end > new_func_mk2() < --------")
    return cat_test, arlabel