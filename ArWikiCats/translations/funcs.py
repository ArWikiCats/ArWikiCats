"""
Data translations and mappings for the ArWikiCats project.
This package aggregates translation data for various categories including
geography, jobs, languages, nationalities, sports, and media.
"""

import functools
import re
from ..helps import logger
from .geo.labels_country import ALIASES_CHAIN, get_from_new_p17_final
from .mixed.all_keys2 import pf_keys2
from .utils.json_dir import open_json_file

# Match "X and Y" patterns
AND_PATTERN = re.compile(r"^(.*?) and (.*)$", flags=re.IGNORECASE)


@functools.lru_cache(maxsize=10000)
def get_and_label(category: str) -> str:
    """
    Resolve the Arabic label for a category composed of two entities separated by "and".

    Parameters:
        category (str): A category string containing two entity names joined by "and" (e.g., "X and Y").

    Returns:
        str: "`<first_label> و<last_label>`" if both entities map to Arabic labels, empty string otherwise.
    """
    if " and " not in category:
        return ""

    logger.info(f"<<lightyellow>>>>get_and_label {category}")
    logger.info(f"Resolving get_and_label, {category=}")
    match = AND_PATTERN.match(category)

    if not match:
        logger.debug(f"<<lightyellow>>>> No match found for get_and_label: {category}")
        return ""

    first_part, last_part = match.groups()
    first_part = first_part.lower()
    last_part = last_part.lower()

    logger.debug(f"<<lightyellow>>>> get_and_label(): {first_part=}, {last_part=}")

    first_label = get_from_new_p17_final(first_part, None)  # or get_pop_All_18(first_part) or ""

    last_label = get_from_new_p17_final(last_part, None)  # or get_pop_All_18(last_part) or ""

    logger.debug(f"<<lightyellow>>>> get_and_label(): {first_label=}, {last_label=}")

    label = ""
    if first_label and last_label:
        label = f"{first_label} و{last_label}"
        logger.info(f"<<lightyellow>>>>get_and_label lab {label}")

    return label


def get_from_pf_keys2(text: str) -> str:
    """Look up the Arabic label for a term in the ``pf_keys2`` mapping."""
    label = pf_keys2.get(text, "")
    logger.info(f">> get_from_pf_keys2() Found: {label}")
    return label


__all__ = [
    "open_json_file",
    "get_and_label",
    "get_from_new_p17_final",
    "get_from_pf_keys2",
]
