#!/usr/bin/python3
"""
!
"""

import re

from ....helps.log import logger
from ....translations import By_table, typeTable
from ....utils import check_key_in_tables, check_key_in_tables_return_tuple
from ...format_bots import pop_format, pop_format2
from ...matables_bots.bot import Films_O_TT
from ...matables_bots.check_bot import check_key_new_players


def make_cnt_lab(tat_o: str, country2: str, c_2_l: str, c_1_l: str, cona_1: str, cona_2: str, sps: str) -> str:
    """Construct a formatted string based on various input parameters."""

    resolved_label = c_1_l + sps + c_2_l
    in_tables_no_lower = check_key_in_tables(cona_1, [typeTable, Films_O_TT])
    in_tables_lowers = check_key_new_players(cona_1.lower())

    to_check_them_tuble = {
        "typeTable": typeTable,
        "Films_O_TT": Films_O_TT,
    }
    co_in_tables, tab_name = check_key_in_tables_return_tuple(cona_1, to_check_them_tuble)
    # print(f"\n\nco_in_tables: {co_in_tables} tab_name:{tab_name}, cona_1: {cona_1}\n\n")

    # if cona_1 in typeTable or cona_1 in Films_O_TT or in_tables_lowers:
    if co_in_tables or in_tables_lowers:
        if in_tables_no_lower or in_tables_lowers:
            # if in_tables_lowers:
            if c_2_l.startswith("أصل "):
                logger.info(f'>>>>>> Add من to cona_1:"{cona_1}" cona_1 in New_players:')
                resolved_label = f"{c_1_l}{sps}من {c_2_l}"
            else:
                logger.info(f'>>>>>> Add في to cona_1:"{cona_1}" cona_1 in New_players:')
                resolved_label += " في "
        if cona_2 not in By_table:
            Films_O_TT[country2] = resolved_label
            # print(f"cn_lab: {country2=}, {resolved_label=}\n"*10)
        else:
            logger.info("<<lightblue>>>>>> cona_2 in By_table")

    if c_2_l:
        faxos = ""
        if not cona_2.startswith("by "):
            tashr = f"{cona_1} {tat_o.strip()}"
            if cona_1 in pop_format:
                faxos = pop_format[cona_1]
            elif tashr in pop_format:
                faxos = pop_format[tashr]
            if faxos:
                logger.info(f'<<lightblue>>>>>> cona_1 in pop_format "{faxos}":')
                resolved_label = faxos.format(c_2_l)

        if cona_1 in pop_format2:
            logger.info(f'<<lightblue>>>>>> cona_1 in pop_format2 "{pop_format2[cona_1]}":')
            resolved_label = pop_format2[cona_1].format(c_2_l)

    logger.info(f'<<lightpurple>> >>>> country 2_tit "{country2}": label: {resolved_label}')
    resolved_label = " ".join(resolved_label.strip().split())

    maren = re.match(r"\d\d\d\d", cona_2)

    if maren:
        if cona_1 == "war of" and resolved_label == f"الحرب في {cona_2}":
            resolved_label = f"حرب {cona_2}"
            logger.info(f'<<lightpurple>> >>>> change cnt_la to "{resolved_label}".')

    # print(f"{resolved_label=}\n"*5)
    # print(dd)

    if resolved_label.endswith(" في "):
        resolved_label = resolved_label[: -len(" في ")]
    return resolved_label
