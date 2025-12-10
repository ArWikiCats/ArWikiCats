#!/usr/bin/python3
"""
!
"""

import functools
import re
from typing import Callable, List

from ....helps.log import logger
from ...date_bots import with_years_bot
from ...format_bots import Tabl_with_in, pop_format
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.table1_bot import get_KAKO
from ...media_bots.films_bot import te_films
from ...o_bots import bys, parties_bot
from ...p17_bots import nats_other
from ...sports_bots import sport_lab_suffixes, team_work
from .. import country2_lab
from ....new.time_to_arabic import convert_time_to_arabic
from ....translations import get_from_pf_keys2
from ....translations.sports_formats_national.sport_lab_nat import sport_lab_nat_load_new

pp_start_with2 = {
    "defunct": "{} سابقة",
    "scheduled": "{} مقررة",
}


def check_sources(cone_1: str) -> str:
    """Check multiple sources for a result based on the provided input."""

    sources: List[Callable[[str], str]] = [
        te_films,
        sport_lab_nat_load_new,
        nats_other.find_nat_others,
        sport_lab_suffixes.get_teams_new,
        parties_bot.get_parties_lab,
        team_work.Get_team_work_Club,
    ]
    for source in sources:
        result = source(cone_1)
        if result:
            return result
    return ""


@functools.lru_cache(maxsize=10000)
def c_1_1_lab(separator: str, cone_1: str, With_Years: bool = False) -> str:
    """
    Retrieve a label based on the given parameters.
    Example:
        {"separator": " in ", "cone_1": "cultural depictions of competitors", "output": "تصوير ثقافي عن منافسون"},
    """

    cone_1 = cone_1.strip().lower()

    part_1_label = get_pop_All_18(cone_1) or ""
    logger.debug(f"{cone_1=} -> {part_1_label=}")

    if not part_1_label:
        part_1_label = check_sources(cone_1)

    if cone_1 == "women" and separator.strip() == "from":
        part_1_label = "نساء"
        logger.info(f'>> >> >> Make {cone_1=}.')

    con_1_in = f"{cone_1.strip()} {separator.strip()}"
    if not part_1_label:
        part_1_label = Tabl_with_in.get(con_1_in, "")
        if part_1_label:
            logger.info(f'<<<< {con_1_in=}, {part_1_label=}')

    if not part_1_label:
        part_1_label = convert_time_to_arabic(cone_1)

    if not part_1_label:
        tst3 = re.sub(r"\d+", "", cone_1.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            part_1_label = cone_1

    if not part_1_label:
        for pri_ss, pri_lab in pp_start_with2.items():
            if cone_1.startswith(pri_ss):
                U_c = cone_1[len(pri_ss) :]
                logger.info(f' pp_start_with2 <<lightblue>> {cone_1=}, {U_c=}, {separator=} ')
                U_lab = country2_lab.get_lab_for_country2(U_c)

                if U_lab == "" and With_Years:
                    U_lab = with_years_bot.Try_With_Years(U_c)

                if U_lab:
                    logger.info(f'>>>><<lightblue>> dddd.startswith pri_ss("{pri_ss}"), {U_c=}, {U_lab=}')
                    part_1_label = pri_lab.format(U_lab)
                    logger.info(f'>>>> {part_1_label=}')
                    break

    if cone_1 in pop_format:
        part_1_label = pop_format[cone_1]

    if not part_1_label:
        part_1_label = get_from_pf_keys2(cone_1.strip().lower())

    if not part_1_label:
        part_1_label = get_KAKO(cone_1)

    if not part_1_label:
        logger.debug(f'>>>> XX--== part_1_label =  "{part_1_label}" {cone_1=}')
    return part_1_label


@functools.lru_cache(maxsize=10000)
def c_2_1_lab(cone_2: str, With_Years: bool = False) -> str:
    """Retrieve a label based on the provided cone identifier."""

    cone_2 = cone_2.strip().lower()

    part_2_label = get_pop_All_18(cone_2) or ""
    logger.debug(f"{cone_2=} -> {part_2_label=}")

    if part_2_label == "" and " by " in cone_2:
        part_2_label = bys.get_by_label(cone_2)

    if not part_2_label:
        part_2_label = te_films(cone_2)
    if not part_2_label:
        part_2_label = sport_lab_nat_load_new(cone_2) or nats_other.find_nat_others(cone_2)
    if not part_2_label:
        part_2_label = sport_lab_suffixes.get_teams_new(cone_2)

    if not part_2_label:
        part_2_label = parties_bot.get_parties_lab(cone_2)

    if part_2_label == "" and " and " in cone_2:
        part_2_label = bys.get_and_label(cone_2)

    if not part_2_label:
        part_2_label = team_work.Get_team_work_Club(cone_2)

    if not part_2_label:
        part_2_label = get_from_pf_keys2(cone_2.strip().lower())

    if not part_2_label:
        part_2_label = get_KAKO(cone_2)

    if not part_2_label:
        tst3 = re.sub(r"\d+", "", cone_2.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            part_2_label = cone_2

    if not part_2_label:
        part_2_label = te_films(cone_2)

    if not part_2_label:
        part_2_label = sport_lab_nat_load_new(cone_2) or nats_other.find_nat_others(cone_2)

    if not part_2_label:
        part_2_label = convert_time_to_arabic(cone_2)

    if part_2_label == "" and With_Years:
        part_2_label = with_years_bot.Try_With_Years(cone_2)

    return part_2_label
