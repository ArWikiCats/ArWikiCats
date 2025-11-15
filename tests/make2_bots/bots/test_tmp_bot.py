"""
Tests
"""
import pytest

from src.make2_bots.bots.tmp_bot import Work_Templates


def test_work_templates():
    # Test with a basic input
    result = Work_Templates("test input")
    assert isinstance(result, str)
    assert result == ""

    # Test with empty string
    result_empty = Work_Templates("")
    assert isinstance(result_empty, str)
    assert result_empty == ""

    # Test with various inputs
    result_various = Work_Templates("sports-related media")
    assert isinstance(result_various, str)
    assert result_various == "إعلام متعلق بألعاب رياضية"

    # Test with input that might match a template
    result_template = Work_Templates("football players")
    assert isinstance(result_template, str)
    assert result_template == ""


@pytest.mark.parametrize(
    "input_label,suffix,resolved,expected",
    [
        # ---------------------------------------------------------
        # pp_ends_with_pase tests
        # ---------------------------------------------------------
        # Example: " - kannada"
        (
            "basketball - kannada",
            " - kannada",
            "كرة السلة",
            "{} - كنادي".format("كرة السلة"),
        ),
        (
            "football – mixed doubles",
            " – mixed doubles",
            "كرة القدم",
            "{} – زوجي مختلط".format("كرة القدم"),
        ),
        (
            "tennis - women's qualification",
            " - women's qualification",
            "كرة المضرب",
            "{} - تصفيات السيدات".format("كرة المضرب"),
        ),
    ]
)
def test_suffix_pase(input_label, suffix, resolved, expected):
    """Test suffix mapping inside pp_ends_with_pase."""

    result = Work_Templates(input_label)
    assert result == expected


# -------------------------------------------------------------
# pp_ends_with tests (full coverage)
# -------------------------------------------------------------
@pytest.mark.parametrize(
    "input_label,resolved,expected",
    [
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
            "american counties",
            "أمريكية",
            "",
        ),
        (
            "european logos",
            "أوروبا",
            "",
        ),
        (
            "latin american variants",
            "أمريكيون لاتينيون",
            "أشكال أمريكيون لاتينيون",
        ),
    ]
)
def test_suffix_pp_ends(input_label, resolved, expected):
    """Test full pp_ends_with suffix dictionary."""

    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Prefix tests (pp_start_with)
# -------------------------------------------------------------
@pytest.mark.parametrize(
    "input_label,resolved,expected",
    [
        (
            "wikipedia categories named after egypt",
            "مصر",
            "تصنيفات سميت بأسماء {}".format("مصر"),
        ),
        (
            "candidates for president of france",
            "فرنسا",
            "مرشحو رئاسة {}".format("فرنسا"),
        ),
        (
            "scheduled qatar",
            "قطر",
            "{} مقررة".format("قطر"),
        ),
    ]
)
def test_prefix_pp_start(input_label, resolved, expected):

    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Test with_years_bot interactions
# -------------------------------------------------------------
def test_with_years():
    """Test translation when the base contains a year."""

    result = Work_Templates("1900 football finals")
    # suffix " finals"
    assert result == "نهائيات كرة القدم 1900"


# -------------------------------------------------------------
# Test translation_general_category fallback
# -------------------------------------------------------------
def test_fallback_general_category():
    result = Work_Templates("basketball finals")
    assert result == "نهائيات كرة السلة"


# -------------------------------------------------------------
# Edge cases: spaces, uppercase, hyphens
# -------------------------------------------------------------
@pytest.mark.parametrize(
    "input_label,resolved,expected",
    [
        ("  BASKETBALL  FINALS  ", "كرة السلة", "نهائيات كرة السلة"),
        ("football  SQUADS", "كرة القدم", "تشكيلات كرة القدم"),
        ("tennis – mixed doubles", "كرة المضرب", "كرة المضرب – زوجي مختلط"),
        ("tennis  –  mixed doubles", "كرة المضرب", ""),
    ]
)
def test_edge_cases(input_label, resolved, expected):

    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Case: No match — must return empty string
# -------------------------------------------------------------
def test_no_match():
    assert Work_Templates("unknown category label!!") == ""


# -------------------------------------------------------------
# Deep combined patterns – complex case
# -------------------------------------------------------------
def test_combined_complex():
    """Example: Ending with '- related lists' with multi-word base."""

    result = Work_Templates("association football-related lists")
    assert result == "قوائم متعلقة بكرة قدم"
