#!/usr/bin/python3
"""
!

"""
from typing import Tuple

from ....helps.log import logger
from ....translations import RELIGIOUS_KEYS_PP, New_female_keys, New_P17_Finall
from ... import tmp_bot
from ...format_bots import Tabl_with_in
from ...jobs_bots.te4_bots.t4_2018_jobs import te4_2018_Jobs
from ...media_bots.films_bot import te_films
from ...o_bots.popl import make_people_lab
from ...p17_bots import nats
from ...sports_bots import team_work
from .. import country2_lab
from ..country_bot import Get_c_t_lab


def get_Type_lab(preposition: str, type_value: str, type_lower: str, country_lower: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters."""

    normalized_preposition = preposition.strip()

    label = ""
    if type_lower == "women" and normalized_preposition == "from":
        label = "نساء"
        logger.info(f'>> >> >> Make label "{label}".')

    elif type_lower == "women of":
        label = "نساء من"
        logger.info(f'>> >> >> Make label "{label}".')

    should_append_in_label = True
    type_lower_with_preposition = type_lower.strip()

    if not type_lower_with_preposition.endswith(f" {normalized_preposition}"):
        type_lower_with_preposition = f"{type_lower.strip()} {normalized_preposition}"

    if not label:
        label = Tabl_with_in.get(type_lower_with_preposition, "")
        if label:
            should_append_in_label = False
            logger.info(f'<<<< type_lower_with_preposition "{type_lower_with_preposition}", label : "{label}"')

    if not label:
        label = New_P17_Finall.get(type_lower, "")
        if label:
            logger.debug(f'<< type_lower_with_preposition "{type_lower_with_preposition}", label : "{label}"')

    if label == "" and type_lower.startswith("the "):
        type_lower_without_article = type_lower[len("the ") :]

        label = New_P17_Finall.get(type_lower_without_article, "")
        if label:
            logger.debug(f'<<< type_lower_with_preposition "{type_lower_with_preposition}", label : "{label}"')
    if type_lower == "sport" and country_lower.startswith("by "):
        label = "رياضة"

    if label == "" and type_lower.strip().endswith(" people"):
        label = make_people_lab(type_lower)

    if not label:
        label = RELIGIOUS_KEYS_PP.get(type_lower, {}).get("mens", "")
    if not label:
        label = New_female_keys.get(type_lower, "")
    if not label:
        label = te_films(type_lower)
    if not label:
        label = nats.find_nat_others(type_lower)
    if not label:
        label = team_work.Get_team_work_Club(type_value.strip())

    if not label:
        label = tmp_bot.Work_Templates(type_lower)

    if not label:
        label = Get_c_t_lab(type_lower, preposition, Type="Type_lab")

    if not label:
        label = te4_2018_Jobs(type_lower)

    if not label:
        label = country2_lab.get_lab_for_country2(type_lower)

    logger.info(f"?????? get_Type_lab: {type_lower=}, {label=}")

    return label, should_append_in_label
