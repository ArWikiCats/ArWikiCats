""" """

from typing import Dict, Tuple

dict_temps: Dict[str, str] = {
    "templates": "قوالب {}",
    "squad templates": "قوالب تشكيلات {}",
}

sorted_data = dict(
    sorted(
        dict_temps.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    )
)


def get_templates_fo(category3: str) -> Tuple[str, str]:
    """
    Examples:
        category3="Category:2016 American television infobox templates"
    """
    category3 = category3.strip()
    list_of_cat = ""

    for key, lab in sorted_data.items():
        if category3.endswith(key):
            list_of_cat = lab
            # remove the key ONLY from the end
            category3 = category3[: -len(key)].strip()
            return list_of_cat, category3

    return "", category3
