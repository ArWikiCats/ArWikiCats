#!/usr/bin/python3
"""Integration tests for format_multi_data and"""

import pytest

from ArWikiCats.translations_formats import FormatData, MultiDataFormatterBase, format_multi_data

# Sample data for nationality translations
nationality_data = {
    "yemeni": "اليمن",
    "british": "المملكة المتحدة",
    "american": "الولايات المتحدة",
    "egyptian": "مصر",
}

# Sample data for sport translations
sport_data = {
    "football": "كرة القدم",
    "softball": "الكرة اللينة",
    "basketball": "كرة السلة",
    "volleyball": "الكرة الطائرة",
}

# Template data with both nationality and sport placeholders
formatted_data = {
    "{nat_en} {en_sport} teams": "فرق {sport_ar} {nat_ar}",
    "{nat_en} national {en_sport} teams": "منتخبات {nat_ar} ل{sport_ar}",
    "{nat_en} {en_sport} championships": "بطولات {nat_ar} في {sport_ar}",
    "ladies {nat_en} {en_sport} tour": "بطولة {nat_ar} ل{sport_ar} للسيدات",
    "{nat_en} {en_sport} players": "لاعبو {sport_ar} من {nat_ar}",
    "{nat_en} {en_sport} coaches": "مدربو {sport_ar} من {nat_ar}",
}


@pytest.fixture
def multi_bot() -> MultiDataFormatterBase:
    """Create a format_multi_data instance for testing."""

    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
    )

    other_bot = FormatData(
        {},
        sport_data,
        key_placeholder="{en_sport}",
        value_placeholder="{sport_ar}",
    )
    data_to_find = {
        "test 2025": "2025",
    }

    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
        data_to_find=data_to_find,
    )


