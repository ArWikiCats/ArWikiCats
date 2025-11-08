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
from typing import Iterable, Mapping
from .. import printe
from humanize import naturalsize

lenth_pri_text = True


def lenth_pri(
    bot: str,
    tab: Mapping[str, int | float],
    Max: int=10000,
    lens: Iterable[str] | None=None,
) -> None:
    if lens is None:
        lens = []
    if not lenth_pri_text:
        return
    if "printhead" in sys.argv or "lenth_pri_text" in sys.argv:
        return

    def format_size(key: str, value: int | float) -> str:
        if key in lens:
            return value
        return naturalsize(value, binary=True)

    formatted_entries = ", ".join(
        [
            # f"<<lightpurple>>{x}<<default>>: {tab[x]}"
            f"<<lightpurple>>{x}<<default>>: {format_size(x, tab[x])}"
            for x in tab
            if tab[x] > Max
        ]
    )
    if formatted_entries:
        printe.output(f"{bot}:".ljust(20) + formatted_entries)
