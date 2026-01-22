#!/usr/bin/python3
""" """

import functools

from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...sub_new_resolvers import team_work
from ...translations import (
    get_from_new_p17_final,
    get_from_pf_keys2,
)
from .. import tmp_bot
from ..common_resolver_chain import get_lab_for_country2
from ..make_bots import get_KAKO
from . import bys
from .bot_2018 import get_pop_All_18


def _lookup_country_with_by(country: str) -> str:
    """Handle country labels with 'by' prefix or infix."""
    if country.startswith("by "):
        return bys.make_by_label(country)

    if " by " in country:
        return bys.get_by_label(country)

    return ""


def _lookup_country_with_in_prefix(country: str) -> str:
    """Handle country labels with 'in ' prefix."""
    if not country.strip().startswith("in "):
        return ""

    inner_country = country.strip()[len("in ") :].strip()
    country_label = (
        ""
        or get_lab_for_country2(inner_country)
        or get_pop_All_18(inner_country)
        or get_KAKO(inner_country)
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
        "_lookup_country_with_by": _lookup_country_with_by,
        "_lookup_country_with_in_prefix": _lookup_country_with_in_prefix,
        "team_work.resolve_clubs_teams_leagues": lambda c: team_work.resolve_clubs_teams_leagues(c.strip()),
        "tmp_bot.Work_Templates": tmp_bot.Work_Templates,
        "get_lab_for_country2": get_lab_for_country2,
        "get_pop_All_18": get_pop_All_18,
        "get_KAKO": get_KAKO,
    }
    label = ""

    for name, lookup_func in lookup_chain.items():
        label = lookup_func(country)
        if label:
            logger.debug(f"get_con_label({country}): Found label '{label}' via {name}")
            break

    logger.info(f"?????? get_con_label: {country=}, {label=}")

    return label


__all__ = [
    "get_con_label",
]
