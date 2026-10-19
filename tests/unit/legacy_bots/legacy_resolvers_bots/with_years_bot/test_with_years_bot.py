"""
Tests
"""

import pytest

from src.ArWikiCats.legacy_bots.legacy_resolvers_bots.with_years_bot import try_with_years

# from src.ArWikiCats.make_bots.date_bots import with_years_bot


@pytest.mark.fast
def test_try_with_years() -> None:
    # Test basic functionality - should return a string
    result = try_with_years("2020 election")
    assert isinstance(result, str)

    # Test with year at end
    result_year_end = try_with_years("American Soccer League (1933–83)")
    assert isinstance(result_year_end, str)

    # Test with political term
    result_political = try_with_years("116th united states congress")
    assert isinstance(result_political, str)

    # Test empty string
    result_empty = try_with_years("")
    assert isinstance(result_empty, str)

    # Test with no year pattern
    result_no_year = try_with_years("random category")
    assert isinstance(result_no_year, str)


# ---------------------------------------------------------------------------
# Year at start: _handle_year_at_start
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text,expected",
    [
        ("1900 births", "مواليد 1900"),
        ("1999 fires", "حرائق 1999"),
        ("2020 earthquakes", "زلازل 2020"),
    ],
)
@pytest.mark.fast
def test_year_at_start_known_word_after_years(text: str, expected: str) -> None:
    # Uses WORD_AFTER_YEARS directly without get_kako/translate
    result = try_with_years(text)
    assert result == expected


@pytest.mark.fast
def test_year_at_start_uses_get_kako() -> None:
    # 1900 novels -> not in WORD_AFTER_YEARS, so it should use get_kako

    result = try_with_years("1900 novels")
    assert result == "روايات 1900"


@pytest.mark.fast
def test_year_at_start_uses_translate_general_category() -> None:
    result = try_with_years("1900 protests")
    assert result == "احتجاجات 1900"


@pytest.mark.fast
def test_year_at_start_uses_country2_lab() -> None:
    result = try_with_years("1900 events in Yemen")
    assert result == "أحداث في اليمن 1900"


@pytest.mark.fast
def test_year_at_start_add_in_tabl_separator() -> None:
    # remainder is in Add_in_table -> separator becomes " في "

    result = try_with_years("1900 historical documents")
    assert result == "وثائق تاريخية في 1900"


@pytest.mark.fast
def test_year_at_start_ar_lab_before_year_to_add_in() -> None:
    # remainder_label in ar_label_before_year_to_add_in -> " في "

    result = try_with_years("1900 rugby union tournaments for national teams")
    assert result == "بطولات اتحاد الرجبي للمنتخبات الوطنية 1900"


@pytest.mark.fast
def test_year_at_start_with_range_and_dash_variants() -> None:
    # Ensure range like "1900–1905" is correctly extracted using RE1/re_sub_year

    # En dash
    result_en_dash = try_with_years("1900–1905 earthquakes")
    assert result_en_dash == "زلازل 1900–1905"

    # Minus sign (U+2212) – normalized to '-' in function
    result_minus_sign = try_with_years("1900−1905 earthquakes")
    assert result_minus_sign == "زلازل 1900-1905"

    # Normal hyphen for completeness
    result_hyphen = try_with_years("1900-1905 earthquakes")
    assert result_hyphen == "زلازل 1900-1905"


# ---------------------------------------------------------------------------
# Year at end (no parentheses): _handle_year_at_end with RE2_compile
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_year_at_end_simple_year_uses_translate() -> None:
    result = try_with_years("earthquakes 1999")
    assert result == "زلازل 1999"


@pytest.mark.fast
def test_year_at_end_range_uses_translate() -> None:
    result = try_with_years("earthquakes 1999-2000")
    assert result == "زلازل 1999-2000"


@pytest.mark.fast
def test_year_at_end_uses_country2_when_translate_empty() -> None:
    result = try_with_years("floods 2001")
    assert result == "فيضانات 2001"


# ---------------------------------------------------------------------------
# Year at end in parentheses (RE33_compile) and "–present"
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_year_at_end_parentheses_range() -> None:
    result = try_with_years("American Soccer League (1933–83)")
    assert result == "الدوري الأمريكي لكرة القدم (1933–83)"


@pytest.mark.fast
def test_year_at_end_parentheses_with_present() -> None:
    result = try_with_years("American Soccer League (1933–present)")
    # "–present" should be converted to "–الآن"
    assert result == "الدوري الأمريكي لكرة القدم (1933–الآن)"


@pytest.mark.fast
def test_year_at_end_parentheses_with_hyphen_variants() -> None:
    # Normal hyphen inside parentheses
    result_hyphen = try_with_years("American Soccer League (1933-83)")
    assert result_hyphen == "الدوري الأمريكي لكرة القدم (1933-83)"

    # Minus sign, normalized
    result_minus = try_with_years("American Soccer League (1933−83)")
    assert result_minus == "الدوري الأمريكي لكرة القدم (1933-83)"


# ---------------------------------------------------------------------------
# Inputs without any year pattern
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "text",
    [
        "Category:History of Yemen",
        "American films",
        "World War II",  # no trailing 4-digit year or range
        "some random category",
    ],
)
@pytest.mark.fast
def test_no_year_pattern_returns_empty(text) -> None:
    assert try_with_years(text) == ""
