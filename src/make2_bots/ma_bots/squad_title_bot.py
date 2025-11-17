"""

from ..ma_bots.squad_title_bot import get_squad_title
# label = get_squad_title(tit)

"""

from ..date_bots import with_years_bot
from ...translations import pop_of_football_lower, Get_New_team_xo
from ...translations import New_P17_Finall

from ..matables_bots.bot import All_P17
from ..lazy_data_bots.bot_2018 import get_pop_All_18

from ...helps.print_bot import print_def_head, print_put


def get_squad_title(tit: str) -> str:
    lab = Get_New_team_xo(tit)

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
                falab = get_pop_All_18(tit2) or pop_of_football_lower.get(tit2) or New_P17_Finall.get(tit2) or ""
                if falab:
                    lab = f"تشكيلات {oo_lab} في {falab}"
                    break

    print_def_head(f'<<lightblue>> get_squad_title:"{tit}", lab:"{lab}" ')

    return lab
