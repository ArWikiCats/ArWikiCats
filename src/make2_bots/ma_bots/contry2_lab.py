#!/usr/bin/python3
"""
python3 core8/pwb.py make/make2_bots.ma_bots/contry2_bot

# from ..make2_bots.ma_bots.contry2_lab import get_lab_for_contry2


"""
from typing import Any
from ..make2_bots.o_bots import fax
from ..make2_bots.media_bots.films_bot import test_films

from ..make2_bots.sports_bots import team_work
from ..make2_bots.p17_bots import nats
from ..make2_bots.matables_bots.centries_bot import centries_years_dec

from ..make2_bots.matables_bots.bot_2018 import pop_All_2018
from ..make2_bots.matables_bots.table1_bot import get_KAKO

from ..helps.print_bot import print_put

from ..make2_bots.p17_bots.us_stat import Work_US_State
from ..make2_bots.o_bots.rele import Work_relations
from ..make2_bots.o_bots.popl import Work_peoples
from ..make2_bots.o_bots import univer

from . import ye_ts_bot


def get_lab_for_contry2(contry: str, with_test_ye: bool = False, **kwargs: Any) -> str:
    """Retrieve laboratory information for a specified country."""

    contry2_no_lower = contry.strip()
    contry2 = contry.lower().strip()
    cnt_la = pop_All_2018.get(contry2, "")

    if not cnt_la:
        cnt_la = test_films(contry2)
    if not cnt_la:
        cnt_la = nats.find_nat_others(contry2)
    if not cnt_la:
        cnt_la = fax.Get_Teams_new(contry2)
    if not cnt_la:
        cnt_la = team_work.Get_team_work_Club(contry2_no_lower)
    if not cnt_la:
        cnt_la = Work_relations(contry2)
    if not cnt_la:
        cnt_la = univer.test_Universities(contry2)
    if not cnt_la:
        cnt_la = Work_US_State(contry2)
    if not cnt_la:
        cnt_la = Work_peoples(contry2)
    if not cnt_la:
        cnt_la = get_KAKO(contry2)

    if not cnt_la:
        cnt_la = centries_years_dec.get(contry2, "")

    if not cnt_la and contry2.startswith("the "):
        cnt_la = pop_All_2018.get(contry2[len("the ") :], "")

    if not cnt_la and with_test_ye:
        cnt_la = ye_ts_bot.translate_general_category(contry2, do_Get_contry2=False)

    if cnt_la:
        print_put(f'>> get_lab_for_contry2 "{contry2}": cnt_la: {cnt_la}')

    return cnt_la
