#!/usr/bin/python3
"""
Extended tests for FormatDataDouble class.

This module provides exhaustive tests for:
1. splitter parameter
2. sort_ar_labels parameter
"""

import pytest
from ArWikiCats.translations_formats import FormatDataDouble


@pytest.fixture
def base_data():
    formatted_data = {
        "{film_key} films": "أفلام {film_ar}",
    }
    data_list = {
        "action": "أكشن",
        "drama": "دراما",
        "comedy": "كوميدي",
        "horror": "رعب",
    }
    return formatted_data, data_list


def test_splitter_default_space(base_data):
    """Test default splitter is a space."""
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        splitter=" ",
    )

    assert bot.search("action drama films") == "أفلام أكشن دراما"
    assert bot.match_key("action drama films") == "action drama"


def test_splitter_underscore(base_data):
    """Test splitter as underscore."""
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        splitter="_",
    )

    # regex for double matching uses splitter
    # rf"(?<!\w)({self.alternation})({self.splitter})({self.alternation})(?!\w)"
    assert bot.search("action_drama films") == "أفلام أكشن دراما"
    assert bot.match_key("action_drama films") == "action_drama"

    # Should NOT match with space if splitter is underscore
    assert bot.match_key("action drama films") == "action"  # Only matches first one if sequence doesn't match


def test_splitter_dash_with_spaces(base_data):
    """Test splitter as ' - '."""
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        splitter=" - ",
    )

    assert bot.search("action - drama films") == "أفلام أكشن دراما"
    assert bot.match_key("action - drama films") == "action - drama"


def test_splitter_none_handled_as_space(base_data):
    """Test that splitter=None or empty string reverts to space."""
    formatted_data, data_list = base_data
    # The code does: self.splitter = splitter or " "
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        splitter="",
    )

    assert bot.splitter == " "
    assert bot.search("action drama films") == "أفلام أكشن دراما"


def test_sort_ar_labels_false(base_data):
    """Test that labels maintain order when sort_ar_labels is False."""
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=False,
    )

    # action (أكشن), drama (دراما)
    result1 = bot.search("action drama films")
    print(f"DEBUG: result1='{result1}'")
    assert result1 == "أفلام أكشن دراما"

    result2 = bot.search("drama action films")
    print(f"DEBUG: result2='{result2}'")
    assert result2 == "أفلام دراما أكشن"


def test_sort_ar_labels_true(base_data):
    """Test that labels are sorted alphabetically when sort_ar_labels is True."""
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=True,
    )

    # أكشن (Action) starts with Alif
    # دراما (Drama) starts with Dal
    # Alif < Dal in Arabic

    # Both should result in "أفلام أكشن دراما"
    assert bot.search("action drama films") == "أفلام أكشن دراما"
    assert bot.search("drama action films") == "أفلام أكشن دراما"


def test_sort_ar_labels_true_complex(base_data):
    """Test sorting with multiple pairs to ensure alphabetical consistency."""
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=True,
    )

    # رعب (Horror) starts with Ra
    # كوميدي (Comedy) starts with Kaf
    # Kaf < Ra in Arabic

    assert bot.search("horror comedy films") == "أفلام كوميدي رعب"
    assert bot.search("comedy horror films") == "أفلام كوميدي رعب"


def test_sort_ar_labels_with_put_label_last(base_data):
    """
    Test interaction between sort_ar_labels and put_label_last.
    According to code, sort_ar_labels=True should override put_label_last.
    """
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=True,
    )
    bot.update_put_label_last({"action"})

    # action (أكشن) is marked to be last.
    # drama (دراما) is NOT.
    # if sort_ar_labels=False, result would be "دراما أكشن".
    # But since sort_ar_labels=True, it should sort: "أكشن", "دراما" -> "أكشن دراما"

    assert bot.search("drama action films") == "أفلام أكشن دراما"


def test_put_label_last_interaction_without_sort(base_data):
    """Verify put_label_last works correctly when sorting is off."""
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=False,
    )
    bot.update_put_label_last({"action"})

    # action is put last
    assert bot.search("action drama films") == "أفلام دراما أكشن"


def test_splitter_regex_special_chars(base_data):
    """Test splitter with regex special characters."""
    formatted_data, data_list = base_data
    # Testing '|' as a splitter
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        splitter="|",
    )

    # rf"(?<!\w)({self.alternation})({self.splitter})({self.alternation})(?!\w)"
    # If self.splitter is not escaped in regex, it might cause issues.
    # Looking at code: re.compile(data_pattern, re.I)
    # The splitter is NOT escaped in the pattern string!
    # Let's see if this test fails or succeeds. Usually splitters are simple.

    # If it's not escaped, '|' means alternation in regex.
    # match = re.search(r"(action|drama)(|)(action|drama)", "action|drama")
    # This might fail if the user expects literal '|'.

    assert bot.search("action|drama films") == "أفلام أكشن دراما"
    assert bot.match_key("action|drama films") == "action|drama"
