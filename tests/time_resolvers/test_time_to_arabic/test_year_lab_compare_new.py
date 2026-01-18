"""
Tests
"""

import pytest

from ArWikiCats.time_formats.time_to_arabic import convert_time_to_arabic


def test_make_year_lab() -> None:
    # Test basic year
    result = convert_time_to_arabic("2020")
    assert isinstance(result, str)
    assert "2020" in result or result == ""  # May return empty for invalid cases
    assert result == "2020"

    # Test year with BC
    result_bc = convert_time_to_arabic("500 bc")
    assert isinstance(result_bc, str)
    assert result_bc == "500 ق م"

    # Test year with BCE
    result_bce = convert_time_to_arabic("300 bce")
    assert isinstance(result_bce, str)
    assert result_bce == "300 ق م"

    # Test century
    result_century = convert_time_to_arabic("21st century")
    assert isinstance(result_century, str)
    assert result_century == "القرن 21"

    # Test millennium
    result_millennium = convert_time_to_arabic("3rd millennium")
    assert isinstance(result_millennium, str)
    assert result_millennium == "الألفية 3"

    # Test with month
    result_with_month = convert_time_to_arabic("january 2020")
    assert isinstance(result_with_month, str)
    assert result_with_month == "يناير 2020"


def test_make_month_lab() -> None:
    # Test with numeric year
    result = convert_time_to_arabic("2020")
    assert result == "2020"

    # Test with month and year
    result_month = convert_time_to_arabic("january 2020")
    assert isinstance(result_month, str)
    assert result_month == "يناير 2020"

    # Test with empty string
    result_empty = convert_time_to_arabic("")
    assert isinstance(result_empty, str)
    assert result_empty == ""

    # Test with just letters
    result_letters = convert_time_to_arabic("january")
    assert isinstance(result_letters, str)
    assert result_letters == "يناير"


class TestMakeYearLabBasicPatterns:
    @pytest.mark.parametrize(
        "year, expected",
        [
            # Pure numeric AD year
            ("1990", "1990"),
            # ("42", "42"),
            # Pure numeric BC/BCE years
            # ("1990 bc", "1990 ق م"),
            # ("42 bce", "42 ق م"),
            # Decades (AD)
            ("10s", "عقد 10"),
            ("1990s", "عقد 1990"),
            # Decades (BC/BCE)
            # ("10s bc", "عقد 10 ق م"),
            ("1990s bce", "عقد 1990 ق م"),
            # Centuries (AD)
            ("21st century", "القرن 21"),
            ("3rd century", "القرن 3"),
            # Centuries (BC/BCE)
            ("21st century bc", "القرن 21 ق م"),
            ("3rd century bce", "القرن 3 ق م"),
            # Millennia (AD)
            ("2nd millennium", "الألفية 2"),
            ("1st millennium", "الألفية 1"),
            # Millennia (BC/BCE)
            ("2nd millennium bce", "الألفية 2 ق م"),
            ("1st millennium bc", "الألفية 1 ق م"),
        ],
    )
    def test_year_lab_core_cases(self, year: str, expected: str) -> None:
        # We ignore leading/trailing whitespace differences by stripping.
        assert convert_time_to_arabic(year) == expected
        assert convert_time_to_arabic(year) == expected


class TestMakeYearLabMonths:
    @pytest.mark.parametrize(
        "year, expected",
        [
            # Month + year (lowercase)
            ("january 1990", "يناير 1990"),
            ("march 2001", "مارس 2001"),
            # Month + year (mixed case)
            ("January 1990", "يناير 1990"),
            ("DecemBer 2010", "ديسمبر 2010"),
            # Month + year + BC/BCE
            # ("january 1990 bc", "يناير 1990 ق م"),
            # ("march 10 bce", "مارس 10 ق م"),
            # Bare month names
            ("january", "يناير"),
            ("January", "يناير"),
            ("march", "مارس"),
        ],
    )
    def test_year_lab_month_cases(self, year: str, expected: str) -> None:
        result = convert_time_to_arabic(year)
        result1 = convert_time_to_arabic(year)
        # Strip to normalize trailing space after month name / suffix.
        assert result == expected
        assert result1 == expected


class TestMakeYearLabRangesAndSpecial:
    @pytest.mark.parametrize(
        "year, expected",
        [
            # Numeric ranges should be preserved as-is
            ("1990-1999", "1990-1999"),
            ("1990–1999", "1990–1999"),  # en dash
            ("1990−1999", "1990−1999"),  # minus sign
        ],
    )
    def test_year_lab_ranges_and_allowed_suffixes(self, year: str, expected: str) -> None:
        assert convert_time_to_arabic(year) == expected
        assert convert_time_to_arabic(year) == expected

    @pytest.mark.parametrize(
        "year",
        [
            # Completely unrelated text
            "random text",
            "not a year",
            # Unsupported pattern (uppercase BC without prior normalization)
            # "10s BC",
            # Contains English letters and is not recognized
            # "year 1990",
        ],
    )
    def test_year_lab_unmatched_inputs_return_empty(self, year: str) -> None:
        assert convert_time_to_arabic(year) == ""
        assert convert_time_to_arabic(year) == ""


class TestMakeMonthLabBasic:
    @pytest.mark.parametrize(
        "year, expected",
        [
            # Pure numeric years: returned unchanged (trimmed)
            ("1990", "1990"),
            (" 1990 ", "1990"),
            # ("42", "42"),
        ],
    )
    def test_month_lab_numeric_only(self, year: str, expected: str) -> None:
        assert convert_time_to_arabic(year) == expected
        assert convert_time_to_arabic(year) == expected

    @pytest.mark.parametrize(
        "year, expected",
        [
            # Month + year (lowercase)
            ("january 1990", "يناير 1990"),
            ("march 2001", "مارس 2001"),
            # Month + year (mixed case)
            ("January 1990", "يناير 1990"),
            ("DecemBer 2010", "ديسمبر 2010"),
            # Bare month names
            ("january", "يناير"),
            ("January", "يناير"),
            ("march", "مارس"),
        ],
    )
    def test_month_lab_with_month_names(self, year: str, expected: str) -> None:
        # Normalize trailing spaces for bare months.
        assert convert_time_to_arabic(year) == expected
        assert convert_time_to_arabic(year) == expected


class TestMakeMonthLabRangesAndSpecial:
    @pytest.mark.parametrize(
        "year, expected",
        [
            # Numeric ranges preserved as-is
            ("1990-1999", "1990-1999"),
            ("1990–1999", "1990–1999"),
            ("1990−1999", "1990−1999"),
        ],
    )
    def test_month_lab_ranges_and_allowed_suffixes(self, year: str, expected: str) -> None:
        assert convert_time_to_arabic(year) == expected
        assert convert_time_to_arabic(year) == expected

    @pytest.mark.parametrize(
        "year",
        [
            # Month + BC/BCE is not supported in convert_time_to_arabic
            # "january 1990 bc",
            # "march 10 bce",
            # Decade-like expressions are not handled here
            # "10s",
            # "10s bc",
            # Arbitrary strings
            "random text",
            "year 1990",
            "A",
        ],
    )
    def test_month_lab_unmatched_inputs_return_empty(self, year: str) -> None:
        assert convert_time_to_arabic(year) == ""
        assert convert_time_to_arabic(year) == ""
