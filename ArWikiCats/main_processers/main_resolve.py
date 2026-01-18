"""
# isort:skip_file
"""

from __future__ import annotations

import functools
from dataclasses import dataclass
from ..helps import logger
from ..patterns_resolvers import all_patterns_resolvers
from ..legacy_bots.make_bots import filter_en
from ..format_bots import change_cat
from ..new_resolvers import all_new_resolvers
from ..fix import fixlabel, cleanse_category_label
from ..legacy_bots.wrap_legacy_resolvers import legacy_resolvers


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
    if not is_cat_okay:
        logger.debug(f"Category filtered out: {category}")
        return CategoryResult(
            en=category,
            ar="",
            from_match=False,
        )

    category_lab = all_patterns_resolvers(changed_cat)
    from_match = bool(category_lab)

    if not category_lab:
        category_lab = all_new_resolvers(changed_cat) or ""

    if not category_lab:
        category_lab = legacy_resolvers(changed_cat)

    if category_lab and fix_label:
        category_lab = fixlabel(category_lab, en=category)

    # NOTE: causing some issues with years and decades
    # [Category:1930s Japanese novels] : "تصنيف:روايات يابانية في عقد 1930",
    # [Category:1930s Japanese novels] : "تصنيف:روايات يابانية في عقد 1930",

    # if not from_year and cat_year:
    # labs_years_bot.lab_from_year_add(category, category_lab, en_year=cat_year)

    category_lab = cleanse_category_label(category_lab)

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
