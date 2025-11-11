#!/usr/bin/python3
"""
Usage:
from .mk2 import new_func_mk2
# cat_test, arlabel = new_func_mk2(category, cat_test, year, typeo, In, contry, arlabel, year_labe, suf, Add_In, country_label, Add_In_Done)

"""

import re

from ...format_bots import ar_lab_before_year_to_add_in, contry_before_year
from ...matables_bots.bot import (
    Add_to_main2_tab,
    Films_O_TT,
    New_players,
    Table_for_frist_word,
    Add_in_table,
    Keep_it_frist,
    add_in_to_contry,
)
from ....helps.print_bot import print_put, output_test


def new_func_mk2(
    category: str,
    cat_test: str,
    year: str,
    typeo: str,
    In: str,
    contry: str,
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
        contry (str): The country name to be checked.
        arlabel (str): The Arabic label to be modified.
        year_labe (str): The label for the year.
        suf (str): A suffix to be added to the label.
        Add_In (bool): A flag indicating whether to add a specific input.
        country_label (str): A resolved label associated with the country.
        Add_In_Done (bool): A flag indicating whether the addition has been completed.

    Returns:
        tuple: A tuple containing the modified `cat_test` and `arlabel`.
    """

    Add_to_main2_tab(contry, country_label)
    cat_test = cat_test.replace(contry, "")
    arlabel = re.sub(r" ", " ", arlabel)
    con_lab = country_label
    Contry_In_Table = False
    for table in Table_for_frist_word.keys():
        if contry in Table_for_frist_word[table]:
            Contry_In_Table = True
            output_test(f'>> >> dX:<<lightpurple>> Contry_In_Table "{contry}" in {table}.')

    if contry in contry_before_year:
        Contry_In_Table = True
        output_test(f'>> >> X:<<lightpurple>> Contry_In_Table "{contry}" in contry_before_year.')

    if suf:
        suf = f" {suf.strip()} "
    else:
        suf = " "

    arlabel2 = arlabel

    if Contry_In_Table and typeo not in Keep_it_frist:
        if (In.strip() == "in" or In.strip() == "at") or (contry.lower() in New_players) and not con_lab.startswith("حسب"):
            if year_labe:
                con_lab = f"{con_lab} في "
                Add_In_Done = True
                output_test(">>> Add في line: 1010")
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

        arlabel = arlabel + suf + con_lab
        # ---
        arlabel = re.sub(r"\s+", " ", arlabel)
        # ---
        arlabel = arlabel.replace(" في في ", " في ")
        # ---
        print_put(f">3252 arlabel: {arlabel}")

        # if (typeo == '" and In == "') and (contry and year != ""):

    print_put(f"{year_labe=}, {arlabel2=}")

    if (typeo == "" and In == "") and (contry and year != ""):
        print_put("a<<lightblue>>>>>> Add year before")
        if (suf.strip() == "" and con_lab.startswith("ال")) or contry in Add_in_table or (contry and year and In == "" and typeo == "" and contry in add_in_to_contry) or contry in Films_O_TT:
            suf = " في "
            print_put("a<<lightblue>>>>>> Add في to suf")
        print_put(f'a<<lightblue>>>>>> con_lab:{con_lab},suf:{suf}:,arlabel2:"{arlabel2}"')

        if not Add_In_Done and In.strip() == "" and suf.strip() == "" and year_labe.strip() == arlabel2.strip():
            if Add_In and con_lab.strip() in ar_lab_before_year_to_add_in:
                print_put("ar_lab_before_year_to_add_in Add في to arlabel")
                suf = " في "
                Add_In = False
                Add_In_Done = True

            elif con_lab.strip().startswith("أعضاء ") and " حسب " not in con_lab:
                print_put(">354 Add في to arlabel")
                suf = " في "
                Add_In = False
                Add_In_Done = True

        arlabel = con_lab + suf + arlabel2

        print_put("a<<lightblue>>>3265>>>arlabel = con_lab + suf +  arlabel2")
        print_put(f"a<<lightblue>>>3265>>>{arlabel}")

    print_put(f'a<<lightblue>>>>>> p:{country_label}, year_labe: {year_labe}:, cat:"{category}"')
    print_put(f'a<<lightblue>>>>>> arlabel  "{arlabel}"')

    return cat_test, arlabel
