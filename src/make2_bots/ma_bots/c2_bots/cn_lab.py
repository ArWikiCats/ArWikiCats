#!/usr/bin/python3
"""
from .cn_lab import make_cnt_lab

"""

import re
from ....ma_lists import By_table
from ...format_bots import pop_format, pop_format2

from ...matables_bots.bot import (
    Films_O_TT,
    New_players,
    typeTable,
)
from ....helps.print_bot import print_put


def make_cnt_lab(tat_o: str, contry2: str, c_2_l: str, c_1_l: str, cona_1: str, cona_2: str, sps: str) -> str:
    """Construct a formatted string based on various input parameters."""

    resolved_label = c_1_l + sps + c_2_l

    if cona_1 in typeTable or cona_1 in Films_O_TT or cona_1.lower() in New_players:
        if cona_1.lower() in New_players:
            if c_2_l.startswith("أصل "):
                print_put(f'>>>>>> Add من to cona_1:"{cona_1}" cona_1 in New_players:')
                resolved_label = f"{(c_1_l + sps)}من {c_2_l}"
            else:
                print_put(f'>>>>>> Add في to cona_1:"{cona_1}" cona_1 in New_players:')
                resolved_label += " في "
        if cona_2 not in By_table:
            Films_O_TT[contry2] = resolved_label
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

    print_put(f'<<lightpurple>> >>>> contry 2_tit "{contry2}": label: {resolved_label}')
    resolved_label = resolved_label.replace("  ", " ")

    maren = re.match(r"\d\d\d\d", cona_2)

    if maren:
        if cona_1 == "war of" and resolved_label == f"الحرب في {cona_2}":
            resolved_label = f"حرب {cona_2}"
            print_put(f'<<lightpurple>> >>>> change cnt_la to "{resolved_label}".')

    if resolved_label.endswith(" في "):
        resolved_label = resolved_label[: -len(" في ")]
    return resolved_label
