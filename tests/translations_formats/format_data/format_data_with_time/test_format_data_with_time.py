#!/usr/bin/python3
"""Integration tests for FormatMultiData and FormatComparisonHelper"""

import pytest

from ArWikiCats.translations_formats.format_multi_data import (
    FormatMultiData,
)

# Sample data for nationality translations
nationality_data = {
    "yemen": "اليمن",
    "United States": "الولايات المتحدة",
    "egypt": "مصر",
}

# Template data with both nationality and sport placeholders
formatted_data = {
    "{year1} in {country1}": "{country1} في {year1}",
    "{year1} establishments in {country1}": "تأسيسات سنة {year1} في {country1}",
    "{year1} events in {country1}": "أحداث {year1} في {country1}",
    "{year1} disestablishments in {country1}": "انحلالات سنة {year1} في {country1}",  # 4600
    "{year1} sports events in {country1}": "أحداث {year1} الرياضية في {country1}",  # 6108
    "{year1} crimes in {country1}": "جرائم {year1} في {country1}",  # 3966
    "{year1} murders in {country1}": "جرائم قتل في {country1} في {year1}",
    "{year1} disasters in {country1}": "كوارث في {country1} في {year1}",  # 2140
}


@pytest.fixture
def multi_bot():
    """Create a FormatMultiData instance for testing."""
    return FormatMultiData(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=sport_data,
        key2_placeholder="{sport_en}",
        value2_placeholder="{sport_ar}",
    )


class TestFormatComparisonHelper:
    """Tests for FormatComparisonHelper class."""

    def test_get_start_p17(self, multi_bot):
        """Test get_start_p17 method returns normalized category and key."""
        category = "yemeni football teams"
        new_category, key = multi_bot.get_start_p17(category)

        assert key == "yemeni"
        assert "{nat_en}" in new_category
        assert new_category == "{nat_en} football teams"


class TestFormatMultiDataInitialization:
    """Tests for FormatMultiData initialization."""

    def test_initialization_with_defaults(self):
        """Test that FormatMultiData initializes with default placeholders."""
        bot = FormatMultiData(
            formatted_data={},
            data_list=nationality_data,
        )

        assert bot.key_placeholder == "natar"
        assert bot.value_placeholder == "natar"
        assert bot.key2_placeholder == "xoxo"
        assert bot.value2_placeholder == "xoxo"

    def test_initialization_with_custom_placeholders(self):
        """Test that FormatMultiData initializes with custom placeholders."""
        bot = FormatMultiData(
            formatted_data={},
            data_list=nationality_data,
            key_placeholder="COUNTRY",
            value_placeholder="{country}",
            data_list2=sport_data,
            key2_placeholder="SPORT",
            value2_placeholder="{sport_name}",
        )

        assert bot.key_placeholder == "COUNTRY"
        assert bot.value_placeholder == "{country}"
        assert bot.key2_placeholder == "SPORT"
        assert bot.value2_placeholder == "{sport_name}"

    def test_nat_bot_and_sport_bot_created(self, multi_bot):
        """Test that nat_bot and sport_bot are properly initialized."""
        assert multi_bot.nat_bot is not None
        assert multi_bot.sport_bot is not None


class TestNormalizeNatLabel:
    """Tests for normalize_nat_label method."""

    def test_normalize_nat_label_with_match(self, multi_bot):
        """Test normalization when nationality is found."""
        category = "yemeni national football teams"
        result = multi_bot.normalize_nat_label(category)

        assert result == "{nat_en} national football teams"

    def test_normalize_nat_label_no_match(self, multi_bot):
        """Test normalization when no nationality is found."""
        category = "some random category"
        result = multi_bot.normalize_nat_label(category)

        assert result == ""

    @pytest.mark.parametrize(
        "input_category,expected",
        [
            ("british football teams", "{nat_en} football teams"),
            ("american basketball players", "{nat_en} basketball players"),
            ("egyptian volleyball coaches", "{nat_en} volleyball coaches"),
        ],
    )
    def test_normalize_nat_label_various_nationalities(self, multi_bot, input_category, expected):
        """Test normalization with various nationalities."""
        result = multi_bot.normalize_nat_label(input_category)
        assert result == expected


