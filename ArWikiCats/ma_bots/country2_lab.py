#!/usr/bin/python3
"""
"""

from ..helps.log import logger
from ..make_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make_bots.matables_bots.table1_bot import get_KAKO
from ..make_bots.media_bots.films_bot import te_films
from ..make_bots.o_bots import parties_bot, univer
from ..make_bots.o_bots.peoples_resolver import work_peoples
from ..make_bots.reslove_relations.rele import resolve_relations_label
from ..new_resolvers.translations_resolvers.us_states import resolve_us_states
from ..make_bots.sports_bots import sport_lab_suffixes, team_work
from ..time_resolvers.time_to_arabic import convert_time_to_arabic
from ..translations import get_from_pf_keys2
from ..new_resolvers.sports_formats_teams.sport_lab_nat import sport_lab_nat_load_new

# Dictionary of resolvers mapped to their callable functions
resolvers = {
    "get_pop_All_18": get_pop_All_18,
    "te_films": te_films,
    "sport_lab_nat_load_new": sport_lab_nat_load_new,
    "sport_lab_suffixes.get_teams_new": sport_lab_suffixes.get_teams_new,
    "parties_bot.get_parties_lab": parties_bot.get_parties_lab,
    "team_work.Get_team_work_Club": team_work.Get_team_work_Club,
    "univer.te_universities": univer.te_universities,
    "resolve_us_states": resolve_us_states,
    "work_peoples": work_peoples,
    "get_KAKO": get_KAKO,
}


def resolve_all(country2) -> str:
    """
    Iterate through all resolver functions. Return the first valid string.
    If any resolver returns a dict, raise an error showing exactly which resolver failed.
    """
    for name, func in resolvers.items():
        result = func(country2)

        # If empty or None → skip
        if not result:
            continue

        # If not a string → also an error
        if not isinstance(result, str):
            raise TypeError(f"Resolver '{name}' returned non-string type {type(result)}: {result}")

        # Valid str → return
        if result:
            logger.info(f'>> resolve_all "{country2}": label: {result}')
            return result

    # No resolver succeeded
    return ""


def get_lab_for_country2(country: str) -> str:
    """Retrieve laboratory information for a specified country."""

    country2 = country.lower().strip()

    resolved_label = (
        resolve_relations_label(country2) or
        get_from_pf_keys2(country2) or
        resolve_all(country2) or
        convert_time_to_arabic(country2) or
        ""
    )
    if not resolved_label and country2.startswith("the "):
        resolved_label = get_pop_All_18(country2[len("the ") :], "")

    logger.info(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label
