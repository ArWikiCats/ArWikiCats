"""Shared helpers for geographic translation tables.

This module centralises small utility helpers that are reused across the
geographic translation modules.  The original codebase implemented similar
loops in multiple modules with only minor variations.  Consolidating those
snippets keeps the modules focused on data definitions while this file owns the
book-keeping logic.
"""

from __future__ import annotations

import logging
from collections.abc import Iterable, Mapping, MutableMapping
from typing import Any

from ..utils import open_json_file

logger = logging.getLogger(__name__)


def load_json_mapping(file_key: str) -> dict[str, str]:
    """
    Load and normalize a JSON mapping file into a cleaned mapping.

    Keys and values are converted to strings and entries with falsy keys or values are omitted.

    Parameters:
        file_key (str): Lookup key used to locate the JSON mapping file.

    Returns:
        cleaned_mapping (dict[str, str]): Mapping of labels (source -> target). Returns an empty dict when the file is missing or contains no usable mapping entries.
    """

    raw_mapping = open_json_file(file_key) or {}
    cleaned_mapping: dict[str, str] = {}

    for key, value in raw_mapping.items():
        if not value or not key:
            continue

        cleaned_mapping[str(key)] = str(value)

    if not cleaned_mapping and raw_mapping:
        logger.debug("JSON mapping '%s' did not contain usable labels", file_key)

    return cleaned_mapping


def merge_mappings(*mappings: Mapping[str, str]) -> dict[str, str]:
    """Merge multiple mappings into a new dictionary."""

    merged: dict[str, str] = {}
    for mapping in mappings:
        merged.update(mapping)
    return merged


def update_with_lowercased(target: MutableMapping[str, str], mapping: Mapping[str, str]) -> None:
    """Update ``target`` with a lower-cased version of ``mapping``."""

    for key, value in mapping.items():
        if not value:
            continue
        target[key.lower()] = value


def apply_suffix_templates(
    target: MutableMapping[str, str],
    mapping: Mapping[str, str],
    suffix_templates: Iterable[tuple[str, str]],
) -> None:
    """Add entries that append suffixes and translated prefixes.

    Args:
        target: Mapping to mutate.
        mapping: Source mapping that provides the base labels.
        suffix_templates: Iterable of ``(" suffix", "template %s")`` pairs. The
            suffix is appended to the lower-cased key while the template is
            formatted with the translated value.
    """

    for key, value in mapping.items():
        if not value:
            continue

        normalized_key = key.lower()
        for suffix, template in suffix_templates:
            target[f"{normalized_key}{suffix}"] = template % value


def normalize_to_lower(mapping: Mapping[str, str]) -> dict[str, str]:
    """Return a new mapping with lower-cased keys."""

    normalized: dict[str, str] = {}
    update_with_lowercased(normalized, mapping)
    return normalized


def log_mapping_stats(name: str, **mappings: Mapping[Any, Any]) -> None:
    """Emit debug logging with information about mapping sizes."""

    for mapping_name, mapping in mappings.items():
        logger.debug("%s.%s contains %d entries", name, mapping_name, len(mapping))
