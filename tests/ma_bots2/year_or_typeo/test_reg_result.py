"""
Tests
"""

import pytest

from ArWikiCats.ma_bots2.year_or_typeo.reg_result import (
    TypiesResult,
    get_reg_result,
)


def test_get_reg_result_1() -> None:
    # Test with basic inputs
    # >>>> self.year_at_first='19th ', self.typeo='', "self.In='', self.country='government of turkey', self.cat_test='government of turkey'
    result = get_reg_result("Category:19th government of turkey")
    assert result.year_at_first_strip == "19th"
    assert result.In == ""
    assert result.typeo == ""
    assert result.country == "government of turkey"
    assert result.cat_test == "government of turkey"


def test_get_reg_result() -> None:
    # Test with basic inputs
    result = get_reg_result("Category:2025 in fishes")
    assert hasattr(result, "year_at_first")
    assert result.year_at_first_strip == "2025"
    assert hasattr(result, "typeo")
    assert hasattr(result, "In")
    assert hasattr(result, "country")
    assert hasattr(result, "cat_test")

    # Test with different parameters
    result_various = get_reg_result("category:year in type")
    assert hasattr(result_various, "year_at_first")
    assert hasattr(result_various, "typeo")
    assert hasattr(result_various, "In")
    assert hasattr(result_various, "country")
    assert hasattr(result_various, "cat_test")


def test_typies() -> None:
    # Test that TypiesResult class can be instantiated
    typies_instance = TypiesResult(
        year_at_first="2020", year_at_first_strip="2020", typeo="test", In="in", country="us", cat_test="test"
    )
    assert typies_instance.year_at_first_strip == "2020"
    assert typies_instance.typeo == "test"
    assert typies_instance.In == "in"
    assert typies_instance.country == "us"
    assert typies_instance.cat_test == "test"

    # Test with empty values
    typies_empty = TypiesResult(year_at_first="", year_at_first_strip="", typeo="", In="", country="", cat_test="")
    assert typies_empty.year_at_first == ""
    assert typies_empty.typeo == ""
    assert typies_empty.In == ""
    assert typies_empty.country == ""
    assert typies_empty.cat_test == ""


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
# 2) Tests for extracting TYPE (typeo)
# -----------------------------------------------------------


class TestTypeExtraction:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:1999 births", "births"),
            ("Category:2020 deaths", "deaths"),
            ("Category:18th century BC conflicts", "conflicts"),
            ("Category:3rd millennium BCE architecture", "architecture"),
            # basedtypeTable
            ("Category:1999 television series", "television series"),
            ("Category:2000 video games", "video games"),
            # No type → empty
            ("Category:1999 France", ""),
            ("Category:2020 Japan", ""),
        ],
    )
    def test_typeo(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        typeo = out.typeo
        assert typeo == expected

    @pytest.mark.parametrize(
        "category,expected",
        [
            # category_relation_mapping as type
            ("Category:1999 manufactured by Toyota", "manufactured by"),
            ("Category:1999 manufactured-by Toyota", "manufactured by"),
            ("Category:2001 written by John", "written by"),
            ("Category:2001 launched in USA", "launched in"),
        ],
    )
    @pytest.mark.skip2
    def test_typeo2(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        typeo = out.typeo
        assert typeo == expected


# -----------------------------------------------------------
# 3) Tests for extracting “In” token
# -----------------------------------------------------------


@pytest.mark.fast
class TestInExtraction:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:1999 births in France", "in"),
            ("Category:2020 elections in Spain", "in"),
            ("Category:19th century architecture in Germany", "in"),
            # should work with variations from category_relation_mapping
            ("Category:1999 written in Canada", "written"),
            ("Category:1999 written by Canada", "written by"),
            ("Category:2001 launched in USA", "launched in"),
            # Test if In is empty
            ("Category:1999 births", ""),
            ("Category:2020 deaths", ""),
        ],
    )
    def test_in(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        assert out.In.strip() == expected


# -----------------------------------------------------------
# 4) Tests for extracting COUNTRY (or final segment)
# -----------------------------------------------------------
@pytest.mark.fast
class TestCountryExtraction:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:1999 births in France", "France"),
            ("Category:2020 elections in Spain", "Spain"),
            ("Category:19th century architecture in Germany", "Germany"),
            # with category_relation_mapping patterns
            ("Category:1999 manufactured in Italy", "Italy"),
            ("Category:1999 written by John", "John"),
            ("Category:1999 launched in USA", "USA"),
            # No country
            ("Category:1999 births", ""),
            ("Category:20th century architecture", ""),
        ],
    )
    def test_country(self, category: str, expected: str) -> None:
        out = get_reg_result(category)
        assert out.country.lower() == expected.lower()


# -----------------------------------------------------------
# 5) Tests for full combined patterns
# -----------------------------------------------------------
@pytest.mark.fast
class TestCombinedPatterns:
    """
    A test class for testing combined pattern matching in category names.
    Uses pytest parametrize decorator to run multiple test cases with different inputs.
    """

    @pytest.mark.parametrize(
        "category,year,typeo,In,country",
        [
            ("Category:1999 births in France", "1999", "births", "in", "france"),
            # ("Category:2020 deaths by cancer in Japan", "2020", "deaths", "in", "japan"),
            ("Category:19th century architecture in Egypt", "19th century", "architecture", "in", "egypt"),
            # ("Category:1933–83 American Soccer League (USA)", "1933–83", "american soccer league", "", ""),
        ],
    )
    def test_combined(self, category: str, year: str, typeo: str, In: str, country: str) -> None:
        out = get_reg_result(category)
        assert out.year_at_first_strip == year
        assert out.typeo == typeo
        assert out.In.strip() == In
        assert out.country == country


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
        assert out.typeo == ""
        assert out.In == ""
        assert out.country == ""

    def test_only_category_prefix(self) -> None:
        cat = "Category:"
        out = get_reg_result(cat)
        assert out.year_at_first == ""
        assert out.typeo == ""

    def test_spaces_only(self) -> None:
        cat = "Category:     "
        out = get_reg_result(cat)
        assert out.year_at_first == ""
        assert out.typeo == ""

    def test_weird_unicode_dashes(self) -> None:
        category = "Category:1933–83 births"
        out = get_reg_result(category)
        assert out.year_at_first == "1933–83"
        assert out.typeo == "births"
