"""
Interface definitions for resolvers.

This module defines the Protocol classes and type hints used by the resolver system.
These protocols enable dependency injection and break circular dependencies.
"""

from __future__ import annotations

from typing import Protocol, Tuple


class CountryLabelResolver(Protocol):
    """Protocol for resolving country labels."""

    def get_country_label(self, country: str, start_get_country2: bool = True) -> str:
        """Resolve an Arabic label for a country name."""
        ...


class TermLabelResolver(Protocol):
    """Protocol for resolving term labels."""

    def get_term_label(
        self,
        term_lower: str,
        separator: str,
        lab_type: str = "",
        start_get_country2: bool = True,
    ) -> str:
        """Resolve an Arabic label for a term."""
        ...


class ArabicLabelBuilder(Protocol):
    """Protocol for building Arabic labels from category components."""

    def build(self) -> str:
        """Build and return the Arabic label."""
        ...


class CategoryResolver(Protocol):
    """Protocol for category resolution functions."""

    def __call__(self, category: str) -> str:
        """Resolve a category to an Arabic label."""
        ...


class TypeResolver(Protocol):
    """Protocol for type resolution."""

    @staticmethod
    def resolve(
        preposition: str,
        type_value: str,
        country_lower: str,
        use_event2: bool = True,
    ) -> Tuple[str, bool]:
        """Resolve the type label and whether to append 'in' label."""
        ...


class PrepositionHandler(Protocol):
    """Protocol for preposition handling."""

    def determine_separator(self) -> str:
        """Determine the Arabic separator."""
        ...


__all__ = [
    "CountryLabelResolver",
    "TermLabelResolver",
    "ArabicLabelBuilder",
    "CategoryResolver",
    "TypeResolver",
    "PrepositionHandler",
]
