import re

import pytest

from src.translations_formats.format_data import FormatData


@pytest.fixture
def sample_data():
    formated_data = {
        "men's xoxo world cup": "كأس العالم للرجال في xoxo",
        "women's xoxo championship": "بطولة السيدات في xoxo",
        "xoxo records": "سجلات xoxo",
    }

    data_list = {
        "football": "كرة القدم",
        "basketball": "كرة السلة",
        "snooker": "سنوكر",
    }

    return formated_data, data_list


# --- keys_to_pattern -------------------------------------------------
def test_keys_to_pattern_returns_pattern(sample_data):
    formated_data, data_list = sample_data
    bot = FormatData(formated_data, data_list)
    pattern = bot.keys_to_pattern()
    assert isinstance(pattern, re.Pattern)
    assert pattern.search("football")
    assert pattern.search("snooker")


def test_keys_to_pattern_empty_dict():
    bot = FormatData({}, {})
    assert bot.keys_to_pattern() is None
    assert bot.pattern is None


# --- match_key -------------------------------------------------------
@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football world cup", "football"),
        ("women's basketball championship", "basketball"),
        ("unknown sport", ""),
    ],
)
def test_match_key(category, expected, sample_data):
    formated_data, data_list = sample_data
    bot = FormatData(formated_data, data_list)
    assert bot.match_key(category) == expected


def test_match_key_no_pattern():
    bot = FormatData({}, {})
    assert bot.match_key("football something") == ""


# --- apply_pattern_replacement ---------------------------------------
@pytest.mark.parametrize(
    "template,sport,expected",
    [
        ("كأس العالم في xoxo", "كرة القدم", "كأس العالم في كرة القدم"),
        ("xoxo بطولة", "كرة السلة", "كرة السلة بطولة"),
        ("بدون متغير", "كرة الطائرة", "بدون متغير"),  # placeholder not found
    ],
    ids=[k for k in range(3)],
)
def test_apply_pattern_replacement(template, sport, expected, sample_data):
    bot = FormatData(*sample_data, value_placeholder="xoxo")
    assert bot.apply_pattern_replacement(template, sport) == expected


# --- normalize_category ----------------------------------------------
@pytest.mark.parametrize(
    "category,sport_key,expected",
    [
        ("men's football world cup", "football", "men's xoxo world cup"),
        ("women's basketball championship", "basketball", "women's xoxo championship"),
    ],
)
def test_normalize_category(category, sport_key, expected, sample_data):
    bot = FormatData(*sample_data)
    assert bot.normalize_category(category, sport_key).lower() == expected.lower()


# --- get_template ----------------------------------------------
def test_get_template_found(sample_data):
    formated_data, data_list = sample_data
    bot = FormatData(formated_data, data_list)
    label = bot.get_template("football", "men's football world cup")
    assert label == "كأس العالم للرجال في xoxo"


def test_get_template_not_found(sample_data):
    formated_data, data_list = sample_data
    bot = FormatData(formated_data, data_list)
    assert bot.get_template("football", "unknown text") == ""


# --- search ----------------------------------------------------------
@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football world cup", "كأس العالم للرجال في كرة القدم"),
        ("women's basketball championship", "بطولة السيدات في كرة السلة"),
        ("snooker records", "سجلات سنوكر"),
        ("random unrelated", ""),
    ],
    ids=[k for k in range(4)],
)
def test_search_output(category, expected, sample_data):
    bot = FormatData(*sample_data)
    result = bot.search(category)
    assert result == expected


def test_search_no_sport_match(sample_data):
    bot = FormatData(*sample_data)
    assert bot.search("غير موجود") == ""


def test_search_missing_label(sample_data):
    formated_data, data_list = sample_data
    bot = FormatData({}, data_list)
    assert bot.search("men's football world cup") == ""


def test_search_missing_sport_label(sample_data):
    formated_data, data_list = sample_data
    del data_list["football"]
    bot = FormatData(formated_data, data_list)
    assert bot.search("men's football world cup") == ""


def test_search_no_pattern():
    bot = FormatData({}, {})
    assert bot.search("men's football world cup") == ""


# --- Case-insensitivity ----------------------------------------------
def test_case_insensitive_match(sample_data):
    bot = FormatData(*sample_data)
    result = bot.search("MEN'S FOOTBALL WORLD CUP")
    assert result == "كأس العالم للرجال في كرة القدم"
