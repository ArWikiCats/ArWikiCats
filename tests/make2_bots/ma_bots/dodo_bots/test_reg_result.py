"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.dodo_bots.reg_result import get_reg_result, Typies
from src.make2_bots.ma_bots.dodo_bots.reg_result import basedtypeTable, Tit_ose_Nmaes


def test_get_reg_result():
    # Test with basic inputs
    result = get_reg_result("test category", "test category", "test category")
    assert hasattr(result, 'year')
    assert hasattr(result, 'typeo')
    assert hasattr(result, 'In')
    assert hasattr(result, 'country')
    assert hasattr(result, 'cat_test')

    # Test with different parameters
    result_various = get_reg_result("category:year in type", "category:year in type", "year in type")
    assert hasattr(result_various, 'year')
    assert hasattr(result_various, 'typeo')
    assert hasattr(result_various, 'In')
    assert hasattr(result_various, 'country')
    assert hasattr(result_various, 'cat_test')


def test_typies():
    # Test that Typies class can be instantiated
    typies_instance = Typies(year="2020", typeo="test", In="in", country="us", cat_test="test")
    assert typies_instance.year == "2020"
    assert typies_instance.typeo == "test"
    assert typies_instance.In == "in"
    assert typies_instance.country == "us"
    assert typies_instance.cat_test == "test"

    # Test with empty values
    typies_empty = Typies(year="", typeo="", In="", country="", cat_test="")
    assert typies_empty.year == ""
    assert typies_empty.typeo == ""
    assert typies_empty.In == ""
    assert typies_empty.country == ""
    assert typies_empty.cat_test == ""


class _TestYearExtraction:
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

            # Four-digit year inside parentheses
            ("Category:American Soccer League (1933)", "1933"),
            ("Category:American Soccer League (1933–83)", "1933–83"),

            # BCE/BC (centuries)
            ("Category:2nd century BC", "2nd century BC"),
            ("Category:5th century BCE", "5th century BCE"),
            ("Category:1st millennium BC", "1st millennium BC"),

            # Plain century
            ("Category:20th century", "20th century"),

            # Decade with s
            ("Category:1990s in music", "1990s"),
            ("Category:10s BC", "10s BC"),

            # No year → should be empty
            ("Category:Animals of North America", ""),
            ("Category:Sports in Europe", ""),

            # Month test (month should remain ignored)
            ("Category:January 1999 events", "1999"),
            ("Category:February 2021 disasters", "2021"),
        ]
    )
    def test_year(self, category, expected):
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.year == expected


# -----------------------------------------------------------
# 2) Tests for extracting TYPE (typeo)
# -----------------------------------------------------------

class _TestTypeExtraction:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:1999 births", "births"),
            ("Category:2020 deaths", "deaths"),
            ("Category:18th century BC conflicts", "conflicts"),
            ("Category:1990s establishments in Japan", "establishments"),
            ("Category:3rd millennium BCE architecture", "architecture"),

            # basedtypeTable
            ("Category:1999 television series", "television series"),
            ("Category:2000 video games", "video games"),
            ("Category:1999 sports events", "sports events"),

            # Tit_ose_Nmaes as type
            ("Category:1999 manufactured by Toyota", "manufactured by"),
            ("Category:2001 written by John", "written by"),
            ("Category:2001 launched in USA", "launched in"),

            # No type → empty
            ("Category:1999 France", ""),
            ("Category:2020 Japan", ""),
        ]
    )
    def test_typeo(self, category, expected):
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        typeo = out.typeo.strip()
        assert typeo == expected.strip()


# -----------------------------------------------------------
# 3) Tests for extracting “In” token
# -----------------------------------------------------------

class _TestInExtraction:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:1999 births in France", "in"),
            ("Category:2020 elections in Spain", "in"),
            ("Category:19th century architecture in Germany", "in"),

            # should work with variations from Tit_ose_Nmaes
            ("Category:1999 written in Canada", "in"),
            ("Category:2001 launched in USA", "in"),

            # Test if In is empty
            ("Category:1999 births", ""),
            ("Category:2020 deaths", ""),
        ]
    )
    def test_in(self, category, expected):
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.In == expected


# -----------------------------------------------------------
# 4) Tests for extracting COUNTRY (or final segment)
# -----------------------------------------------------------

