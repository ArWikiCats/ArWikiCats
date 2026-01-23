"""
Common Resolver Chain Module

"""

from __future__ import annotations

import functools

from ..helps import logger
from ..new_resolvers import all_new_resolvers
from ..sub_new_resolvers import parties_resolver, team_work, university_resolver
from ..sub_new_resolvers.peoples_resolver import work_peoples
from ..translations import (
    People_key,
    get_from_pf_keys2,
    RELIGIOUS_KEYS_PP,
    New_female_keys,
    get_from_new_p17_final,
    religious_entries,
)

from .make_bots import get_KAKO
from .legacy_resolvers_bots.bot_2018 import get_pop_All_18


def _lookup_country_with_in_prefix(country: str) -> str:
    """Handle country labels with 'in ' prefix."""
    if not country.strip().startswith("in "):
        return ""

    inner_country = country.strip()[len("in ") :].strip()
    country_label = (
        "" or get_lab_for_country2(inner_country) or get_pop_All_18(inner_country) or get_KAKO(inner_country)
    )
    if country_label:
        return f"في {country_label}"

    return ""


@functools.lru_cache(maxsize=10000)
def get_con_label(country: str) -> str:
    """Retrieve the corresponding label for a given country.

    Args:
        country: The country part of the category.

    Returns:
        The Arabic label for the country.
    """
    country = country.strip().lower()
    country = country.replace(" the ", " ").removeprefix("the ").removesuffix(" the")

    country_no_dash = country.replace("-", " ")

    label = get_pop_All_18(country_no_dash, "") or get_pop_All_18(country, "")
    if label:
        logger.info(f"?????? get_con_label early return: {country=}, {label=}")
        return label

    lookup_chain = {
        "all_new_resolvers": lambda t: all_new_resolvers(t),
        "get_from_new_p17_final": lambda c: get_from_new_p17_final(c),
        "pf_keys2": lambda c: get_from_pf_keys2(c),
        "_lookup_country_with_in_prefix": _lookup_country_with_in_prefix,
        "team_work.resolve_clubs_teams_leagues": lambda c: team_work.resolve_clubs_teams_leagues(c.strip()),
        "get_lab_for_country2": get_lab_for_country2,
        "get_pop_All_18": get_pop_All_18,
        "get_KAKO": get_KAKO,
    }
    label = ""

    for name, lookup_func in lookup_chain.items():
        label = lookup_func(country) or lookup_func(country_no_dash)
        if label:
            logger.debug(f"get_con_label({country}): Found label '{label}' via {name}")
            break

    logger.info(f"?????? get_con_label: {country=}, {label=}")

    return label


def _lookup_religious_males(type_lower: str) -> str:
    """Look up religious keys for males."""
    return RELIGIOUS_KEYS_PP.get(type_lower, {}).get("males", "")


@functools.lru_cache(maxsize=10000)
def get_type_lab(type_value: str) -> str:
    """Determine the type label based on input parameters.

    Args:
        type_value: The type part of the category.

    Returns:
        - label: The Arabic label for the type
    """
    logger.debug(f"get_type_lab, {type_value=}")

    type_lower = type_value.lower()

    if type_lower == "people":
        return "أشخاص"

    label = ""
    lookup_chain = {
        "get_from_new_p17_final": get_from_new_p17_final,
        "all_new_resolvers": all_new_resolvers,
        "_lookup_religious_males": _lookup_religious_males,
        "New_female_keys": lambda t: New_female_keys.get(t, ""),
        "religious_entries": lambda t: religious_entries.get(t, ""),
        "team_work.resolve_clubs_teams_leagues": team_work.resolve_clubs_teams_leagues,
        "get_lab_for_country2": get_lab_for_country2,
        "get_pop_All_18": get_pop_All_18,
        "get_KAKO": get_KAKO,
    }

    for name, lookup_func in lookup_chain.items():
        label = lookup_func(type_lower)
        if label:
            logger.debug(f"get_type_lab({type_lower}): Found label '{label}' via {name}")
            break
    # Normalize whitespace in the label
    label = " ".join(label.strip().split())

    logger.info(f"?????? get_type_lab: {type_lower=}, {label=}")

    return label


@functools.lru_cache(maxsize=10000)
def get_lab_for_country2(country: str) -> str:
    """Retrieve Arabic label information for a specified country.

    This function attempts to find the Arabic label for a given country
    by querying multiple data sources in sequence.

    Args:
        country: The country name to look up

    Returns:
        The Arabic label for the country or an empty string if not found
    """

    country2 = country.lower().strip()

    resolved_label = (
        ""
        or all_new_resolvers(country2)
        or get_from_pf_keys2(country2)
        or People_key.get(country2)
        or parties_resolver.get_parties_lab(country2)
        or team_work.resolve_clubs_teams_leagues(country2)
        or university_resolver.resolve_university_category(country2)
        or work_peoples(country2)
        or ""
    )
    logger.info(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label


__all__ = [
    "get_lab_for_country2",
]
