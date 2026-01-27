#!/usr/bin/python3
"""
Unit tests for model_multi_data_year_from_2.py module.

This module provides tests for MultiDataFormatterYearAndFrom2 class
which combines year-based and "from" relation category translations
with category_relation_mapping support.
"""

import pytest

from ArWikiCats.translations_formats.DataModel import FormatDataFrom
from ArWikiCats.translations_formats.DataModelMulti import MultiDataFormatterBaseHelpers
from ArWikiCats.translations_formats.DataModelMulti.model_multi_data_year_from_2 import (
    MultiDataFormatterYearAndFrom2,
)


class TestMultiDataFormatterYearAndFrom2Init:
    """Tests for MultiDataFormatterYearAndFrom2 initialization."""

    def test_init_basic(self):
        """Test basic initialization of MultiDataFormatterYearAndFrom2."""
        country_bot = FormatDataFrom(
            formatted_data={"{year1} {country1}": "{country1} في {year1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "اليمن" if "yemen" in x.lower() else "",
            match_key_callback=lambda x: "yemen" if "yemen" in x.lower() else "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "2020" if "2020" in x else "",
            match_key_callback=lambda x: "2020" if "2020" in x else "",
        )

        bot = MultiDataFormatterYearAndFrom2(country_bot, year_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is year_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None
        assert bot.other_key_first is False
        assert bot.category_relation_mapping == {}

    def test_init_with_category_relation_mapping(self):
        """Test initialization with category_relation_mapping."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        mapping = {"from": "من", "in": "في", "by": "بواسطة"}

        bot = MultiDataFormatterYearAndFrom2(country_bot, year_bot, category_relation_mapping=mapping)

        assert "from" in bot.category_relation_mapping
        assert "in" in bot.category_relation_mapping
        assert "by" in bot.category_relation_mapping

    def test_init_with_other_key_first(self):
        """Test initialization with other_key_first=True."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        bot = MultiDataFormatterYearAndFrom2(country_bot, year_bot, other_key_first=True)

        assert bot.other_key_first is True

    def test_inherits_from_base_helpers(self):
        """Test that MultiDataFormatterYearAndFrom2 inherits from MultiDataFormatterBaseHelpers."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        bot = MultiDataFormatterYearAndFrom2(country_bot, year_bot)

        assert isinstance(bot, MultiDataFormatterBaseHelpers)


class TestMultiDataFormatterYearAndFrom2GetRelationWord:
    """Tests for MultiDataFormatterYearAndFrom2.get_relation_word method."""

    @pytest.fixture
    def bot_with_mapping(self):
        """Create a bot with category_relation_mapping."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        mapping = {
            "from": "من",
            "in": "في",
            "published by": "نشرتها",
        }
        return MultiDataFormatterYearAndFrom2(country_bot, year_bot, category_relation_mapping=mapping)

    def test_get_relation_word_from(self, bot_with_mapping):
        """Test get_relation_word with 'from' relation."""
        key, ar = bot_with_mapping.get_relation_word("People from Germany")
        assert key == "from"
        assert ar == "من"

    def test_get_relation_word_in(self, bot_with_mapping):
        """Test get_relation_word with 'in' relation."""
        key, ar = bot_with_mapping.get_relation_word("Buildings in France")
        assert key == "in"
        assert ar == "في"

    def test_get_relation_word_no_match(self, bot_with_mapping):
        """Test get_relation_word when no relation matches."""
        key, ar = bot_with_mapping.get_relation_word("German writers")
        assert key == ""
        assert ar == ""

    def test_get_relation_word_multi_word(self, bot_with_mapping):
        """Test get_relation_word with multi-word relation."""
        key, ar = bot_with_mapping.get_relation_word("Works published by Oxford")
        assert key == "published by"
        assert ar == "نشرتها"


class TestMultiDataFormatterYearAndFrom2ResolveRelationLabel:
    """Tests for MultiDataFormatterYearAndFrom2.resolve_relation_label method."""

    @pytest.fixture
    def bot_with_mapping(self):
        """Create a bot with category_relation_mapping."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        mapping = {"from": "من", "in": "في"}
        return MultiDataFormatterYearAndFrom2(country_bot, year_bot, category_relation_mapping=mapping)

    def test_resolve_relation_label_from(self, bot_with_mapping):
        """Test resolve_relation_label with 'from' relation."""
        result = bot_with_mapping.resolve_relation_label("Writers from Yemen", "كتاب")
        assert result == "كتاب من"

    def test_resolve_relation_label_in(self, bot_with_mapping):
        """Test resolve_relation_label with 'in' relation."""
        result = bot_with_mapping.resolve_relation_label("People in Germany", "أشخاص")
        assert result == "أشخاص في"

    def test_resolve_relation_label_no_match(self, bot_with_mapping):
        """Test resolve_relation_label when no relation matches."""
        result = bot_with_mapping.resolve_relation_label("German writers", "كتاب")
        assert result == "كتاب"

    def test_resolve_relation_label_empty_base_label(self, bot_with_mapping):
        """Test resolve_relation_label with empty base_label."""
        result = bot_with_mapping.resolve_relation_label("Writers from Yemen", "")
        assert result == ""

    def test_resolve_relation_label_empty_category(self, bot_with_mapping):
        """Test resolve_relation_label with empty category."""
        result = bot_with_mapping.resolve_relation_label("", "كتاب")
        assert result == "كتاب"

    def test_resolve_relation_label_already_has_relation(self, bot_with_mapping):
        """Test resolve_relation_label when base_label already ends with relation."""
        result = bot_with_mapping.resolve_relation_label("Writers from Yemen", "كتاب من")
        assert result == "كتاب من"

    def test_resolve_relation_label_relation_in_middle(self, bot_with_mapping):
        """Test resolve_relation_label when relation is in the middle of base_label."""
        result = bot_with_mapping.resolve_relation_label("Writers from Yemen", "كتاب من اليمن")
        assert result == "كتاب من اليمن"


class TestMultiDataFormatterYearAndFrom2GetRelationMapping:
    """Tests for MultiDataFormatterYearAndFrom2.get_relation_mapping method."""

    def test_get_relation_mapping_empty(self):
        """Test get_relation_mapping with empty mapping."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        bot = MultiDataFormatterYearAndFrom2(country_bot, year_bot)

        assert bot.get_relation_mapping() == {}

    def test_get_relation_mapping_with_data(self):
        """Test get_relation_mapping with populated mapping."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        mapping = {"from": "من", "in": "في"}

        bot = MultiDataFormatterYearAndFrom2(country_bot, year_bot, category_relation_mapping=mapping)

        result = bot.get_relation_mapping()
        assert "from" in result
        assert "in" in result
        assert result["from"] == "من"
        assert result["in"] == "في"
