"""Tests for :mod:`make2_bots.o_bots.utils`."""

from __future__ import annotations

from typing import Dict

import pytest

from src.make2_bots.o_bots import utils


def test_build_cache_key_normalises_and_joins_parts() -> None:
    result = utils.build_cache_key("  Foo  ", "Bar", "", "Baz")
    assert result == "foo, bar, baz"


def test_get_or_set_returns_cached_value() -> None:
    cache: Dict[str, str] = {}
    calls = 0

    def factory() -> str:
        nonlocal calls
        calls += 1
        return "value"

    first = utils.get_or_set(cache, "key", factory)
    second = utils.get_or_set(cache, "key", factory)

    assert first == "value"
    assert second == "value"
    assert calls == 1


@pytest.mark.parametrize(
    "name,suffixes,expected",
    [
        ("Alpha beta", {"beta": "template"}, ("Alpha", "template")),
        ("Alpha beta", {" beta": "template"}, ("Alpha", "template")),
        ("Gamma", {"beta": "template"}, None),
    ],
)
def test_match_suffix_template_matches_expected_suffix(
    name: str, suffixes: Dict[str, str], expected: tuple[str, str] | None
) -> None:
    assert utils.match_suffix_template(name, suffixes) == expected


def test_resolve_suffix_template_uses_lookup_and_percent_format() -> None:
    suffixes = {"suffix": "Prefix %s"}
    lookup_calls = []

    def lookup(prefix: str) -> str:
        lookup_calls.append(prefix)
        return "VALUE" if prefix == "Name" else ""

    result = utils.resolve_suffix_template("Name suffix", suffixes, lookup)
    assert result == "Prefix VALUE"
    assert lookup_calls == ["Name"]


def test_resolve_suffix_template_supports_brace_format() -> None:
    suffixes = {"suffix": "Prefix {}"}

    result = utils.resolve_suffix_template("Name suffix", suffixes, lambda prefix: "VALUE")
    assert result == "Prefix VALUE"


def test_first_non_empty_returns_first_value() -> None:
    tables = [{"key": ""}, {"key": "value"}, {"key": "other"}]
    assert utils.first_non_empty("key", tables) == "value"


@pytest.mark.parametrize(
    "label,expected",
    [("", ""), ("كتاب", "الكتاب"), ("بيت جميل", "البيت الجميل")],
)
def test_apply_arabic_article(label: str, expected: str) -> None:
    assert utils.apply_arabic_article(label) == expected
