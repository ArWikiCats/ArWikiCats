#!/usr/bin/python3
"""
!
"""

import re

from ....helps.log import logger
from ....translations import By_table, typeTable
from ....utils import check_key_in_tables, check_key_in_tables_return_tuple
from ...format_bots import pop_format, pop_format2
from ...matables_bots.bot import Films_O_TT, add_to_Films_O_TT
from ...matables_bots.check_bot import check_key_new_players


def make_cnt_lab(separator: str, country2: str, part_2_label: str, part_1_label: str, part_1_normalized: str, part_2_normalized: str, sps: str) -> str:
    """Construct a formatted string based on various input parameters."""

    resolved_label = part_1_label + sps + part_2_label
    in_tables_no_lower = check_key_in_tables(part_1_normalized, [typeTable, Films_O_TT])
    in_players = check_key_new_players(part_1_normalized.lower())

    to_check_them_tuble = {
        "typeTable": typeTable,
        "Films_O_TT": Films_O_TT,
    }
    co_in_tables, tab_name = check_key_in_tables_return_tuple(part_1_normalized, to_check_them_tuble)
    if co_in_tables or in_players:
        if in_players:
            if part_2_label.startswith("أصل "):
                logger.info(f'>>>>>> Add من to part_1_normalized:"{part_1_normalized}" part_1_normalized in New_players:')
                resolved_label = f"{part_1_label}{sps}من {part_2_label}"
            else:
                logger.info(f'>>>>>> Add في to part_1_normalized:"{part_1_normalized}" part_1_normalized in New_players:')
                resolved_label += " في "
        if part_2_normalized not in By_table:
            # Films_O_TT[country2] = resolved_label
            add_to_Films_O_TT(country2, resolved_label)
            # print(f"cn_lab: {country2=}, {resolved_label=}\n"*10)
        else:
            logger.info("<<lightblue>>>>>> part_2_normalized in By_table")

    if part_2_label:
        faxos = ""
        if not part_2_normalized.startswith("by "):
            tashr = f"{part_1_normalized} {separator.strip()}"
            if part_1_normalized in pop_format:
                faxos = pop_format[part_1_normalized]
            elif tashr in pop_format:
                faxos = pop_format[tashr]
            if faxos:
                logger.info(f'<<lightblue>>>>>> part_1_normalized in pop_format "{faxos}":')
                resolved_label = faxos.format(part_2_label)

        if part_1_normalized in pop_format2:
            logger.info(f'<<lightblue>>>>>> part_1_normalized in pop_format2 "{pop_format2[part_1_normalized]}":')
            resolved_label = pop_format2[part_1_normalized].format(part_2_label)

    logger.info(f'<<lightpurple>> >>>> country 2_tit "{country2}": label: {resolved_label}')
    resolved_label = " ".join(resolved_label.strip().split())

    maren = re.match(r"\d\d\d\d", part_2_normalized)

    if maren:
        if part_1_normalized == "war of" and resolved_label == f"الحرب في {part_2_normalized}":
            resolved_label = f"حرب {part_2_normalized}"
            logger.info(f'<<lightpurple>> >>>> change cnt_la to "{resolved_label}".')

    # print(f"{resolved_label=}\n"*5)
    # print(dd)

    if resolved_label.endswith(" في "):
        resolved_label = resolved_label[: -len(" في ")]
    return resolved_label
