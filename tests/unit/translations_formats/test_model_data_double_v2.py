#!/usr/bin/python3
"""
Tests for model_data_double_v2.py module.

This module provides tests for FormatDataDoubleV2 class which handles
double-key template-driven category translations where data_list values
can be dictionaries.
"""

import pytest

from ArWikiCats.translations_formats.DataModelDouble.model_data_double_v2 import (
    FormatDataDoubleV2,
)


class TestFormatDataDoubleV2Init:
    """Tests for FormatDataDoubleV2 initialization."""

    def test_init_default(self):
        """Test initialization with default parameters."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        assert bot.formatted_data == formatted_data
        assert bot.data_list == data_list
        assert bot.key_placeholder == "{genre}"
        assert bot.text_after == ""
        assert bot.text_before == ""
        assert bot.splitter == " "
        assert bot.ar_joiner == " "
        assert bot.sort_ar_labels is False
        assert bot.log_multi_cache is True

    def test_init_with_text_after(self):
        """Test initialization with text_after parameter."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            text_after="test",
        )
        assert bot.text_after == "test"

    def test_init_with_text_before(self):
        """Test initialization with text_before parameter."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            text_before="test ",
        )
        assert bot.text_before == "test "

    def test_init_with_splitter(self):
        """Test initialization with custom splitter."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            splitter="[_ ]",
        )
        assert bot.splitter == "[_ ]"

    def test_init_with_ar_joiner(self):
        """Test initialization with custom ar_joiner."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            ar_joiner=" و ",
        )
        assert bot.ar_joiner == " و "

    def test_init_with_sort_ar_labels(self):
        """Test initialization with sort_ar_labels=True."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            sort_ar_labels=True,
        )
        assert bot.sort_ar_labels is True

    def test_init_with_log_multi_cache_false(self):
        """Test initialization with log_multi_cache=False."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            log_multi_cache=False,
        )
        assert bot.log_multi_cache is False


class TestFormatDataDoubleV2UpdatePutLabelLast:
    """Tests for FormatDataDoubleV2.update_put_label_last method."""

    def test_update_put_label_last_with_list(self):
        """Test update_put_label_last with a list."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        bot.update_put_label_last(["upcoming", "recent"])
        assert bot.put_label_last == ["upcoming", "recent"]

    def test_update_put_label_last_with_set(self):
        """Test update_put_label_last with a set."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        bot.update_put_label_last({"upcoming", "recent"})
        assert bot.put_label_last == {"upcoming", "recent"}


class TestFormatDataDoubleV2Search:
    """Tests for FormatDataDoubleV2._search method."""

    def test_search_exact_match_in_formatted_data(self):
        """Test _search with exact match in formatted_data_ci."""
        formatted_data = {"action films": "أفلام أكشن"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot._search("action films")
        assert result == "أفلام أكشن"

    def test_search_single_key(self):
        """Test _search with single key match."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot._search("action films")
        assert result == "أفلام أكشن"

    def test_search_double_key(self):
        """Test _search with double key match."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot._search("action drama films")
        assert result == "أفلام أكشن دراما"

    def test_search_no_key_match(self):
        """Test _search when no key matches."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot._search("no match films")
        assert result == ""

    def test_search_no_label_match(self):
        """Test _search when key matches but no label found."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {}  # Empty data_list
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot._search("action films")
        assert result == ""

    def test_search_no_template_match(self):
        """Test _search when key and label match but no template found."""
        formatted_data = {}  # Empty formatted_data
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot._search("action films")
        assert result == ""


class TestFormatDataDoubleV2KeysToPatternDouble:
    """Tests for FormatDataDoubleV2.keys_to_pattern_double method."""

    def test_keys_to_pattern_double_returns_pattern(self):
        """Test keys_to_pattern_double returns a compiled regex pattern."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        pattern = bot.keys_to_pattern_double()
        assert pattern is not None
        # Should match "action drama" with space separator
        match = pattern.search(" action drama ")
        assert match is not None
        assert match.group(1) == "action"
        assert match.group(2) == " "
        assert match.group(3) == "drama"

    def test_keys_to_pattern_double_with_custom_splitter(self):
        """Test keys_to_pattern_double with custom splitter."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            splitter="[_ ]",
        )
        pattern = bot.keys_to_pattern_double()
        assert pattern is not None
        # Should match "action_drama" with underscore separator
        match = pattern.search(" action_drama ")
        assert match is not None
        assert match.group(1) == "action"
        assert match.group(2) == "_"
        assert match.group(3) == "drama"

    def test_keys_to_pattern_double_empty_data_list(self):
        """Test keys_to_pattern_double returns None with empty data_list."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        pattern = bot.keys_to_pattern_double()
        assert pattern is None


