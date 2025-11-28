"""Tests for :mod:`ArWikiCats.translations.mixed.key_registry`."""

from __future__ import annotations

from typing import Iterable

import pytest

from ArWikiCats.translations.mixed.key_registry import KeyRegistry


class DummyIterable(Iterable[tuple[str, str]]):
    """Simple iterable returning a predefined sequence of pairs."""

    def __init__(self, items: list[tuple[str, str]]) -> None:
        self._items = items

    def __iter__(self):  # type: ignore[override]
        return iter(self._items)


@pytest.fixture
def registry() -> KeyRegistry:
    """Return a fresh registry for each test."""

    return KeyRegistry({"existing": "value"})


def test_update_respects_skip_existing(registry: KeyRegistry) -> None:
    """Updating with ``skip_existing`` preserves original entries."""

    registry.update(
        {"existing": "new value", " fresh ": " spaced "},
        transform=lambda key, value: (key.strip(), value.strip()),
        skip_existing=True,
    )

    assert registry.data["existing"] == "value"
    assert registry.data["fresh"] == "spaced"


def test_update_lowercase_strips_whitespace() -> None:
    """``update_lowercase`` normalises keys and values by default."""

    registry = KeyRegistry()
    registry.update_lowercase({" HeLLo ": " Value "})

    assert registry.data == {"hello": "Value"}


def test_update_from_iterable_supports_custom_iterables(registry: KeyRegistry) -> None:
    """Iterables of pairs integrate seamlessly with optional skipping."""

    registry.update_from_iterable(
        DummyIterable([("existing", "override"), ("fresh", "item"), ("", "")]),
        skip_existing=True,
    )

    assert registry.data["existing"] == "value"
    assert registry.data["fresh"] == "item"
    assert "" not in registry.data


def test_add_cross_product_accepts_mappings_and_iterables() -> None:
    """Cartesian products combine labels from mappings and iterables."""

    registry = KeyRegistry()
    registry.add_cross_product({"A": "Alpha"}, ["x", "y"])

    assert registry.data == {
        "A x": "Alpha x",
        "A y": "Alpha y",
    }
