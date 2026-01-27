"""Regression tests for helper utilities in :mod:`ArWikiCats.fix.mv_years`."""

from __future__ import annotations

from ArWikiCats.fix.mv_years import move_by_in, move_years, move_years_first


def test_move_years_first_reorders_when_possible() -> None:
    """``move_years_first`` should only move recognised prefixes."""
    data = [
        ("2020 في الرياضة في تكساس", "الرياضة في تكساس في 2020"),
        ("2020 في أفلام", "2020 في أفلام"),
    ]
    for label, expected in data:
        assert move_years_first(label) == expected


def test_move_by_in_swaps_by_clause() -> None:
    """``move_by_in`` should reorder "حسب" clauses when the full pattern matches."""

    data = [
        ("الرياضة حسب المدينة في 2020", "الرياضة في 2020 حسب المدينة"),
        ("الرياضة في باريس", "الرياضة في باريس"),
    ]
    for label, expected in data:
        assert move_by_in(label) == expected


def test_move_years_preserves_namespace_and_falls_back() -> None:
    """``move_years`` should handle namespaces and fall back to secondary helpers."""

    data = [
        ("تصنيف:2020 في الرياضة في تكساس", "تصنيف:الرياضة في تكساس في 2020"),
        ("عنوان بلا سنة", "عنوان بلا سنة"),
    ]
    for label, expected in data:
        assert move_years(label) == expected
