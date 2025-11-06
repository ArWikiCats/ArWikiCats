#!/usr/bin/python3
"""

Usage:
from .helps import len_print
# ---
# len_print.enable_length_printing = False
# ---
Lentha = {
    "New_P17_Finall": sys.getsizeof(New_P17_Finall),
    "opop": sys.getsizeof(opop),
    "the_keys": the_keys,
}
# ---
len_print.print_lengths("Labels_Contry.py", Lentha)

"""

import sys
from .. import printe
from humanize import naturalsize

enable_length_printing = True


def print_lengths(script_name, size_map, max_size=10000, lens=[]):
    if not enable_length_printing:
        return
    if "printhead" in sys.argv or "enable_length_printing" in sys.argv:
        return

    def do(x, y):
        if x in lens:
            return y
        return naturalsize(y, binary=True)

    output_string = ", ".join(
        [
            # f"<<lightpurple>>{x}<<default>>: {size_map[x]}"
            f"<<lightpurple>>{x}<<default>>: {do(x, size_map[x])}"
            for x in size_map
            if size_map[x] > max_size
        ]
    )
    if output_string:
        printe.output(f"{script_name}:".ljust(20) + output_string)
