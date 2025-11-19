#!/usr/bin/python3
"""
!
"""

import re
from ....fix import fixtitle
from ....translations import pop_of_without_in

from ...format_bots import category_relation_mapping, for_table, pop_format33, pop_format, pop_format2, tito_list_s, Dont_Add_min

from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.bot import (
    Table_for_frist_word,
    Add_ar_in,
    Keep_it_last,
    Keep_it_frist,
)

from ...matables_bots.check_bot import check_key_new_players
from ....helps.log import logger
from ....utils import check_key_in_tables_return_tuple

from ...ma_bots_new.bot_type_country import get_type_country
from .bot_type_lab import get_Type_lab
from .bot_con_lab import get_con_lab
from ....main_processers import event2bot

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


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


def find_ar_label(
    category: str,
    tito: str,
    tito_name: str,
    Cate_test: str,
    category_r: str,
    start_get_country2: bool = True
) -> str:
    """Find the Arabic label based on the provided parameters."""

    CAO = True

    logger.info(f'<<lightblue>>>>>> yementest: tito:"{tito_name}":"{tito}" in category ')
    tito2 = tito.strip()
    Type, country = get_type_country(category, tito)

    arlabel = ""
    Type_lower = Type.strip().lower()
    country_lower = country.strip().lower()

    Type_lab, Add_in_lab = get_Type_lab(tito, Type, Type_lower, country_lower)

    if not Type_lab:
        Type_lab = event2bot.event2(Type_lower)

    if Type_lab:
        Cate_test = Cate_test.replace(Type_lower, "")

    con_lab = get_con_lab(tito, tito2, country, country_lower, start_get_country2)

    if con_lab:
        Cate_test = Cate_test.replace(country_lower, "")

    if not Type_lab:
        logger.info('>>>> Type_lower "%s" not in pop_of_in' % Type_lower)
        CAO = False
    else:
        Cate_test = Cate_test.replace(Type_lower, "")

    if not con_lab:
        logger.info('>>>> country_lower not in pop new "%s"' % country_lower)
        CAO = False
    else:
        Cate_test = Cate_test.replace(country_lower, "")

    if Type_lab or con_lab:
        logger.info(f'<<lightgreen>>>>>> ------------- country_lower:"{country_lower}", con_lab:"{con_lab}"')
        logger.info(f'<<lightgreen>>>>>> ------------- Type_lower:"{Type_lower}", Type_lab:"{Type_lab}"')

    if not CAO:
        return ""
    logger.info('<<lightblue>> CAO: cat:"%s":' % category)
    if not Type_lab or not con_lab:
        return ""
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
        if tito2 in category_relation_mapping and tito2 not in tito_list_s:
            tatl = category_relation_mapping[tito2]
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

    logger.debug('>>>> sps "%s"' % sps)
    logger.debug('>>>> arlabel "%s"' % arlabel)
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

    if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) != arlabel:
        return ""
    arlabel = fixtitle.fixlab(arlabel, en=category_r)
    logger.info('>>>>>> <<lightyellow>>Cate_test: "%s" ' % Cate_test)
    logger.info(f'>>>>>> <<lightyellow>>test: cat "{category_r}", arlabel:"{arlabel}"')
    logger.info('>>>> <<lightblue>>Cate_test :"%s"' % Cate_test)
    return arlabel


__all__ = [
    "find_ar_label",
    "add_in_tab",
]
