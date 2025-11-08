"""Utilities for managing gendered Arabic labels used across job modules.

This module replaces hand-written dictionary concatenation with typed helper
functions.  Each helper keeps the original Arabic content intact while
documenting the logic used to combine masculine and feminine labels.
"""

from __future__ import annotations

from typing import Any, Dict, Mapping, MutableMapping, TypedDict

from ..utils.json_dir import open_json_file


class GenderedLabel(TypedDict):
    """Represent an Arabic label split into masculine and feminine forms."""

    mens: str
    womens: str


GenderedLabelMap = Dict[str, GenderedLabel]


def gendered_label(mens: str, womens: str) -> GenderedLabel:
    """Return a :class:`GenderedLabel` mapping.

    Args:
        mens: Masculine Arabic label.
        womens: Feminine Arabic label.

    Returns:
        A dictionary containing the masculine and feminine label pair.  Keeping
        this helper centralised avoids repeated inline dictionary literals and
        makes future validation changes easier to implement in one place.
    """

    return {"mens": mens, "womens": womens}


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


def load_gendered_label_map(filename: str) -> GenderedLabelMap:
    """Load a JSON document into a :class:`GenderedLabelMap` instance.

    Args:
        filename: Basename of the JSON document stored inside ``jsons``.

    Returns:
        A dictionary keyed by category whose values expose masculine and
        feminine Arabic text.  Non-string or malformed entries are ignored so
        downstream consumers receive a consistent mapping structure.
    """

    raw_data: Any = open_json_file(filename)
    result: GenderedLabelMap = {}
    if isinstance(raw_data, Mapping):
        for raw_key, raw_value in raw_data.items():
            if not isinstance(raw_key, str) or not isinstance(raw_value, Mapping):
                continue
            mens_value = str(raw_value.get("mens", ""))
            womens_value = str(raw_value.get("womens", ""))
            result[raw_key] = gendered_label(mens_value, womens_value)
    return result


def copy_gendered_map(source: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Return a deep copy of ``source`` using :func:`gendered_label`."""

    return {key: gendered_label(value["mens"], value["womens"]) for key, value in source.items()}


def merge_gendered_maps(
    target: MutableMapping[str, GenderedLabel],
    source: Mapping[str, GenderedLabel],
) -> None:
    """Update ``target`` with copies from ``source`` to avoid shared state."""

    for key, value in source.items():
        target[key] = gendered_label(value["mens"], value["womens"])


def ensure_gendered_label(
    target: MutableMapping[str, GenderedLabel],
    key: str,
    value: GenderedLabel,
) -> None:
    """Insert ``value`` into ``target`` if ``key`` is not present."""

    if key not in target:
        target[key] = gendered_label(value["mens"], value["womens"])


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

    mens_label = join_terms(base_labels["mens"], suffix_labels["mens"])
    womens_label = ""
    if not require_base_womens or base_labels["womens"]:
        womens_label = join_terms(base_labels["womens"], suffix_labels["womens"])
    return {"mens": mens_label, "womens": womens_label}


__all__ = [
    "GenderedLabel",
    "GenderedLabelMap",
    "combine_gendered_labels",
    "copy_gendered_map",
    "ensure_gendered_label",
    "gendered_label",
    "join_terms",
    "load_gendered_label_map",
    "merge_gendered_maps",
]
