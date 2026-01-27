#!/usr/bin/python3
"""
Integration tests for model_multi_data_double.py module.

This module provides integration tests for MultiDataFormatterDataDouble class
which combines FormatData with FormatDataDouble for double-key category translations.
"""

import pytest

from ArWikiCats.translations_formats.DataModel import FormatData
from ArWikiCats.translations_formats.DataModelDouble import FormatDataDouble
from ArWikiCats.translations_formats.DataModelDouble.model_multi_data_double import (
    MultiDataFormatterDataDouble,
)


class TestMultiDataFormatterDataDoubleIntegration:
    """Integration tests for MultiDataFormatterDataDouble class."""

    @pytest.fixture
    def film_bot(self):
        """Create a MultiDataFormatterDataDouble instance for film categories."""
        country_bot = FormatData(
            formatted_data={
                "{nat_en} films": "أفلام {nat_ar}",
                "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
            },
            data_list={"british": "بريطانية", "american": "أمريكية", "french": "فرنسية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={"{film_key} films": "أفلام {film_ar}"},
            data_list={
                "action": "حركة",
                "drama": "درامية",
                "comedy": "كوميدية",
                "horror": "رعب",
            },
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )
        return MultiDataFormatterDataDouble(country_bot, genre_bot)

    def test_create_label_single_genre(self, film_bot):
        """Test create_label with single genre."""
        result = film_bot.create_label("british action films")
        assert result == "أفلام حركة بريطانية"

    def test_create_label_double_genre(self, film_bot):
        """Test create_label with double genre."""
        result = film_bot.create_label("american action drama films")
        assert result == "أفلام حركة درامية أمريكية"

    def test_create_label_nationality_only(self, film_bot):
        """Test create_label with nationality only."""
        result = film_bot.country_bot.search("french films")
        assert result == "أفلام فرنسية"

    def test_search_same_as_create_label(self, film_bot):
        """Test that search is same as create_label."""
        create_result = film_bot.create_label("british comedy films")
        search_result = film_bot.search("british comedy films")
        assert create_result == search_result

    def test_normalize_both_new(self, film_bot):
        """Test normalize_both_new extracts both keys."""
        result = film_bot.normalize_both_new("american action films")
        assert result.nat_key == "american"
        assert result.other_key == "action"
        assert result.category == "american action films"


class TestMultiDataFormatterDataDoubleSearchAll:
    """Integration tests for MultiDataFormatterDataDouble.search_all method."""

    @pytest.fixture
    def bot(self):
        """Create a MultiDataFormatterDataDouble instance."""
        country_bot = FormatData(
            formatted_data={
                "{nat_en} films": "أفلام {nat_ar}",
                "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
            },
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={"{film_key} films": "أفلام {film_ar}"},
            data_list={"action": "حركة", "drama": "درامية"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )
        return MultiDataFormatterDataDouble(country_bot, genre_bot)

    def test_search_all_combined_label(self, bot):
        """Test search_all with combined nationality and genre."""
        result = bot.search_all("british action films")
        assert result == "أفلام حركة بريطانية"

    def test_search_all_country_only(self, bot):
        """Test search_all falls back to country_bot."""
        result = bot.search_all("british films")
        assert result == "أفلام بريطانية"

    def test_search_all_genre_only(self, bot):
        """Test search_all falls back to other_bot."""
        result = bot.search_all("action films")
        assert result == "أفلام حركة"

    def test_search_all_with_prefix(self, bot):
        """Test search_all with Arabic category prefix."""
        result = bot.search_all("Category:british action films", add_arabic_category_prefix=True)
        assert result == "تصنيف:أفلام حركة بريطانية"


class TestMultiDataFormatterDataDoubleWithDataToFind:
    """Integration tests for MultiDataFormatterDataDouble with data_to_find."""

    @pytest.fixture
    def bot_with_data_to_find(self):
        """Create a bot with data_to_find for direct lookups."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={},
            data_list={"action": "حركة"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )
        data_to_find = {"special film": "فيلم خاص"}
        return MultiDataFormatterDataDouble(country_bot, genre_bot, data_to_find=data_to_find)

    def test_create_label_uses_data_to_find(self, bot_with_data_to_find):
        """Test that create_label uses data_to_find for direct lookups."""
        result = bot_with_data_to_find.create_label("special film")
        assert result == "فيلم خاص"


class TestMultiDataFormatterDataDoubleEdgeCases:
    """Integration tests for MultiDataFormatterDataDouble edge cases."""

    def test_empty_result_when_no_match(self):
        """Test returns empty string when no match found."""
        country_bot = FormatData(
            formatted_data={"{nat_en} films": "أفلام {nat_ar}"},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={"{film_key} films": "أفلام {film_ar}"},
            data_list={"action": "حركة"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )
        bot = MultiDataFormatterDataDouble(country_bot, genre_bot)

        result = bot.create_label("unknown category")
        assert result == ""

    def test_double_key_genre(self):
        """Test with double-key genre like 'action drama'."""
        country_bot = FormatData(
            formatted_data={
                "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
            },
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={},
            data_list={
                "action": "حركة",
                "drama": "درامية",
            },
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )
        bot = MultiDataFormatterDataDouble(country_bot, genre_bot)

        result = bot.create_label("british action drama films")
        assert result == "أفلام حركة درامية بريطانية"
