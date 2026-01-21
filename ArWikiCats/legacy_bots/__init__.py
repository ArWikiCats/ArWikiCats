"""
Wrapper for legacy category resolvers.
This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.
"""

from __future__ import annotations

import functools
import re
from typing import Callable

from ..helps import logger
from ..sub_new_resolvers import university_resolver
from .legacy_resolvers_bots import (
    country_bot,
    event_lab_bot,
    general_resolver,
    with_years_bot,
    year_or_typeo,
)


class LegacyBotsResolver:
    """
    A unified resolver class for legacy category translation logic.
    Encapsulates multiple resolution strategies into a single pipeline.
    """

    def __init__(self) -> None:
        """Initialize the resolver pipeline in priority order."""
        # Define the pipeline as a list of bound methods
        self._pipeline: list[Callable[[str], str]] = [
            self._resolve_university,
            self._resolve_country_event,
            self._resolve_with_years,
            self._resolve_year_or_typo,
            self._resolve_event_lab,
            self._resolve_general,
        ]

    def _normalize(self, text: str) -> str:
        """Standard normalization for category strings."""
        normalized = text.lower().strip()
        if normalized.startswith("category:"):
            normalized = normalized[len("category:") :].strip()
        return normalized

    def _has_blocked_prepositions(self, text: str) -> bool:
        """Check if the string contains blocked English prepositions."""
        blocked = ("in", "of", "from", "by", "at")
        # Ensure we check for whole words by adding spaces around the preposition
        return any(f" {word} " in text for word in blocked)

    def _resolve_university(self, text: str) -> str:
        """1. Specialized resolver for university categories (highest priority)."""
        return university_resolver.resolve_university_category(text)

    def _resolve_country_event(self, text: str) -> str:
        """2. Country and event-based resolution."""
        normalized = self._normalize(text)
        if self._has_blocked_prepositions(normalized):
            return ""

        # Original logic from country_bot.event2_d2: only if it DOES NOT start with a digit
        if re.sub(r"^\d", "", normalized) == normalized:
            return country_bot.get_country(normalized)
        return ""

    def _resolve_with_years(self, text: str) -> str:
        """3. Year-based category resolution."""
        normalized = self._normalize(text)
        if self._has_blocked_prepositions(normalized):
            return ""

        # Original logic from with_years_bot.wrap_try_with_years: only if it DOES start with a digit
        if re.sub(r"^\d", "", normalized) != normalized:
            return with_years_bot.Try_With_Years(normalized)
        return ""

    def _resolve_year_or_typo(self, text: str) -> str:
        """4. Year prefix patterns and typo handling."""
        return year_or_typeo.label_for_startwith_year_or_typeo(text)

    def _resolve_event_lab(self, text: str) -> str:
        """5. General event labeling."""
        return event_lab_bot.event_Lab(text)

    def _resolve_general(self, text: str) -> str:
        """6. Catch-all general resolution (lowest priority)."""
        return general_resolver.translate_general_category(text)

    def resolve(self, text: str) -> str:
        """
        Processes the input through all legacy resolvers in priority order.

        Returns the first non-empty result from the pipeline.
        """
        for method in self._pipeline:
            result = method(text)
            if result:
                logger.debug(f"LegacyBotsResolver: {method.__name__} matched for input: {text}")
                return result
        return ""


# Instantiate the resolver for global use
_resolver = LegacyBotsResolver()

# Maintain the pipeline list for backward compatibility with __all__
RESOLVER_PIPELINE: list[Callable[[str], str]] = _resolver._pipeline


@functools.lru_cache(maxsize=None)
def legacy_resolvers(changed_cat: str) -> str:
    """
    Resolve a category label using the legacy resolver chain in priority order.

    This function implements a pipeline pattern using the LegacyBotsResolver class.

    Parameters:
        changed_cat (str): Category name or identifier to resolve.

    Returns:
        category_label (str): The resolved category label, or an empty string
            if no legacy resolver produces a value.
    """
    return _resolver.resolve(changed_cat)


__all__ = [
    "legacy_resolvers",
    "RESOLVER_PIPELINE",
]
