"""
!
"""
from __future__ import annotations
from dataclasses import dataclass

import functools

from . import event2bot, event_lab_bot  # isort:skip
from .labs_years import LabsYears  # isort:skip
from ..config import app_settings  # isort:skip
from ..fix import fixtitle
from ..make2_bots.co_bots import filter_en
from ..make2_bots.format_bots import change_cat
from ..make2_bots.ma_bots import ye_ts_bot
from ..make2_bots.matables_bots.bot import cash_2022


labs_years_bot = LabsYears()


@dataclass
class CategoryResult:
    """Data structure representing each processed category."""

    en: str
    ar: str
    from_match: str


@functools.lru_cache(maxsize=None)
def resolve_label(category: str) -> CategoryResult:
    """Resolve the label using multi-step logic."""
    changed_cat = change_cat(category)

    if category.isdigit():
        return category

    if changed_cat.isdigit():
        return changed_cat

    is_cat_okay = filter_en.filter_cat(category)

    category_lab = ""
    cat_year, from_year = labs_years_bot.lab_from_year(category)

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
        labs_years_bot.lab_from_year_add(category, category_lab, en_year=cat_year)

    return CategoryResult(
        en=category,
        ar=category_lab,
        from_match=cat_year,
    )
