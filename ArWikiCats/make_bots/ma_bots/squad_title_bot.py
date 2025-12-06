"""

from ..ma_bots.squad_title_bot import get_squad_title
# label = get_squad_title(tit)

"""

import functools

from ...helps.log import logger
from ...translations import get_from_new_p17_final, pop_of_football_lower
from ...utils import fix_minor
from ..date_bots import with_years_bot
from ..lazy_data_bots.bot_2018 import get_pop_All_18
from ..matables_bots.bot import All_P17

from ...translations_resolvers.nats_sports import nats_new_create_label
from ...translations.sports_formats_teams.sport_lab2 import wrap_team_xo_normal_2025


@functools.lru_cache(maxsize=None)
def get_squad_title(tit: str) -> str:
    """Generate a squad title label using team, year, and country data."""
    lab = wrap_team_xo_normal_2025(tit) or nats_new_create_label(tit)

    if not lab:
        lab = with_years_bot.Try_With_Years(tit)

    if lab:
        lab = f"تشكيلات {lab}"

    if not lab:
        for oo, oo_lab in All_P17.items():
            if tit.lower().startswith(f"{oo.lower()} "):
                tit2 = tit[len(f"{oo} ") :]
                tit2 = tit2.strip()
                logger.info(f'<<lightblue>> get_squad_title tit.startswith("{oo}"), tit2:({tit2}) ')
                falab = get_pop_All_18(tit2) or pop_of_football_lower.get(tit2) or get_from_new_p17_final(tit2) or ""
                if falab:
                    lab = f"تشكيلات {oo_lab} في {falab}"
                    break

    lab = fix_minor(lab)
    logger.info(f'<<lightblue>> get_squad_title:"{tit}", {lab=} ')

    return lab
