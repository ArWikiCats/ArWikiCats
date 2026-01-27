#!/usr/bin/python3
"""Integration tests"""

import re

import pytest

from ArWikiCats.translations_formats import FormatData


@pytest.fixture
def sample_data() -> tuple[dict[str, str], dict[str, str]]:
    formatted_data = {
        "men's {sport} world cup": "كأس العالم للرجال في {sport_label}",
        "women's {sport} championship": "بطولة السيدات في {sport_label}",
        "{sport} records": "سجلات {sport_label}",
        "{sport} league": "دوري {sport_label}",
    }

    data_list = {
        "football": "كرة القدم",
        "basketball": "كرة السلة",
        "snooker": "سنوكر",
        "rugby league": "دوري الرجبي",
        "rugby": "الرجبي",
    }

    return formatted_data, data_list


@pytest.mark.unit
def test_keys_to_pattern(sample_data: tuple[dict[str, str], dict[str, str]]) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, "{sport}", "{sport_label}")
    pattern = bot.keys_to_pattern()
    assert isinstance(pattern, re.Pattern)
    assert pattern.search("football") is not None
    assert pattern.search("snooker") is not None


@pytest.mark.unit
@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football world cup", "football"),
        ("women's basketball championship", "basketball"),
        ("women's rugby league championship", "rugby league"),
        ("random text", ""),
    ],
)
def test_match_key(category: str, expected: str, sample_data: tuple[dict[str, str], dict[str, str]]) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, "{sport}", "{sport_label}")
    assert bot.match_key(category) == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "template_label,sport_label,expected",
    [
        ("كأس العالم في xoxo", "كرة القدم", "كأس العالم في كرة القدم"),
        ("xoxo بطولة", "كرة السلة", "كرة السلة بطولة"),
        ("", "كرة الطائرة", ""),  # placeholder not found
    ],
    ids=[k for k in range(3)],
)
def test_apply_pattern_replacement(
    template_label: str, sport_label: str, expected: str, sample_data: tuple[dict[str, str], dict[str, str]]
) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, value_placeholder="xoxo")
    assert bot.apply_pattern_replacement(template_label, sport_label) == expected


@pytest.mark.unit
@pytest.mark.parametrize(
    "category,sport_key,expected",
    [
        ("men's football world cup", "football", "men's xoxo world cup"),
        ("women's basketball championship", "basketball", "women's xoxo championship"),
    ],
)
def test_normalize_category(
    category: str, sport_key: str, expected: str, sample_data: tuple[dict[str, str], dict[str, str]]
) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list)
    result = bot.normalize_category(category, sport_key)
    assert result.lower() == expected.lower()


@pytest.mark.unit
@pytest.mark.parametrize(
    "category,expected",
    [
        ("men's football world cup", "كأس العالم للرجال في كرة القدم"),
        ("women's basketball championship", "بطولة السيدات في كرة السلة"),
        ("women's Rugby championship", "بطولة السيدات في الرجبي"),
        ("women's Rugby League championship", "بطولة السيدات في دوري الرجبي"),
        ("snooker records", "سجلات سنوكر"),
        ("unknown category", ""),
    ],
    ids=[k for k in range(6)],
)
def test_search(sample_data: tuple[dict[str, str], dict[str, str]], category: str, expected: str) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")
    assert bot.search(category) == expected


@pytest.mark.unit
def test_search_no_sport_match(sample_data: tuple[dict[str, str], dict[str, str]]) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list)
    assert bot.search("unrelated topic") == ""


@pytest.mark.unit
def test_search_no_template_label(sample_data: tuple[dict[str, str], dict[str, str]]) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list)
    bot.formatted_data = {}  # remove templates
    assert bot.search("men's football world cup") == ""


@pytest.mark.unit
def test_case(sample_data: tuple[dict[str, str], dict[str, str]]) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")
    result = bot.search("men's football world cup")
    assert result == "كأس العالم للرجال في كرة القدم"


@pytest.mark.unit
def test_get_template(sample_data: tuple[dict[str, str], dict[str, str]]) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")
    normalized = bot.normalize_category("men's football world cup", "football")
    assert normalized == "men's {sport} world cup"
    template_label = bot.get_template("football", "men's football world cup")
    assert template_label == "كأس العالم للرجال في {sport_label}"


@pytest.mark.unit
def test_empty_data_lists() -> None:
    bot = FormatData({}, {}, key_placeholder="{k}", value_placeholder="{v}")
    assert bot.match_key("any") == ""
    assert bot.search("text") == ""
    assert bot.keys_to_pattern() is None


@pytest.mark.unit
def test_case_insensitivity(sample_data: tuple[dict[str, str], dict[str, str]]) -> None:
    formatted_data, data_list = sample_data
    bot = FormatData(formatted_data, data_list, key_placeholder="{sport}", value_placeholder="{sport_label}")
    result = bot.search("MEN'S FOOTBALL WORLD CUP")
    assert result == "كأس العالم للرجال في كرة القدم"
