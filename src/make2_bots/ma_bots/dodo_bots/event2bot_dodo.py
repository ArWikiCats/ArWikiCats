#!/usr/bin/python3
"""
Usage:
from .event2bot_dodo import make_lab_dodo

"""

import re
from ....fix import fixtitle
from ...date_bots import year_lab
from ...format_bots import Tit_ose_Nmaes
from ....ma_lists import Nat_mens, typeTable
from ...matables_bots.bot import (
    New_Lan,
    Films_O_TT,
)
from ...matables_bots.check_bot import check_key_new_players
from .dodo_2019 import work_2019
from .mk3 import new_func_mk2
from ..country_bot import get_country
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ....helps.print_bot import print_put, output_test
from ....utils import check_key_in_tables
from .reg_result import get_reg_result, get_cats

en_literes = "[abcdefghijklmnopqrstuvwxyz]"

type_after_country = ["non-combat"]


def make_lab_dodo(
    category_r: str,
) -> str:
    """
    Generate a label based on various input parameters related to categories
    and years.
    """
    # ---
    cate, cate3 = get_cats(category_r)
    # ---
    cat_test = cate3
    # ---
    result = get_reg_result(category_r)
    # ---
    year = result.year
    typeo = result.typeo
    In = result.In
    country = result.country
    cat_test = result.cat_test
    # ---
    country_not_lower = country
    country_lower = country.lower()
    # ---
    print_put(f'>>>> year:"{year}", typeo:"{typeo}", In:"{In}", country_lower:"{country_lower}"')
    # ---
    arlabel = ""
    suf = ""
    typeo_lab = ""

    Add_In = True
    if typeo:
        if typeo in typeTable:
            print_put('a<<lightblue>>>>>> typeo "{}" in typeTable "{}"'.format(typeo, typeTable[typeo]["ar"]))
            cat_test = cat_test.replace(typeo.lower(), "")
            typeo_lab = typeTable[typeo]["ar"]
            if (typeo == "sports events" or typeo == "sorts-events") and year:
                typeo_lab = "أحداث"
            arlabel = arlabel + typeo_lab

            print_put("a<<lightblue>>>typeo_lab : %s" % typeo_lab)
            if "s" in typeTable[typeo]:
                suf = typeTable[typeo]["s"]
        else:
            print_put('a<<lightblue>>>>>> typeo "%s" not in typeTable' % typeo)

    country_label = ""

    if country_lower:
        country_label = get_pop_All_18(country_lower, "")

        if not country_label:
            country_label = get_country(country_not_lower)

        if country_label == "" and cate3 == year + " " + country_lower:
            country_label = Nat_mens.get(country_lower, "")
            if country_label:
                country_label = country_label + " في"
                print_put("a<<lightblue>>>2021 cnt_la == %s" % country_label)

        if country_label:
            cat_test = cat_test.lower()
            cat_test = cat_test.replace(country_lower.lower(), "")
            print_put("a<<lightblue>>>cnt_la : %s" % country_label)

    Add_In_Done = False
    year_labe = ""
    if year:
        year_labe = year_lab.make_year_lab(year)
        if year_labe:
            cat_test = cat_test.lower().replace(year.lower(), "")
            arlabel = arlabel + " " + year_labe
            print_put(f'252: year != ""({year}) arlabel:"{arlabel}",In.strip() == "{In.strip()}"')
            if (In.strip() == "in" or In.strip() == "at") and suf.strip() == "":
                print_put('Add في to arlabel:in,at"%s"' % arlabel)
                arlabel = arlabel + " في "
                cat_test = cat_test.replace(In, "")
                Add_In = False
                Add_In_Done = True

    if not (country_lower != "" and country_label == "") and not (year != "" and year_labe == ""):
        if not (typeo != "" and typeo_lab == ""):
            if In.strip():
                if In.strip() in Tit_ose_Nmaes and Tit_ose_Nmaes[In.strip()].strip() in arlabel:
                    cat_test = cat_test.replace(In.strip(), "")
                else:
                    print_put('<<lightred>>>>>> In in Tit_ose_Nmaes, and arlabel wothout "%s" ' % Tit_ose_Nmaes[In.strip()])
            else:
                cat_test = cat_test.replace(In.strip(), "")

    cat_test = re.sub(r"category:", "", cat_test)
    output_test('<<lightblue>>>>>> cat_test, : "%s" ' % cat_test)
    cat_test3 = cat_test

    NoLab = False
    # ---
    if (year == "" or year_labe == "") and cat_test.strip():
        NoLab = True
        print_put("year == " ' or year_labe == ""')
    elif country_lower == "" and In == "":
        print_put('a<<lightblue>>>>>> country_lower == "" and In ==  "" ')
        arlabel = re.sub(r" ", " ", arlabel)
        if suf:
            arlabel = arlabel + " " + suf
        arlabel = re.sub(r"\s+", " ", arlabel)
        output_test("a<<lightblue>>>>>> No country_lower.")
    elif country_lower:
        if country_label:
            cat_test, arlabel = new_func_mk2(
                cate,
                cat_test,
                year,
                typeo,
                In,
                country_lower,
                arlabel,
                year_labe,
                suf,
                Add_In,
                country_label,
                Add_In_Done,
            )
        else:
            print_put('a<<lightblue>>>>>> Cant id country_lower : "%s" ' % country_lower)
    else:
        print_put("a<<lightblue>>>>>> No label.")
        NoLab = True

    if NoLab and cat_test == "":
        if country_label and typeo_lab and year == "" and In == "":
            # ---
            in_tables_lowers = check_key_new_players(typeo.lower())
            in_tables = check_key_in_tables(typeo, [Films_O_TT, typeTable])
            # ---
            if typeo in type_after_country:
                ar = f"{country_label} {typeo_lab}"
            elif in_tables or in_tables_lowers:
                ar = f"{typeo_lab} {country_label}"
            else:
                ar = f"{country_label} {typeo_lab}"
            # ---
            New_Lan[category_r.lower()] = ar
            print_put(f'>>>> <<lightyellow>> typeo_lab:"{typeo_lab}", cnt_la "{country_label}"')
            print_put(f'>>>> <<lightyellow>> New_Lan[{category_r}] = "{ar}" ')

    category2 = cate[len("category:") :] if cate.lower().startswith("category:") else cate
    category2 = category2.lower()

    if cat_test != cat_test3:
        output_test('<<lightgreen>>>>>> cat_test : "%s" ' % cat_test)
        output_test("<<lightgreen>>>>>> arlabel " + arlabel)
    if not cat_test.strip():
        output_test("<<lightgreen>>>>>> arlabel " + arlabel)
    elif cat_test == country_lower or (cat_test == "in " + country_lower):
        output_test("<<lightgreen>>>>>> cat_test False.. ")
        output_test('<<lightblue>>>>>> cat_test = country_lower : "%s" ' % country_lower)
        NoLab = True
    elif cat_test.lower() == category2.lower():
        output_test("<<lightblue>>>>>> cat_test = category2 ")
    else:
        output_test("<<lightgreen>>>> >> cat_test False.. ")
        output_test(' cat_test : "%s" ' % cat_test)
        output_test("<<lightgreen>>>>>> arlabel " + arlabel)
        NoLab = True

    cat4_lab = work_2019(cate3, year, year_labe) if year and year_labe else ""

    if NoLab and year and year_labe:
        # cat4_lab = work_2019(cate3, year, year_labe)
        if cat4_lab:
            New_Lan[category_r.lower()] = cat4_lab

    if not NoLab:
        if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) == arlabel:
            arlabel = fixtitle.fixlab(arlabel, en=category_r)
            print_put("a<<lightred>>>>>> arlabel ppoi:%s" % arlabel)
            print_put(f'>>>> <<lightyellow>> cat:"{category_r}", category_lab "{arlabel}"')
            print_put("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
            return arlabel
    return ""
