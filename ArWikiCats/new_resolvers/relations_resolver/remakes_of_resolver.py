#!/usr/bin/python3
""" """

import functools

from ...helps import logger
from ...translations import All_Nat
from ...translations_formats import format_multi_data_v2


def fix_keys(category: str) -> str:
    """Fix known issues in category keys before searching.

    Args:
        category: The original category key.
    """
    # Fix specific known issues with category keys
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    return category.strip()


@functools.lru_cache(maxsize=1)
def _load_remakes_of_bot():
    """Load the remakes of bot using All_Nat and format_multi_data_v2."""
    formatted_data = {
        "{en} remakes of {en2} films": "أفلام {female} مأخوذة من أفلام {female2}",
        "{en} remakes of {en2} television series": "مسلسلات تلفزيونية {female} مأخوذة من مسلسلات تلفزيونية {female2}",
        "television remakes of films": "مسلسلات تلفزيونية مأخوذة من أفلام",
    }

    # Prepare data_list from All_Nat for the first element {en}
    # We use 'female' for the nationality to match "أفلام أمريكية" or "مسلسلات تلفزيونية أمريكية"
    # Filter out empty strings to avoid partial matches
    data_list = {
        k: {
            "female": v["female"],
        }
        for k, v in All_Nat.items()
        if v.get("female") and v["female"].strip()
    }

    # Prepare data_list2 from All_Nat for the second element {en2}
    # This element represents the original film/series nationality
    data_list2 = {
        k: {
            "female2": v["female"],
        }
        for k, v in All_Nat.items()
        if v.get("female") and v["female"].strip()
    }

    # Add "silent" to data_list2
    data_list2["silent"] = {"female2": "صامتة"}

    return format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{en}",
        data_list2=data_list2,
        key2_placeholder="{en2}",
    )


@functools.lru_cache(maxsize=10000)
def resolve_remakes_of_resolver(category: str) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start resolve_remakes_of_resolver: {category=}")

    # Handling special case: "television remakes of films"
    if category == "television remakes of films":
        return "مسلسلات تلفزيونية مأخوذة من أفلام"

    bot = _load_remakes_of_bot()
    result = bot.search(category)
    if result:
        return result

    return ""


__all__ = [
    "resolve_remakes_of_resolver",
]
