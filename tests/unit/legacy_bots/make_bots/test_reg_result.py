"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.make_bots.reg_result import get_reg_result


def test_get_reg_result_1() -> None:
    # Test with basic inputs
    result = get_reg_result("Category:19th government of turkey")
    assert result.year_at_first_strip == "19th"
    assert result.In == ""
    assert result.country == "government of turkey"
    assert result.cat_test == "government of turkey"


def test_get_reg_result() -> None:
    # Test with basic inputs
    result = get_reg_result("Category:2025 in fishes")
    assert hasattr(result, "year_at_first")
    assert result.year_at_first_strip == "2025"
    assert hasattr(result, "In")
    assert hasattr(result, "country")
    assert hasattr(result, "cat_test")

    # Test with different parameters
    result_various = get_reg_result("category:year in type")
    assert hasattr(result_various, "year_at_first")
    assert hasattr(result_various, "In")
    assert hasattr(result_various, "country")
    assert hasattr(result_various, "cat_test")


class TestYearExtraction:
    @pytest.mark.parametrize(
        "category,expected",
        [
            # Basic year
            ("Category:1999 events in France", "1999"),
            ("Category:2020 births", "2020"),
            # Year range
            ("Category:1933–83 American Soccer League", "1933–83"),
            ("Category:1933-83 American Soccer League", "1933-83"),
            ("Category:1933−83 American Soccer League", "1933−83"),
            # Decade with s
            ("Category:1990s in music", "1990s"),
            # No year → should be empty
            ("Category:Animals of North America", ""),
            ("Category:Sports in Europe", ""),
            # Month test (month should remain ignored)
            ("Category:January 1999 events", "January 1999"),
            ("Category:February 2021 disasters", "february 2021"),
        ],
    )
    def test_year(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        assert out.year_at_first_strip.lower() == expected.lower()

    @pytest.mark.parametrize(
        "category,expected",
        [
            # BCE/BC (centuries)
            ("Category:2nd century BC", "2nd century BC"),
            ("Category:5th century BCE", "5th century BCE"),
            ("Category:1st millennium BC", "1st millennium BC"),
            # Plain century
            ("Category:20th century", "20th century"),
            # Decade with s
            ("Category:10s BC", "10s BC"),
        ],
    )
    def test_year2(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        assert out.year_at_first.lower() == expected.lower()


# -----------------------------------------------------------
# 6) Tests for cat_test modification after removing year
# -----------------------------------------------------------
@pytest.mark.fast
class TestCatTestModification:
    def test_cat_test_year_removed(self) -> None:
        category = "Category:1999 births in France"
        out = get_reg_result(category)
        assert "1999" not in out.cat_test

    def test_cat_test_unchanged_if_no_year(self) -> None:
        category = "Category:births in France"
        out = get_reg_result(category)
        assert out.cat_test == "births in france"


# -----------------------------------------------------------
# 7) Tests for month suppression (tita_year_no_month)
# -----------------------------------------------------------
@pytest.mark.fast
class TestMonthSuppression:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:January 1999 events", "january 1999"),
            ("Category:December 2020 births", "december 2020"),
        ],
    )
    def test_month_suppression(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        assert out.year_at_first_strip == expected


# -----------------------------------------------------------
# 8) Tests for BCE / BC variations
# -----------------------------------------------------------


class TestBCE_BC:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:10th century BC", "10th century BC"),
            ("Category:5th century BCE", "5th century BCE"),
            ("Category:1st millennium BC", "1st millennium BC"),
            ("Category:2nd millennium BCE", "2nd millennium BCE"),
        ],
    )
    def test_bce(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        assert out.year_at_first.lower() == expected.lower()


# -----------------------------------------------------------
# 11) Edge cases
# -----------------------------------------------------------
@pytest.mark.fast
class TestEdgeCases:
    def test_empty_category(self) -> None:
        out = get_reg_result("")
        assert out.year_at_first == ""
        assert out.In == ""
        assert out.country == ""

    def test_only_category_prefix(self) -> None:
        cat = "Category:"
        out = get_reg_result(cat)
        assert out.year_at_first == ""

    def test_spaces_only(self) -> None:
        cat = "Category:     "
        out = get_reg_result(cat)
        assert out.year_at_first == ""
