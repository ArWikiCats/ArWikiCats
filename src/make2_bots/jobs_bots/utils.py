"""Shared utilities for the jobs bots package.

This module contains helper utilities that are reused across multiple
modules in :mod:`make2_bots.jobs_bots`. Consolidating these helpers keeps the
individual modules focused on their domain logic while providing consistent
behaviour for common tasks such as caching and logging.
"""

from __future__ import annotations

import logging
from collections.abc import Callable, Iterable, MutableMapping
from typing import TypeVar

from ...helps.print_bot import output_test4

LOGGER = logging.getLogger(__name__)

T = TypeVar("T")

__all__ = [
    "LOGGER",
    "cached_lookup",
    "log_debug",
    "normalize_cache_key",
]


def normalize_cache_key(*parts: object) -> str:
    """Normalise values into a lowercase cache key.

    Args:
        *parts: Arbitrary values that should contribute to the cache key.

    Returns:
        A comma-separated string containing the normalised parts. ``None``
        values are ignored, while all other values are stringified, stripped
        from whitespace, and lowercased.
    """

    normalized_parts: list[str] = []
    for part in parts:
        if part is None:
            continue
        normalized_parts.append(str(part).strip().lower())
    return ", ".join(normalized_parts)


def cached_lookup(
    cache: MutableMapping[str, T],
    key_parts: Iterable[object],
    factory: Callable[[], T],
) -> T:
    """Retrieve a cached value or compute and cache it on demand.

    Args:
        cache: Mutable mapping that stores cached results.
        key_parts: Values that together form the cache key.
        factory: Callable that computes the value when it is absent from the
            cache.

    Returns:
        The cached or newly computed value.
    """

    cache_key = normalize_cache_key(*key_parts)
    if cache_key in cache:
        return cache[cache_key]

    value = factory()
    cache[cache_key] = value
    return value


def log_debug(message: str, *args: object) -> None:
    """Log debugging information consistently across modules.

    The project historically relied on :func:`output_test4` for emitting
    coloured terminal output. To improve maintainability we log every message
    through :mod:`logging` while keeping the legacy output for compatibility.

    Args:
        message: The human readable message to log.
    """

    LOGGER.debug(message, *args)
    try:
        if args:
            message = message % args
        output_test4(message)
    except Exception:  # pragma: no cover - defensive logging
        LOGGER.debug("output_test4 failed for message: %s", message)
