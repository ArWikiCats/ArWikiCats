import re

import pytest

from ArWikiCats.translations import SPORTS_KEYS_FOR_JOBS
from ArWikiCats.translations_resolvers.match_labs import load_data
from ArWikiCats.translations_formats import FormatData

# --- Fixtures ---------------------------------------------------------


@pytest.fixture(scope="session")
def formatted_data():
    return load_data()


@pytest.fixture(scope="session")
def data_list():
    return SPORTS_KEYS_FOR_JOBS


@pytest.fixture
def bot(formatted_data, data_list):
    return FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")


# --- keys_to_pattern --------------------------------------------------
def test_keys_to_pattern_returns_regex(bot) -> None:
    pattern = bot.keys_to_pattern()
    assert isinstance(pattern, re.Pattern)
    assert pattern.search("football")
    assert pattern.search("rugby union")


def test_keys_to_pattern_empty() -> None:
    bot_empty = FormatData({}, {})
    assert bot_empty.keys_to_pattern() is None
    assert bot_empty.pattern is None


# --- match_key --------------------------------------------------------
@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football players", "football"),
        ("women's basketball coaches", "basketball"),
        ("youth snooker records", "snooker"),
        ("rugby league World Cup", "rugby league"),
        ("wheelchair rugby league World Cup", "wheelchair rugby league"),
        ("rugby league World Cup", "rugby league"),
        ("unknown sport category", ""),
    ],
)
def test_match_key(bot, category, expected) -> None:
    result = bot.match_key(category)
    assert result == expected


def test_match_key_no_pattern() -> None:
    bot = FormatData({}, {})
    assert bot.match_key("football") == ""


# --- normalize_category -----------------------------------------------
@pytest.mark.parametrize(
    "category,sport_key,expected",
    [
        ("men's football players", "football", "men's {sport} players"),
        ("youth snooker records", "snooker", "youth {sport} records"),
    ],
)
def test_normalize_category(bot, category, sport_key, expected) -> None:
    normalized = bot.normalize_category(category, sport_key)
    assert normalized == expected


# --- get_template -----------------------------------------------
def test_get_template_found(bot) -> None:
    label = bot.get_template("football", "men's football players")
    assert "لاعبو كرة قدم رجالية" in label or label != ""


def test_get_template_not_found(bot) -> None:
    label = bot.get_template("football", "unrelated term")
    assert label == ""


# --- apply_pattern_replacement ----------------------------------------
@pytest.mark.parametrize(
    "template_label,sport_label,expected",
    [
        ("بطولة xoxo العالمية", "كرة القدم", "بطولة كرة القدم العالمية"),
        ("xoxo مدربون", "كرة السلة", "كرة السلة مدربون"),
        ("بدون متغير", "كرة اليد", "بدون متغير"),  # placeholder missing
    ],
)
def test_apply_pattern_replacement(bot, template_label, sport_label, expected) -> None:
    bot.value_placeholder = "xoxo"
    result = bot.apply_pattern_replacement(template_label, sport_label)
    assert result == expected


# --- search basic functionality --------------------------------------
@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football players", "لاعبو كرة قدم رجالية"),
        ("women's basketball coaches", "مدربات كرة سلة نسائية"),
        ("men's youth snooker records and statistics", "سجلات وإحصائيات سنوكر للشباب"),
    ],
)
def test_search_valid(bot, category, expected) -> None:
    assert bot.search(category) == expected


@pytest.mark.parametrize(
    "category",
    [
        "unknown sport",
        "غير معروف",
    ],
)
def test_search_invalid(bot, category) -> None:
    assert bot.search(category) == ""


# --- search edge cases -----------------------------------------------
def test_search_missing_sport_label(formatted_data, data_list) -> None:
    # remove a key intentionally
    temp = dict(data_list)
    del temp["football"]
    bot = FormatData(formatted_data, temp)
    assert bot.search("men's football players") == ""


def test_search_missing_template_label(formatted_data, data_list) -> None:
    bot = FormatData({}, data_list)
    assert bot.search("men's football players") == ""


def test_search_case_insensitive(bot) -> None:
    result = bot.search("MEN'S FOOTBALL PLAYERS")
    assert result == "لاعبو كرة قدم رجالية"


# --- broader sampling -------------------------------------------------
@pytest.mark.parametrize(
    "sport_key",
    [
        "rugby union",
        "basketball",
        "handball",
        "volleyball",
        "cycling",
    ],
)
def test_multiple_sports(bot, sport_key) -> None:
    category = f"men's {sport_key} teams"
    result = bot.search(category)
    assert isinstance(result, str)
    assert result != ""


# --- consistency check ------------------------------------------------
def test_all_templates_work(bot) -> None:
    """Randomly sample a few template keys and ensure no crash occurs."""
    import random

    keys = random.sample(list(bot.formatted_data.keys()), 50)
    for k in keys:
        sample = k.replace("{sport}", "football")
        try:
            bot.search(sample)
        except Exception as e:
            pytest.fail(f"Unexpected exception for key {k}: {e}")