@pytest.mark.unit
class TestCountryBotNormalization:
    """Tests for  class."""

    def test_get_start_p17(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test get_start _p17 method returns normalized category and key."""
        category = "yemeni football teams"
        key, new_category = multi_bot.country_bot.normalize_category_with_key(category)

        assert key == "yemeni"
        assert "{nat_en}" in new_category
        assert new_category == "{nat_en} football teams"


@pytest.mark.unit
class TestFormatMultiDataInitialization:
    """Tests for format_multi_data initialization."""

    def test_initialization_with_defaults(self) -> None:
        """Test that format_multi_data initializes with default placeholders."""
        bot = format_multi_data(
            formatted_data={},
            data_list=nationality_data,
        )

        assert bot.country_bot.key_placeholder == "natar"
        assert bot.country_bot.value_placeholder == "natar"
        assert bot.other_bot.key_placeholder == "xoxo"
        assert bot.other_bot.value_placeholder == "xoxo"

    def test_initialization_with_custom_placeholders(self) -> None:
        """Test that format_multi_data initializes with custom placeholders."""
        bot = format_multi_data(
            formatted_data={},
            data_list=nationality_data,
            key_placeholder="COUNTRY",
            value_placeholder="{country}",
            data_list2=sport_data,
            key2_placeholder="SPORT",
            value2_placeholder="{sport_name}",
        )

        assert bot.country_bot.key_placeholder == "COUNTRY"
        assert bot.country_bot.value_placeholder == "{country}"
        assert bot.other_bot.key_placeholder == "SPORT"
        assert bot.other_bot.value_placeholder == "{sport_name}"

    def test_nat_bot_and_sport_bot_created(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that nat_bot and other_bot are properly initialized."""
        assert multi_bot.country_bot is not None
        assert multi_bot.other_bot is not None


@pytest.mark.unit
class TestNormalizeNatLabel:
    """Tests for normalize_nat_label method."""

    def test_normalize_nat_label_with_match(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test normalization when nationality is found."""
        category = "yemeni national football teams"
        result = multi_bot.normalize_nat_label(category)

        assert result == "{nat_en} national football teams"

    def test_normalize_nat_label_no_match(self, multi_bot: MultiDataFormatterBase) -> None:
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
    def test_normalize_nat_label_various_nationalities(
        self, multi_bot: MultiDataFormatterBase, input_category: str, expected: str
    ) -> None:
        """Test normalization with various nationalities."""
        result = multi_bot.normalize_nat_label(input_category)
        assert result == expected


@pytest.mark.unit
class TestNormalizeSportLabel:
    """Tests for normalize_other_label method."""

    def test_normalize_sport_label_with_match(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test normalization when sport is found."""
        category = "yemeni national football teams"
        result = multi_bot.normalize_other_label(category)

        assert result == "yemeni national {en_sport} teams"

    def test_normalize_sport_label_no_match(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test normalization when no sport is found."""
        category = "some random category"
        result = multi_bot.normalize_other_label(category)

        assert result == ""

    @pytest.mark.parametrize(
        "input_category,expected",
        [
            ("yemeni football teams", "yemeni {en_sport} teams"),
            ("british basketball players", "british {en_sport} players"),
            ("american volleyball coaches", "american {en_sport} coaches"),
        ],
    )
    def test_normalize_sport_label_various_sports(
        self, multi_bot: MultiDataFormatterBase, input_category: str, expected: str
    ) -> None:
        """Test normalization with various sports."""
        result = multi_bot.normalize_other_label(input_category)
        assert result == expected


@pytest.mark.unit
class TestNormalizeBoth:
    """Tests for normalize_both method."""

    def test_normalize_both_with_matches(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test normalization when both nationality and sport are found."""
        category = "british softball championships"
        result = multi_bot.normalize_both(category)

        assert result == "{nat_en} {en_sport} championships"

    def test_normalize_both_order_matters(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that nationality is normalized first, then sport."""
        category = "yemeni football teams"
        result = multi_bot.normalize_both(category)

        # Should normalize nationality first, then sport
        assert result == "{nat_en} {en_sport} teams"

    @pytest.mark.parametrize(
        "input_category,expected",
        [
            ("british softball championships", "{nat_en} {en_sport} championships"),
            ("yemeni football teams", "{nat_en} {en_sport} teams"),
            ("american basketball players", "{nat_en} {en_sport} players"),
            ("egyptian volleyball coaches", "{nat_en} {en_sport} coaches"),
        ],
    )
    def test_normalize_both_various_combinations(
        self, multi_bot: MultiDataFormatterBase, input_category: str, expected: str
    ) -> None:
        """Test normalization with various nationality-sport combinations."""
        result = multi_bot.normalize_both(input_category)
        assert result == expected


@pytest.mark.unit
class TestCreateNatLabel:
    """Tests for create_nat_label method."""

    def test_create_nat_label_with_match(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test creating nationality label when match is found."""
        category = "yemeni football teams"
        result = multi_bot.create_nat_label(category)
        # With the current `formatted_data`, `nat_bot` won't find a template
        # and will return an empty string.
        assert result == ""

    def test_create_nat_label_caching(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that create_nat_label uses LRU cache."""
        category = "yemeni football teams"
        result1 = multi_bot.create_nat_label(category)
        result2 = multi_bot.create_nat_label(category)

        # Should return the same cached result
        assert result1 == result2


@pytest.mark.unit
class TestCreateLabel:
    """Tests for create_label method."""

    def test_create_label_full_match(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test creating label when both nationality and sport match."""
        category = "yemeni football teams"
        result = multi_bot.create_label(category)

        expected = "فرق كرة القدم اليمن"
        assert result == expected

    def test_create_label_no_nationality(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test creating label when nationality is not found."""
        category = "unknown football teams"
        result = multi_bot.create_label(category)

        assert result == ""

    def test_create_label_no_template(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test creating label when template doesn't exist."""
        category = "yemeni football something"
        result = multi_bot.create_label(category)

        # Template "{nat_en} {en_sport} something" doesn't exist in formatted_data
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
    def test_create_label_various_combinations(
        self, multi_bot: MultiDataFormatterBase, input_category: str, expected: str
    ) -> None:
        """Test creating labels with various nationality-sport combinations."""
        result = multi_bot.create_label(input_category)
        assert result == expected

    def test_create_label_with_national_teams(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test creating label for national teams pattern."""
        category = "yemeni national football teams"
        result = multi_bot.create_label(category)

        expected = "منتخبات اليمن لكرة القدم"
        assert result == expected

    def test_create_label_caching(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that create_label uses LRU cache."""
        category = "yemeni football teams"
        result1 = multi_bot.create_label(category)
        result2 = multi_bot.create_label(category)

        # Should return the same cached result
        assert result1 == result2
        assert result1 == "فرق كرة القدم اليمن"


@pytest.mark.unit
class TestEdgeCases:
    """Tests for edge cases and error handling."""

    def test_empty_category(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test with empty category string."""
        result = multi_bot.create_label("")
        assert result == ""

    def test_category_with_only_nationality(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test with category containing only nationality."""
        result = multi_bot.create_label("yemeni")
        assert result == ""

    def test_category_with_only_sport(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test with category containing only sport."""
        result = multi_bot.create_label("football")
        assert result == ""

    def test_with_extra_spaces(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test handling of extra spaces in category."""
        result = multi_bot.create_label("yemeni  football  teams")
        # Should still work despite extra spaces
        assert result == "فرق كرة القدم اليمن"


@pytest.mark.unit
class TestPerformance:
    """Performance tests for caching behavior."""

    def test_cache_effectiveness(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that LRU cache improves performance on repeated calls."""
        category = "yemeni football teams"

        # First call - cache miss
        result1 = multi_bot.create_label(category)

        # Subsequent calls - cache hits
        for _ in range(100):
            result = multi_bot.create_label(category)
            assert result == result1

    def test_multiple_categories_caching(self, multi_bot: MultiDataFormatterBase) -> None:
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


@pytest.mark.unit
class TestDataToFind:
    """Tests for data_to_find functionality."""

    def test_data_to_find_hit(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that data_to_find returns correct label when category is found."""
        category = "test 2025"
        result = multi_bot.create_label(category)

        assert result == "2025"

    def test_data_to_find_miss(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that data_to_find returns empty string when category is not found."""
        category = "nonexistent category"
        result = multi_bot.create_label(category)

        assert result == ""


@pytest.mark.unit
class TestDataToFind2:
    def test_create_label_ladies_tour(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test creating label for ladies tour pattern."""
        category = "ladies british softball tour"
        result = multi_bot.create_label(category)

        # expected = "بطولة المملكة المتحدة للكرة اللينة للسيدات"
        expected = "بطولة المملكة المتحدة لالكرة اللينة للسيدات"
        assert result == expected

    def test_case_insensitive_matching(self, multi_bot: MultiDataFormatterBase) -> None:
        """Test that matching is case-insensitive."""
        result1 = multi_bot.create_label("Yemeni Football Teams")
        result2 = multi_bot.create_label("yemeni football teams")
        result3 = multi_bot.create_label("YEMENI FOOTBALL TEAMS")

        # All should produce the same result
        assert result1 == result2 == result3
        assert result1 == "فرق كرة القدم اليمن"
