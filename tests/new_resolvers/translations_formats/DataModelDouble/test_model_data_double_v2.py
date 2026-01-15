#!/usr/bin/python3
"""
Comprehensive tests for FormatDataDoubleV2 class.

This module provides exhaustive tests for:
1. ar_joiner parameter (default, custom, None, empty)
2. sort_ar_labels parameter (True/False)
3. splitter parameter (default, custom, regex patterns)
4. Combination of parameters
5. Edge cases and error handling
"""

import pytest

from ArWikiCats.translations_formats import FormatDataDoubleV2


@pytest.fixture
def base_data_v2():
    """Base data fixture with dict-based labels."""
    formatted_data = {
        "{film_key} films": "أفلام {film_label}",
        "{film_key} movies": "أفلام {film_label}",
    }
    data_list = {
        "action": {"film_label": "أكشن"},
        "drama": {"film_label": "دراما"},
        "comedy": {"film_label": "كوميدي"},
        "horror": {"film_label": "رعب"},
    }
    return formatted_data, data_list


@pytest.fixture
def multi_key_data():
    """Data with multiple keys per entry."""
    formatted_data = {
        "{genre} films": "أفلام {genre_label}",
    }
    data_list = {
        "action": {"genre_label": "أكشن"},
        "drama": {"genre_label": "دراما"},
        "horror": {"genre_label": "رعب"},
    }
    return formatted_data, data_list


# ============================================================================
# Tests for ar_joiner parameter
# ============================================================================


def test_ar_joiner_default_space(base_data_v2):
    """Test default ar_joiner (space)."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_ar_joiner_with_wa(base_data_v2):
    """Test ar_joiner with Arabic 'و' (and)."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        ar_joiner=" و ",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن و دراما"


def test_ar_joiner_with_dash(base_data_v2):
    """Test ar_joiner with dash."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        ar_joiner="-",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن-دراما"


def test_ar_joiner_none_defaults_to_space(base_data_v2):
    """Test ar_joiner=None defaults to space."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        ar_joiner=None,
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_ar_joiner_empty_defaults_to_space(base_data_v2):
    """Test ar_joiner='' defaults to space."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        ar_joiner="",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_ar_joiner_with_comma(base_data_v2):
    """Test ar_joiner with comma and space."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        ar_joiner="، ",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن، دراما"


# ============================================================================
# Tests for sort_ar_labels parameter
# ============================================================================


def test_sort_ar_labels_false_preserves_order(base_data_v2):
    """Test sort_ar_labels=False preserves original order."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        sort_ar_labels=False,
        log_multi_cache=False,
    )
    result1 = bot.search("action drama films")
    result2 = bot.search("drama action films")
    assert result1 == "أفلام أكشن دراما"
    assert result2 == "أفلام دراما أكشن"


def test_sort_ar_labels_true_sorts_alphabetically(base_data_v2):
    """Test sort_ar_labels=True sorts labels alphabetically."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        sort_ar_labels=True,
    )
    # أكشن < دراما alphabetically
    result1 = bot.search("action drama films")
    result2 = bot.search("drama action films")
    assert result1 == "أفلام أكشن دراما"
    assert result2 == "أفلام أكشن دراما"


def test_sort_ar_labels_with_comedy_drama(base_data_v2):
    """Test sort_ar_labels with comedy and drama."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        sort_ar_labels=True,
    )
    # دراما < كوميدي alphabetically
    result = bot.search("comedy drama films")
    assert result == "أفلام دراما كوميدي"


def test_sort_ar_labels_with_horror_action(base_data_v2):
    """Test sort_ar_labels with horror and action."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        sort_ar_labels=True,
    )
    # أكشن < رعب alphabetically
    result1 = bot.search("horror action films")
    result2 = bot.search("action horror films")
    assert result1 == "أفلام أكشن رعب"
    assert result2 == "أفلام أكشن رعب"


# ============================================================================
# Tests for splitter parameter
# ============================================================================


def test_splitter_default_space(base_data_v2):
    """Test default splitter (space)."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_splitter_underscore(base_data_v2):
    """Test splitter with underscore pattern."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        splitter="[_ ]",
    )
    # Should match both underscore and space
    result1 = bot.search("action_drama films")
    result2 = bot.search("action drama films")
    assert result1 == "أفلام أكشن دراما"
    assert result2 == "أفلام أكشن دراما"


def test_splitter_dash(base_data_v2):
    """Test splitter with dash."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        splitter="-",
    )
    result = bot.search("action-drama films")
    assert result == "أفلام أكشن دراما"


def test_splitter_regex_dot(base_data_v2):
    """Test splitter with regex dot (matches any character)."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        splitter=".",
    )
    # Dot matches any character
    result1 = bot.search("action.drama films")
    result2 = bot.search("action_drama films")
    result3 = bot.search("action drama films")
    assert result1 == "أفلام أكشن دراما"
    assert result2 == "أفلام أكشن دراما"
    assert result3 == "أفلام أكشن دراما"


def test_splitter_multiple_chars(base_data_v2):
    """Test splitter with multiple character pattern."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        splitter="[_\\- ]",
    )
    # Should match underscore, dash, or space
    result1 = bot.search("action_drama films")
    result2 = bot.search("action-drama films")
    result3 = bot.search("action drama films")
    assert result1 == "أفلام أكشن دراما"
    assert result2 == "أفلام أكشن دراما"
    assert result3 == "أفلام أكشن دراما"


# ============================================================================
# Tests for combined parameters
# ============================================================================


def test_ar_joiner_and_sort_combined(base_data_v2):
    """Test ar_joiner with sort_ar_labels."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        ar_joiner=" و ",
        sort_ar_labels=True,
    )
    result1 = bot.search("action drama films")
    result2 = bot.search("drama action films")
    assert result1 == "أفلام أكشن و دراما"
    assert result2 == "أفلام أكشن و دراما"


