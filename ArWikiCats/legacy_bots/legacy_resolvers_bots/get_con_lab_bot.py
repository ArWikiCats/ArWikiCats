#!/usr/bin/python3
"""

"""

import functools
from ...helps import logger
from ...new_resolvers import all_new_resolvers
from ...sub_new_resolvers import team_work
from ...translations import (
    get_from_new_p17_final,
    get_from_pf_keys2,
)
from .. import tmp_bot
from ..circular_dependency import country_bot
from ..common_resolver_chain import get_lab_for_country2
from ..make_bots import get_KAKO
from . import bys
from .bot_2018 import get_pop_All_18


def _lookup_country_with_by(country_lower: str) -> str:
    """Handle country labels with 'by' prefix or infix."""
    if country_lower.startswith("by "):
        return bys.make_by_label(country_lower)

    if " by " in country_lower:
        return bys.get_by_label(country_lower)

    return ""


def _lookup_country_with_in_prefix(country_lower: str) -> str:
    """Handle country labels with 'in ' prefix."""
    if not country_lower.strip().startswith("in "):
        return ""

    inner_country = country_lower.strip()[len("in ") :].strip()
    country_label = (
        ""
        or country_bot.get_country(inner_country)
        or get_lab_for_country2(inner_country)
        or get_pop_All_18(inner_country)
        or get_KAKO(inner_country)
    )
    if country_label:
        return f"في {country_label}"

    return ""


@functools.lru_cache(maxsize=10000)
def get_con_lab(separator: str, country: str, start_get_country2: bool = False) -> str:
    """Retrieve the corresponding label for a given country.

    Args:
        separator: The separator/delimiter.
        country: The country part of the category.
        start_get_country2: Whether to use the secondary country lookup.

    Returns:
        The Arabic label for the country.
    """
    separator = separator.strip()
    country_lower = country.strip().lower()
    country_no_dash = country_lower.replace("-", " ")

    for_table = {
        "for national teams": "للمنتخبات الوطنية",
        "for member-of-parliament": "لعضوية البرلمان",
    }

    label = get_pop_All_18(country_no_dash, "") or get_pop_All_18(country_lower, "")
    if label:
        logger.info(f"?????? get_con_lab early return: {country_lower=}, {label=}")
        return label

    lookup_chain = {
        "all_new_resolvers": lambda t: all_new_resolvers(t),
        "get_from_new_p17_final": lambda c: get_from_new_p17_final(c),
        "pf_keys2": lambda c: get_from_pf_keys2(c),
        "_lookup_country_with_by": _lookup_country_with_by,
        "for_table": lambda c: for_table.get(c, "") if separator.lower() == "for" else "",
        "_lookup_country_with_in_prefix": _lookup_country_with_in_prefix,
        "team_work.resolve_clubs_teams_leagues": lambda c: team_work.resolve_clubs_teams_leagues(c.strip()),
        "term_label": lambda c: country_bot.fetch_country_term_label(
            c, separator, start_get_country2=start_get_country2
        ),
        "tmp_bot.Work_Templates": tmp_bot.Work_Templates,
        "get_lab_for_country2": get_lab_for_country2,
        "get_pop_All_18": get_pop_All_18,
        "get_KAKO": get_KAKO,
    }
    label = ""

    for name, lookup_func in lookup_chain.items():
        label = lookup_func(country_lower)
        if label:
            logger.debug(f"get_con_lab({country_lower}): Found label '{label}' via {name}")
            break

    logger.info(f"?????? get_con_lab: {country_lower=}, {label=}")
    logger.info(f"?????? get_con_lab: {start_get_country2=}, {country=}, {separator=}")

    return label


__all__ = [
    "get_con_lab",
]
