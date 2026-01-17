"""
# isort:skip_file
"""

from __future__ import annotations

import functools
from dataclasses import dataclass
import re

from ..patterns_resolvers.time_patterns_resolvers import resolve_lab_from_years_patterns
from ..helps import logger
from ..patterns_resolvers import all_patterns_resolvers
from ..legacy_bots import with_years_bot
from ..legacy_bots.o_bots import univer
from ..legacy_bots.ma_bots.country_bot import event2_d2
from . import event_lab_bot
from ..legacy_bots.ma_bots2.year_or_typeo import label_for_startwith_year_or_typeo
from ..legacy_bots.make_bots import filter_en
from ..format_bots import change_cat
from ..legacy_bots.ma_bots import ye_ts_bot
from ..new_resolvers import all_new_resolvers
from ..fix import fixlabel


@dataclass
class CategoryResult:
    """Data structure representing each processed category."""

    en: str
    ar: str
    from_match: str


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

    from_match = False

    category_lab = resolve_lab_from_years_patterns(category)

    if category_lab:
        from_match = True

    if not category_lab:
        category_lab = (
            all_new_resolvers(changed_cat)
            or ""
        )

    if not category_lab:
        category_lab = (
            all_patterns_resolvers(changed_cat)
            # resolve_country_time_pattern(changed_cat)
            # or nat_males_pattern.resolve_nat_males_pattern(changed_cat)
        )
        from_match = category_lab != ""

    if not category_lab and is_cat_okay:

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
        from_match=from_match,
    )


def resolve_label_ar(category: str, fix_label: bool = True) -> str:
    """Resolve the Arabic label for a given category."""
    result = resolve_label(category, fix_label=fix_label)
    return result.ar


__all__ = [
    "resolve_label",
    "resolve_label_ar",
]
