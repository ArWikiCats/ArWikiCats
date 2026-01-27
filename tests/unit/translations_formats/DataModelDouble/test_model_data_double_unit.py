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
        "{film_key} movies": "أفلام {film_ar}",
    }
    data_list = {
        "action": "أكشن",
        "drama": "دراما",
        "comedy": "كوميدي",
        "horror": "رعب",
    }
    return formatted_data, data_list


def test_splitter_default_space(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_splitter_underscore(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        splitter="[_ ]",
    )
    assert bot.search("action_drama films") == "أفلام أكشن دراما"
    # Also matches with space since "[_ ]" is a character class matching both
    assert bot.search("action drama films") == "أفلام أكشن دراما"


def test_sort_simple_no_sort(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=False,
        log_multi_cache=False,
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"

    result2 = bot.search("drama action movies")
    assert result2 == "أفلام دراما أكشن"


def test_sort_simple_with_sort(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=True,
    )
    # أكشن (Action) < دراما (Drama)
    assert bot.search("action drama films") == "أفلام أكشن دراما"
    assert bot.search("drama action films") == "أفلام أكشن دراما"


def test_sort_alphabetical_complex(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=True,
    )
    # كوميدي (Comedy) Kaf > دراما (Drama) Dal ?
    # Let's check: د is U+062F, ك is U+0643. So د < ك.
    # So "دراما كوميدي"
    assert bot.search("comedy drama films") == "أفلام دراما كوميدي"


def test_splitter_regex_chars(base_data):
    formatted_data, data_list = base_data
    # Use something that needs escaping if literal, but code doesn't escape it.
    # '.' matches any char.
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        splitter=".",
    )
    # If not escaped, 'action.drama' matches 'actionXdrama'
    assert bot.search("action.drama films") == "أفلام أكشن دراما"
    # This might pass even if not escaped because '.' matches '.'.
    # But does it match 'action_drama'?
    # If not escaped, yes!
    assert bot.search("action_drama films") == "أفلام أكشن دراما"


def test_ar_joiner_default(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_ar_joiner_and(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        ar_joiner=" و ",
    )
    # "أكشن" + " و " + "دراما" -> "أفلام أكشن و دراما"
    result = bot.search("action drama films")
    assert result == "أفلام أكشن و دراما"


def test_ar_joiner_dash(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        ar_joiner="-",
    )
    # "أكشن" + "-" + "دراما" -> "أفلام أكشن-دراما"
    result = bot.search("action drama films")
    assert result == "أفلام أكشن-دراما"


def test_ar_joiner_with_sort(base_data):
    formatted_data, data_list = base_data
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        sort_ar_labels=True,
        ar_joiner=" و ",
    )
    # أكشن (Action) < دراما (Drama)
    # "action drama" -> "أفلام أكشن و دراما"
    assert bot.search("action drama films") == "أفلام أكشن و دراما"
    # "drama action" -> "أفلام أكشن و دراما"
    assert bot.search("drama action films") == "أفلام أكشن و دراما"


def test_ar_joiner_none(base_data):
    formatted_data, data_list = base_data
    # ar_joiner=None should default to space " "
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        ar_joiner=None,
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"


def test_ar_joiner_empty(base_data):
    formatted_data, data_list = base_data
    # ar_joiner="" should ALSO default to space " " because of 'or " "' in __init__
    bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
        ar_joiner="",
    )
    result = bot.search("action drama films")
    assert result == "أفلام أكشن دراما"
