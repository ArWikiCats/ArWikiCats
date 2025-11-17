"""
"""

from typing import Dict, Tuple


def get_templates_fo(category3: str) -> Tuple[str, str]:
    """
    examples:
    Category:2016 American television episodes
    Category:Game of Thrones (season 1) episodes
    Category:Game of Thrones season 1 episodes
    """
    category3 = category3.strip()
    list_of_cat = ""

    dict_temps: Dict[str, str] = {
        "sidebar templates": "قوالب اشرطة جانبية {}",
        "politics and government templates": "قوالب سياسة وحكومة {}",
        "infobox templates": "قوالب معلومات {}",
        "squad templates": "قوالب تشكيلات {}",
    }

    for key, lab in dict_temps.items():
        if category3.endswith(key):
            list_of_cat = lab
            # remove the key ONLY from the end
            category3 = category3[: -len(key)].strip()
            break

    if not list_of_cat:
        list_of_cat = "قوالب {}"
        if category3.endswith(" templates"):
            category3 = category3[: -len(" templates")].strip()

    return list_of_cat, category3
