""" """

from typing import Any, Dict, Tuple


def get_from_starts_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str]:
    """Strip matching prefixes from ``category3`` based on provided patterns."""
    list_of_cat = ""

    category3_original = category3

    try:
        sorted_data = sorted(
            data.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    except AttributeError:
        sorted_data = data.items()

    for key, tab in sorted_data:
        # precise removal
        remove_key = tab.get("remove", key)
        if category3_original.startswith(remove_key):
            list_of_cat = tab["lab"]

            category3 = category3_original[len(remove_key) :]  # .lstrip()

            break

    return category3, list_of_cat


def get_from_endswith_dict(category3: str, data: Dict[str, Dict[str, Any]]) -> Tuple[str, str]:
    """Strip matching suffixes from ``category3`` based on provided patterns."""
    list_of_cat = ""

    category3_original = category3

    try:
        sorted_data = sorted(
            data.items(),
            key=lambda k: (-k[0].count(" "), -len(k[0])),
        )
    except AttributeError:
        sorted_data = data.items()

    for key, tab in sorted_data:
        if category3_original.endswith(key):
            list_of_cat = tab["lab"]

            # precise removal
            remove_key = tab.get("remove", key)

            category3 = category3_original[: -len(remove_key)]  # .strip()

            break

    return category3, list_of_cat
