"""

from ..ma_bots.squad_title_bot import get_squad_title
# label = get_squad_title(tit)

"""

from ...make2_bots.date_bots import with_years_bot
from ... import malists_sport_lab as sport_lab
from ...ma_lists import pop_of_football_lower
from ...ma_lists import New_P17_Finall
from ...make2_bots.fromnet.wd_bot import find_wikidata

from ...make2_bots.matables_bots.bot import All_P17
from ...make2_bots.matables_bots.bot_2018 import pop_All_2018

from ...helps.print_bot import print_def_head, print_put


def get_squad_title(tit: str) -> str:
    lab = ""

    lab = sport_lab.Get_New_team_xo(tit)

    if not lab:
        lab = with_years_bot.Try_With_Years(tit)

    if lab:
        lab = f"تشكيلات {lab}"

    if not lab:
        for oo, oo_lab in All_P17.items():
            if tit.lower().startswith(f"{oo.lower()} "):
                tit2 = tit[len(f"{oo} ") :]
                tit2 = tit2.strip()
                print_put(f'<<lightblue>> get_squad_title tit.startswith("{oo}"), tit2:({tit2}) ')
                falab = pop_All_2018.get(tit2) or pop_of_football_lower.get(tit2) or New_P17_Finall.get(tit2) or ""
                if not falab:
                    falab = find_wikidata(tit2)

                if falab:
                    lab = f"تشكيلات {oo_lab} في {falab}"
                    break

    print_def_head(f'<<lightblue>> get_squad_title:"{tit}", lab:"{lab}" ')

    return lab