class _TestCountryExtraction:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:1999 births in France", "France"),
            ("Category:2020 elections in Spain", "Spain"),
            ("Category:19th century architecture in Germany", "Germany"),

            # with Tit_ose_Nmaes patterns
            ("Category:1999 manufactured in Italy", "Italy"),
            ("Category:1999 written by John", "John"),
            ("Category:1999 launched in USA", "USA"),

            # No country
            ("Category:1999 births", ""),
            ("Category:20th century architecture", ""),
        ]
    )
    def test_country(self, category, expected):
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.country == expected


# -----------------------------------------------------------
# 5) Tests for full combined patterns
# -----------------------------------------------------------

class _TestCombinedPatterns:
    @pytest.mark.parametrize(
        "category,year,typeo,In,country",
        [
            ("Category:1999 births in France", "1999", "births", "in", "france"),
            ("Category:2020 deaths by cancer in Japan", "2020", "deaths", "in", "japan"),
            ("Category:19th century architecture in Egypt", "19th century", "architecture", "in", "egypt"),
            ("Category:1933–83 American Soccer League (USA)", "1933–83", "american soccer league", "", ""),
        ]
    )
    def test_combined(self, category, year, typeo, In, country):
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.year == year
        assert out.typeo == typeo
        assert out.In == In
        assert out.country == country


# -----------------------------------------------------------
# 6) Tests for cat_test modification after removing year
# -----------------------------------------------------------

class _TestCatTestModification:
    def test_cat_test_year_removed(self):
        category = "Category:1999 births in France"
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert "1999" not in out.cat_test

    def test_cat_test_unchanged_if_no_year(self):
        category = "Category:births in France"
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.cat_test == category


# -----------------------------------------------------------
# 7) Tests for month suppression (tita_year_no_month)
# -----------------------------------------------------------

class _TestMonthSuppression:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:January 1999 events", "1999"),
            ("Category:December 2020 births", "2020"),
        ]
    )
    def test_month_suppression(self, category, expected):
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.year == expected


# -----------------------------------------------------------
# 8) Tests for BCE / BC variations
# -----------------------------------------------------------

class _TestBCE_BC:
    @pytest.mark.parametrize(
        "category,expected",
        [
            ("Category:10th century BC", "10th century BC"),
            ("Category:5th century BCE", "5th century BCE"),
            ("Category:1st millennium BC", "1st millennium BC"),
            ("Category:2nd millennium BCE", "2nd millennium BCE"),
        ]
    )
    def test_bce(self, category, expected):
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.year == expected


# -----------------------------------------------------------
# 9) Stress-test with all basedtypeTable + years
# -----------------------------------------------------------

class _TestBasedTypeTableCoverage:
    @pytest.mark.parametrize("eng", list(basedtypeTable.keys()))
    def test_all_based_types(self, eng):
        category = f"Category:1999 {eng} in France"
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        assert out.typeo == eng
        assert out.year == "1999"
        assert out.country == "france"


# -----------------------------------------------------------
# 10) Stress-test with all Tit_ose_Nmaes keys
# -----------------------------------------------------------

class _TestTitOseCoverage:
    @pytest.mark.parametrize("eng", list(Tit_ose_Nmaes.keys()))
    def test_all_tit_ose(self, eng):
        category = f"Category:2001 {eng} Canada"
        out = get_reg_result(
            category=category,
            cate_gory=category,
            cate3=category,
        )
        typeo = out.typeo
        # Only test that typeo and country extracted
        assert typeo == eng or eng in typeo
        assert out.country in ("canada", "")


# -----------------------------------------------------------
# 11) Edge cases
# -----------------------------------------------------------

class _TestEdgeCases:
    def test_empty_category(self):
        out = get_reg_result("", "", "", "")
        assert out.year == ""
        assert out.typeo == ""
        assert out.In == ""
        assert out.country == ""

    def test_only_category_prefix(self):
        cat = "Category:"
        out = get_reg_result(cat, cat, cat)
        assert out.year == ""
        assert out.typeo == ""

    def test_spaces_only(self):
        cat = "Category:     "
        out = get_reg_result(cat, cat, cat)
        assert out.year == ""
        assert out.typeo == ""

    def test_weird_unicode_dashes(self):
        category = "Category:1933–83 births"
        out = get_reg_result(
            category, category, category
        )
        assert out.year == "1933–83"
        assert out.typeo == "births"
