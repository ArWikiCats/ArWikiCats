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

import json
import sys
from typing import Iterable, Mapping
from .. import printe
from humanize import naturalsize

lenth_pri_text = True

all_len = {}


def lenth_pri(
    bot: str,
    tab: Mapping[str, int | float],
    Max: int=10000,
    lens: Iterable[str] | None=None,
) -> None:
    lens = lens or []
    """
    Print formatted information based on the provided parameters.

    This function checks if certain conditions are met before printing a
    formatted string that includes the keys and values from the `tab`
    dictionary. It filters the entries based on a maximum value (`Max`) and
    applies a specific formatting style to the output. The function also
    utilizes a nested helper function to determine how to format the values
    based on their presence in the `lens` list.

    Args:
        bot (str): A string identifier used in the output.
        tab (dict): A dictionary containing key-value pairs to be processed.
        Max (int?): The threshold value for filtering entries. Defaults to 10000.
        lens (list?): A list of keys for special formatting. Defaults to an empty list.

    Returns:
        None: This function does not return a value; it prints output directly.
    """

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

    all_len.setdefault(bot, {})

    all_len[bot].update({
        x: format_size(x, tab[x])
        for x in tab
    })

    if formatted_entries:
        printe.output(f"{bot}:".ljust(20) + formatted_entries)


def dump_all_len(file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(all_len, f, ensure_ascii=False, indent=4)
