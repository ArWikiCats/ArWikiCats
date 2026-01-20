"""
Main resolution logic for category labels.
This module coordinates different resolvers (pattern-based, new, and legacy)
to translate and normalize Wikipedia category labels into Arabic.
"""

from __future__ import annotations

import functools
from dataclasses import dataclass

from ..fix import cleanse_category_label, fixlabel
from ..format_bots import change_cat
from ..helps import logger
from ..legacy_bots.make_bots import filter_en
from ..legacy_bots.wrap_legacy_resolvers import legacy_resolvers
from ..new_resolvers import all_new_resolvers
from ..patterns_resolvers import all_patterns_resolvers


@dataclass
class CategoryResult:
    """Data structure representing each processed category."""

    en: str
    ar: str
    from_match: bool


@functools.lru_cache(maxsize=None)
def resolve_label(category: str, fix_label: bool = True) -> CategoryResult:
    """
    Resolve an English Wikipedia category label to its Arabic equivalent.

    Parameters:
        category (str): English category label to resolve.
        fix_label (bool): If true, apply label fixes before final cleansing.

    Returns:
        CategoryResult: dataclass with:
            - en: the original English category label.
            - ar: the resolved Arabic label, or an empty string if no resolution or the category was filtered.
            - from_match: `true` if the label was matched by the pattern-based resolver, `false` otherwise.
    """
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
        category_lab = (
            ""
            or all_new_resolvers(changed_cat)
            or legacy_resolvers(changed_cat)
            or ""
        )

    if category_lab and fix_label:
        category_lab = fixlabel(category_lab, en=category)

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