class TestNormalizeSportLabel:
    """Tests for normalize_sport_label method."""

    def test_normalize_sport_label_with_match(self, multi_bot):
        """Test normalization when sport is found."""
        category = "yemeni national football teams"
        result = multi_bot.normalize_sport_label(category)

        assert result == "yemeni national {sport_en} teams"

    def test_normalize_sport_label_no_match(self, multi_bot):
        """Test normalization when no sport is found."""
        category = "some random category"
        result = multi_bot.normalize_sport_label(category)

        assert result == ""

    @pytest.mark.parametrize(
        "input_category,expected",
        [
            ("yemeni football teams", "yemeni {sport_en} teams"),
            ("british basketball players", "british {sport_en} players"),
            ("american volleyball coaches", "american {sport_en} coaches"),
        ],
    )
    def test_normalize_sport_label_various_sports(self, multi_bot, input_category, expected):
        """Test normalization with various sports."""
        result = multi_bot.normalize_sport_label(input_category)
        assert result == expected


class TestNormalizeBoth:
    """Tests for normalize_both method."""

    def test_normalize_both_with_matches(self, multi_bot):
        """Test normalization when both nationality and sport are found."""
        category = "british softball championships"
        result = multi_bot.normalize_both(category)

        assert result == "{nat_en} {sport_en} championships"

    def test_normalize_both_order_matters(self, multi_bot):
        """Test that nationality is normalized first, then sport."""
        category = "yemeni football teams"
        result = multi_bot.normalize_both(category)

        # Should normalize nationality first, then sport
        assert result == "{nat_en} {sport_en} teams"

    @pytest.mark.parametrize(
        "input_category,expected",
        [
            ("british softball championships", "{nat_en} {sport_en} championships"),
            ("yemeni football teams", "{nat_en} {sport_en} teams"),
            ("american basketball players", "{nat_en} {sport_en} players"),
            ("egyptian volleyball coaches", "{nat_en} {sport_en} coaches"),
        ],
    )
    def test_normalize_both_various_combinations(self, multi_bot, input_category, expected):
        """Test normalization with various nationality-sport combinations."""
        result = multi_bot.normalize_both(input_category)
        assert result == expected


class TestCreateNatLabel:
    """Tests for create_nat_label method."""

    def test_create_nat_label_with_match(self, multi_bot):
        """Test creating nationality label when match is found."""
        category = "yemeni football teams"
        result = multi_bot.create_nat_label(category)
        # With the current `formated_data`, `nat_bot` won't find a template
        # and will return an empty string.
        assert result == ""

    def test_create_nat_label_caching(self, multi_bot):
        """Test that create_nat_label uses LRU cache."""
        category = "yemeni football teams"
        result1 = multi_bot.create_nat_label(category)
        result2 = multi_bot.create_nat_label(category)

        # Should return the same cached result
        assert result1 == result2


class TestCreateLabel:
    """Tests for create_label method."""

    def test_create_label_full_match(self, multi_bot):
        """Test creating label when both nationality and sport match."""
        category = "yemeni football teams"
        result = multi_bot.create_label(category)

        expected = "فرق كرة القدم اليمن"
        assert result == expected

    def test_create_label_no_nationality(self, multi_bot):
        """Test creating label when nationality is not found."""
        category = "unknown football teams"
        result = multi_bot.create_label(category)

        assert result == ""

    def test_create_label_no_template(self, multi_bot):
        """Test creating label when template doesn't exist."""
        category = "yemeni football something"
        result = multi_bot.create_label(category)

        # Template "{nat_en} {sport_en} something" doesn't exist in formatted_data
        assert result == ""

    @pytest.mark.parametrize(
        "input_category,expected",
        [
            ("yemeni football teams", "فرق كرة القدم اليمن"),
            ("british softball championships", "بطولات المملكة المتحدة في الكرة اللينة"),
            ("american basketball players", "لاعبو كرة السلة من الولايات المتحدة"),
            ("egyptian volleyball coaches", "مدربو الكرة الطائرة من مصر"),
        ],
    )
    def test_create_label_various_combinations(self, multi_bot, input_category, expected):
        """Test creating labels with various nationality-sport combinations."""
        result = multi_bot.create_label(input_category)
        assert result == expected

    def test_create_label_with_national_teams(self, multi_bot):
        """Test creating label for national teams pattern."""
        category = "yemeni national football teams"
        result = multi_bot.create_label(category)

        expected = "منتخبات اليمن لكرة القدم"
        assert result == expected

    @pytest.mark.skip2
    def test_create_label_ladies_tour(self, multi_bot):
        """Test creating label for ladies tour pattern."""
        category = "ladies british softball tour"
        result = multi_bot.create_label(category)

        expected = "بطولة المملكة المتحدة للكرة اللينة للسيدات"
        assert result == expected

    def test_create_label_caching(self, multi_bot):
        """Test that create_label uses LRU cache."""
        category = "yemeni football teams"
        result1 = multi_bot.create_label(category)
        result2 = multi_bot.create_label(category)

        # Should return the same cached result
        assert result1 == result2
        assert result1 == "فرق كرة القدم اليمن"


