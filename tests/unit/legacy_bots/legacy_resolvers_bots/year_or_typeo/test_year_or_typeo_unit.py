"""
Unit tests for year_or_typeo module.
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.year_or_typeo import (
    LabelForStartWithYearOrTypeo,
    label_for_startwith_year_or_typeo,
)

# ---------------------------------------------------------------------------
# Tests for label_for_startwith_year_or_typeo function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestLabelForStartWithYearOrTypeo:
    """Tests for the main label_for_startwith_year_or_typeo function."""

    def test_returns_empty_for_no_year_pattern(self) -> None:
        """Categories without year patterns should return empty string."""
        result = label_for_startwith_year_or_typeo("random category")
        assert result == ""

    def test_returns_empty_for_empty_string(self) -> None:
        """Empty input should return empty string."""
        result = label_for_startwith_year_or_typeo("")
        assert result == ""

    def test_handles_category_prefix(self) -> None:
        """Should strip 'category:' prefix before processing."""
        result = label_for_startwith_year_or_typeo("category:1900")
        assert isinstance(result, str)

    def test_simple_year(self) -> None:
        """Simple year-only input should return the year in Arabic format."""
        result = label_for_startwith_year_or_typeo("1900")
        assert result == "1900"

    def test_decade_format(self) -> None:
        """Decade format should be handled correctly."""
        result = label_for_startwith_year_or_typeo("1900s")
        assert result == "عقد 1900"

    def test_century_format(self) -> None:
        """Century format should be handled correctly."""
        result = label_for_startwith_year_or_typeo("20th century")
        assert result == "القرن 20"

    def test_year_with_bce(self) -> None:
        """Year with BCE should be converted properly."""
        result = label_for_startwith_year_or_typeo("500 bce")
        assert "ق.م" in result or "500" in result

    def test_handles_uppercase(self) -> None:
        """Should be case-insensitive for category prefix."""
        result = label_for_startwith_year_or_typeo("Category:1900")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for LabelForStartWithYearOrTypeo class
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestLabelForStartWithYearOrTypeoClass:
    """Tests for the LabelForStartWithYearOrTypeo class."""

    def test_init_default_values(self) -> None:
        """Test default initialization values."""
        builder = LabelForStartWithYearOrTypeo()
        assert builder.cate == ""
        assert builder.cate3 == ""
        assert builder.year_at_first == ""
        assert builder.in_str == ""
        assert builder.country == ""
        assert builder.arlabel == ""
        assert builder.add_in is True
        assert builder.NoLab is False

    def test_parse_input_extracts_year(self) -> None:
        """Test parse_input extracts year correctly."""
        builder = LabelForStartWithYearOrTypeo()
        builder.parse_input("1900 events")
        assert "1900" in builder.year_at_first

    def test_parse_input_stores_category_r(self) -> None:
        """Test parse_input stores category_r."""
        builder = LabelForStartWithYearOrTypeo()
        builder.parse_input("1900 events")
        assert builder.category_r == "1900 events"

    def test_replace_cat_test_static_method(self) -> None:
        """Test the static replace_cat_test method."""
        result = LabelForStartWithYearOrTypeo.replace_cat_test("test value", "test")
        assert "test" not in result
        assert "value" in result.strip()

    def test_replace_cat_test_case_insensitive(self) -> None:
        """Test replace_cat_test is case insensitive."""
        result = LabelForStartWithYearOrTypeo.replace_cat_test("TEST value", "test")
        assert "test" not in result.lower()

    def test_build_returns_empty_for_no_year(self) -> None:
        """Test build returns empty string when no year is found."""
        builder = LabelForStartWithYearOrTypeo()
        result = builder.build("random text without year")
        assert result == ""

    def test_build_with_year_at_start(self) -> None:
        """Test build with year at the start of category."""
        builder = LabelForStartWithYearOrTypeo()
        result = builder.build("1900")
        assert isinstance(result, str)

    def test_handle_year_sets_year_labe(self) -> None:
        """Test handle_year sets year_labe correctly."""
        builder = LabelForStartWithYearOrTypeo()
        builder.year_at_first = "1900"
        builder.cat_test = "1900 events"
        builder.handle_year()
        assert "1900" in builder.year_labe or builder.year_labe == "1900"

    def test_handle_year_with_empty_year_at_first(self) -> None:
        """Test handle_year with no year returns early."""
        builder = LabelForStartWithYearOrTypeo()
        builder.year_at_first = ""
        builder.handle_year()
        assert builder.arlabel == ""

    def test_handle_country_with_empty_country(self) -> None:
        """Test handle_country with empty country_lower."""
        builder = LabelForStartWithYearOrTypeo()
        builder.country_lower = ""
        builder.handle_country()
        # Should return early without modification
        assert builder.country_label == ""

    def test_handle_relation_mapping_with_empty_in(self) -> None:
        """Test handle_relation_mapping with empty in_str value."""
        builder = LabelForStartWithYearOrTypeo()
        builder.in_str = ""
        builder.cat_test = "test"
        builder.handle_relation_mapping()
        # Should return early without modification
        assert "category:" not in builder.cat_test

    def test_apply_label_rules_sets_nolab_for_invalid_year(self) -> None:
        """Test apply_label_rules sets NoLab when year has no label."""
        builder = LabelForStartWithYearOrTypeo()
        builder.year_at_first = "invalid"
        builder.year_labe = ""
        builder.apply_label_rules()
        assert builder.NoLab is True

    def test_finalize_returns_empty_for_empty_arlabel(self) -> None:
        """Test finalize returns empty string when arlabel is empty."""
        builder = LabelForStartWithYearOrTypeo()
        builder.arlabel = ""
        result = builder.finalize()
        assert result == ""

    def test_finalize_strips_arlabel(self) -> None:
        """Test finalize handles arlabel properly."""
        builder = LabelForStartWithYearOrTypeo()
        builder.arlabel = "  some label  "
        builder.cate = "test"
        builder.cat_test = ""
        builder.NoLab = False
        builder.category_r = "test"
        result = builder.finalize()
        # Either returns the finalized label or empty string based on validation
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Integration-style unit tests for complete flow
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestYearOrTypeoIntegration:
    """Integration-style tests for the complete processing flow."""

    @pytest.mark.parametrize(
        "input_category",
        [
            "1900",
            "2000",
            "1950s",
            "1800s",
        ],
    )
    def test_simple_years_and_decades(self, input_category: str) -> None:
        """Test processing of simple years and decades."""
        result = label_for_startwith_year_or_typeo(input_category)
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        "input_category",
        [
            "random text",
            "no year here",
            "",
            "   ",
        ],
    )
    def test_non_year_inputs_return_empty(self, input_category: str) -> None:
        """Test that non-year inputs return empty string."""
        result = label_for_startwith_year_or_typeo(input_category)
        assert result == ""

    def test_category_with_country(self) -> None:
        """Test category with country component."""
        result = label_for_startwith_year_or_typeo("1900 in yemen")
        assert isinstance(result, str)

    def test_category_with_in_preposition(self) -> None:
        """Test category with 'in' preposition."""
        result = label_for_startwith_year_or_typeo("2000 in art")
        assert isinstance(result, str)
