"""
Tests
"""

import pytest

from ArWikiCats.translations_formats import MultiDataFormatterBaseYear, format_year_country_data


@pytest.fixture
def yc_bot() -> MultiDataFormatterBaseYear:
    countries_data = {
        "united states": "الولايات المتحدة",
        "yemen": "اليمن",
        "china": "الصين",
        "france": "فرنسا",
        "germany": "ألمانيا",
    }

    COUNTRY_YEAR_DATA = {
        "{year1} in {country1}": "{year1} في {country1}",
        "{year1} disestablishments in {country1}": "انحلالات سنة {year1} في {country1}",
    }

    yc_bot = format_year_country_data(
        formatted_data=COUNTRY_YEAR_DATA,
        data_list=countries_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        key2_placeholder="{year1}",
        value2_placeholder="{year1}",
        text_after="",
        text_before="the ",
    )

    yc_bot.country_bot.add_formatted_data("{year1} in {country1}", "{country1} في {year1}")
    return yc_bot


class TestLoadBot:
    test_data2 = {
        "Category:2010s in united states": "تصنيف:الولايات المتحدة في عقد 2010",
        # with text_before
        "Category:2010s in the united states": "تصنيف:الولايات المتحدة في عقد 2010",
        "Category:2025 in Yemen": "تصنيف:اليمن في 2025",
        "Category:2020s in Yemen": "تصنيف:اليمن في عقد 2020",
        "Category:2025 in yemen": "تصنيف:اليمن في 2025",
    }

    @pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
    @pytest.mark.fast
    def test_load_bot(self, yc_bot: MultiDataFormatterBaseYear, category: str, expected: str) -> None:
        """Test loading the bot and using it."""
        result = yc_bot.search_all_category(category)
        assert result == expected