class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_empty_category(self, multi_bot):
        """Test with empty category string."""
        result = multi_bot.create_label("")
        assert result == ""

    def test_category_with_only_nationality(self, multi_bot):
        """Test with category containing only nationality."""
        result = multi_bot.create_label("yemeni")
        assert result == ""

    def test_category_with_only_sport(self, multi_bot):
        """Test with category containing only sport."""
        result = multi_bot.create_label("football")
        assert result == ""

    @pytest.mark.skip2
    def test_case_insensitive_matching(self, multi_bot):
        """Test that matching is case-insensitive."""
        result1 = multi_bot.create_label("Yemeni Football Teams")
        result2 = multi_bot.create_label("yemeni football teams")
        result3 = multi_bot.create_label("YEMENI FOOTBALL TEAMS")

        # All should produce the same result
        assert result1 == result2 == result3
        assert result1 == "فرق كرة القدم اليمن"

    def test_with_extra_spaces(self, multi_bot):
        """Test handling of extra spaces in category."""
        result = multi_bot.create_label("yemeni  football  teams")
        # Should still work despite extra spaces
        assert result == "فرق كرة القدم اليمن"


class TestWithTextAfterAndBefore:
    """Tests for FormatMultiData with text_after and text_before parameters."""

    @pytest.mark.skip2
    def test_with_text_after(self):
        """Test FormatMultiData with text_after parameter."""
        bot = FormatMultiData(
            formatted_data={"{nat_en}ian {sport_en} teams": "فرق {sport_ar} {nat_ar}"},
            data_list={"yemeni": "اليمن"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
            data_list2={"football": "كرة القدم"},
            key2_placeholder="{sport_en}",
            value2_placeholder="{sport_ar}",
            text_after="ian",
        )

        category = "yemenian football teams"
        result = bot.create_label(category)

        assert result == "فرق كرة القدم اليمن"

    @pytest.mark.skip2
    def test_with_text_before(self):
        """Test FormatMultiData with text_before parameter."""
        bot = FormatMultiData(
            formatted_data={"the {nat_en} {sport_en} teams": "فرق {sport_ar} {nat_ar}"},
            data_list={"yemeni": "اليمن"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
            data_list2={"football": "كرة القدم"},
            key2_placeholder="{sport_en}",
            value2_placeholder="{sport_ar}",
            text_before="the ",
        )

        category = "the yemeni football teams"
        result = bot.create_label(category)

        assert result == "فرق كرة القدم اليمن"


@pytest.mark.slow
class TestPerformance:
    """Performance tests for caching behavior."""

    def test_cache_effectiveness(self, multi_bot):
        """Test that LRU cache improves performance on repeated calls."""
        category = "yemeni football teams"

        # First call - cache miss
        result1 = multi_bot.create_label(category)

        # Subsequent calls - cache hits
        for _ in range(100):
            result = multi_bot.create_label(category)
            assert result == result1

    def test_multiple_categories_caching(self, multi_bot):
        """Test caching with multiple different categories."""
        categories = [
            "yemeni football teams",
            "british softball championships",
            "american basketball players",
        ]

        # Cache all categories
        results = [multi_bot.create_label(cat) for cat in categories]

        # Verify cached results match
        for i, cat in enumerate(categories):
            assert multi_bot.create_label(cat) == results[i]
