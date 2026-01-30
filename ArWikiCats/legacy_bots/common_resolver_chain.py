"""
Common Resolver Chain Module

"""

from __future__ import annotations

import functools
import logging

from ..new_resolvers import all_new_resolvers
from ..sub_new_resolvers import parties_resolver, team_work, university_resolver
from ..sub_new_resolvers.peoples_resolver import work_peoples
from ..translations import (
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    religious_entries,
)
from ..translations.funcs import get_from_new_p17_final, get_from_pf_keys2
from .legacy_resolvers_bots.bot_2018 import get_pop_All_18
from .make_bots import get_KAKO

logger = logging.getLogger(__name__)


def _lookup_country_with_in_prefix(country: str) -> str:
    """
    Strip a leading "in " from the input and, if the inner term has a resolvable Arabic label, return that label prefixed with "في ".

    Parameters:
        country (str): Input label; may start with the prefix "in ".

    Returns:
        str: `"في <label>"` when `country` starts with "in " and the inner term resolves to an Arabic label, otherwise an empty string.
    """
    if not country.strip().startswith("in "):
        return ""

    inner_country = country.strip()[len("in ") :].strip()
    country_label = (
        "" or get_lab_for_country2(inner_country) or get_pop_All_18(inner_country) or get_KAKO(inner_country)
    )
    if country_label:
        return f"في {country_label}"

    return ""


# Lookup chain for country labels - defined after all functions are available
con_lookup_both = {
    "get_from_new_p17_final": get_from_new_p17_final,
    "all_new_resolvers": all_new_resolvers,
    "get_from_pf_keys2": get_from_pf_keys2,
    "_lookup_country_with_in_prefix": _lookup_country_with_in_prefix,
    "_lookup_religious_males": lambda t: RELIGIOUS_KEYS_PP.get(t, {}).get("males", ""),
    "New_female_keys": lambda t: New_female_keys.get(t, ""),
    "religious_entries": lambda t: religious_entries.get(t, ""),
    "team_work.resolve_clubs_teams_leagues": team_work.resolve_clubs_teams_leagues,
    "get_parties_lab": parties_resolver.get_parties_lab,
    "resolve_university_category": university_resolver.resolve_university_category,
    "work_peoples": work_peoples,
    "get_pop_All_18": get_pop_All_18,
    "get_KAKO": get_KAKO,
}


@functools.lru_cache(maxsize=10000)
def get_con_label(country: str) -> str:
    """
    Resolve the Arabic label for a country or category name.

    The input is normalized and matched against a chain of resolver sources; a special case returns the Arabic label for "people". If no resolver yields a result, an empty string is returned.

    Parameters:
        country (str): Country or category name to resolve.

    Returns:
        str: Arabic label for the given country/category, or an empty string if not found.
    """
    country = country.strip().lower()
    country = country.replace(" the ", " ").removeprefix("the ").removesuffix(" the")

    if country == "people":
        return "أشخاص"

    country_no_dash = country.replace("-", " ")

    label = get_pop_All_18(country_no_dash, "") or get_pop_All_18(country, "")
    if label:
        logger.info(f"??????  early return: {country=}, {label=}")
        return label

    for name, lookup_func in con_lookup_both.items():
        label = lookup_func(country) or lookup_func(country_no_dash)
        if label:
            logger.debug(f"({country}): Found label '{label}' via {name}")
            break

    # Normalize whitespace in the label
    label = " ".join(label.strip().split())
    logger.info(f"?????? {country=}, {label=}")
    return label


@functools.lru_cache(maxsize=10000)
def get_lab_for_country2(country: str) -> str:
    """
    Return the Arabic label for a country or category.

    Lookup is case- and surrounding-whitespace-insensitive. If a label cannot be resolved, returns an empty string.

    Parameters:
        country (str): Country or category name to resolve.

    Returns:
        str: The resolved Arabic label, or an empty string if none was found.
    """

    country2 = country.lower().strip()

    resolved_label = (
        ""
        or all_new_resolvers(country2)
        or get_from_pf_keys2(country2)
        or parties_resolver.get_parties_lab(country2)
        or team_work.resolve_clubs_teams_leagues(country2)
        or university_resolver.resolve_university_category(country2)
        or work_peoples(country2)
        or ""
    )
    logger.info(f'>> "{country2}": label: {resolved_label}')

    return resolved_label


get_type_lab = get_con_label

__all__ = [
    "get_lab_for_country2",
    "get_con_label",
    "get_type_lab",
]
