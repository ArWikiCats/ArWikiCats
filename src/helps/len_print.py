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

import importlib.util
import sys
from .. import printe

if importlib.util.find_spec("humanize") is not None:
    from humanize import naturalsize  # type: ignore
else:

    def naturalsize(value, binary=True):
        """Minimal replacement for :func:`humanize.naturalsize`."""

        try:
            size = float(value)
        except (TypeError, ValueError):
            return str(value)

        base = 1024.0 if binary else 1000.0
        suffixes = [
            "B",
            "KiB" if binary else "KB",
            "MiB" if binary else "MB",
            "GiB" if binary else "GB",
            "TiB" if binary else "TB",
            "PiB" if binary else "PB",
        ]

        index = 0
        while size >= base and index < len(suffixes) - 1:
            size /= base
            index += 1

        if index == 0:
            return f"{int(size)} {suffixes[index]}"
        return f"{size:.1f} {suffixes[index]}"

lenth_pri_text = True


def lenth_pri(bot, tab, Max=10000, lens=None):
    if lens is None:
        lens = []
    if not lenth_pri_text:
        return
    if "printhead" in sys.argv or "lenth_pri_text" in sys.argv:
        return

    def format_size(key, value):
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
