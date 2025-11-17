"""

"""

from typing import Dict, Tuple, Any


def get_from_starts_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str, bool]:
    list_of_cat = ""
    Find_wd = False

    for key, tab in data.items():
        if category3.startswith(key):
            list_of_cat = tab["lab"]

            # precise removal
            remove_key = tab.get("remove", key)

            category3 = category3.replace(remove_key, "", 1)

            Find_wd = tab.get("Find_wd") is True
            break

    return category3, list_of_cat, Find_wd


def get_from_endswith_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str, bool, bool]:
    list_of_cat = ""
    Find_wd = False
    Find_ko = False

    category3_original = category3
    for key, tab in data.items():
        if category3.endswith(key):
            list_of_cat = tab["lab"]

            # precise removal
            remove_key = tab.get("remove", key)

            category3 = category3_original.replace(remove_key, "", 1)
            Find_wd = tab.get("Find_wd") is True
            Find_ko = tab.get("Find_ko") is True
            break

    return category3, list_of_cat, Find_wd, Find_ko
