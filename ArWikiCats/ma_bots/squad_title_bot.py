"""
TODO: remove it
"""

import functools

from ..helps.log import logger
from ..translations import get_from_new_p17_final, pop_of_football_lower
from ..utils import fix_minor
from ..make_bots.date_bots import with_years_bot
from ..make_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make_bots.matables_bots.bot import All_P17

from ..new_resolvers.translations_resolvers.nats_sports import nats_new_create_label
from ..translations.sports_formats_teams.sport_lab2 import wrap_team_xo_normal_2025


@functools.lru_cache(maxsize=None)
def get_squad_title(tit: str) -> str:
    """Generate a squad title label using team, year, and country data."""
    lab = wrap_team_xo_normal_2025(tit) or nats_new_create_label(tit)

    if not lab:
        lab = with_years_bot.Try_With_Years(tit)

    # if lab: lab = f"تشكيلات {lab}"

    if not lab:
        for oo, oo_lab in All_P17.items():
            if tit.lower().startswith(f"{oo.lower()} "):
                tit2 = tit[len(f"{oo} ") :]
                tit2 = tit2.strip()
                logger.info(f'<<lightblue>> get_squad_title tit.startswith("{oo}"), tit2:({tit2}) ')
                falab = get_pop_All_18(tit2) or pop_of_football_lower.get(tit2) or get_from_new_p17_final(tit2) or ""
                if falab:
                    # lab = f"تشكيلات {oo_lab} في {falab}"
                    lab = f"{oo_lab} في {falab}"
                    break

    lab = fix_minor(lab)
    logger.info(f'<<lightblue>> get_squad_title:"{tit}", {lab=} ')

    return lab


def resolve_squads_labels_and_templates(category3_o: str) -> str:
    """
    Process squad-related category labels.

    Args:
        category3_o (str): The original category string

    Returns:
        str: The processed category label or empty string
    """
    category_lab = ""
    list_of_cat = ""
    category3 = category3_o.strip()

    if category3.endswith(" squad templates"):
        list_of_cat = "قوالب تشكيلات {}"
        category3 = category3[: -len(" squad templates")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            # category_lab = f"قوالب {cate_labs}"
            category_lab = list_of_cat.format(cate_labs)

    elif category3.endswith(" squad navigational boxes"):
        list_of_cat = "صناديق تصفح تشكيلات {}"
        category3 = category3[: -len(" squad navigational boxes")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            # category_lab = f"صناديق تصفح {cate_labs}"
            category_lab = list_of_cat.format(cate_labs)

    if category_lab:
        logger.debug(f"<<lightblue>>get_list_of_and_cat3_with_lab(): {list_of_cat=}, {category3=}, {category_lab=}")
        logger.debug(f"<<lightblue>>(): {category3_o=}, {category_lab=}")

    return category_lab
