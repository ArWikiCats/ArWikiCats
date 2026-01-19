"""
Common Resolver Chain Module

"""

from __future__ import annotations

import functools

from ..helps import logger
from ..new_resolvers import all_new_resolvers, main_sports_resolvers
from ..new_resolvers.languages_resolves import resolve_languages_labels_with_time
from ..sub_new_resolvers.peoples_resolver import work_peoples
from ..sub_new_resolvers import team_work
from ..new_resolvers.sports_resolvers.raw_sports import (
    resolve_sport_label_by_jobs_key,
    wrap_team_xo_normal_2025_with_ends,
)
from ..time_formats.time_to_arabic import convert_time_to_arabic
from ..translations import People_key, get_from_pf_keys2
from .make_bots.bot_2018 import get_pop_All_18
from .matables_bots.table1_bot import get_KAKO
from .o_bots import parties_resolver, university_resolver


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
        all_new_resolvers(country2)
        or get_from_pf_keys2(country2)
        or get_pop_All_18(country2)
        or resolve_languages_labels_with_time(country2)
        or People_key.get(country2)
        or main_sports_resolvers(country2)
        or wrap_team_xo_normal_2025_with_ends(country2)
        or resolve_sport_label_by_jobs_key(country2)
        or parties_resolver.get_parties_lab(country2)
        or team_work.resolve_clubs_teams_leagues(country2)
        or university_resolver.resolve_university_category(country2)
        or work_peoples(country2)
        or get_KAKO(country2)
        or convert_time_to_arabic(country2)
        or get_pop_All_18(country2)
        or ""
    )
    logger.info(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label


__all__ = [
    "get_lab_for_country2",
]