class TestFormatDataDoubleV2MatchKey:
    """Tests for FormatDataDoubleV2.match_key method."""

    def test_match_key_exact_in_data_list(self):
        """Test match_key with exact match in data_list_ci."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot.match_key("action")
        assert result == "action"

    def test_match_key_double_key(self):
        """Test match_key with double key match."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot.match_key("action drama films")
        assert result == "action drama"
        # Check that keys_to_split was populated
        assert "action drama" in bot.keys_to_split
        assert bot.keys_to_split["action drama"] == ["action", "drama"]

    def test_match_key_single_key(self):
        """Test match_key with single key match."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot.match_key("action films")
        assert result == "action"

    def test_match_key_no_match(self):
        """Test match_key with no match."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot.match_key("no match here")
        assert result == ""

    def test_match_key_normalizes_spaces(self):
        """Test match_key normalizes extra spaces."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        result = bot.match_key("action    drama   films")
        assert result == "action drama"


class TestFormatDataDoubleV2ApplyPatternReplacement:
    """Tests for FormatDataDoubleV2.apply_pattern_replacement method."""

    def test_apply_pattern_replacement_dict(self):
        """Test apply_pattern_replacement with dict value."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن", "other": "other"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        template_label = "أفلام {genre_label}"
        sport_label = {"genre_label": "أكشن", "other": "other"}
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == "أفلام أكشن"

    def test_apply_pattern_replacement_string_value(self):
        """Test apply_pattern_replacement with string value returns template unchanged."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": "أكشن"}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        template_label = "أفلام {genre_label}"
        sport_label = "أكشن"
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == template_label

    def test_apply_pattern_replacement_multiple_placeholders(self):
        """Test apply_pattern_replacement with multiple placeholders."""
        formatted_data = {"{genre} films": "أفلام {genre_label} {other}"}
        data_list = {"action": {"genre_label": "أكشن", "other": "اخرى"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        template_label = "أفلام {genre_label} {other}"
        sport_label = {"genre_label": "أكشن", "other": "اخرى"}
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == "أفلام أكشن اخرى"


class TestFormatDataDoubleV2CreateLabelFromKeys:
    """Tests for FormatDataDoubleV2.create_label_from_keys method."""

    def test_create_label_from_keys_both_exist(self):
        """Test create_label_from_keys when both keys have dict labels."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.create_label_from_keys("action", "drama")
        assert result == {"genre_label": "أكشن دراما"}

    def test_create_label_from_keys_missing_first(self):
        """Test create_label_from_keys when first key is missing."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"drama": {"genre_label": "دراما"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.create_label_from_keys("action", "drama")
        assert result == ""

    def test_create_label_from_keys_missing_second(self):
        """Test create_label_from_keys when second key is missing."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.create_label_from_keys("action", "drama")
        assert result == ""

    def test_create_label_from_keys_non_dict_first(self):
        """Test create_label_from_keys when first key has non-dict label."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": "أكشن",  # String instead of dict
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.create_label_from_keys("action", "drama")
        assert result == ""

    def test_create_label_from_keys_non_dict_second(self):
        """Test create_label_from_keys when second key has non-dict label."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": "دراما",  # String instead of dict
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.create_label_from_keys("action", "drama")
        assert result == ""

    def test_create_label_from_keys_with_put_label_last(self):
        """Test create_label_from_keys with put_label_last."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "upcoming": {"genre_label": "قادمة"},
            "horror": {"genre_label": "رعب"},
            "yemeni": {"genre_label": "يمنية"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )
        bot.update_put_label_last(["upcoming"])

        result = bot.create_label_from_keys("upcoming", "horror")
        # "upcoming" is in put_label_last, so order is swapped
        assert result == {"genre_label": "رعب قادمة"}

    def test_create_label_from_keys_with_sort(self):
        """Test create_label_from_keys with sort_ar_labels=True."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            sort_ar_labels=True,
        )

        result = bot.create_label_from_keys("action", "drama")
        # Should be sorted alphabetically: "أكشن" < "دراما"
        assert result == {"genre_label": "أكشن دراما"}

    def test_create_label_from_keys_with_log_multi_cache(self):
        """Test create_label_from_keys caches result when log_multi_cache=True."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            log_multi_cache=True,
        )

        bot.create_label_from_keys("action", "drama")
        # Check that result was cached in search_multi_cache
        # Key is "drama action" (part2 + " " + part1)
        assert "drama action" in bot.search_multi_cache
        assert bot.search_multi_cache["drama action"] == {"genre_label": "أكشن دراما"}

    def test_create_label_from_keys_no_log_multi_cache(self):
        """Test create_label_from_keys doesn't cache when log_multi_cache=False."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            log_multi_cache=False,
        )

        bot.create_label_from_keys("action", "drama")
        # Check that result was NOT cached in search_multi_cache
        assert "drama action" not in bot.search_multi_cache


