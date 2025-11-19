#
from __future__ import annotations

import functools

from . import labs_years, event2bot, event_lab_bot

from ..fix import fixtitle
from ..make2_bots.co_bots import filter_en
from ..make2_bots.format_bots import change_cat
from ..make2_bots.ma_bots import ye_ts_bot
from ..make2_bots.matables_bots.bot import cash_2022
from ..config import app_settings


@functools.lru_cache(maxsize=None)
def resolve_label(category: str) -> str:
    """Resolve the label using multi-step logic."""
    changed_cat = change_cat(category)

    if category.isdigit():
        return category

    if changed_cat.isdigit():
        return changed_cat

    is_cat_okay = filter_en.filter_cat(category)

    category_lab = ""
    cat_year, from_year = labs_years.lab_from_year(category)

    if from_year:
        category_lab = from_year

    start_ylab = ""

    if not category_lab:
        start_ylab = ye_ts_bot.translate_general_category(changed_cat)

    if not category_lab and is_cat_okay:
        category_lower = category.lower()
        category_lab = cash_2022.get(category_lower, "")

        if not category_lab and app_settings.start_yementest:
            category_lab = start_ylab

        if not category_lab:
            category_lab = event2bot.event2(changed_cat)

        if not category_lab:
            category_lab = event_lab_bot.event_Lab(changed_cat)

    if not category_lab and is_cat_okay:
        category_lab = start_ylab

    if category_lab:
        category_lab = fixtitle.fixlab(category_lab, en=category)

    if not from_year and cat_year:
        labs_years.lab_from_year_add(category, category_lab, cat_year)

    return category_lab
