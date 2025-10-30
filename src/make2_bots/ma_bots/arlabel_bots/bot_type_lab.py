#!/usr/bin/python3
"""
from .arlabel_bots.bot_type_lab import get_Type_lab

"""
from typing import Tuple
from .. import contry2_lab
from ...o_bots.popl import make_people_lab
from ...sports_bots import team_work

from ...bots import tmp_bot
from ...p17_bots import nats
from ...jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs
from ...media_bots.films_bot import test_films
from .. import event2bot

from ....ma_lists import New_P17_Finall
from ....ma_lists import religious_keys_PP
from ....ma_lists import New_female_keys

from ...format_bots import Tabl_with_in

from ....helps.print_bot import print_put, output_test, mainoutput

from ..contry_bot import Get_c_t_lab


def get_Type_lab(tito: str, Type: str, Type_lower: str, contry_lower: str) -> Tuple[str, bool]:
    """Determine the type label based on input parameters."""

    tito2 = tito.strip()

    Type_lab = ""
    if Type_lower == "women" and tito2 == "from":
        Type_lab = "نساء"
        print_put(f'>> >> >> Make Type_lab "{Type_lab}".')

    elif Type_lower == "women of":
        Type_lab = "نساء من"
        print_put(f'>> >> >> Make Type_lab "{Type_lab}".')

    Add_in_lab = True
    Type_lower_in = Type_lower.strip()

    if not Type_lower_in.endswith(f" {tito2}"):
        Type_lower_in = f"{Type_lower.strip()} {tito2}"

    if not Type_lab:
        Type_lab = Tabl_with_in.get(Type_lower_in, "")
        if Type_lab:
            Add_in_lab = False
            print_put(f'<<<< Type_lower_in "{Type_lower_in}",Type_lab : "{Type_lab}"')

    if not Type_lab:
        Type_lab = New_P17_Finall.get(Type_lower, "")
        if Type_lab:
            output_test(f'<< Type_lower_in "{Type_lower_in}", Type_lab : "{Type_lab}"')

    if Type_lab == "" and Type_lower.startswith("the "):
        Type_lower2 = Type_lower[len("the ") :]

        Type_lab = New_P17_Finall.get(Type_lower2, "")
        if Type_lab:
            output_test(f'<<< Type_lower_in "{Type_lower_in}", Type_lab : "{Type_lab}"')
    if Type_lower == "sport" and contry_lower.startswith("by "):
        Type_lab = "رياضة"

    if Type_lab == "" and Type_lower.strip().endswith(" people"):
        Type_lab = make_people_lab(Type_lower)

    if not Type_lab:
        Type_lab = religious_keys_PP.get(Type_lower, {}).get("mens", "")
    if not Type_lab:
        Type_lab = New_female_keys.get(Type_lower, "")
    if not Type_lab:
        Type_lab = test_films(Type_lower)
    if not Type_lab:
        Type_lab = nats.find_nat_others(Type_lower)
    if not Type_lab:
        Type_lab = team_work.Get_team_work_Club(Type.strip())

    if not Type_lab:
        Type_lab = tmp_bot.Work_Templates(Type_lower)

    if not Type_lab:
        Type_lab = Get_c_t_lab(Type_lower, tito, Type="Type_lab")

    if not Type_lab:
        Type_lab = event2bot.event2(Type_lower)
    if not Type_lab:
        Type_lab = test4_2018_Jobs(Type_lower, out=mainoutput[1])

    if not Type_lab:
        Type_lab = contry2_lab.get_lab_for_contry2(Type_lower)

    print_put(f"?????? get_Type_lab: {Type_lower=}, {Type_lab=}")

    return Type_lab, Add_in_lab
