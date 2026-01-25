#!/usr/bin/python3
"""
Interfaces for resolver components.

This module defines Protocol classes and type aliases that break circular dependencies
by allowing modules to depend on interfaces rather than concrete implementations.

The lazy import pattern used here defers the import of country_bot until the
resolver functions are actually called, breaking the circular import at module
load time while preserving all runtime functionality.
"""

from typing import Callable, Protocol


class CountryTermLabelResolver(Protocol):
    """Protocol for country term label resolution functions.

    Matches the signature of country_bot.fetch_country_term_label.
    """

    def __call__(
        self,
        term_lower: str,
        separator: str,
        lab_type: str = "",
        start_get_country2: bool = True,
    ) -> str:
        """Resolve a term/country to its Arabic label.

        Args:
            term_lower: The lowercase term to look up.
            separator: Context separator used when resolving terms (e.g., "for", "in").
            lab_type: Optional label type that enables special handling.
            start_get_country2: Whether to use extended country lookup.

        Returns:
            The Arabic label for the term, or an empty string if not found.
        """
        ...


class EventResolver(Protocol):
    """Protocol for event-based category resolution functions."""

    def __call__(self, category: str) -> str:
        """Resolve an event-based category to its Arabic label.

        Args:
            category: The category string to resolve.

        Returns:
            The Arabic label, or an empty string if not found.
        """
        ...


# Type aliases for resolver functions
CountryTermLabelFunc = Callable[[str, str, str, bool], str]
Event2D2Func = Callable[[str], str]


# Lazy resolver accessors - these will be populated at runtime
_country_term_label_resolver: CountryTermLabelFunc | None = None
_event2_d2_resolver: Event2D2Func | None = None


def get_country_term_label_resolver() -> CountryTermLabelFunc:
    """Get the country term label resolver function.

    Uses lazy import to break circular dependency.
    """
    global _country_term_label_resolver
    if _country_term_label_resolver is None:
        from . import country_bot

        _country_term_label_resolver = country_bot.fetch_country_term_label
    return _country_term_label_resolver


def get_event2_d2_resolver() -> Event2D2Func:
    """Get the event2_d2 resolver function.

    Uses lazy import to break circular dependency.
    """
    global _event2_d2_resolver
    if _event2_d2_resolver is None:
        from . import country_bot

        _event2_d2_resolver = country_bot.event2_d2
    return _event2_d2_resolver
