"""

"""

from typing import Dict, Tuple, Any


def get_from_starts_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str, bool]:
    list_of_cat = ""
    Find_wd = False

    category3_original = category3

    try:
        sorted_data = sorted(data.items(), key=lambda x: x[0].count(" "), reverse=True)
    except AttributeError:
        sorted_data = data.items()

    for key, tab in sorted_data:

        # precise removal
        remove_key = tab.get("remove", key)
        if category3_original.startswith(remove_key):
            list_of_cat = tab["lab"]

            category3 = category3_original[len(remove_key):]  # .lstrip()

            Find_wd = tab.get("Find_wd") is True
            break

    return category3, list_of_cat, Find_wd


def get_from_endswith_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str, bool, bool]:
    list_of_cat = ""
    Find_wd = False
    Find_ko = False

    category3_original = category3

    try:
        sorted_data = sorted(data.items(), key=lambda x: x[0].count(" "), reverse=True)
    except AttributeError:
        sorted_data = data.items()

    for key, tab in sorted_data:

        if category3_original.endswith(key):
            list_of_cat = tab["lab"]

            # precise removal
            remove_key = tab.get("remove", key)

            category3 = category3_original[: -len(remove_key)]#.strip()

            Find_wd = tab.get("Find_wd") is True
            Find_ko = tab.get("Find_ko") is True

            break

    return category3, list_of_cat, Find_wd, Find_ko
