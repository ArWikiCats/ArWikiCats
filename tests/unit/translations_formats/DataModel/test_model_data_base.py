#!/usr/bin/python3
"""
Tests for model_data_base.py module.

This module provides tests for FormatDataBase abstract class which is the foundation
for all single-element category translation formatters.
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data_base import FormatDataBase


class TestFormatDataBaseAbstractMethods:
    """Tests for abstract methods that raise NotImplementedError."""

    def test_apply_pattern_replacement_raises(self):
        """Test apply_pattern_replacement raises NotImplementedError in base class."""

        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )
        with pytest.raises(NotImplementedError):
            bot.apply_pattern_replacement("template", "label")

    def test_replace_value_placeholder_raises(self):
        """Test replace_value_placeholder raises NotImplementedError in base class."""

        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )
        with pytest.raises(NotImplementedError):
            bot.replace_value_placeholder("label", "value")


class TestFormatDataBaseDataManagement:
    """Tests for data management methods: add_data_list_entry, rebuild_patterns."""

    def test_add_data_list_entry(self):
        """Test adding a new entry to data_list."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
        )
        bot.add_data_list_entry("tennis", "تنس")

        assert "tennis" in bot.data_list
        assert "tennis" in bot.data_list_ci
        assert bot.data_list["tennis"] == "تنس"
        assert bot.data_list_ci["tennis"] == "تنس"

    def test_add_data_list_entry_case_insensitive(self):
        """Test that data_list_ci stores lowercase key."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )
        bot.add_data_list_entry("Football", "كرة القدم")

        # Original case preserved in data_list
        assert "Football" in bot.data_list
        # Lowercase in data_list_ci
        assert "football" in bot.data_list_ci

    def test_rebuild_patterns(self):
        """Test that rebuild_patterns updates the regex pattern."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
        )
        # Build initial pattern
        bot.alternation = bot.create_alternation()
        bot.pattern = bot.keys_to_pattern()

        # Add new entry
        bot.add_data_list_entry("tennis", "تنس")
        bot.rebuild_patterns()

        # Verify pattern includes new key
        assert bot.alternation is not None
        assert "tennis" in bot.alternation
        assert "football" in bot.alternation


class TestFormatDataBaseCacheManagement:
    """Tests for cache management methods: clear_cache, get_cache_stats."""

    def test_clear_cache_resets_stats(self):
        """Test that clear_cache resets the cache statistics."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
        )
        bot._cache_hits = 100
        bot._cache_misses = 50

        bot.clear_cache()

        assert bot._cache_hits == 0
        assert bot._cache_misses == 0

    def test_get_cache_stats_returns_sizes(self):
        """Test that get_cache_stats returns correct dictionary sizes."""
        bot = FormatDataBase(
            formatted_data={"{sport} players": "لاعبو {sport}"},
            data_list={"football": "كرة القدم", "tennis": "تنس"},
            key_placeholder="{sport}",
        )

        stats = bot.get_cache_stats()

        assert stats["data_list_size"] == 2
        assert stats["formatted_data_size"] == 1

    def test_get_cache_stats_with_lru_cache(self):
        """Test that get_cache_stats includes LRU cache info when available."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
        )
        # Build pattern and call match_key to populate cache
        bot.alternation = bot.create_alternation()
        bot.pattern = bot.keys_to_pattern()
        bot.match_key("football players")

        stats = bot.get_cache_stats()

        # match_key should have cache info since it uses @lru_cache
        assert "match_key_cache" in stats
        assert isinstance(stats["match_key_cache"]["hits"], int)
        assert isinstance(stats["match_key_cache"]["misses"], int)


class TestFormatDataBaseMixin:
    """Tests for CategoryPrefixMixin methods inherited by FormatDataBase."""

    def test_prepend_arabic_category_prefix_inherits_from_mixin(self):
        """Test that prepend_arabic_category_prefix works via mixin inheritance."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )

        result = bot.prepend_arabic_category_prefix("category:Football", "كرة القدم")
        assert result == "تصنيف:كرة القدم"

    def test_check_placeholders_inherits_from_mixin(self):
        """Test that check_placeholders works via mixin inheritance."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )

        # Valid result
        result = bot.check_placeholders("Football", "كرة القدم")
        assert result == "كرة القدم"

        # Invalid result with unprocessed placeholder
        result = bot.check_placeholders("Football", "لاعبو {sport}")
        assert result == ""

    def test_strip_category_prefix_static_method(self):
        """Test the strip_category_prefix static method from mixin."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )

        assert bot.strip_category_prefix("category:Football") == "Football"
        assert bot.strip_category_prefix("Category:Football") == "Football"
        assert bot.strip_category_prefix("Football") == "Football"

    def test_normalize_category_string_static_method(self):
        """Test the normalize_category_string static method from mixin."""
        bot = FormatDataBase(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
        )

        # Normalize whitespace
        assert bot.normalize_category_string("  Football   players  ") == "Football players"

        # Normalize and strip prefix
        assert bot.normalize_category_string("category:Football players", strip_prefix=True) == "Football players"
