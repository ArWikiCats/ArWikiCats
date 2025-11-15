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
            "تنس",
            "{} - تصفيات السيدات".format("تنس"),
        ),
    ]
)
def test_suffix_pase(monkeypatch, input_label, suffix, resolved, expected):
    """Test suffix mapping inside pp_ends_with_pase."""

    # Mock sub-functions
    monkeypatch.setattr(
        "src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2",
        lambda lbl: resolved,
    )
    monkeypatch.setattr(
        "src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years",
        lambda lbl: "",
    )
    monkeypatch.setattr(
        "src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category",
        lambda lbl: resolved,
    )

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
            "مواسم دوريات اتحاد الرجبي",
        ),
        (
            "american counties",
            "أمريكية",
            "مقاطعات {}".format("أمريكية"),
        ),
        (
            "european logos",
            "أوروبا",
            "شعارات {}".format("أوروبا"),
        ),
        (
            "latin american variants",
            "أمريكا اللاتينية",
            "أشكال {}".format("أمريكا اللاتينية"),
        ),
    ]
)
def test_suffix_pp_ends(monkeypatch, input_label, resolved, expected):
    """Test full pp_ends_with suffix dictionary."""

    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2", lambda lbl: resolved)
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category", lambda lbl: resolved)

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
def test_prefix_pp_start(monkeypatch, input_label, resolved, expected):

    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2", lambda lbl: resolved)
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category", lambda lbl: resolved)

    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Test with_years_bot interactions
# -------------------------------------------------------------
def test_with_years(monkeypatch):
    """Test translation when the base contains a year."""

    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2", lambda lbl: "")
    monkeypatch.setattr(
        "src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years",
        lambda lbl: "1900" if "1900" in lbl else "",
    )
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category", lambda lbl: "")

    result = Work_Templates("1900 football finals")
    # suffix " finals"
    assert result == "نهائيات 1900"


# -------------------------------------------------------------
# Test translation_general_category fallback
# -------------------------------------------------------------
def test_fallback_general_category(monkeypatch):
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category", lambda lbl: "العامة")

    result = Work_Templates("basketball finals")
    assert result == "نهائيات العامة"


# -------------------------------------------------------------
# Edge cases: spaces, uppercase, hyphens
# -------------------------------------------------------------
@pytest.mark.parametrize(
    "input_label,resolved,expected",
    [
        ("  BASKETBALL  FINALS  ", "كرة السلة", "نهائيات كرة السلة"),
        ("football  SQUADS", "كرة القدم", "تشكيلات كرة القدم"),
        ("tennis – mixed doubles", "تنس", "تنس – زوجي مختلط"),
        ("tennis  –  mixed doubles", "تنس", ""),
    ]
)
def test_edge_cases(monkeypatch, input_label, resolved, expected):

    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2", lambda lbl: resolved)
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category", lambda lbl: resolved)

    assert Work_Templates(input_label) == expected


# -------------------------------------------------------------
# Case: No match — must return empty string
# -------------------------------------------------------------
def test_no_match(monkeypatch):
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category", lambda lbl: "")

    assert Work_Templates("unknown category label!!") == ""


# -------------------------------------------------------------
# Deep combined patterns – complex case
# -------------------------------------------------------------
def test_combined_complex(monkeypatch):
    """Example: Ending with '- related lists' with multi-word base."""

    monkeypatch.setattr(
        "src.make2_bots.bots.tmp_bot.country2_lab.get_lab_for_country2",
        lambda lbl: "كرة القدم",
    )
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.with_years_bot.Try_With_Years", lambda lbl: "")
    monkeypatch.setattr("src.make2_bots.bots.tmp_bot.ye_ts_bot.translate_general_category", lambda lbl: "كرة القدم")

    result = Work_Templates("association football-related lists")
    assert result == "قوائم متعلقة بكرة القدم"
