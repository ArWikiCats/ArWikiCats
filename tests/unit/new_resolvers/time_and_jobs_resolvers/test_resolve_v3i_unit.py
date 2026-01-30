#!/usr/bin/python3
"""Integration tests for MultiDataFormatterBase and MultiDataFormatterYearAndFrom with year-based translations."""

import pytest

from ArWikiCats.time_formats.time_to_arabic import convert_time_to_arabic, match_time_en_first
from ArWikiCats.translations_formats import FormatDataFrom, MultiDataFormatterYearAndFrom


def get_label(text: str) -> str:
    data = {
        "writers from Hong Kong": "كتاب من هونغ كونغ",
        "writers from yemen": "كتاب من اليمن",
        "writers from Crown of Aragon": "كتاب من تاج أرغون",
        "writers gg yemen": "كتاب من اليمن",
    }
    print(f"search: {text=}")
    return data.get(text, "")


@pytest.fixture
def multi_bot_v4() -> MultiDataFormatterYearAndFrom:
    formatted_data = {
        "{year1} {country1}": "{country1} في {year1}",
    }
    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        search_callback=get_label,
        match_key_callback=lambda x: x.replace("{year1}", "").strip(),
    )
    year_bot = FormatDataFrom(
        formatted_data={},
        key_placeholder="{year1}",
        value_placeholder="{year1}",
        search_callback=convert_time_to_arabic,
        match_key_callback=match_time_en_first,
    )

    # year_bot = YearFormatData(key_placeholder="{year1}", value_placeholder="{year1}")

    return MultiDataFormatterYearAndFrom(
        country_bot=country_bot,
        year_bot=year_bot,
        other_key_first=True,
    )


@pytest.mark.unit
class TestYearPart:
    test_data_standard = {
        "100s": "عقد 100",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_combinations(self, multi_bot_v4: MultiDataFormatterYearAndFrom, category: str, expected: str) -> None:
        """
        Test
        """
        result = multi_bot_v4.other_bot.search_all(category)
        assert result == expected


@pytest.mark.unit
class TestMatchKeys:
    test_keys = {
        "14th-century writers from Hong Kong": ("14th-century", "writers from Hong Kong"),
        "14th-century writers from yemen": ("14th-century", "writers from yemen"),
        "14th-century writers from yemen by city": ("14th-century", "writers from yemen by city"),
    }

    @pytest.mark.parametrize("category,expected", test_keys.items(), ids=test_keys.keys())
    def test_match_key_other_bot(
        self, multi_bot_v4: MultiDataFormatterYearAndFrom, category: str, expected: tuple[str, str]
    ) -> None:
        """
        Test
        """
        year_key, _ = expected

        result = multi_bot_v4.other_bot.match_key(category)
        assert result == year_key

    @pytest.mark.parametrize("category,expected", test_keys.items(), ids=test_keys.keys())
    def test_match_key_country_bot(
        self, multi_bot_v4: MultiDataFormatterYearAndFrom, category: str, expected: tuple[str, str]
    ) -> None:
        """
        Test
        """
        _, c_key = expected
        result = multi_bot_v4.normalize_both_new(category).nat_key
        assert result == c_key


@pytest.mark.unit
class TestCountriesPart:
    test_data_standard = {
        "writers from Hong Kong": "كتاب من هونغ كونغ",
        "writers from yemen": "كتاب من اليمن",
        "writers gg yemen": "كتاب من اليمن",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_country_combinations(
        self, multi_bot_v4: MultiDataFormatterYearAndFrom, category: str, expected: str
    ) -> None:
        """
        Test
        """
        result = multi_bot_v4.country_bot.search_all(category)
        assert result == expected


@pytest.mark.unit
class TestPart3:
    test_data_standard = {
        "14th-century writers from Hong Kong": "كتاب من هونغ كونغ في القرن 14",
        "14th-century writers from yemen": "كتاب من اليمن في القرن 14",
        "14th-century writers from yemen by city": "",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_country_combinations(
        self, multi_bot_v4: MultiDataFormatterYearAndFrom, category: str, expected: str
    ) -> None:
        """
        Test
        """
        result = multi_bot_v4.create_label(category)
        assert result == expected
