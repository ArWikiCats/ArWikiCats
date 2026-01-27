#!/usr/bin/python3
"""
Tests for model_data_v2.py module.

This module provides tests for:
2. MultiDataFormatterBaseV2 class - combines two FormatDataV2 instances
"""

from ArWikiCats.translations_formats.DataModel import FormatDataV2
from ArWikiCats.translations_formats.DataModelMulti import MultiDataFormatterBaseV2


class TestMultiDataFormatterBaseV2Init:
    """Tests for MultiDataFormatterBaseV2 initialization."""

    def test_init_default(self):
        """Test initialization with default parameters."""
        country_bot = FormatDataV2(
            formatted_data={"{country}": "{demonym}"},
            data_list={"yemeni": {"demonym": "يمنيون"}},
            key_placeholder="{country}",
        )
        other_bot = FormatDataV2(
            formatted_data={"{job}": "{job_ar}"},
            data_list={"writers": {"job_ar": "كتاب"}},
            key_placeholder="{job}",
        )

        bot = MultiDataFormatterBaseV2(country_bot=country_bot, other_bot=other_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is other_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None

    def test_init_with_search_first_part(self):
        """Test initialization with search_first_part=True."""
        country_bot = FormatDataV2(
            formatted_data={"{country}": "{demonym}"},
            data_list={"yemeni": {"demonym": "يمنيون"}},
            key_placeholder="{country}",
        )
        other_bot = FormatDataV2(
            formatted_data={"{job}": "{job_ar}"},
            data_list={"writers": {"job_ar": "كتاب"}},
            key_placeholder="{job}",
        )

        bot = MultiDataFormatterBaseV2(
            country_bot=country_bot,
            other_bot=other_bot,
            search_first_part=True,
        )

        assert bot.search_first_part is True

    def test_init_with_data_to_find(self):
        """Test initialization with data_to_find dictionary."""
        country_bot = FormatDataV2(
            formatted_data={"{country}": "{demonym}"},
            data_list={"yemeni": {"demonym": "يمنيون"}},
            key_placeholder="{country}",
        )
        other_bot = FormatDataV2(
            formatted_data={"{job}": "{job_ar}"},
            data_list={"writers": {"job_ar": "كتاب"}},
            key_placeholder="{job}",
        )

        data_to_find = {"yemeni writers": "كتاب يمنيون"}
        bot = MultiDataFormatterBaseV2(
            country_bot=country_bot,
            other_bot=other_bot,
            data_to_find=data_to_find,
        )

        assert bot.data_to_find == data_to_find
