import re

import pytest

from ArWikiCats.translations_formats import FormatData

sample_data_type = tuple[dict[str, str], dict[str, str]]


@pytest.fixture
def sample_data() -> sample_data_type:
    formatted_data = {
        "men's {en} world cup": "كأس العالم للرجال في {ar}",
        "women's {en} championship": "بطولة السيدات في {ar}",
        "{en} records": "سجلات {ar}",
    }

    data_list = {
        "football": "كرة القدم",
        "basketball": "كرة السلة",
        "snooker": "سنوكر",
    }

    return formatted_data, data_list


# --- keys_to_pattern -------------------------------------------------
def test_keys_to_pattern_returns_pattern(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    pattern = bot.keys_to_pattern()
    assert isinstance(pattern, re.Pattern)
    assert pattern.search("football")
    assert pattern.search("snooker")


def test_keys_to_pattern_empty_dict() -> None:
    bot = FormatData({}, {}, key_placeholder="{en}", value_placeholder="{ar}")
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
def test_match_key(category: str, expected: str, sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.match_key(category) == expected


def test_match_key_no_pattern() -> None:
    bot = FormatData({}, {}, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.match_key("football something") == ""


# --- apply_pattern_replacement ---------------------------------------
@pytest.mark.parametrize(
    "template,sport,expected",
    [
        ("كأس العالم في {ar}", "كرة القدم", "كأس العالم في كرة القدم"),
        ("{ar} بطولة", "كرة السلة", "كرة السلة بطولة"),
        ("بدون متغير", "كرة الطائرة", "بدون متغير"),  # placeholder not found
    ],
    ids=list(range(3)),
)
def test_apply_pattern_replacement(template: str, sport: str, expected: str, sample_data: sample_data_type) -> None:
    bot = FormatData(*sample_data, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.apply_pattern_replacement(template, sport) == expected


# --- normalize_category ----------------------------------------------
@pytest.mark.parametrize(
    "category,sport_key,expected",
    [
        ("men's football world cup", "football", "men's {en} world cup"),
        ("women's basketball championship", "basketball", "women's {en} championship"),
    ],
)
def test_normalize_category(category: str, sport_key: str, expected: str, sample_data: sample_data_type) -> None:
    bot = FormatData(*sample_data, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.normalize_category(category, sport_key).lower() == expected.lower()


# --- get_template ----------------------------------------------
def test_get_template_found(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    label = bot.get_template("football", "men's football world cup")
    assert label == "كأس العالم للرجال في {ar}"


def test_get_template_not_found(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
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
    ids=list(range(4)),
)
def test_search_output(category: str, expected: str, sample_data: sample_data_type) -> None:
    bot = FormatData(*sample_data, key_placeholder="{en}", value_placeholder="{ar}")
    result = bot.search(category)
    assert result == expected


def test_search_no_sport_match(sample_data: sample_data_type) -> None:
    bot = FormatData(*sample_data, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.search("غير موجود") == ""


def test_search_missing_label(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData({}, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.search("men's football world cup") == ""


def test_search_missing_sport_label(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data
    del data_list["football"]
    bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.search("men's football world cup") == ""


def test_search_no_pattern() -> None:
    bot = FormatData({}, {}, key_placeholder="{en}", value_placeholder="{ar}")
    assert bot.search("men's football world cup") == ""


# --- Case-insensitivity ----------------------------------------------
def test_case_insensitive_match(sample_data: sample_data_type) -> None:
    bot = FormatData(*sample_data, key_placeholder="{en}", value_placeholder="{ar}")
    result = bot.search("MEN'S FOOTBALL WORLD CUP")
    assert result == "كأس العالم للرجال في كرة القدم"
