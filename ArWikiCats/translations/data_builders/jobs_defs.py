"""Utilities for managing gendered Arabic labels used across job modules.

This module replaces hand-written dictionary concatenation with typed helper
functions.  Each helper keeps the original Arabic content intact while
documenting the logic used to combine masculine and feminine labels.
"""

from __future__ import annotations

from typing import Dict, Mapping, MutableMapping, TypedDict


class GenderedLabel(TypedDict):
    """Represent an Arabic label split into masculine and feminine forms."""

    males: str
    females: str


GenderedLabelMap = Dict[str, GenderedLabel]


def combine_gender_labels(first_label: str, second_label: str) -> str:
    label = f"{first_label} {second_label}" if first_label and second_label else ""
    return label


def join_terms(*terms: str) -> str:
    """Join non-empty terms with a single space.

    Args:
        *terms: Terms that should be concatenated.

    Returns:
        A single string that concatenates the provided terms while skipping
        empty values.  The implementation strips whitespace from each term so
        callers can pass loosely formatted strings without creating duplicate
        spaces.
    """

    filtered_terms = [term.strip() for term in terms if term and term.strip()]
    return " ".join(filtered_terms)


def copy_gendered_map(source: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Return a deep copy of ``source``."""

    return {key: {"males": value["males"], "females": value["females"]} for key, value in source.items()}


def merge_gendered_maps(
    target: MutableMapping[str, GenderedLabel],
    source: Mapping[str, GenderedLabel],
) -> None:
    """Update ``target`` with copies from ``source`` to avoid shared state."""

    for key, value in source.items():
        target[key] = {"males": value["males"], "females": value["females"]}


def ensure_gendered_label(
    target: MutableMapping[str, GenderedLabel],
    key: str,
    value: GenderedLabel,
) -> None:
    """Insert ``value`` into ``target`` if ``key`` is not present."""

    if key not in target:
        target[key] = {"males": value["males"], "females": value["females"]}


def combine_gendered_labels(
    base_labels: GenderedLabel,
    suffix_labels: GenderedLabel,
    *,
    require_base_womens: bool = False,
) -> GenderedLabel:
    """Merge two :class:`GenderedLabel` mappings into a new mapping.

    Args:
        base_labels: The primary role labels.
        suffix_labels: The modifiers appended to the base labels.  These may be
            prefixes (e.g. ``"متزلجو"``) or suffixes (e.g. ``"أولمبيون"``).
        require_base_womens: When ``True`` the feminine label is emitted only if
            the base feminine label is available.  This mirrors the legacy
            behaviour used for some religious titles where the feminine form
            should remain empty unless explicitly defined for the base role.

    Returns:
        A new mapping containing concatenated masculine and feminine labels.

    Notes:
        ``combine_gendered_labels`` centralises the join logic that previously
        appeared across multiple modules.  Using the helper ensures consistent
        trimming behaviour and keeps future changes confined to a single
        implementation.
    """

    mens_label = join_terms(base_labels["males"], suffix_labels["males"])
    womens_label = ""
    if not require_base_womens or base_labels["females"]:
        womens_label = join_terms(base_labels["females"], suffix_labels["females"])
    return {"males": mens_label, "females": womens_label}


__all__ = [
    "GenderedLabel",
    "GenderedLabelMap",
    "combine_gendered_labels",
    "copy_gendered_map",
    "ensure_gendered_label",
    "join_terms",
    "merge_gendered_maps",
]
