#!/usr/bin/python3
"""

Usage:
from ..helps import len_print
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
from .. import printe
from humanize import naturalsize

lenth_pri_text = True


def lenth_pri(bot, tab, Max=10000, lens=[]):
    """Print formatted information based on the provided parameters.

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

    def do(x, y):
        if x in lens:
            return y
        return naturalsize(y, binary=True)

    faf = ", ".join([
        # f"<<lightpurple>>{x}<<default>>: {tab[x]}"
        f"<<lightpurple>>{x}<<default>>: {do(x, tab[x])}" for x in tab if tab[x] > Max
    ])
    if faf:
        printe.output(f"{bot}:".ljust(20) + faf)
