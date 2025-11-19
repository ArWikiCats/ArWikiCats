#!/usr/bin/python3
"""
!
"""

import re
import functools
from typing import Callable, List

from ....helps.print_bot import print_put, output_test
from ...date_bots import with_years_bot
from ...format_bots import Tabl_with_in, pp_start_with2, pop_format
from ...lazy_data_bots.bot_2018 import get_pop_All_18
from ...matables_bots.centries_bot import centries_years_dec
from ...matables_bots.table1_bot import get_KAKO
from ...media_bots.films_bot import te_films
from ...o_bots import bys, parties_bot
from ...sports_bots import sport_lab_suffixes
from ...p17_bots import nats
from ...sports_bots import team_work
from .. import country2_lab


def check_sources(cone_1: str) -> str:
    """Check multiple sources for a result based on the provided input."""

    sources: List[Callable[[str], str]] = [
        te_films,
        nats.find_nat_others,
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
def c_1_1_lab(tat_o: str, cone_1: str, With_Years: bool=False) -> str:
    """Retrieve a label based on the given parameters."""

    cone_1 = cone_1.strip().lower()

    c_1_l = get_pop_All_18(cone_1, "")

    if not c_1_l:
        c_1_l = check_sources(cone_1)

    if cone_1 == "women" and tat_o.strip() == "from":
        c_1_l = "نساء"
        print_put(f'>> >> >> Make cone_1 "{cone_1}".')

    con_1_in = f"{cone_1.strip()} {tat_o.strip()}"
    if not c_1_l:
        c_1_l = Tabl_with_in.get(con_1_in, "")
        if c_1_l:
            print_put(f'<<<< con_1_in "{con_1_in}", c_1_l : "{c_1_l}"')

    if not c_1_l:
        c_1_l = centries_years_dec.get(cone_1, "")

    if not c_1_l:
        tst3 = re.sub(r"\d+", "", cone_1.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            c_1_l = cone_1

    for pri_ss, pri_lab in pp_start_with2.items():
        if not c_1_l:
            if cone_1.startswith(pri_ss):
                U_c = cone_1[len(pri_ss) :]
                print_put(f' pp_start_with2 <<lightblue>> cone_1 :"{cone_1}", U_c :"{U_c}", tat_o:"{tat_o}" ')
                U_lab = country2_lab.get_lab_for_country2(U_c)

                if U_lab == "" and With_Years:
                    U_lab = with_years_bot.Try_With_Years(U_c)

                if U_lab:
                    print_put(f'>>>><<lightblue>> dddd.startswith pri_ss("{pri_ss}"),U_c:"{U_c}", U_lab:"{U_lab}"')
                    c_1_l = pri_lab.format(U_lab)
                    print_put(f'>>>> c_1_l:"{c_1_l}"')

    if cone_1 in pop_format:
        c_1_l = pop_format[cone_1]

    if not c_1_l:
        c_1_l = get_KAKO(cone_1)

    if not c_1_l:
        output_test(f'>>>> XX--== c_1_l =  "{c_1_l}" cone_1:"{cone_1}" not in pop_new')
    return c_1_l


@functools.lru_cache(maxsize=10000)
def c_2_1_lab(cone_2: str, With_Years: bool=False) -> str:
    """Retrieve a label based on the provided cone identifier."""

    cone_2 = cone_2.strip().lower()

    c_2_l = get_pop_All_18(cone_2, "")
    if c_2_l == "" and " by " in cone_2:
        c_2_l = bys.get_by_label(cone_2)

    if not c_2_l:
        c_2_l = te_films(cone_2)
    if not c_2_l:
        c_2_l = nats.find_nat_others(cone_2)
    if not c_2_l:
        c_2_l = sport_lab_suffixes.get_teams_new(cone_2)

    if not c_2_l:
        c_2_l = parties_bot.get_parties_lab(cone_2)

    if c_2_l == "" and " and " in cone_2:
        c_2_l = bys.get_and_label(cone_2)
    if not c_2_l:
        c_2_l = team_work.Get_team_work_Club(cone_2)

    if not c_2_l:
        c_2_l = get_KAKO(cone_2)

    if not c_2_l:
        tst3 = re.sub(r"\d+", "", cone_2.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            c_2_l = cone_2

    if not c_2_l:
        c_2_l = te_films(cone_2)
    if not c_2_l:
        c_2_l = nats.find_nat_others(cone_2)
    if not c_2_l:
        c_2_l = centries_years_dec.get(cone_2, "")
    if c_2_l == "" and With_Years:
        c_2_l = with_years_bot.Try_With_Years(cone_2)

    return c_2_l
