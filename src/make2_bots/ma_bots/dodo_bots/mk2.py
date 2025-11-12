#!/usr/bin/python3
"""
Usage:
"""

import re

from ...format_bots import ar_lab_before_year_to_add_in, country_before_year
from ...matables_bots.check_bot import check_key_new_players
from ...matables_bots.bot import (
    Add_to_main2_tab,
    Films_O_TT,
    Table_for_frist_word,
    Add_in_table,
    Keep_it_frist,
    add_in_to_country,
)
from ....utils import check_key_in_tables_return_tuple, check_key_in_tables
from ....helps.print_bot import print_put, output_test


to_check_them = [
    Add_in_table,
    add_in_to_country,
    Films_O_TT
]

to_check_them = [
    [x.lower() for x in Add_in_table],
    [x.lower() for x in add_in_to_country],
    [x.lower() for x in Films_O_TT],
]


def check_country_in_tables(country):

    if country in country_before_year:
        output_test(f'>> >> X:<<lightpurple>> in_table "{country}" in country_before_year.')
        return True

    in_table, table_name = check_key_in_tables_return_tuple(country, Table_for_frist_word)
    if in_table:
        output_test(f'>> >> X:<<lightpurple>> in_table "{country}" in {table_name}.')
        return True

    return False


def add_the_in(country, arlabel, suf, In, typeo, year_labe, con_lab, cat_test):
    Add_In_Done = False
    arlabel2 = arlabel

    in_table = check_country_in_tables(country)

    if in_table and typeo not in Keep_it_frist:
        in_tables = check_key_new_players(country.lower())
        print_put(f"{in_tables=}")
        if not con_lab.startswith("حسب") and year_labe:
            if (In.strip() == "in" or In.strip() == "at") or in_tables:
                con_lab = f"{con_lab} في "
                Add_In_Done = True
                print_put(">>> Add في line: 79")
                cat_test = cat_test.replace(In, "")

        arlabel = con_lab + suf + arlabel
        if arlabel.startswith("حسب"):
            arlabel = arlabel2 + suf + con_lab
        Add_to_main2_tab(In.strip(), "في")
    else:
        if In.strip() == "in" or In.strip() == "at":
            con_lab = f"في {con_lab}"

            cat_test = cat_test.replace(In, "")
            Add_to_main2_tab(In.strip(), "في")
            Add_In_Done = True
            print_put(">>> Add في line: 92")

        arlabel = arlabel + suf + con_lab
        # ---
        arlabel = re.sub(r"\s+", " ", arlabel)
        # ---
        arlabel = arlabel.replace(" في في ", " في ")
        # ---
        print_put(f">3252 arlabel: {arlabel}")

        # if (typeo == '" and In == "') and (country and year != ""):
    return Add_In_Done, arlabel, cat_test


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

    Add_to_main2_tab(country, country_label)
    cat_test = cat_test.replace(country, "")
    arlabel = re.sub(r" ", " ", arlabel)
    con_lab = country_label

    suf = f" {suf.strip()} " if suf else " "

    arlabel2 = arlabel

    print_put(f"{country=}, {Add_In_Done=}, {Add_In=}")

    Add_In_Done, arlabel, cat_test = add_the_in(country, arlabel, suf, In, typeo, year_labe, con_lab, cat_test)

    print_put(f"{year_labe=}, {arlabel2=}")

    if Add_In_Done:
        print_put('------- end --------')
        print_put(f'a<<lightblue>>>>>> p:{country_label}, year_labe: {year_labe}:, cat:"{category}"')
        print_put(f'a<<lightblue>>>>>> arlabel  "{arlabel}"')
        return cat_test, arlabel

    if typeo == "" and In.strip() == "" and country and year:
        print_put("a<<lightblue>>>>>> Add year before")
        # ---
        co_in_tables = check_key_in_tables(country.lower(), to_check_them) or check_key_new_players(country.lower())
        # co_in_tables = country in Add_in_table or country in add_in_to_country or country in Films_O_TT
        # ---
        print(f"{co_in_tables=}")
        # ---
        if (suf.strip() == "" and con_lab.startswith("ال")) or co_in_tables:
            suf = " في "
            print_put("a<<lightblue>>>>>> Add في to suf")
        print_put(f'a<<lightblue>>>>>> con_lab:{con_lab},suf:{suf}:,arlabel2:"{arlabel2}"')

        if suf.strip() == "" and year_labe.strip() == arlabel2.strip():
            if Add_In and con_lab.strip() in ar_lab_before_year_to_add_in:
                print_put("ar_lab_before_year_to_add_in Add في to arlabel")
                suf = " في "
                Add_In = False
                Add_In_Done = True

            elif con_lab.strip().startswith("أعضاء ") and con_lab.find(" حسب ") == -1:
                print_put(">354 Add في to arlabel")
                suf = " في "
                Add_In = False
                Add_In_Done = True

        arlabel = con_lab + suf + arlabel2

        print_put("a<<lightblue>>>3265>>>arlabel = con_lab + suf +  arlabel2")
        print_put(f"a<<lightblue>>>3265>>>{arlabel}")

    print_put('------- end --------')
    print_put(f'a<<lightblue>>>>>> p:{country_label}, year_labe: {year_labe}:, cat:"{category}"')
    print_put(f'a<<lightblue>>>>>> arlabel "{arlabel}"')

    return cat_test, arlabel
