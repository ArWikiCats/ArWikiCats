#!/usr/bin/python3
"""
!
Module for Arabic label generation.
"""

import functools
from dataclasses import dataclass
import re
from typing import Tuple

from ...helps.log import logger
from ...main_processers import event2bot
from ...translations import (
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    New_P17_Finall,
    pf_keys2,
    pop_of_without_in,
)
from ...utils import check_key_in_tables_return_tuple, fix_minor
from .. import tmp_bot
from ..date_bots import year_lab
from ..format_bots import (
    Dont_Add_min,
    Tabl_with_in,
    category_relation_mapping,
    for_table,
    pop_format,
    pop_format2,
    pop_format33,
)
from ..jobs_bots.te4_bots.t4_2018_jobs import te4_2018_Jobs
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.bot import (
    Add_ar_in,
    Keep_it_frist,
    Keep_it_last,
    Table_for_frist_word,
)
from ..matables_bots.check_bot import check_key_new_players
from ..media_bots.films_bot import te_films
from ..o_bots import bys
from ..o_bots.popl import make_people_lab
from ..p17_bots import nats
from ..sports_bots import team_work
from . import country2_lab
from .country_bot import Get_c_t_lab, get_country
from ...helps.jsonl_dump import dump_data, save

TITO_LIST_S = [
    "in",
    "from",
    "at",
    "by",
    "of",
]


@dump_data()
@functools.lru_cache(maxsize=10000)
def wrap_event2(category: str, tito: str="") -> str:
    return event2bot.event2(category)


def get_type_country(category: str, tito: str) -> Tuple[str, str]:
    """Extract the type and country from a given category string.

    This function takes a category string and a delimiter (tito) to split
    the category into a type and a country. It processes the strings to
    ensure proper formatting and handles specific cases based on the value
    of tito. The function also performs some cleanup on the extracted
    strings to remove any unwanted characters or formatting issues.

    Args:
        category (str): The category string containing type and country information.
        tito (str): The delimiter used to separate the type and country in the category
            string.

    Returns:
        tuple: A tuple containing the processed type (str) and country (str).
    """
    lab_type, country = "", ""
    if tito and tito in category:
        lab_type = category.split(tito)[0]
        country = category.split(tito)[1]
    else:
        lab_type = category

    country = country.lower()
    Type_t, country_t = "", ""

    Mash = f"^(.*?)(?:{tito}?)(.*?)$"

    test_N = category.lower()
    try:
        Type_t = re.sub(Mash, r"\g<1>", category.lower())
        country_t = re.sub(Mash, r"\g<2>", category.lower())
        test_N = re.sub(lab_type.lower(), "", test_N)
        test_N = re.sub(country.lower(), "", test_N)

    except Exception:
        logger.info("<<lightred>>>>>> except test_N ")
    test_N = test_N.strip()

    tito_stripped = tito.strip()

    if tito_stripped == "in" and lab_type.endswith(" playerss"):
        lab_type = lab_type.replace(" playerss", " players")

    titoends = f" {tito_stripped}"
    titostarts = f"{tito_stripped} "

    if tito_stripped == "of" and not lab_type.endswith(titoends):
        lab_type = f"{lab_type} of"
    elif tito_stripped == "spies for" and not lab_type.endswith(" spies"):
        lab_type = f"{lab_type} spies"

    elif tito_stripped == "by" and not country.startswith(titostarts):
        country = f"by {country}"
    elif tito_stripped == "for" and not country.startswith(titostarts):
        country = f"for {country}"

    logger.info(f'>xx>>> lab_type: "{lab_type.strip()}", country: "{country.strip()}", {tito=} ')

    if test_N and test_N != tito_stripped:
        logger.info(f'>>>> test_N != "", Type_t:"{Type_t}", tito:"{tito}", country_t:"{country_t}" ')

        if tito_stripped == "of" and not Type_t.endswith(titoends):
            Type_t = f"{Type_t} of"
        elif tito_stripped == "by" and not country_t.startswith(titostarts):
            country_t = f"by {country_t}"
        elif tito_stripped == "for" and not country_t.startswith(titostarts):
            country_t = f"for {country_t}"
        lab_type = Type_t
        country = country_t

        logger.info(f'>>>> yementest: Type_t:"{Type_t}", country_t:"{country_t}"')
    else:
        logger.info(f'>>>> test_N:"{test_N}" == tito')

    return lab_type, country


