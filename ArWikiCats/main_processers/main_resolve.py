"""
Main resolution logic for category labels.
This module coordinates different resolvers (pattern-based, new, and legacy)
to translate and normalize Wikipedia category labels into Arabic.
"""

from __future__ import annotations

import functools
import logging
from dataclasses import dataclass, field

from ..fix import cleanse_category_label, filter_en, fixlabel
from ..format_bots import change_cat
from ..legacy_bots import legacy_resolvers
from ..new_resolvers import all_new_resolvers
from ..patterns_resolvers import all_patterns_resolvers
from ..sub_new_resolvers import university_resolver

logger = logging.getLogger(__name__)


@dataclass
class CategoryResult:
    """Data structure representing each processed category.

    Attributes:
        en: The original English category label.
        ar: The resolved Arabic label, or empty string if not resolved.
        from_match: True if pattern-based match produced the label.
    """

    en: str
    ar: str
    from_match: bool


@dataclass
class ResolverMatch:
    """Data structure containing the resolved label and its source.

    Attributes:
        label: The resolved Arabic label.
        source: The resolver that produced this label (e.g., "pattern", "time_resolver").
        confidence: Confidence score for future use (default 1.0 for exact matches).
    """

    label: str
    source: str
    confidence: float = 1.0


@dataclass
class ResolutionContext:
    """Context passed through the resolver chain.

    Attributes:
        original_category: The original category string before any normalization.
        normalized_category: The normalized category string after preprocessing.
        cache_hit: Whether the result was found in cache.
        matched_resolver: Name of the resolver that matched (if any).
        debug_info: List of debug messages for troubleshooting.
    """

    original_category: str
    normalized_category: str
    cache_hit: bool = False
    matched_resolver: str | None = None
    debug_info: list[str] = field(default_factory=list)

    def log(self, message: str) -> None:
        """Add a debug message to the context."""
        self.debug_info.append(message)


@functools.lru_cache(maxsize=50000)
def resolve_label(category: str, fix_label: bool = True) -> CategoryResult:
    """Translate an English Wikipedia category label into its Arabic equivalent.

    Parameters
    ----------
    category : str
        The original English category label to translate.
    fix_label : bool, optional
        If True, apply post-resolution label fixes before final cleansing.
        Default is True.

    Returns
    -------
    CategoryResult
        A dataclass containing:
        - ``en``: The original English category label.
        - ``ar``: The resolved Arabic label, or empty string if not resolved.
        - ``from_match``: True if a pattern-based match produced the label.
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

    is_cat_okay = filter_en.is_category_allowed(category)
    if not is_cat_okay:
        logger.debug(f"Category filtered out: {category}")
        return CategoryResult(
            en=category,
            ar="",
            from_match=False,
        )

    category_lab = all_patterns_resolvers(changed_cat)
    from_match = bool(category_lab)

    # If no pattern match, try the resolver chain
    # The chain works because empty string is falsy - first non-empty result wins
    if not category_lab:
        category_lab = (
            all_new_resolvers(changed_cat)
            or university_resolver.resolve_university_category(changed_cat)
            or legacy_resolvers(changed_cat)
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
    "CategoryResult",
    "ResolverMatch",
    "ResolutionContext",
]
