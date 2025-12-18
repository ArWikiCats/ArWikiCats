"""
# isort:skip_file
"""

from __future__ import annotations

import functools
from dataclasses import dataclass

from . import event2bot, event_lab_bot, nat_men_pattern, resolve_nat_genders_pattern
from .labs_years import LabsYears
from .country_time_pattern import resolve_country_time_pattern
# from ..translations_resolvers_v2.nats_time_v2 import resolve_nats_time_v2
from ..config import app_settings
from ..make_bots.co_bots import filter_en
from ..make_bots.format_bots import change_cat
from ..make_bots.ma_bots import ye_ts_bot
from ..make_bots.matables_bots.bot import cash_2022
from ..translations_resolvers import resolved_translations_resolvers
from ..translations_resolvers_v3i import resolved_translations_resolvers_v3i
from ..translations_resolvers_v2 import resolved_translations_resolvers_v2

from ..fix import fixlabel


@dataclass
class CategoryResult:
    """Data structure representing each processed category."""

    en: str
    ar: str
    from_match: str


@functools.lru_cache(maxsize=1)
def build_labs_years_object() -> LabsYears:
    labs_years_bot = LabsYears()
    return labs_years_bot


@functools.lru_cache(maxsize=None)
def resolve_label(category: str, fix_label: bool=True) -> CategoryResult:
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

    labs_years_bot = build_labs_years_object()

    cat_year, from_year = labs_years_bot.lab_from_year(category)

    if from_year:
        category_lab = from_year

    if not category_lab:
        category_lab = (
            # NOTE: resolve_nat_genders_pattern IN TESTING HERE ONLY
            # resolve_nat_genders_pattern(changed_cat) or
            resolved_translations_resolvers_v3i(changed_cat) or
            resolved_translations_resolvers_v2(changed_cat) or
            resolved_translations_resolvers(changed_cat) or
            ""
        )

    start_ylab = ""
    from_match = False
    if not category_lab:
        category_lab = resolve_country_time_pattern(changed_cat)  # or resolve_nat_women_time_pattern(changed_cat)
        from_match = category_lab != ""

    if not category_lab:
        category_lab = nat_men_pattern.resolve_nat_men_pattern_new(changed_cat)
        from_match = category_lab != ""

    if not category_lab:
        start_ylab = ye_ts_bot.translate_general_category(changed_cat)

    if not category_lab and is_cat_okay:
        category_lab = cash_2022.get(category.lower(), "") or cash_2022.get(changed_cat, "")

        if not category_lab and app_settings.start_tgc_resolver_first:
            category_lab = start_ylab

        if not category_lab:
            category_lab = event2bot.event2(changed_cat)

        if not category_lab:
            category_lab = event_lab_bot.event_Lab(changed_cat)

    if not category_lab and is_cat_okay:
        category_lab = start_ylab

    if category_lab and fix_label:
        category_lab = fixlabel(category_lab, en=category)

    if not from_year and cat_year:
        labs_years_bot.lab_from_year_add(category, category_lab, en_year=cat_year)

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
