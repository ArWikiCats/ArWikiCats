#!/usr/bin/python3
"""
!
"""

import functools
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


# تم تحويلها إلى
# اقتبست في
# حولت إلى
tito_list_s = [
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
    Type, country = "", ""
    if tito and tito in category:
        Type = category.split(tito)[0]
        country = category.split(tito)[1]
    else:
        Type = category

    country = country.lower()
    Mash = f"^(.*?)(?:{tito}?)(.*?)$"
    Type_t = re.sub(Mash, r"\g<1>", category.lower())
    country_t = re.sub(Mash, r"\g<2>", category.lower())

    test_N = category.lower()
    try:
        test_N = re.sub(Type.lower(), "", test_N)
        test_N = re.sub(country.lower(), "", test_N)

    except Exception:
        logger.info("<<lightred>>>>>> except test_N ")
    test_N = test_N.strip()

    tito2 = tito.strip()

    if tito2 == "in" and Type.endswith(" playerss"):
        Type = Type.replace(" playerss", " players")

    titoends = f" {tito2}"
    titostarts = f"{tito2} "

    if tito2 == "of" and not Type.endswith(titoends):
        Type = f"{Type} of"
    elif tito2 == "spies for" and not Type.endswith(" spies"):
        Type = f"{Type} spies"

    elif tito2 == "by" and not country.startswith(titostarts):
        country = f"by {country}"
    elif tito2 == "for" and not country.startswith(titostarts):
        country = f"for {country}"

    logger.info(f'>xx>>> Type: "{Type.strip()}", country: "{country.strip()}", {tito=} ')

    if test_N and test_N != tito2:
        logger.info(f'>>>> test_N != "", Type_t:"{Type_t}", tito:"{tito}", country_t:"{country_t}" ')

        if tito2 == "of" and not Type_t.endswith(titoends):
            Type_t = f"{Type_t} of"
        elif tito2 == "by" and not country_t.startswith(titostarts):
            country_t = f"by {country_t}"
        elif tito2 == "for" and not country_t.startswith(titostarts):
            country_t = f"for {country_t}"
        Type = Type_t
        country = country_t

        logger.info(f'>>>> yementest: Type_t:"{Type_t}", country_t:"{country_t}"')
    else:
        logger.info(f'>>>> test_N:"{test_N}" == tito')

    return Type, country


def get_Type_lab(preposition: str, type_value: str, type_lower: str, country_lower: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters."""

    normalized_preposition = preposition.strip()

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
    if type_lower == "sport" and country_lower.startswith("by "):
        label = "رياضة"

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
        label = team_work.Get_team_work_Club(type_value.strip())

    if not label:
        label = tmp_bot.Work_Templates(type_lower)

    if not label:
        label = Get_c_t_lab(type_lower, preposition, Type="Type_lab")

    if not label:
        label = te4_2018_Jobs(type_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(type_lower)

    logger.info(f"?????? get_Type_lab: {type_lower=}, {label=}")

    return label, should_append_in_label


def get_con_lab(preposition: str, tito2: str, country: str, country_lower: str, start_get_country2: bool) -> str:
    """Retrieve the corresponding label for a given country."""

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

    if tito2 == "for":
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


def add_in_tab(Type_lab, Type_lower, tito2):
    ty_in18 = get_pop_All_18(Type_lower)
    if tito2 == "from":
        if not Type_lab.strip().endswith(" من"):
            logger.info(f">>>> nAdd من to Type_lab '{Type_lab}' line:44")
            Type_lab = f"{Type_lab} من "
        return Type_lab
    if not ty_in18 or not Type_lower.endswith(" of") or " في" in Type_lab:
        return Type_lab
    Type_lower2 = Type_lower[: -len(" of")]
    in_tables = check_key_new_players(Type_lower)
    in_tables2 = check_key_new_players(Type_lower2)
    if in_tables or in_tables2:
        logger.info(f">>>> nAdd من to Type_lab '{Type_lab}' line:59")
        Type_lab = f"{Type_lab} من "
    return Type_lab


def _check_in_tables_new(country_lower, Type_lower):
    country_in_Table, table1 = check_key_in_tables_return_tuple(country_lower, Table_for_frist_word)
    Type_in_Table, table2 = check_key_in_tables_return_tuple(Type_lower, Table_for_frist_word)
    if country_in_Table:
        logger.info(f'>>>> X:<<lightpurple>> country_lower "{country_lower}" in {table1}.')

    if Type_in_Table:
        logger.info(f'>>>>xX:<<lightpurple>> Type_lower "{Type_lower}" in {table2}.')
    return country_in_Table, Type_in_Table


def tito_list_s_fixing(Type_lab, tito2, Add_in_lab, Type_lower):
    # ---
    if tito2 in tito_list_s and Add_in_lab:
        if tito2 == "in" or " in" in Type_lower:
            if Type_lower in pop_of_without_in:
                logger.info(f'>>-- Skip aAdd في to Type_lab:"{Type_lab}", "{Type_lower}"')

            else:
                if " في" not in Type_lab and " in" in Type_lower:
                    logger.info(f'>>-- aAdd في to Type_lab:in"{Type_lab}", for "{Type_lower}"')
                    Type_lab = Type_lab + " في"

                elif tito2 == "in" and " in" in Type_lower:
                    logger.info(f'>>>> aAdd في to Type_lab:in"{Type_lab}", for "{Type_lower}"')
                    Type_lab = Type_lab + " في"

        elif (tito2 == "at" or " at" in Type_lower) and (" في" not in Type_lab):
            logger.info('>>>> Add في to Type_lab:at"%s"' % Type_lab)
            Type_lab = Type_lab + " في"
    # ---
    return Type_lab


@dump_data(["category", "tito"])
@functools.lru_cache(maxsize=10000)
def find_ar_label(
    category: str,
    tito: str,
    Cate_test: str="",
    start_get_country2: bool = True,
    use_event2: bool = True
) -> str:
    """Find the Arabic label based on the provided parameters."""

    CAO = True

    logger.info(f'<<lightblue>>>>>> find_ar_label: {category=}, {tito=}')
    tito2 = tito.strip()
    Type, country = get_type_country(category, tito)

    arlabel = ""
    Type_lower = Type.strip().lower()
    country_lower = country.strip().lower()

    Type_lab, Add_in_lab = get_Type_lab(tito, Type, Type_lower, country_lower)

    if not Type_lab and use_event2:
        Type_lab = wrap_event2(Type_lower, tito)

    if Type_lab:
        Cate_test = Cate_test.replace(Type_lower, "")

    con_lab = get_con_lab(tito, tito2, country, country_lower, start_get_country2)

    if con_lab:
        Cate_test = Cate_test.replace(country_lower, "")

    if not Type_lab:
        logger.info('>>>> Type_lower "%s" not in pop_of_in' % Type_lower)
        CAO = False

    if not con_lab:
        logger.info('>>>> country_lower not in pop new "%s"' % country_lower)
        CAO = False

    if Type_lab or con_lab:
        logger.info(f'<<lightgreen>>>>>> ------------- country_lower:"{country_lower}", con_lab:"{con_lab}"')
        logger.info(f'<<lightgreen>>>>>> ------------- Type_lower:"{Type_lower}", Type_lab:"{Type_lab}"')

    if not CAO:
        return ""
    logger.info('<<lightblue>> CAO: cat:"%s":' % category)
    if not Type_lab or not con_lab:
        return ""

    Type_lab = tito_list_s_fixing(Type_lab, tito2, Add_in_lab, Type_lower)
    # ---
    if Add_in_lab:
        if Type_lower in Dont_Add_min:
            logger.info(f'>>>> Type_lower "{Type_lower}" in Dont_Add_min ')
        else:
            Type_lab = add_in_tab(Type_lab, Type_lower, tito2)
    country_in_Table, Type_in_Table = _check_in_tables_new(country_lower, Type_lower)
    sps = " "
    if tito2 == "in":
        sps = " في "

    if country_in_Table and Add_in_lab:
        if (tito2 == "in" or tito2 == "at") and (" في" not in con_lab or Type_lower in Add_ar_in):
            sps = " في "
            logger.info("ssps:%s" % sps)
    else:
        if (tito2 == "in" or tito2 == "at") and (" في" not in Type_lab or Type_lower in Add_ar_in):
            Type_lab = Type_lab + " في"

    if Add_in_lab:
        logger.info(f">>>>> > Add_in_lab ({tito2=})")
        tito2_lab = category_relation_mapping.get(tito2)
        if tito2_lab not in tito_list_s:
            tatl = tito2_lab
            logger.info(f">>>>> > ({tito2=}): tito2 in category_relation_mapping and tito2 not in tito_list_s, {tatl=}")

            if tito2 == "for" and country_lower.startswith("for "):
                if Type_lower.strip().endswith("competitors") and "competitors for" in category:
                    tatl = "من"

                if Type_lower.strip().endswith("medalists") and "medalists for" in category:
                    tatl = "من"

            if tito2 == "to" and Type_lower.strip().startswith("ambassadors of"):
                tatl = "لدى"

            if con_lab == "لعضوية البرلمان":
                tatl = ""

            if tito2 == "for" and country_lower.startswith("for "):
                p18lab = get_pop_All_18(country_lower)
                if p18lab and p18lab == con_lab:
                    tatl = ""

            if country_lower in for_table:
                tatl = ""

            sps = f" {tatl} "
            logger.info("sps:%s" % sps)
            Cate_test = Cate_test.replace(tito, "")

    in_tables_1 = check_key_new_players(country_lower)
    in_tables_2 = check_key_new_players(Type_lower)

    if in_tables_1 and in_tables_2:
        logger.info(">>>> ================ ")
        logger.info(">>>>> > X:<<lightred>> Type_lower and country_lower in players_new_keys.")
        logger.info(">>>> ================ ")

    faa = category_relation_mapping.get(tito2.strip()) or category_relation_mapping.get(tito2.replace("-", " ").strip())
    # print(f"{tito2=}, {faa=}, {sps=}")

    if not sps.strip() and faa:
        sps = f" {faa} "

    Keep_Type_last = False
    keep_Type_first = False

    t_to = f"{Type_lower} {tito2}"

    if Type_lower in Keep_it_last:
        logger.info('>>>>> > X:<<lightred>> Keep_Type_last = True, Type_lower:"%s" in Keep_it_last' % Type_lower)
        Keep_Type_last = True

    elif Type_lower in Keep_it_frist:
        logger.info('>>>>> > X:<<lightred>> keep_Type_first = True, Type_lower:"%s" in Keep_it_frist' % Type_lower)
        keep_Type_first = True

    elif t_to in Keep_it_frist:
        logger.info('>>>>> > X:<<lightred>> keep_Type_first = True, t_to:"%s" in Keep_it_frist' % t_to)
        keep_Type_first = True

    if Type_in_Table and country_in_Table:
        logger.info(">>> > X:<<lightpurple>> Type_lower and country_lower in Table_for_frist_word.")
        in_tables = check_key_new_players(country_lower)
        if not keep_Type_first and in_tables:
            arlabel = con_lab + sps + Type_lab
        else:
            arlabel = Type_lab + sps + con_lab
    else:
        if keep_Type_first and country_in_Table:
            arlabel = con_lab + sps + Type_lab
        else:
            arlabel = Type_lab + sps + con_lab

    if Keep_Type_last:
        logger.info('>>>>> > X:<<lightred>> Keep_Type_last = True, Type_lower:"%s" in Keep_it_last' % Type_lower)
        arlabel = con_lab + sps + Type_lab

    elif keep_Type_first:
        logger.info('>>>>> > X:<<lightred>> keep_Type_first = True, Type_lower:"%s" in Keep_it_frist' % Type_lower)
        arlabel = Type_lab + sps + con_lab

    if tito2 == "about" or (tito2 not in tito_list_s):
        arlabel = Type_lab + sps + con_lab

    if Type_lower == "years" and tito2 == "in":
        arlabel = Type_lab + sps + con_lab

    logger.debug(f">>>> {sps=}")
    logger.debug(f">>>> {arlabel=}")

    vr = re.sub(country_lower, "{}", category.lower())
    if vr in pop_format2:
        logger.info('<<lightblue>>>>>> vr in pop_format2 "%s":' % pop_format2[vr])
        logger.info('<<lightblue>>>>>>> vr: "%s":' % vr)
        arlabel = pop_format2[vr].format(con_lab)
    elif Type_lower in pop_format:
        if not con_lab.startswith("حسب"):
            logger.info('>>>> <<lightblue>> Type_lower in pop_format "%s":' % pop_format[Type_lower])
            arlabel = pop_format[Type_lower].format(con_lab)
        else:
            logger.info('>>>> <<lightblue>> Type_lower in pop_format "%s" and con_lab.startswith("حسب") ' % pop_format[Type_lower])

    elif tito2 in pop_format33:
        logger.info('>>>> <<lightblue>> tito in pop_format33 "%s":' % pop_format33[tito2])
        arlabel = pop_format33[tito2].format(Type_lab, con_lab)

    arlabel = arlabel.replace("  ", " ")
    maren = re.match(r"\d\d\d\d", country_lower.strip())
    if Type_lower.lower() == "the war of" and maren and arlabel == f"الحرب في {country_lower}":
        arlabel = f"حرب {country_lower}"
        logger.info('<<lightpurple>> >>>> change arlabel to "%s".' % arlabel)

    logger.info(f'>>>> <<lightblue>>Cate_test :"{Cate_test}"')
    logger.info(f'>>>>>> <<lightyellow>>test: cat "{category}", arlabel:"{arlabel}"')
    logger.info(f'>>>> <<lightblue>>Cate_test :"{Cate_test}"')
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
]
