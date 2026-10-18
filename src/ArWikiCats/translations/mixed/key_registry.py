"""Utilities for building consistent key-to-label mappings.

This module centralises the helper utilities that are repeatedly required by
the historical ``all_keys`` modules.  The original modules previously
implemented ad-hoc loops that manipulated dictionaries in place.  The helper
objects defined here provide a typed, well documented and reusable interface
that makes those operations easier to understand and unit test.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field

KeyValueTransform = Callable[[str, str], tuple[str, str]]


def _DEFAULT_SANITISER(key, value):
    """
    Return the input key and value unchanged.

    Returns:
        tuple[str, str]: A tuple (key, value) containing the original inputs.
    """
    return (key, value)


@dataclass(slots=True)
class KeyRegistry:
    """Utility container for building key-to-label mappings.

    The registry exposes convenience helpers for the common transformation
    patterns used across the ``all_keys`` modules.  This avoids repeating the
    same for-loops in multiple modules and ensures consistent behaviour (for
    example automatically ignoring empty keys).
    """

    data: dict[str, str] = field(default_factory=dict)

    def update(
        self,
        mapping: Mapping[str, str],
        *,
        transform: KeyValueTransform = _DEFAULT_SANITISER,
        skip_existing: bool = False,
    ) -> None:
        """Update the registry with items from *mapping*.

        Args:
            mapping: The mapping to merge into the registry.
            transform: Optional callable applied to each key/value pair before
                insertion.  The callable should return a ``(key, value)`` tuple
                that will be stored in the registry.  The callable is executed
                only for items with non-empty keys and values.
            skip_existing: When ``True`` previously stored keys are preserved
                and only new keys are added.
        """

        for key, value in mapping.items():
            if not key or not value:
                continue

            transformed_key, transformed_value = transform(str(key), str(value))
            if not transformed_key or not transformed_value:
                continue

            if skip_existing and transformed_key in self.data:
                continue

            self.data[transformed_key] = transformed_value

    def update_lowercase(
        self,
        mapping: Mapping[str, str],
        *,
        skip_existing: bool = False,
        strip: bool = True,
    ) -> None:
        """Update the registry with a mapping whose keys are lower-cased.

        Args:
            mapping: Mapping to merge into the registry.
            skip_existing: Preserve already stored keys when ``True``.
            strip: Remove leading/trailing whitespace from keys and values when
                ``True``.
        """

        def _lowercase_transform(key: str, value: str) -> tuple[str, str]:
            """Normalize a mapping entry by stripping and lowercasing the key."""
            if strip:
                key = key.strip()
                value = value.strip()
            return key.lower(), value

        self.update(mapping, transform=_lowercase_transform, skip_existing=skip_existing)

    def update_from_iterable(
        self,
        items: Iterable[tuple[str, str]],
        *,
        skip_existing: bool = False,
    ) -> None:
        """Insert a sequence of ``(key, value)`` pairs into the registry."""

        for key, value in items:
            if not key or not value:
                continue
            if skip_existing and key in self.data:
                continue
            self.data[key] = value

    def add_cross_product(
        self,
        first: Mapping[str, str] | Iterable[str],
        second: Mapping[str, str] | Iterable[str],
        *,
        key_template: str = "{first} {second}",
        value_template: str = "{first_label} {second_label}",
    ) -> None:
        """Add entries for the cartesian product of *first* and *second*.

        Args:
            first: Mapping (or iterable of keys) that provides the first
                component of the key and label.
            second: Mapping (or iterable of keys) that provides the second
                component of the key and label.
            key_template: String template used to build the new key.  The
                template receives ``first`` and ``second`` keyword arguments.
            value_template: Template used to generate the entry label.  The
                template receives ``first_label`` and ``second_label`` keyword
                arguments.
        """

        first_items = list(first.items() if isinstance(first, Mapping) else ((value, value) for value in first))
        second_items = list(second.items() if isinstance(second, Mapping) else ((value, value) for value in second))

        for first_key, first_label in first_items:
            for second_key, second_label in second_items:
                key = key_template.format(first=first_key, second=second_key)
                value = value_template.format(first_label=first_label, second_label=second_label)
                if key and value:
                    self.data[key] = value


__all__ = ["KeyRegistry", "KeyValueTransform"]
