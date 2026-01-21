"""
Wrapper for legacy category resolvers.
This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.
"""

from __future__ import annotations

import functools

from ..sub_new_resolvers import university_resolver
from .legacy_resolvers import country_bot, event_lab_bot, general_resolver, with_years_bot, year_or_typeo


@functools.lru_cache(maxsize=None)
def legacy_resolvers(changed_cat) -> str:
    """
    Resolve a category label using the legacy resolver chain in priority order.

    Parameters:
        changed_cat (str): Category name or identifier to resolve.

    Returns:
        category_label (str): The resolved category label, or an empty string if no legacy resolver produces a value.
    """
    category_lab = (
        university_resolver.resolve_university_category(changed_cat)
        or country_bot.event2_d2(changed_cat)
        or with_years_bot.wrap_try_with_years(changed_cat)
        or year_or_typeo.label_for_startwith_year_or_typeo(changed_cat)
        or event_lab_bot.event_Lab(changed_cat)
        or general_resolver.translate_general_category(changed_cat)
        or ""
    )

    return category_lab


__all__ = [
    "legacy_resolvers",
]
