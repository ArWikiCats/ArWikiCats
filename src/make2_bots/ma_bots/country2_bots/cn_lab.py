#!/usr/bin/python3
"""
!
"""

import re
from ....translations import By_table, typeTable
from ...format_bots import pop_format, pop_format2

from ...matables_bots.bot import Films_O_TT
from ...matables_bots.check_bot import check_key_new_players
from ....utils import check_key_in_tables
from ....helps.print_bot import print_put


def make_cnt_lab(tat_o: str, country2: str, c_2_l: str, c_1_l: str, cona_1: str, cona_2: str, sps: str) -> str:
    """Construct a formatted string based on various input parameters."""

    resolved_label = c_1_l + sps + c_2_l
    in_tables_no_lower = check_key_in_tables(cona_1, [typeTable, Films_O_TT])
    in_tables_lowers = check_key_new_players(cona_1.lower())
    if in_tables_no_lower or in_tables_lowers:
        if in_tables_lowers:
            if c_2_l.startswith("أصل "):
                print_put(f'>>>>>> Add من to cona_1:"{cona_1}" cona_1 in players_new_keys:')
                resolved_label = f"{c_1_l}{sps}من {c_2_l}"
            else:
                print_put(f'>>>>>> Add في to cona_1:"{cona_1}" cona_1 in players_new_keys:')
                resolved_label += " في "
        if cona_2 not in By_table:
            Films_O_TT[country2] = resolved_label
        else:
            print_put("<<lightblue>>>>>> cona_2 in By_table")

    if c_2_l:
        faxos = ""
        if not cona_2.startswith("by "):
            tashr = f"{cona_1} {tat_o.strip()}"
            if cona_1 in pop_format:
                faxos = pop_format[cona_1]
            elif tashr in pop_format:
                faxos = pop_format[tashr]
            if faxos:
                print_put(f'<<lightblue>>>>>> cona_1 in pop_format "{faxos}":')
                resolved_label = faxos.format(c_2_l)

        if cona_1 in pop_format2:
            print_put(f'<<lightblue>>>>>> cona_1 in pop_format2 "{pop_format2[cona_1]}":')
            resolved_label = pop_format2[cona_1].format(c_2_l)

    print_put(f'<<lightpurple>> >>>> country 2_tit "{country2}": label: {resolved_label}')
    resolved_label = resolved_label.replace("  ", " ")

    maren = re.match(r"\d\d\d\d", cona_2)

    if maren:
        if cona_1 == "war of" and resolved_label == f"الحرب في {cona_2}":
            resolved_label = f"حرب {cona_2}"
            print_put(f'<<lightpurple>> >>>> change cnt_la to "{resolved_label}".')

    if resolved_label.endswith(" في "):
        resolved_label = resolved_label[: -len(" في ")]
    return resolved_label
