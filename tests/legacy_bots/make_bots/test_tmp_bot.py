"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.tmp_bot import Work_Templates

suffix_pase_data = [
    # ---------------------------------------------------------
    # pp_ends_with_pase tests
    # ---------------------------------------------------------
    # Example: " - kannada"
    (
        "basketball - kannada",
        " - kannada",
        "كرة السلة",
        "كرة السلة - كنادي",
    ),
    (
        "football – mixed doubles",
        " – mixed doubles",
        "كرة القدم",
        "كرة القدم – زوجي مختلط",
    ),
    (
        "tennis - women's qualification",
        " - women's qualification",
        "كرة المضرب",
        "كرة المضرب - تصفيات السيدات",
    ),
]


@pytest.mark.parametrize(
    "input_label,suffix,resolved,expected",
    suffix_pase_data,
    ids=lambda x: x[0],
)
def test_suffix_pase(input_label: str, suffix: str, resolved: str, expected: str) -> None:
    """Test suffix mapping inside pp_ends_with_pase."""

    result = Work_Templates(input_label)
    assert result == expected


# -------------------------------------------------------------
# pp_ends_with tests (full coverage)
# -------------------------------------------------------------
pp_ends_data = [
    (
        "basketball squaDs",  # suffix " squads"
        "كرة السلة",
        "تشكيلات كرة السلة",
    ),
    (
        "rugby leagues seasons",  # " leagues seasons"
        "اتحاد الرجبي",
        "مواسم دوريات الرجبي",
    ),
    (
        "latin american variants",
        "أمريكيون لاتينيون",
        "أشكال أمريكيون لاتينيون",
    ),
]


@pytest.mark.parametrize(
    "input_label,resolved,expected",
    pp_ends_data,
    ids=[x[0] for x in pp_ends_data],
)
def test_suffix_pp_ends(input_label: str, resolved: str, expected: str) -> None:
    """Test full pp_ends_with suffix dictionary."""

    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Prefix tests (pp_start_with)
# -------------------------------------------------------------
pp_start_data = [
    (
        "wikipedia categories named after egypt",
        "مصر",
        "تصنيفات سميت بأسماء مصر",
    ),
    (
        "candidates for president of france",
        "فرنسا",
        "مرشحو رئاسة فرنسا",
    ),
    (
        "scheduled qatar",
        "قطر",
        "قطر مقررة",
    ),
]


@pytest.mark.parametrize(
    "input_label,resolved,expected",
    pp_start_data,
    ids=lambda x: x[0],
)
def test_prefix_pp_start(input_label: str, resolved: str, expected: str) -> None:
    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Test translation_general_category fallback
# -------------------------------------------------------------
def test_fallback_general_category() -> None:
    result = Work_Templates("basketball finals")
    assert result == "نهائيات كرة السلة"


# -------------------------------------------------------------
# Edge cases: spaces, uppercase, hyphens
# -------------------------------------------------------------
edge_cases_data = [
    ("  BASKETBALL  FINALS  ", "كرة السلة", "نهائيات كرة السلة"),
    ("football  SQUADS", "كرة القدم", "تشكيلات كرة القدم"),
    ("tennis – mixed doubles", "كرة المضرب", "كرة المضرب – زوجي مختلط"),
    ("tennis  –  mixed doubles", "كرة المضرب", ""),
]


@pytest.mark.parametrize(
    "input_label,resolved,expected",
    edge_cases_data,
    ids=[x[0] for x in edge_cases_data],
)
def test_edge_cases(input_label: str, resolved: str, expected: str) -> None:
    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Case: No match — must return empty string
# -------------------------------------------------------------
def test_no_match() -> None:
    assert Work_Templates("unknown category label!!") == ""


# -------------------------------------------------------------
# Deep combined patterns – complex case
# -------------------------------------------------------------
def test_combined_complex() -> None:
    """Example: Ending with '- related lists' with multi-word base."""

    result = Work_Templates("association football-related lists")
    assert result == "قوائم متعلقة بكرة القدم"
