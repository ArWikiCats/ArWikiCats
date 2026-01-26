#!/usr/bin/python3
"""
Resolver Factory Module

This module wires together all the resolver components and breaks the circular
dependency by setting up callbacks at runtime after all modules are loaded.

IMPORTANT: The `initialize_resolvers()` function must be called explicitly
after all modules are imported to set up the callbacks. This is done in
`legacy_bots/__init__.py`.
"""

from __future__ import annotations

from ...fix import fixtitle


def translate_general_category_wrap(category: str) -> str:
    """
    Resolve an Arabic label for a general category using layered resolvers.

    This function combines sub_translate_general_category and work_separator_names
    to provide comprehensive category resolution.

    Parameters:
        category (str): The input category string to resolve.

    Returns:
        str: Arabic label for the category, or an empty string if unresolved.
    """
    from .separator_based_resolver import work_separator_names
    from .sub_resolver import sub_translate_general_category

    arlabel = (
        ""
        or sub_translate_general_category(category)
        or work_separator_names(category)
    )
    if arlabel:
        arlabel = fixtitle.fixlabel(arlabel, en=category)
    return arlabel


def _translate_general_no_fixtitle(category: str) -> str:
    """
    Resolve an Arabic label for a general category without fixtitle.

    This version is used as a callback for with_years_bot.
    """
    from .separator_based_resolver import work_separator_names
    from .sub_resolver import sub_translate_general_category

    return "" or sub_translate_general_category(category) or work_separator_names(category)


_initialized = False


def initialize_resolvers() -> None:
    """
    Initialize all callback resolvers.

    This function must be called after all resolver modules are loaded.
    It sets up the callbacks that break the circular dependencies.
    """
    global _initialized
    if _initialized:
        return

    from ..legacy_resolvers_bots.country2_label_bot import set_term_label_resolver
    from ..legacy_resolvers_bots.with_years_bot import set_translate_callback
    from .country_resolver import fetch_country_term_label, set_fallback_resolver

    # Set up the fallback resolver for country_resolver
    set_fallback_resolver(translate_general_category_wrap)

    # Set up the term label resolver for country2_label_bot
    def term_label_wrapper(term: str, separator: str, lab_type: str = "") -> str:
        return fetch_country_term_label(term, separator, lab_type=lab_type)

    set_term_label_resolver(term_label_wrapper)

    # Set up the translate callback for with_years_bot
    set_translate_callback(_translate_general_no_fixtitle)

    _initialized = True


__all__ = [
    "translate_general_category_wrap",
    "initialize_resolvers",
]
