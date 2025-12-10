#!/usr/bin/python3
"""
python3 core8/pwb.py make/make_bots.ma_bots/country2_bot

# from ..ma_bots.country2_lab import get_lab_for_country2


TODO: need refactoring

"""

from ...helps.log import logger
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.table1_bot import get_KAKO
from ..media_bots.films_bot import te_films
from ..o_bots import parties_bot, univer
from ..o_bots.popl import work_peoples
from ..o_bots.rele import work_relations
from ..p17_bots import nats_other
from ...translations_resolvers.us_states import resolve_us_states
from ..sports_bots import sport_lab_suffixes, team_work
from ...new.time_to_arabic import convert_time_to_arabic
from ...translations import get_from_pf_keys2
from ...translations.sports_formats_national.sport_lab_nat import sport_lab_nat_load_new

# Dictionary of resolvers mapped to their callable functions
resolvers = {
    "get_pop_All_18": get_pop_All_18,
    "te_films": te_films,
    "sport_lab_nat_load_new": sport_lab_nat_load_new,
    "nats.find_nat_others": nats_other.find_nat_others,
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
        return result

    # No resolver succeeded
    return ""


def get_lab_for_country2(country: str) -> str:
    """Retrieve laboratory information for a specified country."""

    country2 = country.lower().strip()
    resolved_label = work_relations(country2)

    if not resolved_label:
        resolved_label = get_from_pf_keys2(country2)

    if not resolved_label:
        resolved_label = resolve_all(country2)

    if not resolved_label:
        resolved_label = convert_time_to_arabic(country2)

    if not resolved_label and country2.startswith("the "):
        resolved_label = get_pop_All_18(country2[len("the ") :], "")

    if resolved_label:
        logger.info(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label
