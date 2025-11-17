#!/usr/bin/python3
"""
python3 core8/pwb.py make/make2_bots.ma_bots/country2_bot

# from ..ma_bots.country2_lab import get_lab_for_country2


"""
from ...helps.print_bot import print_put
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.centries_bot import centries_years_dec
from ..matables_bots.table1_bot import get_KAKO
from ..media_bots.films_bot import te_films
from ..sports_bots import sport_lab_suffixes
from ..o_bots import univer, parties_bot
from ..o_bots.popl import work_peoples
from ..o_bots.rele import work_relations
from ..p17_bots import nats
from ..p17_bots.us_stat import Work_US_State
from ..sports_bots import team_work

# Dictionary of resolvers mapped to their callable functions
resolvers = {
    "get_pop_All_18": get_pop_All_18,
    "te_films": te_films,
    "nats.find_nat_others": nats.find_nat_others,
    "sport_lab_suffixes.get_teams_new": sport_lab_suffixes.get_teams_new,
    "parties_bot.get_parties_lab": parties_bot.get_parties_lab,
    "team_work.Get_team_work_Club": team_work.Get_team_work_Club,
    "work_relations": work_relations,
    "univer.te_universities": univer.te_universities,
    "Work_US_State": Work_US_State,
    "work_peoples": work_peoples,
    "get_KAKO": get_KAKO,
}


def resolve_all(country2):
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
            raise TypeError(
                f"Resolver '{name}' returned non-string type {type(result)}: {result}"
            )

        # Valid str → return
        return result

    # No resolver succeeded
    return ""


def get_lab_for_country2(country: str) -> str:
    """Retrieve laboratory information for a specified country."""

    country2 = country.lower().strip()
    resolved_label = resolve_all(country2)

    if not resolved_label:
        resolved_label = centries_years_dec.get(country2, "")

    if not resolved_label and country2.startswith("the "):
        resolved_label = get_pop_All_18(country2[len("the ") :], "")

    if resolved_label:
        print_put(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label
