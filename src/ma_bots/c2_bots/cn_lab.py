#!/usr/bin/python3
"""
from .cn_lab import make_cnt_lab

"""

import re
from ...ma_lists_bots import By_table
from ...format_bots import pop_format, pop_format2

from ...matables_bots.bot import (
    Films_O_TT,
    New_players,
    typeTable,
)
from ...helps.print_bot import print_put


def make_cnt_lab(tat_o: str, contry2: str, c_2_l: str, c_1_l: str, cona_1: str, cona_2: str, sps: str) -> str:
    """Construct a formatted string based on various input parameters."""

    cnt_la = c_1_l + sps + c_2_l

    if cona_1 in typeTable or cona_1 in Films_O_TT or cona_1.lower() in New_players:
        if cona_1.lower() in New_players:
            if c_2_l.startswith("أصل "):
                print_put(f'>>>>>> Add من to cona_1:"{cona_1}" cona_1 in New_players:')
                cnt_la = f"{(c_1_l + sps)}من {c_2_l}"
            else:
                print_put(f'>>>>>> Add في to cona_1:"{cona_1}" cona_1 in New_players:')
                cnt_la += " في "
        if cona_2 not in By_table:
            Films_O_TT[contry2] = cnt_la
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
                cnt_la = faxos.format(c_2_l)

        if cona_1 in pop_format2:
            print_put(f'<<lightblue>>>>>> cona_1 in pop_format2 "{pop_format2[cona_1]}":')
            cnt_la = pop_format2[cona_1].format(c_2_l)

    print_put(f'<<lightpurple>> >>>> contry_2_tit "{contry2}": cnt_la: {cnt_la}')
    cnt_la = cnt_la.replace("  ", " ")

    maren = re.match(r"\d\d\d\d", cona_2)

    if maren:
        if cona_1 == "war of" and cnt_la == f"الحرب في {cona_2}":
            cnt_la = f"حرب {cona_2}"
            print_put(f'<<lightpurple>> >>>> change cnt_la to "{cnt_la}".')

    if cnt_la.endswith(" في "):
        cnt_la = cnt_la[: -len(" في ")]
    return cnt_la
