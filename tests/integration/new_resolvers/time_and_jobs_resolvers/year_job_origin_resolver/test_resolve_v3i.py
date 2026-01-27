#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest

from ArWikiCats.new_resolvers.time_and_jobs_resolvers.year_job_origin_resolver import (
    multi_bot_v4,
    resolve_year_job_from_countries,
)

bot = multi_bot_v4()


class TestCountriesPart:
    test_data_standard = {
        "writers from Crown of Aragon": "كتاب من تاج أرغون",
        "writers from yemen": "كتاب من اليمن",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_country_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        result = bot.country_bot.search(category)
        assert result == expected


class TestYearPart:
    test_data_standard = {
        "100s": "عقد 100",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        result = bot.other_bot.search_all(category)
        assert result == expected


class TestAllParts:
    test_data_standard = {
        "20th-century non-fiction writers from russian empire": "كتاب غير روائيين من الإمبراطورية الروسية في القرن 20",
        "14th-century writers from Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
        "14th-century writers from yemen": "كتاب من اليمن في القرن 14",
        "18th-century non-fiction writers from Russian Empire": "كتاب غير روائيين من الإمبراطورية الروسية في القرن 18",
        "18th-century non-fiction writers from the Russian Empire": "كتاب غير روائيين من الإمبراطورية الروسية في القرن 18",
        "18th-century sculptors from Bohemia": "نحاتون من بوهيميا في القرن 18",
        "19th-century non-fiction writers from Russian Empire": "كتاب غير روائيين من الإمبراطورية الروسية في القرن 19",
        "20th-century architects from Northern Ireland": "معماريون من أيرلندا الشمالية في القرن 20",
        "20th-century engineers from Northern Ireland": "مهندسون من أيرلندا الشمالية في القرن 20",
        "20th-century non-fiction writers from Northern Ireland": "كتاب غير روائيين من أيرلندا الشمالية في القرن 20",
        "20th-century non-fiction writers from northern ireland": "كتاب غير روائيين من أيرلندا الشمالية في القرن 20",
        "21st-century engineers from Northern Ireland": "مهندسون من أيرلندا الشمالية في القرن 21",
        "21st-century male actors from Georgia (country)": "ممثلون ذكور من جورجيا في القرن 21",
        "21st-century male artists from Northern Ireland": "فنانون ذكور من أيرلندا الشمالية في القرن 21",
        "21st-century medical doctors from Northern Ireland": "أطباء من أيرلندا الشمالية في القرن 21",
        "21st-century non-fiction writers from Northern Ireland": "كتاب غير روائيين من أيرلندا الشمالية في القرن 21",
        "21st-century painters from Northern Ireland": "رسامون من أيرلندا الشمالية في القرن 21",
        "9th-century historians from al-Andalus": "مؤرخون من الأندلس في القرن 9",
        "17th-century historians from Bohemia": "مؤرخون من بوهيميا في القرن 17",
        "19th-century biographers from Russian Empire": "كتاب سيرة من الإمبراطورية الروسية في القرن 19",
        "14th-century people from Holy Roman Empire": "أشخاص من الإمبراطورية الرومانية المقدسة في القرن 14",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_country_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        result = resolve_year_job_from_countries(category)
        assert result == expected

    data_2 = {
        # "21st-century musicians by instrument from Northern Ireland": "موسيقيون في القرن 21 حسب الآلة من أيرلندا الشمالية",
        # "20th-century musicians by instrument from Northern Ireland": "موسيقيون في القرن 20 حسب الآلة من أيرلندا الشمالية",
        "9th-century people from East Francia": "أشخاص من مملكة الفرنجة الشرقيين في القرن 9",
        "9th-century people from West Francia": "أشخاص من مملكة الفرنجة الغربيين في القرن 9",
        "21st-century women educators from Northern Ireland": "معلمات من أيرلندا الشمالية في القرن 21",
        "21st-century women medical doctors from Northern Ireland": "طبيبات من أيرلندا الشمالية في القرن 21",
        "20th century people from al-andalus": "أشخاص من الأندلس في القرن 20",
        "18th-century women singers from the Holy Roman Empire": "مغنيات من الإمبراطورية الرومانية المقدسة في القرن 18",
        "10th-century people from West Francia": "أشخاص من مملكة الفرنجة الغربيين في القرن 10",
        "17th-century women from the Republic of Venice": "نساء من جمهورية البندقية في القرن 17",
    }

    @pytest.mark.parametrize("category,expected", data_2.items(), ids=data_2.keys())
    def test_data_2(self, category: str, expected: str) -> None:
        """
        Test
        """
        result = resolve_year_job_from_countries(category)
        assert result == expected

    deaths_data = {
        "15th-century deaths from cancer": "وفيات بسبب السرطان في القرن 15",
    }

    @pytest.mark.parametrize("category,expected", deaths_data.items(), ids=deaths_data.keys())
    def test_deaths_data(self, category: str, expected: str) -> None:
        """
        pytest tests/time_and_jobs_resolvers/test_year_job_origin_resolver.py::TestAllParts::test_deaths_data
        """
        result = resolve_year_job_from_countries(category)
        assert result == expected
