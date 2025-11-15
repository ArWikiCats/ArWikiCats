#!/usr/bin/python3
"""
python3 core8/pwb.py make/make2_bots.ma_bots/country2_bot

# from ..ma_bots.country2_lab import get_lab_for_country2


"""
from typing import Any

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
from . import ye_ts_bot


def get_lab_for_country2(country: str, with_test_ye: bool = False, **kwargs: Any) -> str:
    """Retrieve laboratory information for a specified country."""

    country2_no_lower = country.strip()
    country2 = country.lower().strip()
    resolved_label = get_pop_All_18(country2, "")

    if not resolved_label:
        resolved_label = te_films(country2)
    if not resolved_label:
        resolved_label = nats.find_nat_others(country2)

    if not resolved_label:
        resolved_label = sport_lab_suffixes.get_teams_new(country2)

    if not resolved_label:
        resolved_label = parties_bot.get_parties_lab(country2)

    if not resolved_label:
        resolved_label = team_work.Get_team_work_Club(country2_no_lower)
    if not resolved_label:
        resolved_label = work_relations(country2)
    if not resolved_label:
        resolved_label = univer.te_universities(country2)
    if not resolved_label:
        resolved_label = Work_US_State(country2)
    if not resolved_label:
        resolved_label = work_peoples(country2)
    if not resolved_label:
        resolved_label = get_KAKO(country2)

    if not resolved_label:
        resolved_label = centries_years_dec.get(country2, "")

    if not resolved_label and country2.startswith("the "):
        resolved_label = get_pop_All_18(country2[len("the ") :], "")

    if not resolved_label and with_test_ye:
        resolved_label = ye_ts_bot.translate_general_category(country2, start_get_country2=False)

    if resolved_label:
        print_put(f'>> get_lab_for_country2 "{country2}": label: {resolved_label}')

    return resolved_label
