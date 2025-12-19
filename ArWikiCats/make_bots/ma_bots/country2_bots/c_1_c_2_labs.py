#!/usr/bin/python3
"""
!
"""

import functools
import re

from ....helps.log import logger
from ...date_bots import with_years_bot
from ...format_bots import get_tabl_with_in, pop_format
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.table1_bot import get_KAKO
from ...media_bots.films_bot import te_films
from ...o_bots import bys, parties_bot
from ...sports_bots import sport_lab_suffixes, team_work
from ....ma_bots import country2_lab
from ....time_resolvers.time_to_arabic import convert_time_to_arabic
from ....translations import get_from_pf_keys2
from ....translations.sports_formats_national.sport_lab_nat import sport_lab_nat_load_new

pp_start_with2 = {
    "defunct": "{} سابقة",
    "scheduled": "{} مقررة",
}


def work_with_pp_start_with2(cone_1: str, separator: str, with_years: bool = False) -> str:
    part_1_label = ""
    for pri_ss, pri_lab in pp_start_with2.items():
        if cone_1.startswith(pri_ss):
            U_c = cone_1[len(pri_ss) :]
            logger.debug(f' pp_start_with2 <<lightblue>> {cone_1=}, {U_c=}, {separator=} ')
            U_lab = country2_lab.get_lab_for_country2(U_c)

            if U_lab == "" and with_years:
                U_lab = with_years_bot.Try_With_Years(U_c)

            if U_lab:
                logger.debug(f'>>>><<lightblue>> dddd.startswith pri_ss("{pri_ss}"), {U_c=}, {U_lab=}')
                part_1_label = pri_lab.format(U_lab)
                logger.debug(f'>>>> {part_1_label=}')
                break
    return part_1_label


def time_label(text: str) -> str:
    """Generate a time-related label based on the provided text."""
    tst3 = re.sub(r"\d+", "", text.strip())
    test3_results = ["", "-", "–", "−"]
    if tst3 in test3_results:
        return text
    return ""


@functools.lru_cache(maxsize=10000)
def c_1_1_lab(separator: str, cone_1: str, With_Years: bool = False) -> str:
    """
    Retrieve a label based on the given parameters.
    Example:
        {"separator": " in ", "cone_1": "cultural depictions of competitors", "output": "تصوير ثقافي عن منافسون"},
    """

    cone_1 = cone_1.strip().lower()

    if cone_1 == "women" and separator.strip() == "from":
        part_1_label = "نساء"
        logger.debug(f'>> >> >> Make {cone_1=}.')
        return part_1_label

    part_1_label = (
        get_pop_All_18(cone_1) or
        te_films(cone_1) or
        sport_lab_nat_load_new(cone_1) or
        sport_lab_suffixes.get_teams_new(cone_1) or
        parties_bot.get_parties_lab(cone_1) or
        team_work.Get_team_work_Club(cone_1) or
        get_tabl_with_in(cone_1, separator) or
        convert_time_to_arabic(cone_1) or
        time_label(cone_1) or
        work_with_pp_start_with2(cone_1, separator, With_Years) or
        pop_format.get(cone_1) or
        get_from_pf_keys2(cone_1) or
        get_KAKO(cone_1) or
        ""
    )

    if not part_1_label:
        logger.debug(f'>>>> XX--== part_1_label =  "{part_1_label}" {cone_1=}')

    return part_1_label


@functools.lru_cache(maxsize=10000)
def c_2_1_lab(cone_2: str, With_Years: bool = False) -> str:
    """Retrieve a label based on the provided cone identifier."""

    cone_2 = cone_2.strip().lower()

    part_2_label = (
        get_pop_All_18(cone_2) or
        bys.get_by_label(cone_2) or
        te_films(cone_2) or
        sport_lab_nat_load_new(cone_2) or
        sport_lab_suffixes.get_teams_new(cone_2) or
        parties_bot.get_parties_lab(cone_2) or
        bys.get_and_label(cone_2) or
        team_work.Get_team_work_Club(cone_2) or
        get_from_pf_keys2(cone_2.strip().lower()) or
        get_KAKO(cone_2) or
        time_label(cone_2) or
        convert_time_to_arabic(cone_2) or
        ""
    )

    if not part_2_label and With_Years:
        part_2_label = with_years_bot.Try_With_Years(cone_2)

    logger.debug(f"{cone_2=} -> {part_2_label=}")

    return part_2_label