class TestFormatDataDoubleV2GetKeyLabel:
    """Tests for FormatDataDoubleV2.get_key_label method."""

    def test_get_key_label_direct_match(self):
        """Test get_key_label with direct match in data_list_ci."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.get_key_label("action")
        assert result == {"genre_label": "أكشن"}

    def test_get_key_label_from_cache(self):
        """Test get_key_label retrieves from search_multi_cache."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        # Pre-populate the cache
        bot.search_multi_cache["drama action"] = {"genre_label": "أكشن دراما"}

        result = bot.get_key_label("drama action")
        assert result == {"genre_label": "أكشن دراما"}

    def test_get_key_label_from_keys_to_split(self):
        """Test get_key_label creates label from keys_to_split."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        # Pre-populate keys_to_split
        bot.keys_to_split["action drama"] = ["action", "drama"]

        result = bot.get_key_label("action drama")
        assert result == {"genre_label": "أكشن دراما"}

    def test_get_key_label_no_match(self):
        """Test get_key_label returns empty string when no match."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.get_key_label("nomatch")
        assert result == ""


class TestFormatDataDoubleV2ReplaceValuePlaceholder:
    """Tests for FormatDataDoubleV2.replace_value_placeholder method."""

    def test_replace_value_placeholder_dict(self):
        """Test replace_value_placeholder with dict value."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        label = "أفلام {genre_label}"
        value = {"genre_label": "أكشن"}
        result = bot.replace_value_placeholder(label, value)
        assert result == "أفلام أكشن"

    def test_replace_value_placeholder_multiple_keys(self):
        """Test replace_value_placeholder with multiple placeholder keys."""
        formatted_data = {"{genre} films": "أفلام {genre_label} {other}"}
        data_list = {"action": {"genre_label": "أكشن", "other": "اخرى"}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        label = "أفلام {genre_label} {other}"
        value = {"genre_label": "أكشن", "other": "اخرى"}
        result = bot.replace_value_placeholder(label, value)
        assert result == "أفلام أكشن اخرى"

    def test_replace_value_placeholder_string_value(self):
        """Test replace_value_placeholder with string value returns label unchanged."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": "أكشن"}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        label = "أفلام {genre_label}"
        value = "أكشن"
        result = bot.replace_value_placeholder(label, value)
        assert result == label

    def test_replace_value_placeholder_non_string_value_in_dict(self):
        """Test replace_value_placeholder skips non-string values in dict."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {"action": {"genre_label": "أكشن", "other": 123}}
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        label = "أفلام {genre_label} {other}"
        value = {"genre_label": "أكشن", "other": 123}
        result = bot.replace_value_placeholder(label, value)
        # Should replace genre_label but skip other (not a string)
        assert result == "أفلام أكشن {other}"


class TestFormatDataDoubleV2SearchIntegration:
    """Integration tests for FormatDataDoubleV2.search method."""

    def test_search_single_key_full(self):
        """Test full search flow with single key."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.search("action films")
        assert result == "أفلام أكشن"

    def test_search_double_key_full(self):
        """Test full search flow with double key."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
            "comedy": {"genre_label": "كوميدي"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
        )

        result = bot.search("action drama films")
        assert result == "أفلام أكشن دراما"

    def test_search_with_custom_ar_joiner(self):
        """Test search with custom ar_joiner."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            ar_joiner=" و ",
        )

        result = bot.search("action drama films")
        assert result == "أفلام أكشن و دراما"

    def test_search_with_sort_ar_labels(self):
        """Test search with sort_ar_labels=True."""
        formatted_data = {"{genre} films": "أفلام {genre_label}"}
        data_list = {
            "action": {"genre_label": "أكشن"},
            "drama": {"genre_label": "دراما"},
        }
        bot = FormatDataDoubleV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{genre}",
            sort_ar_labels=True,
        )

        result1 = bot.search("action drama films")
        result2 = bot.search("drama action films")
        # Both should be sorted the same way
        assert result1 == result2
        assert result1 == "أفلام أكشن دراما"
