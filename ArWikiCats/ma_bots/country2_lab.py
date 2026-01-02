#!/usr/bin/python3
"""
"""

import functools

from ..helps.log import logger
from ..make_bots.films_and_others_bot import te_films
from ..make_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make_bots.matables_bots.table1_bot import get_KAKO
from ..make_bots.o_bots import parties_bot, univer
from ..make_bots.o_bots.peoples_resolver import work_peoples
from ..make_bots.reslove_relations.rele import resolve_relations_label
from ..make_bots.sports_bots import sport_lab_suffixes, team_work
from ..new_resolvers.countries_names_resolvers.us_states import resolve_us_states
from ..new_resolvers.sports_resolvers.sport_lab_nat import sport_lab_nat_load_new
from ..time_resolvers.time_to_arabic import convert_time_to_arabic
from ..translations import get_from_pf_keys2


@functools.lru_cache(maxsize=10000)
def get_lab_for_country2(country: str) -> str:
    """Retrieve laboratory information for a specified country."""

    country2 = country.lower().strip()

    resolved_label = (
        resolve_relations_label(country2)
        or get_from_pf_keys2(country2)
        or get_pop_All_18(country2)
        or te_films(country2)
        or sport_lab_nat_load_new(country2)
        or sport_lab_suffixes.get_teams_new(country2)
        or parties_bot.get_parties_lab(country2)
        or team_work.Get_team_work_Club(country2)
        or univer.te_universities(country2)
        or resolve_us_states(country2)
        or work_peoples(country2)
        or get_KAKO(country2)
        or convert_time_to_arabic(country2)
        or get_pop_All_18(country2)
        or ""
    )
    logger.info(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label
