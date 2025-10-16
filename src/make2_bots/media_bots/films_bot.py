#!/usr/bin/python3
"""

# from ..media_bots.films_bot import test_films


from ..media_bots import films_bot

lab = films_bot.test_films()

films_bot.

"""

import re
from typing import Dict
from ..make2_bots.o_bots.army import test_Army
from ..make2_bots.p17_bots import p17_bot
from ..media_bots.film_keys_bot import get_Films_key_CAO
from ..make2_bots.jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs
from ..make2_bots.jobs_bots.test_4 import test4_2018_with_nat, Jobs_in_Multi_Sports, nat_match
from ..make2_bots.o_bots import fax
from ..make2_bots.matables_bots.bot import Add_to_main2_tab
from ..make2_bots.matables_bots.bot import Films_O_TT, New_players
from ..helps.print_bot import print_def_head, output_test, mainoutput

test_films_done: Dict[str, str] = {}


def test_films(cate: str, fa: str = "") -> str:
    cate = cate.lower()
    if cate in test_films_done:
        output_test(f'>>>> cate: "{cate}" in test_films_done, lab:"{test_films_done[cate]}"')
        return test_films_done[cate]

    print_def_head(f"<<lightblue>>>> xxxxxxxxxx test_films cate:{cate} xxxxxxxxxxx ")
    cnt_la = ""

    if re.match(r"^\d+$", cate.strip()):
        cnt_la = cate.strip()

    if not cnt_la:
        cnt_la = get_Films_key_CAO(cate)

    if not cnt_la:
        cnt_la = Jobs_in_Multi_Sports(cate, out=mainoutput[1])
        if cnt_la:
            New_players[cate] = cnt_la
            Add_to_main2_tab(cate, cnt_la)
            output_test(f'>>>> Jobs_in_Multi Sports: New_players[{cate}] ="{cnt_la}"')

    if not cnt_la:
        cnt_la = test4_2018_with_nat(cate, out=mainoutput[1], fa=fa)
        if cnt_la:
            Add_to_main2_tab(cate, cnt_la)
            Films_O_TT[cate] = cnt_la

    if not cnt_la:
        cnt_la = test4_2018_Jobs(cate, out=mainoutput[1])
        if cnt_la:
            New_players[cate] = cnt_la
            Add_to_main2_tab(cate, cnt_la)
            output_test(f'>>>> test_4 2018 Jobs: New_players[{cate}] ="{cnt_la}"')

    if not cnt_la:
        cnt_la = nat_match(cate)
        if cnt_la:
            Add_to_main2_tab(cate, cnt_la)
            output_test(f'>>>> nat_match: [{cate}] ="{cnt_la}"')
    if not cnt_la:
        cnt_la = p17_bot.Get_P17(cate)

    if not cnt_la:
        cnt_la = p17_bot.Get_P17_2(cate)

    if not cnt_la:
        cnt_la = fax.test_Lang(cate)

    if not cnt_la:
        cnt_la = test_Army(cate)

    if not cnt_la:
        cnt_la = test4_2018_Jobs(cate, out=mainoutput[1])

    test_films_done[cate] = cnt_la
    print_def_head(f"<<lightblue>>>> xxxxxxxxx test_films end xxxxxxxxxxx cnt_la:{cnt_la}")
    return cnt_la
