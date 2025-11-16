#!/usr/bin/python3
"""
Usage:
from .bot_lab import label_for_startwith_year_or_typeo

"""

import re
from ....fix import fixtitle
from ....helps.log import logger
from ....ma_lists import Nat_mens, typeTable
from ....utils import check_key_in_tables
from ...date_bots import year_lab
from ...format_bots import category_relation_mapping
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.bot import New_Lan, Films_O_TT
from ...matables_bots.check_bot import check_key_new_players
from ..country_bot import get_country
from .dodo_2019 import work_2019
from .mk3 import new_func_mk2
from .reg_result import get_reg_result, get_cats

type_after_country = ["non-combat"]


def get_country_label(country_lower, country_not_lower, cate3, compare_lab):
    country_label = ""

    if country_lower:
        country_label = get_pop_All_18(country_lower, "")

        if not country_label:
            country_label = get_country(country_not_lower)

        if country_label == "" and cate3 == compare_lab:
            country_label = Nat_mens.get(country_lower, "")
            if country_label:
                country_label = country_label + " في"
                logger.info("a<<lightblue>>>2021 cnt_la == %s" % country_label)

    return country_label


def do_ar(typeo, country_label, typeo_lab, category_r):

    in_tables_lowers = check_key_new_players(typeo.lower())
    in_tables = check_key_in_tables(typeo, [Films_O_TT, typeTable])

    if typeo in type_after_country:
        ar = f"{country_label} {typeo_lab}"
    elif in_tables or in_tables_lowers:
        ar = f"{typeo_lab} {country_label}"
    else:
        ar = f"{country_label} {typeo_lab}"

    New_Lan[category_r.lower()] = ar

    logger.info(f'>>>> <<lightyellow>> typeo_lab:"{typeo_lab}", cnt_la "{country_label}"')
    logger.info(f'>>>> <<lightyellow>> New_Lan[{category_r}] = "{ar}" ')


def replace_cat_test(cat_test, text):
    cat_test = cat_test.lower().replace(text.lower().strip(), "")
    return cat_test


