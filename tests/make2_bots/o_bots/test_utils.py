"""Tests for :mod:`make_bots.o_bots.utils`."""

from __future__ import annotations

from typing import Dict

import pytest

from ArWikiCats.legacy_bots.o_bots import utils


@pytest.mark.parametrize(
    "name,suffixes,expected",
    [
        (
            "football governing bodies",
            {"bodies": "هيئات {}", "governing bodies": "هيئات تنظيم {}"},
            ("football", "هيئات تنظيم {}"),
        ),
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
