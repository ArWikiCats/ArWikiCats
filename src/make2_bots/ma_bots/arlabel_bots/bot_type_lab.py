#!/usr/bin/python3
"""
from .arlabel_bots.bot_type_lab import get_Type_lab

"""
from typing import Tuple
from .. import country2_lab
from ...o_bots.popl import make_people_lab
from ...sports_bots import team_work

from ...bots import tmp_bot
from ...p17_bots import nats
from ...jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs
from ...media_bots.films_bot import test_films
from .. import event2bot

from ....ma_lists import New_P17_Finall
from ....ma_lists import RELIGIOUS_KEYS_PP
from ....ma_lists import New_female_keys

from ...format_bots import Tabl_with_in

from ....helps.print_bot import print_put, output_test

from ..country_bot import Get_c_t_lab


def get_Type_lab(preposition: str, type_value: str, type_lower: str, country_lower: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters."""

    normalized_preposition = preposition.strip()

    type_label = ""
    if type_lower == "women" and normalized_preposition == "from":
        type_label = "نساء"
        print_put(f'>> >> >> Make type_label "{type_label}".')

    elif type_lower == "women of":
        type_label = "نساء من"
        print_put(f'>> >> >> Make type_label "{type_label}".')

    should_append_in_label = True
    type_lower_with_preposition = type_lower.strip()

    if not type_lower_with_preposition.endswith(f" {normalized_preposition}"):
        type_lower_with_preposition = f"{type_lower.strip()} {normalized_preposition}"

    if not type_label:
        type_label = Tabl_with_in.get(type_lower_with_preposition, "")
        if type_label:
            should_append_in_label = False
            print_put(
                f'<<<< type_lower_with_preposition "{type_lower_with_preposition}", type_label : "{type_label}"'
            )

    if not type_label:
        type_label = New_P17_Finall.get(type_lower, "")
        if type_label:
            output_test(
                f'<< type_lower_with_preposition "{type_lower_with_preposition}", type_label : "{type_label}"'
            )

    if type_label == "" and type_lower.startswith("the "):
        type_lower_without_article = type_lower[len("the ") :]

        type_label = New_P17_Finall.get(type_lower_without_article, "")
        if type_label:
            output_test(
                f'<<< type_lower_with_preposition "{type_lower_with_preposition}", type_label : "{type_label}"'
            )
    if type_lower == "sport" and country_lower.startswith("by "):
        type_label = "رياضة"

    if type_label == "" and type_lower.strip().endswith(" people"):
        type_label = make_people_lab(type_lower)

    if not type_label:
        type_label = RELIGIOUS_KEYS_PP.get(type_lower, {}).get("mens", "")
    if not type_label:
        type_label = New_female_keys.get(type_lower, "")
    if not type_label:
        type_label = test_films(type_lower)
    if not type_label:
        type_label = nats.find_nat_others(type_lower)
    if not type_label:
        type_label = team_work.Get_team_work_Club(type_value.strip())

    if not type_label:
        type_label = tmp_bot.Work_Templates(type_lower)

    if not type_label:
        type_label = Get_c_t_lab(type_lower, preposition, Type="Type_lab")

    if not type_label:
        type_label = event2bot.event2(type_lower)
    if not type_label:
        type_label = test4_2018_Jobs(type_lower)

    if not type_label:
        type_label = country2_lab.get_lab_for_contry2(type_lower)

    print_put(f"?????? get_Type_lab: {type_lower=}, {type_label=}")

    return type_label, should_append_in_label
