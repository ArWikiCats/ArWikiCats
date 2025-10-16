#!/usr/bin/python3
"""

from ..jobs_bots.get_helps import get_con_3

"""
from typing import Dict, Tuple, List, Any
from ...helps.print_bot import output_test4

get_con_cash: Dict[Tuple[str, str], Tuple[str, str]] = {}


def get_con_3(cate: str, keys: List[str], Type: str) -> Tuple[str, str]:
    """Retrieve country information based on category and keys.

    This function checks if a given category and type tuple exists in a
    cached dictionary. If it does, it returns the cached result. If not, it
    processes the provided keys to extract relevant country information. The
    function looks for specific patterns in the keys and modifies the
    category string accordingly. The results are then cached for future
    reference.

    Args:
        cate (str): The category string to be processed.
        keys (list): A list of keys to match against the category.
        Type (str): The type of information being processed, e.g., "nat".

    Returns:
        tuple: A tuple containing the modified category string and the
        corresponding country name, or empty strings if no match is found.
    """

    # ---
    T_uple = (cate, Type)
    # ---
    if T_uple in get_con_cash:
        return get_con_cash[T_uple]
    # ---
    fo_3: str = ""
    contry_start: str = ""
    # ---
    for key in keys:
        tables: Dict[int, str] = {}
        if not fo_3:
            # ---
            tables[2] = f"{key.lower()} "
            # ---
            # tables[1] = key.lower().strip() + " people "
            if Type == "nat":
                tables[1] = f"{key.lower().strip()} people "
            # ---
            if key.startswith("the "):
                tables[3] = key[len("the ") :]  #
            # ---
            for key_d in [1, 2, 3, 4]:
                if fo_3 == "" and tables.get(key_d):
                    if cate.lower().startswith(tables[key_d].lower()):
                        contry_start = key
                        fo_3 = cate[len(tables[key_d]) :].strip()
                        output_test4(
                            f'<<lightyellow>>>>>> get_con_3 start_th key_:{key_d} ("{tables[key_d]}"), fo_3:"{fo_3}",contry_start:"{contry_start}"'
                        )
                        break
    # ---
    get_con_cash[T_uple] = (fo_3, contry_start)
    # ---
    if fo_3 and contry_start:
        output_test4(f'<<lightpurple>>>>>> test_4.py contry_start:"{contry_start}",get_con_3 fo_3:"{fo_3}",Type:{Type}')
    # ---
    return fo_3, contry_start
