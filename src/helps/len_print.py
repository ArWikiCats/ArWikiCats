#!/usr/bin/python3
"""

Usage:
from .helps import len_print
# ---
# len_print.lenth_pri_text = False
# ---
Lentha = {
    "New_P17_Finall": sys.getsizeof(New_P17_Finall),
    "opop": sys.getsizeof(opop),
    "the_keys": the_keys,
}
# ---
len_print.lenth_pri("Labels_Contry.py", Lentha)

"""

import sys
from ..ma_lists.helps import printe
from humanize import naturalsize

lenth_pri_text = True


def lenth_pri(bot, tab, Max=10000, lens=[]):
    if not lenth_pri_text:
        return
    if "printhead" in sys.argv or "lenth_pri_text" in sys.argv:
        return

    def do(x, y):
        if x in lens:
            return y
        return naturalsize(y, binary=True)

    faf = ", ".join(
        [
            # f"<<lightpurple>>{x}<<default>>: {tab[x]}"
            f"<<lightpurple>>{x}<<default>>: {do(x, tab[x])}"
            for x in tab
            if tab[x] > Max
        ]
    )
    if faf:
        printe.output(f"{bot}:".ljust(20) + faf)
