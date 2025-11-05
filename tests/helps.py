"""

from .tests.helps import get_titles_to_tests

"""

import sys
from src import printe


def get_titles_to_tests(lista):
    # ---
    to_work = []
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg == "-list":
            to_work = lista.get(value) or lista.get(int(value)) or []
            # ---
            if not to_work:
                printe.output(f"<<red>> {value} not in lista...")
                exit()

    # ---
    if not to_work:
        if len(sys.argv) > 1:
            to_work = [" ".join(sys.argv[1:])]
            print(to_work)
        else:
            to_work = lista[1]
    # ---
    return to_work
