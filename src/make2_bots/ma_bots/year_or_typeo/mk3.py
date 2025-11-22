#!/usr/bin/python3
"""
Usage:
"""

import re

from ....helps.log import logger
from ....utils import check_key_in_tables, check_key_in_tables_return_tuple
from ...format_bots import ar_lab_before_year_to_add_in, country_before_year
from ...matables_bots.bot import (
    Add_in_table,
    Films_O_TT,
    Keep_it_frist,
    Table_for_frist_word,
    add_in_to_country,
)
from ...matables_bots.check_bot import check_key_new_players

to_check_them = [Add_in_table, add_in_to_country, Films_O_TT]


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


def add_the_in(in_table, country, arlabel, suf, In, typeo, year_labe, country_label, cat_test):
    """Insert location prepositions into labels when table rules require them."""
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
        logger.info(f">3252 arlabel: {arlabel}")

        # if (typeo == '" and In == "') and (country and year != ""):
    return Add_In_Done, arlabel, cat_test


def added_in_new(country: str, arlabel: str, suf: str, year_labe: str, country_label: str, Add_In: bool, arlabel2: str):
    """Handle cases where a year prefix needs a linking preposition."""
    logger.info("a<<lightblue>>>>>> Add year before")
    co_in_tables = check_key_in_tables(country, to_check_them)
    # co_in_tables = country in Add_in_table or country in add_in_to_country or country in Films_O_TT
    # ANY CHANGES IN FOLOWING LINE MAY BRAKE THE CODE !
    if (suf.strip() == "" and country_label.startswith("ال")) or co_in_tables or check_key_new_players(country.lower()):
        suf = " في "
        logger.info("a<<lightblue>>>>>> Add في to suf")

    logger.info(f'a<<lightblue>>>>>> country_label:{country_label},suf:{suf}:,arlabel2:"{arlabel2}"')

    Add_In_Done = False

    if suf.strip() == "" and year_labe.strip() == arlabel2.strip():
        if Add_In and country_label.strip() in ar_lab_before_year_to_add_in:
            logger.info("ar_lab_before_year_to_add_in Add في to arlabel")
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
        In (str): A string indicating location (e.g., "in", "at").
        country (str): The country name to be checked.
        arlabel (str): The Arabic label to be modified.
        year_labe (str): The label for the year.
        suf (str): A suffix to be added to the label.
        Add_In (bool): A flag indicating whether to add a specific input.
        country_label (str): A resolved label associated with the country.
        Add_In_Done (bool): A flag indicating whether the addition has been completed.

    Returns:
        tuple: A tuple containing the modified `cat_test` and `arlabel`.
    """

    cat_test = cat_test.replace(country, "")

    arlabel = " ".join(arlabel.strip().split())
    suf = f" {suf.strip()} " if suf else " "
    arlabel2 = arlabel

    logger.info(f"{country=}, {Add_In_Done=}, {Add_In=}")
    # ---------------------
    # phase 1
    # ---------------------
    in_table = check_country_in_tables(country)

    Add_In_Done, arlabel, cat_test = add_the_in(in_table, country, arlabel, suf, In, typeo, year_labe, country_label, cat_test)

    logger.info(f"{year_labe=}, {arlabel2=}")

    # ---------------------
    # phase 2
    # ---------------------
    # print(xx)
    if not Add_In_Done:
        if typeo == "" and In == "" and country and year:
            arlabel, Add_In, Add_In_Done = added_in_new(country, arlabel, suf, year_labe, country_label, Add_In, arlabel2)

    arlabel = " ".join(arlabel.strip().split())

    logger.info("------- end --------")
    logger.info(f'a<<lightblue>>>>>> p:{country_label}, year_labe: {year_labe}:, cat:"{category}"')
    logger.info(f'a<<lightblue>>>>>> arlabel  "{arlabel}"')

    return cat_test, arlabel
