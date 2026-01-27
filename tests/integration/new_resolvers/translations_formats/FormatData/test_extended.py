import re
from typing import Dict

import pytest

from ArWikiCats.translations import SPORTS_KEYS_FOR_JOBS
from ArWikiCats.translations_formats import FormatData

# --- Fixtures ---------------------------------------------------------


@pytest.fixture(scope="session")
def formatted_data() -> Dict[str, str]:
    return {
        "{sport}": "{sport_label}",
        "amateur {sport}": "{sport_label} للهواة",
        "mens youth {sport}": "{sport_label} للشباب",
        "mens {sport}": "{sport_label} رجالية",
        "womens youth {sport}": "{sport_label} للشابات",
        "womens {sport}": "{sport_label} نسائية",
        "youth {sport}": "{sport_label} شبابية",
    }


@pytest.fixture(scope="session")
def data_list() -> Dict[str, str]:
    return SPORTS_KEYS_FOR_JOBS


@pytest.fixture
def bot(formatted_data: Dict[str, str], data_list: Dict[str, str]) -> FormatData:
    return FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")


# --- keys_to_pattern --------------------------------------------------
def test_keys_to_pattern_returns_regex(bot: FormatData) -> None:
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
def test_match_key(bot: FormatData, category: str, expected: str) -> None:
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
def test_normalize_category(bot: FormatData, category: str, sport_key: str, expected: str) -> None:
    normalized = bot.normalize_category(category, sport_key)
    assert normalized == expected


def test_get_template_not_found(bot: FormatData) -> None:
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
def test_apply_pattern_replacement(bot: FormatData, template_label: str, sport_label: str, expected: str) -> None:
    bot.value_placeholder = "xoxo"
    result = bot.apply_pattern_replacement(template_label, sport_label)
    assert result == expected


@pytest.mark.parametrize(
    "category",
    [
        "unknown sport",
        "غير معروف",
    ],
)
def test_search_invalid(bot: FormatData, category: str) -> None:
    assert bot.search(category) == ""


# --- search edge cases -----------------------------------------------
def test_search_missing_sport_label(formatted_data: Dict[str, str], data_list: Dict[str, str]) -> None:
    # remove a key intentionally
    temp = dict(data_list)
    del temp["football"]
    bot = FormatData(formatted_data, temp)
    assert bot.search("men's football players") == ""


def test_search_missing_template_label(formatted_data: Dict[str, str], data_list: Dict[str, str]) -> None:
    bot = FormatData({}, data_list)
    assert bot.search("men's football players") == ""
