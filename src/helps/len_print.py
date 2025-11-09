#!/usr/bin/python3
"""

Usage:
from .helps import len_print
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
from typing import Any, List, Optional, Union, Iterable, Mapping
from .printe_helper import make_str
from humanize import naturalsize
from ..config import print_settings
from .log import logger

all_len = {}


def format_size(key: str, value: int | float, lens: List[Union[str, Any]]) -> str:
    if key in lens:
        return value
    return naturalsize(value, binary=True)


def _lenth_pri(
    bot: str,
    tab: Mapping[str, int | float],
    Max: int=10000,
    lens: Iterable[str] | None=None,
) -> str:
    """
    Print formatted information based on the provided parameters.
    """
    formatted_entries = ", ".join(
        [
            # f"<<lightpurple>>{x}<<default>>: {tab[x]}"
            f"<<lightpurple>>{x}<<default>>: {format_size(x, tab[x], lens)}"
            for x in tab
            if tab[x] > Max
        ]
    )
    if not formatted_entries:
        return ""

    text = f"{bot}:".ljust(20) + formatted_entries
    return text


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

    data = {
        x: format_size(x, tab[x], lens)
        for x in tab
    }

    if not data:
        return

    all_len.setdefault(bot, {})
    all_len[bot].update(data)

    if not print_settings.print_memory_usage or print_settings.noprint:
        return

    text = _lenth_pri(bot, tab, Max, lens)

    if print_settings.print_memory_usage:
        print(make_str(text))
    else:
        logger.debug(text)


def dump_all_len(file):
    # sort all_len by keys ignore case
    all_len_save = dict(sorted(all_len.items(), key=lambda item: item[0].lower()))

    with open(file, "w", encoding="utf-8") as f:
        json.dump(all_len_save, f, ensure_ascii=False, indent=4)