def label_for_startwith_year_or_typeo(category_r: str) -> str:
    """
    Generate a label based on various input parameters related to categories and years.
    """

    # --- Step 0: Extract parsing results ---
    cate, cate3 = get_cats(category_r)
    result = get_reg_result(category_r)

    year_at_first = result.year_at_first
    typeo = result.typeo
    In = result.In
    country = result.country
    cat_test = result.cat_test

    # Paralympic competitors for Cape Verde (no year_at_first)
    if not year_at_first and not typeo:  # and not country:
        return ""

    country_lower = country.lower()
    country_not_lower = country

    logger.info(f'>>>> year_at_first:"{year_at_first}", typeo:"{typeo}", In:"{In}", country_lower:"{country_lower}"')

    # Working variables
    arlabel = ""
    suf = ""
    typeo_lab = ""
    Add_In = True
    Add_In_Done = False

    # --- Step 1: Handle type label ---
    if typeo:
        if typeo in typeTable:
            typeo_lab = typeTable[typeo]["ar"]
            logger.info('a<<lightblue>>>>>> typeo "{}" in typeTable "{}"'.format(typeo, typeTable[typeo]["ar"]))
            cat_test = replace_cat_test(cat_test, typeo)

            # Fix special case for sports events
            if typeo in ("sports events", "sorts-events") and year_at_first:
                typeo_lab = "أحداث"
            arlabel += typeo_lab

            logger.info("a<<lightblue>>>typeo_lab : %s" % typeo_lab)
            if "s" in typeTable[typeo]:
                suf = typeTable[typeo]["s"]
        else:
            logger.info(f'a<<lightblue>>>>>> typeo "{typeo}" not in typeTable')

    # --- Step 2: Country label ---
    country_label = get_country_label(
        country_lower,
        country_not_lower,
        cate3,
        year_at_first + " " + country_lower
    )

    if country_label:
        cat_test = replace_cat_test(cat_test, country_lower)
        logger.info("a<<lightblue>>>cnt_la : %s" % country_label)

    # --- Step 3: Year label ---
    year_labe = ""
    if year_at_first:
        year_labe = year_lab.make_year_lab(year_at_first)

        if year_labe:
            cat_test = replace_cat_test(cat_test, year_at_first)
            arlabel += " " + year_labe
            logger.info(f'252: year_at_first({year_at_first}) != "" arlabel:"{arlabel}",In.strip() == "{In.strip()}"')

            # If In is 'in' or 'at' and no suffix
            if (In.strip() in ("in", "at")) and not suf.strip():
                logger.info('Add في to arlabel:in,at"%s"' % arlabel)
                arlabel += " في "
                cat_test = replace_cat_test(cat_test, In)
                Add_In = False
                Add_In_Done = True

    # --- Step 4: Validate cat_test for category_relation_mapping ---
    if In.strip():
        if In.strip() in category_relation_mapping:
            if category_relation_mapping[In.strip()].strip() in arlabel:
                cat_test = replace_cat_test(cat_test, In)
        else:
            cat_test = replace_cat_test(cat_test, In)

    cat_test = re.sub(r"category:", "", cat_test)
    logger.debug(f'<<lightblue>>>>>> cat_test: "{cat_test}" ')

    # cat_test_original = cat_test
    NoLab = False

    # --- Step 5: Labeling rules ---
    if (not year_at_first or not year_labe) and cat_test.strip():
        NoLab = True
        logger.info("year_at_first == " ' or year_labe == ""')
    elif not country_lower and not In:
        logger.info('a<<lightblue>>>>>> country_lower == "" and In ==  "" ')
        if suf:
            arlabel = arlabel + " " + suf
        arlabel = re.sub(r"\s+", " ", arlabel)
        logger.debug("a<<lightblue>>>>>> No country_lower.")
    elif country_lower:
        if country_label:
            cat_test, arlabel = new_func_mk2(
                cate, cat_test, year_at_first, typeo, In,
                country_lower, arlabel, year_labe, suf,
                Add_In, country_label, Add_In_Done
            )
        else:
            logger.info('a<<lightblue>>>>>> Cant id country_lower : "%s" ' % country_lower)
            NoLab = True
    else:
        logger.info("a<<lightblue>>>>>> No label.")
        NoLab = True

    # --- Step 6: Fallback rule ---
    if NoLab and cat_test == "":
        if country_label and typeo_lab and not year_at_first and In == "":
            do_ar(typeo, country_label, typeo_lab, category_r)

    # --- Step 7: Final cleanup ---
    category2 = cate[len("category:"):].lower() if cate.lower().startswith("category:") else cate.lower()

    if not cat_test.strip():
        logger.debug("<<lightgreen>>>>>> arlabel " + arlabel)
    elif cat_test == country_lower or cat_test == ("in " + country_lower):
        logger.debug("<<lightgreen>>>>>> cat_test False.. ")
        logger.debug('<<lightblue>>>>>> cat_test = country_lower : "%s" ' % country_lower)
        NoLab = True
    elif cat_test.lower() == category2.lower():
        logger.debug("<<lightblue>>>>>> cat_test = category2 ")
    else:
        logger.debug("<<lightgreen>>>> >> cat_test False result.. ")
        logger.debug(' cat_test : "%s" ' % cat_test)
        logger.debug("<<lightgreen>>>>>> arlabel " + arlabel)
        NoLab = True

    logger.debug("<<lightgreen>>>>>> arlabel " + arlabel)

    # --- Step 8: Special 2019 handler ---
    cat4_lab = work_2019(cate3, year_at_first, year_labe) if year_at_first and year_labe else ""

    if NoLab and year_at_first and year_labe:
        if cat4_lab:
            New_Lan[category_r.lower()] = cat4_lab

    # --- Step 9: Return final result ---
    if not NoLab:
        if re.sub("[abcdefghijklmnopqrstuvwxyz]", "", arlabel, flags=re.IGNORECASE) == arlabel:
            arlabel = fixtitle.fixlab(arlabel, en=category_r)
            logger.info("a<<lightred>>>>>> arlabel ppoi:%s" % arlabel)
            logger.info(f'>>>> <<lightyellow>> cat:"{category_r}", category_lab "{arlabel}"')
            logger.info("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
            return arlabel

    return ""
