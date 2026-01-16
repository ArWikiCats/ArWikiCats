"""
# isort:skip_file
"""

from __future__ import annotations

import functools
from dataclasses import dataclass
import re
from ..helps import logger
from ..patterns_resolvers import nat_men_pattern
from ..legacy_bots import with_years_bot
from ..legacy_bots.o_bots import univer
from ..legacy_bots.ma_bots.country_bot import event2_d2
from . import event_lab_bot
from ..time_resolvers.labs_years import LabsYears
from ..patterns_resolvers.country_time_pattern import resolve_country_time_pattern
from ..legacy_bots.ma_bots2.year_or_typeo import label_for_startwith_year_or_typeo
from ..config import app_settings
from ..legacy_bots.make_bots import filter_en
from ..format_bots import change_cat
from ..legacy_bots.ma_bots import ye_ts_bot
from ..legacy_bots.matables_bots.bot import cash_2022
from ..new_resolvers.reslove_all import new_resolvers_all
from ..fix import fixlabel


@dataclass
class CategoryResult:
    """Data structure representing each processed category."""

    en: str
    ar: str
    from_match: str


@functools.lru_cache(maxsize=1)
def build_labs_years_object() -> LabsYears:
    return LabsYears()


def retrieve_year_from_category(category):
    logger.debug(f"<<yellow>> start lab_from_year: {category=}")

    labs_years_bot = build_labs_years_object()
    cat_year, from_year = labs_years_bot.lab_from_year(category)

    logger.info_if_or_debug(f"<<yellow>> end lab_from_year: {category=}, {from_year=}", from_year)
    return cat_year, from_year


@functools.lru_cache(maxsize=None)
def resolve_label(category: str, fix_label: bool = True) -> CategoryResult:
    """Resolve the label using multi-step logic."""
    changed_cat = change_cat(category)

    if category.isdigit():
        return CategoryResult(
            en=category,
            ar=category,
            from_match=False,
        )

    if changed_cat.isdigit():
        return CategoryResult(
            en=category,
            ar=changed_cat,
            from_match=False,
        )

    is_cat_okay = filter_en.filter_cat(category)

    category_lab = ""

    cat_year, from_year = retrieve_year_from_category(category)

    if from_year:
        category_lab = from_year

    if not category_lab:
        category_lab = (
            # NOTE: resolve_nat_genders_pattern_v2 IN TESTING HERE ONLY
            # resolve_nat_genders_pattern_v2(changed_cat) or
            new_resolvers_all(changed_cat)
            or ""
        )

    start_ylab = ""
    from_match = False
    if not category_lab:
        category_lab = resolve_country_time_pattern(changed_cat)  # or resolve_nat_women_time_pattern(changed_cat)
        from_match = category_lab != ""

    if not category_lab:
        category_lab = nat_men_pattern.resolve_nat_men_pattern_new(changed_cat)
        from_match = category_lab != ""

    start_ylab = ""
    # if not category_lab: start_ylab = ye_ts_bot.translate_general_category(changed_cat)

    if not category_lab and is_cat_okay:
        category_lower = category.lower()
        if category_lower != changed_cat:
            category_lab = cash_2022.get(category_lower, "")
        if not category_lab:
            category_lab = cash_2022.get(changed_cat, "")

        if not category_lab and app_settings.start_tgc_resolver_first:
            category_lab = start_ylab

        if not category_lab:
            category_lab = (
                univer.te_universities(changed_cat)
                or event2_d2(changed_cat)
                or with_years_bot.Try_With_Years2(changed_cat)
                or label_for_startwith_year_or_typeo(changed_cat)
                or ""
            )

        if not category_lab:
            category_lab = event_lab_bot.event_Lab(changed_cat)

    if not category_lab and is_cat_okay:
        # category_lab = start_ylab
        category_lab = ye_ts_bot.translate_general_category(changed_cat)

    if category_lab and fix_label:
        category_lab = fixlabel(category_lab, en=category)

    # NOTE: causing some issues with years and decades
    # [Category:1930s Japanese novels] : "تصنيف:روايات يابانية في عقد 1930",
    # [Category:1930s Japanese novels] : "تصنيف:روايات يابانية في عقد 1930",

    # if not from_year and cat_year:
    # labs_years_bot.lab_from_year_add(category, category_lab, en_year=cat_year)

    category_lab = re.sub(r"سانتا-في", "سانتا في", category_lab)

    return CategoryResult(
        en=category,
        ar=category_lab,
        from_match=cat_year or from_match,
    )


def resolve_label_ar(category: str, fix_label: bool = True) -> str:
    """Resolve the Arabic label for a given category."""
    result = resolve_label(category, fix_label=fix_label)
    return result.ar


__all__ = [
    "resolve_label",
    "resolve_label_ar",
]