# @dump_data(enable=True)
def get_Type_lab(preposition: str, type_value: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters."""
    normalized_preposition = preposition.strip()
    type_lower = type_value.lower()

    label = ""
    if type_lower == "women" and normalized_preposition == "from":
        label = "نساء"
        logger.info(f'>> >> >> Make label "{label}".')

    elif type_lower == "women of":
        label = "نساء من"
        logger.info(f'>> >> >> Make label "{label}".')

    should_append_in_label = True
    type_lower_with_preposition = type_lower.strip()

    if not type_lower_with_preposition.endswith(f" {normalized_preposition}"):
        type_lower_with_preposition = f"{type_lower.strip()} {normalized_preposition}"

    if not label:
        label = Tabl_with_in.get(type_lower_with_preposition, "")
        if label:
            should_append_in_label = False
            logger.info(f'<<<< type_lower_with_preposition "{type_lower_with_preposition}", label : "{label}"')

    if not label:
        label = New_P17_Finall.get(type_lower, "")
        if label:
            logger.debug(f'<< type_lower_with_preposition "{type_lower_with_preposition}", label : "{label}"')

    if label == "" and type_lower.startswith("the "):
        type_lower_without_article = type_lower[len("the ") :]

        label = New_P17_Finall.get(type_lower_without_article, "")
        if label:
            logger.debug(f'<<< type_lower_with_preposition "{type_lower_with_preposition}", label : "{label}"')

    if label == "" and type_lower.strip().endswith(" people"):
        label = make_people_lab(type_lower)

    if not label:
        label = RELIGIOUS_KEYS_PP.get(type_lower, {}).get("mens", "")
    if not label:
        label = New_female_keys.get(type_lower, "")
    if not label:
        label = te_films(type_lower)
    if not label:
        label = nats.find_nat_others(type_lower)
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

    logger.info(f"?????? get_Type_lab: {type_lower=}, {label=}")

    return label, should_append_in_label


# @dump_data(enable=True)
def get_con_lab(preposition: str, country: str, start_get_country2: bool=False) -> str:
    """Retrieve the corresponding label for a given country."""
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
        label = year_lab.make_month_lab(country_lower)
    if not label:
        label = te_films(country)
    if not label:
        label = nats.find_nat_others(country)
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


def add_in_tab(type_label, type_lower, tito_stripped):
    ty_in18 = get_pop_All_18(type_lower)

    if tito_stripped == "from":
        if not type_label.strip().endswith(" من"):
            logger.info(f">>>> nAdd من to type_label '{type_label}' line:44")
            type_label = f"{type_label} من "
        return type_label

    if not ty_in18 or not type_lower.endswith(" of") or " في" in type_label:
        return type_label

    Type_lower2 = type_lower[: -len(" of")]
    in_tables = check_key_new_players(type_lower)
    in_tables2 = check_key_new_players(Type_lower2)

    if in_tables or in_tables2:
        logger.info(f">>>> nAdd من to type_label '{type_label}' line:59")
        type_label = f"{type_label} من "

    return type_label


def check_in_tables_new(country_lower, type_lower):
    country_in_table, table1 = check_key_in_tables_return_tuple(country_lower, Table_for_frist_word)
    type_in_table, table2 = check_key_in_tables_return_tuple(type_lower, Table_for_frist_word)
    if country_in_table:
        logger.info(f'>>>> X:<<lightpurple>> country_lower "{country_lower}" in {table1}.')

    if type_in_table:
        logger.info(f'>>>>xX:<<lightpurple>> type_lower "{type_lower}" in {table2}.')
    return country_in_table, type_in_table


# @dump_data(enable=True, compare_with_output="type_label")
def tito_list_s_fixing(type_label, tito_stripped, type_lower):
    """
    {"type_label": "منشآت عسكرية", "tito_stripped": "in", "type_lower": "military installations", "output": "منشآت عسكرية في"}
    """
    if tito_stripped in TITO_LIST_S:
        if tito_stripped == "in" or " in" in type_lower:
            if type_lower in pop_of_without_in:
                logger.info(f'>>-- Skip aAdd في to type_label:"{type_label}", "{type_lower}"')

            else:
                if " في" not in type_label and " in" in type_lower:
                    logger.info(f'>>-- aAdd في to type_label:in"{type_label}", for "{type_lower}"')
                    type_label = type_label + " في"

                elif tito_stripped == "in" and " in" in type_lower:
                    logger.info(f'>>>> aAdd في to type_label:in"{type_label}", for "{type_lower}"')
                    type_label = type_label + " في"

        elif (tito_stripped == "at" or " at" in type_lower) and (" في" not in type_label):
            logger.info('>>>> Add في to type_label:at"%s"' % type_label)
            type_label = type_label + " في"
    # ---
    return type_label


def determine_separator(tito_stripped, country_label, type_label, type_lower, country_in_table, add_in_lab, tito, cate_test, for_table, country_lower, category):
    # ---
    sps = " "
    if tito_stripped == "in":
        sps = " في "

    if country_in_table and add_in_lab:
        if (tito_stripped == "in" or tito_stripped == "at") and (" في" not in country_label or type_lower in Add_ar_in):
            sps = " في "
            logger.info("ssps:%s" % sps)
    else:
        if (tito_stripped == "in" or tito_stripped == "at") and (" في" not in type_label or type_lower in Add_ar_in):
            type_label = type_label + " في"

    if add_in_lab:
        logger.info(f">>>>> > add_in_lab ({tito_stripped=})")
        tito2_lab = category_relation_mapping.get(tito_stripped)
        if tito2_lab not in TITO_LIST_S:
            tatl = tito2_lab
            logger.info(f">>>>> > ({tito_stripped=}): tito_stripped in category_relation_mapping and tito_stripped not in TITO_LIST_S, {tatl=}")

            if tito_stripped == "for" and country_lower.startswith("for "):
                if type_lower.strip().endswith("competitors") and "competitors for" in category:
                    tatl = "من"

                if type_lower.strip().endswith("medalists") and "medalists for" in category:
                    tatl = "من"

            if tito_stripped == "to" and type_lower.strip().startswith("ambassadors of"):
                tatl = "لدى"

            if country_label == "لعضوية البرلمان":
                tatl = ""

            if tito_stripped == "for" and country_lower.startswith("for "):
                p18lab = get_pop_All_18(country_lower)
                if p18lab and p18lab == country_label:
                    tatl = ""

            if country_lower in for_table:
                tatl = ""

            sps = f" {tatl} "
            logger.info("sps:%s" % sps)
            cate_test = cate_test.replace(tito, "")

    # in_tables_1 = check_key_new_players(country_lower)
    # in_tables_2 = check_key_new_players(type_lower)

    # if in_tables_1 and in_tables_2:
    logger.info(">>>> ================ ")
    logger.info(">>>>> > X:<<lightred>> type_lower and country_lower in players_new_keys.")
    logger.info(">>>> ================ ")

    faa = category_relation_mapping.get(tito_stripped.strip()) or category_relation_mapping.get(tito_stripped.replace("-", " ").strip())
    # print(f"{tito_stripped=}, {faa=}, {sps=}")

    if not sps.strip() and faa:
        sps = f" {faa} "
    return sps, cate_test


def join_labels(tito_stripped, country_label, type_label, type_lower, country_in_table, type_in_table, cate_test, country_lower, category, sps):
    # ---
    Keep_Type_last = False
    keep_Type_first = False

    arlabel = ""
    t_to = f"{type_lower} {tito_stripped}"

    if type_lower in Keep_it_last:
        logger.info('>>>>> > X:<<lightred>> Keep_Type_last = True, type_lower:"%s" in Keep_it_last' % type_lower)
        Keep_Type_last = True

    elif type_lower in Keep_it_frist:
        logger.info('>>>>> > X:<<lightred>> keep_Type_first = True, type_lower:"%s" in Keep_it_frist' % type_lower)
        keep_Type_first = True

    elif t_to in Keep_it_frist:
        logger.info('>>>>> > X:<<lightred>> keep_Type_first = True, t_to:"%s" in Keep_it_frist' % t_to)
        keep_Type_first = True

    if type_in_table and country_in_table:
        logger.info(">>> > X:<<lightpurple>> type_lower and country_lower in Table_for_frist_word.")
        in_tables = check_key_new_players(country_lower)
        if not keep_Type_first and in_tables:
            arlabel = country_label + sps + type_label
        else:
            arlabel = type_label + sps + country_label
    else:
        if keep_Type_first and country_in_table:
            arlabel = country_label + sps + type_label
        else:
            arlabel = type_label + sps + country_label

    if Keep_Type_last:
        logger.info('>>>>> > X:<<lightred>> Keep_Type_last = True, type_lower:"%s" in Keep_it_last' % type_lower)
        arlabel = country_label + sps + type_label

    elif keep_Type_first:
        logger.info('>>>>> > X:<<lightred>> keep_Type_first = True, type_lower:"%s" in Keep_it_frist' % type_lower)
        arlabel = type_label + sps + country_label

    if tito_stripped == "about" or (tito_stripped not in TITO_LIST_S):
        arlabel = type_label + sps + country_label

    if type_lower == "years" and tito_stripped == "in":
        arlabel = type_label + sps + country_label

    logger.debug(f">>>> {sps=}")
    logger.debug(f">>>> {arlabel=}")

    vr = re.sub(country_lower, "{}", category.lower())
    if vr in pop_format2:
        logger.info('<<lightblue>>>>>> vr in pop_format2 "%s":' % pop_format2[vr])
        logger.info('<<lightblue>>>>>>> vr: "%s":' % vr)
        arlabel = pop_format2[vr].format(country_label)
    elif type_lower in pop_format:
        if not country_label.startswith("حسب"):
            logger.info('>>>> <<lightblue>> type_lower in pop_format "%s":' % pop_format[type_lower])
            arlabel = pop_format[type_lower].format(country_label)
        else:
            logger.info('>>>> <<lightblue>> type_lower in pop_format "%s" and country_label.startswith("حسب") ' % pop_format[type_lower])

    elif tito_stripped in pop_format33:
        logger.info('>>>> <<lightblue>> tito in pop_format33 "%s":' % pop_format33[tito_stripped])
        arlabel = pop_format33[tito_stripped].format(type_label, country_label)

    arlabel = arlabel.replace("  ", " ")
    maren = re.match(r"\d\d\d\d", country_lower.strip())
    if type_lower.lower() == "the war of" and maren and arlabel == f"الحرب في {country_lower}":
        arlabel = f"حرب {country_lower}"
        logger.info('<<lightpurple>> >>>> change arlabel to "%s".' % arlabel)
    return arlabel, cate_test


@dump_data(["category", "tito"])
@functools.lru_cache(maxsize=10000)
def find_ar_label(
    category: str,
    tito: str,
    cate_test: str = "",
    start_get_country2: bool = True,
    use_event2: bool = True,
) -> str:
    """Find the Arabic label based on the provided parameters."""

    CAO = True

    logger.info(f'<<lightblue>>>>>> find_ar_label: {category=}, {tito=}')
    tito_stripped = tito.strip()
    lab_type, country = get_type_country(category, tito)

    type_lower = lab_type.strip().lower()
    country_lower = country.strip().lower()

    type_label, add_in_lab = get_Type_lab(tito, lab_type)

    if type_lower == "sport" and country_lower.startswith("by "):
        type_label = "رياضة"

    if not type_label and use_event2:
        type_label = wrap_event2(type_lower, tito)

    if type_label:
        cate_test = cate_test.replace(type_lower, "")

    country_label = get_con_lab(tito, country, start_get_country2=start_get_country2)

    if country_label:
        cate_test = cate_test.replace(country_lower, "")

    if not type_label:
        logger.info('>>>> type_lower "%s" not in pop_of_in' % type_lower)
        CAO = False

    if not country_label:
        logger.info('>>>> country_lower not in pop new "%s"' % country_lower)
        CAO = False

    if type_label or country_label:
        logger.info(f'<<lightgreen>>>>>> ------------- country_lower:"{country_lower}", country_label:"{country_label}"')
        logger.info(f'<<lightgreen>>>>>> ------------- type_lower:"{type_lower}", type_label:"{type_label}"')

    if not CAO:
        return ""
    # ---
    logger.info('<<lightblue>> CAO: cat:"%s":' % category)
    # ---
    if not type_label or not country_label:
        return ""
    # ---
    tito_stripped = tito.strip()
    # ---
    if add_in_lab:
        type_label = tito_list_s_fixing(type_label, tito_stripped, type_lower)
        if type_lower in Dont_Add_min:
            logger.info(f'>>>> type_lower "{type_lower}" in Dont_Add_min ')
        else:
            type_label = add_in_tab(type_label, type_lower, tito_stripped)
    # ---
    country_in_table, type_in_table = check_in_tables_new(country_lower, type_lower)
    # ---
    sps, cate_test = determine_separator(tito_stripped, country_label, type_label, type_lower, country_in_table, add_in_lab, tito, cate_test, for_table, country_lower, category)
    # ---
    arlabel, cate_test = join_labels(tito_stripped, country_label, type_label, type_lower, country_in_table, type_in_table, cate_test, country_lower, category, sps)
    # ---
    logger.info(f'>>>> <<lightblue>>cate_test :"{cate_test}"')
    logger.info(f'>>>>>> <<lightyellow>>test: cat "{category}", arlabel:"{arlabel}"')
    logger.info(f'>>>> <<lightblue>>cate_test :"{cate_test}"')
    # ---
    arlabel = arlabel.strip()
    # ---
    arlabel = fix_minor(arlabel, sps)
    # ---
    return arlabel


__all__ = [
    "find_ar_label",
    "add_in_tab",
    "get_Type_lab",
    "get_con_lab",
    "get_type_country",
]