def test_splitter_and_ar_joiner_combined(base_data_v2):
    """Test splitter with ar_joiner."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        splitter="-",
        ar_joiner=" و ",
    )
    result = bot.search("action-drama films")
    assert result == "أفلام أكشن و دراما"


def test_all_three_parameters_combined(base_data_v2):
    """Test splitter, ar_joiner, and sort_ar_labels together."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        splitter="[_\\- ]",
        ar_joiner="، ",
        sort_ar_labels=True,
    )
    result1 = bot.search("drama_action films")
    result2 = bot.search("action-drama movies")
    assert result1 == "أفلام أكشن، دراما"
    assert result2 == "أفلام أكشن، دراما"


# ============================================================================
# Tests for multi-key data
# ============================================================================


def test_multi_key_default(multi_key_data):
    """Test multi-key data with default settings."""
    formatted_data, data_list = multi_key_data
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{genre}",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_multi_key_with_ar_joiner(multi_key_data):
    """Test multi-key data with custom ar_joiner."""
    formatted_data, data_list = multi_key_data
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{genre}",
        ar_joiner=" و ",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن و دراما"


def test_multi_key_with_sort(multi_key_data):
    """Test multi-key data with sort_ar_labels."""
    formatted_data, data_list = multi_key_data
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{genre}",
        sort_ar_labels=True,
    )
    result1 = bot.search("action drama films")
    result2 = bot.search("drama action films")
    # Both should be sorted: أكشن < دراما
    assert result1 == "أفلام أكشن دراما"
    assert result2 == "أفلام أكشن دراما"


# ============================================================================
# Tests for single key matching
# ============================================================================


def test_single_key_match(base_data_v2):
    """Test matching single key (not double)."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result = bot.search("action films")
    assert result == "أفلام أكشن"


def test_single_key_with_different_template(base_data_v2):
    """Test single key with different template."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result = bot.search("comedy movies")
    assert result == "أفلام كوميدي"


# ============================================================================
# Tests for edge cases
# ============================================================================


def test_no_match_returns_empty(base_data_v2):
    """Test that non-matching category returns empty string."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result = bot.search("science fiction films")
    assert result == ""


def test_partial_match_returns_empty(base_data_v2):
    """Test that partial match returns empty string."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result = bot.search("action science films")
    assert result == ""


def test_case_insensitive_matching(base_data_v2):
    """Test case-insensitive matching."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result1 = bot.search("ACTION DRAMA films")
    result2 = bot.search("Action Drama Films")
    result3 = bot.search("action drama films")
    assert result1 == "أفلام أكشن دراما"
    assert result2 == "أفلام أكشن دراما"
    assert result3 == "أفلام أكشن دراما"


def test_extra_spaces_normalized(base_data_v2):
    """Test that extra spaces are normalized."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
    )
    result = bot.search("action  drama   films")
    assert result == "أفلام أكشن دراما"


# ============================================================================
# Tests for put_label_last functionality
# ============================================================================


def test_put_label_last_basic(base_data_v2):
    """Test put_label_last functionality with log_multi_cache=False."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        log_multi_cache=False,
    )
    bot.update_put_label_last(["action"])
    # When "action" is in put_label_last, it should appear last
    result = bot.search("action drama films")
    assert result == "أفلام دراما أكشن"


def test_put_label_last_with_reverse_order(base_data_v2):
    """Test put_label_last with reverse order input."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        log_multi_cache=False,
    )
    bot.update_put_label_last(["drama"])
    result = bot.search("action drama films")
    # drama should be last, so: أكشن دراما
    assert result == "أفلام أكشن دراما"


def test_put_label_last_with_ar_joiner(base_data_v2):
    """Test put_label_last with custom ar_joiner."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        ar_joiner=" و ",
        log_multi_cache=False,
    )
    bot.update_put_label_last(["action"])
    result = bot.search("action drama films")
    assert result == "أفلام دراما و أكشن"


def test_put_label_last_both_in_list(base_data_v2):
    """Test when both keys are in put_label_last."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        log_multi_cache=False,
    )
    bot.update_put_label_last(["action", "drama"])
    # When both are in the list, order should be preserved
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


# ============================================================================
# Tests for log_multi_cache parameter
# ============================================================================


def test_log_multi_cache_true_default(base_data_v2):
    """Test log_multi_cache=True (default) caches results."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        log_multi_cache=True,
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"
    # Check that cache was populated
    assert len(bot.search_multi_cache) > 0


def test_log_multi_cache_false_no_caching(base_data_v2):
    """Test log_multi_cache=False doesn't cache results."""
    formatted_data, data_list = base_data_v2
    bot = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        log_multi_cache=False,
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"
    # Check that cache was NOT populated
    assert len(bot.search_multi_cache) == 0


def test_log_multi_cache_affects_put_label_last(base_data_v2):
    """Test that log_multi_cache=False allows put_label_last to work correctly."""
    formatted_data, data_list = base_data_v2
    # With caching enabled, put_label_last might not work after first call
    bot_cached = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        log_multi_cache=True,
    )
    bot_cached.update_put_label_last(["action"])
    result_cached = bot_cached.search("action drama films")

    # With caching disabled, put_label_last works correctly
    bot_no_cache = FormatDataDoubleV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        log_multi_cache=False,
    )
    bot_no_cache.update_put_label_last(["action"])
    result_no_cache = bot_no_cache.search("action drama films")

    # The no-cache version should respect put_label_last
    assert result_no_cache == "أفلام دراما أكشن"
