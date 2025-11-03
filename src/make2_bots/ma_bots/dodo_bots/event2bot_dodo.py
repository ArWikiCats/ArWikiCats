#!/usr/bin/python3
"""
Usage:
from .event2bot_dodo import make_lab_dodo

"""

import re
from ...matables_bots.bot import safo, titttto
from ....fix import fixtitle
from ...date_bots import year_lab
from ...format_bots import Tit_ose_Nmaes, NewFormat
from ....ma_lists import Nat_mens
from ...matables_bots.bot import Add_to_main2_tab
from ...matables_bots.bot import (
    New_Lan,
    Films_O_TT,
    New_players,
    typeTable,
    type_after_contry,
)
from .dodo_2019 import work_2019
from .mk2 import new_func_mk2
from ..contry_bot import Get_contry
from ...matables_bots.bot_2018 import pop_All_2018
from ...reg_lines import tita, tita_year, ddd, tita_year_no_month
from ....helps.print_bot import print_put, output_test

en_literes = "[abcdefghijklmnopqrstuvwxyz]"

tita_other = r"\s*(" + safo + r"|)\s*(" + titttto + r"|)\s*(.*|).*"


def make_lab_dodo(
    _category_: str,
    category3: str,
    category: str,
    cat_test: str,
    category_r: str,
) -> str:
    """
    Generate a label based on various input parameters related to categories
    and years.
    """
    # ---
    Tita_year = tita_year
    # ---
    test_month = re.sub(ddd, "", category.lower())
    # ---
    if test_month == category:
        Tita_year = tita_year_no_month
    # ---
    Add_In_Done = False
    NoLab = False
    # ---
    reg_line_1 = tita + tita_other
    reg_line_1 = reg_line_1.lower()
    # ---
    category2 = category.lower()
    if category2.startswith("category:"):
        category2 = category2[len("category:") :]
    # ---
    year = re.sub(Tita_year, r"\g<1>\g<2>", _category_)
    typeo = re.sub(reg_line_1, r"\g<3>", _category_)
    # ---
    if year == _category_ or year == category3:
        year = ""
    elif year and _category_.startswith("category:" + year):
        cat_test = cat_test.replace(year.lower(), "")
        tita_n = "category:" + year + tita_other
        typeo = re.sub(tita_n, r"\g<1>", _category_)

    if typeo == _category_ or typeo == category3:
        typeo = ""
    # ---
    In = re.sub(reg_line_1, r"\g<4>", _category_)
    # ---
    if In == _category_ or In == category3:
        In = ""
    # ---
    contry = re.sub(reg_line_1, r"\g<5>", _category_)
    # ---
    if contry == _category_ or contry == category3:
        contry = ""

    if In.strip() == "by":
        contry = f"by {contry}"

    contry_not_lower = contry
    contry = contry.lower()
    print_put(f'>>>> year:"{year}", typeo:"{typeo}", In:"{In}", contry:"{contry}"')
    arlabel = ""
    year_labe = ""
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
            Add_to_main2_tab(typeo, typeo_lab)

            print_put("a<<lightblue>>>typeo_lab : %s" % typeo_lab)
            if "s" in typeTable[typeo]:
                suf = typeTable[typeo]["s"]
        else:
            print_put('a<<lightblue>>>>>> typeo "%s" not in typeTable' % typeo)

    cnt_la = ""

    if contry:
        cnt_la = pop_All_2018.get(contry, "")

        if not cnt_la:
            cnt_la = Get_contry(contry_not_lower)

        if cnt_la == "" and category3 == year + " " + contry:
            cnt_la = Nat_mens.get(contry, "")
            if cnt_la:
                cnt_la = cnt_la + " في"
                print_put("a<<lightblue>>>2021 cnt_la == %s" % cnt_la)

        if cnt_la:
            Add_to_main2_tab(contry, cnt_la)
            cat_test = cat_test.lower()
            cat_test = cat_test.replace(contry.lower(), "")
            print_put("a<<lightblue>>>cnt_la : %s" % cnt_la)

    if year:
        year_labe = year_lab.make_year_lab(year)
        if year_labe:
            Add_to_main2_tab(year, year_labe)
            cat_test = cat_test.lower().replace(year.lower(), "")
            arlabel = arlabel + " " + year_labe
            print_put(f'252: year != ""({year}) arlabel:"{arlabel}",In.strip() == "{In.strip()}"')
            if (In.strip() == "in" or In.strip() == "at") and suf.strip() == "":
                print_put('Add في to arlabel:in,at"%s"' % arlabel)
                arlabel = arlabel + " في "
                cat_test = cat_test.replace(In, "")
                Add_In = False
                Add_In_Done = True

    if not (contry != "" and cnt_la == "") and not (year != "" and year_labe == ""):
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

    if (year == "" or year_labe == "") and cat_test.strip():
        NoLab = True
        print_put("year == " ' or year_labe == ""')
    elif contry == "" and In == "":
        print_put('a<<lightblue>>>>>> contry == "" and In ==  "" ')
        arlabel = re.sub(r" ", " ", arlabel)
        if suf:
            arlabel = arlabel + " " + suf
        arlabel = re.sub(r"\s+", " ", arlabel)
        output_test("a<<lightblue>>>>>> No contry.")
    elif contry:
        if cnt_la:
            cat_test, arlabel = new_func_mk2(
                category, cat_test, year, typeo, In, contry, arlabel, year_labe, suf, Add_In, cnt_la, Add_In_Done
            )
        else:
            print_put('a<<lightblue>>>>>> Cant id contry : "%s" ' % contry)
    else:
        print_put("a<<lightblue>>>>>> No label.")
        NoLab = True

    if NoLab and cat_test == "":
        if cnt_la and typeo_lab and year == "" and In == "":
            if typeo in type_after_contry:
                ar = f"{cnt_la} {typeo_lab}"
            elif (typeo in typeTable) or (typeo in Films_O_TT) or (typeo.lower() in New_players):
                ar = f"{typeo_lab} {cnt_la}"
            else:
                ar = f"{cnt_la} {typeo_lab}"
            New_Lan[category_r] = ar
            print_put(f'>>>> <<lightyellow>> typeo_lab:"{typeo_lab}", cnt_la "{cnt_la}"')
            print_put(f'>>>> <<lightyellow>> New_Lan[{category_r}] = "{ar}" ')

    if cat_test != cat_test3:
        output_test('<<lightgreen>>>>>> cat_test : "%s" ' % cat_test)
        output_test("<<lightgreen>>>>>> arlabel " + arlabel)
    if not cat_test.strip():
        output_test("<<lightgreen>>>>>> arlabel " + arlabel)
    elif cat_test == contry.lower() or (cat_test == "in " + contry.lower()):
        output_test("<<lightgreen>>>>>> cat_test False.. ")
        output_test('<<lightblue>>>>>> cat_test = contry : "%s" ' % contry)
        NoLab = True
    elif cat_test.lower() == category2.lower():
        output_test("<<lightblue>>>>>> cat_test = category2 ")
    else:
        output_test("<<lightgreen>>>> >> cat_test False.. ")
        output_test(' cat_test : "%s" ' % cat_test)
        output_test("<<lightgreen>>>>>> arlabel " + arlabel)
        NoLab = True

    if NoLab and year and year_labe:
        formatt = category.lower()
        formatt = re.sub(r"category:", "", formatt)
        formatt = re.sub(r"_", " ", formatt)
        formatt = re.sub(year, "###", formatt)

        if formatt in NewFormat:
            print_put('<<lightgreen>>>>>> formatt:"%s" in NewFormat. ' % formatt)
            NoLab = False
            arlabel = re.sub(r"###", year_labe, NewFormat[formatt])
            print_put('<<lightgreen>>>>>> New formatt lab :"%s" ' % arlabel)

        cat4_lab = work_2019(category3, year, year_labe)
        if cat4_lab:
            New_Lan[category_r] = cat4_lab

    if not NoLab:
        if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) == arlabel:
            arlabel = fixtitle.fixlab(arlabel, en=category_r)
            print_put("a<<lightred>>>>>> arlabel ppoi:%s" % arlabel)
            print_put(f'>>>> <<lightyellow>> cat:"{category_r}", category_lab "{arlabel}"')
            print_put("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
            return arlabel
    return ""
