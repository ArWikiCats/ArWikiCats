#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.time_and_jobs_resolvers.year_job_origin_resolver import resolve_year_job_from_countries

test_data_standard = {
    "20th-century male actors from Georgia (country)": "ممثلون ذكور من جورجيا في القرن 20",
    "21st-century male actors from Georgia (country)": "ممثلون ذكور من جورجيا في القرن 21",
    "20th-century male actors from Northern Ireland": "ممثلون ذكور من أيرلندا الشمالية في القرن 20",
    "21st-century male actors from Northern Ireland": "ممثلون ذكور من أيرلندا الشمالية في القرن 21",
    "19th-century male actors from the Russian Empire": "ممثلون ذكور من الإمبراطورية الروسية في القرن 19",
    "19th-century male artists from the Russian Empire": "فنانون ذكور من الإمبراطورية الروسية في القرن 19",
    "19th-century male writers from the Russian Empire": "كتاب ذكور من الإمبراطورية الروسية في القرن 19",
    "18th-century male actors from the Holy Roman Empire": "ممثلون ذكور من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century male singers from the Holy Roman Empire": "مغنون ذكور من الإمبراطورية الرومانية المقدسة في القرن 18",
    "21st-century male composers from Northern Ireland": "ملحنون ذكور من أيرلندا الشمالية في القرن 21",
    "21st-century male musicians from Northern Ireland": "موسيقيون ذكور من أيرلندا الشمالية في القرن 21",
    "21st-century male singers from Northern Ireland": "مغنون ذكور من أيرلندا الشمالية في القرن 21",
    "21st-century male writers from Northern Ireland": "كتاب ذكور من أيرلندا الشمالية في القرن 21",
    "20th-century male actors from the Ottoman Empire": "ممثلون ذكور من الدولة العثمانية في القرن 20",
    "20th-century male artists from Northern Ireland": "فنانون ذكور من أيرلندا الشمالية في القرن 20",
    "20th-century male composers from Northern Ireland": "ملحنون ذكور من أيرلندا الشمالية في القرن 20",
    "20th-century male musicians from Northern Ireland": "موسيقيون ذكور من أيرلندا الشمالية في القرن 20",
    "20th-century male singers from Northern Ireland": "مغنون ذكور من أيرلندا الشمالية في القرن 20",
    "20th-century male writers from Northern Ireland": "كتاب ذكور من أيرلندا الشمالية في القرن 20",
    "19th-century male actors from the Ottoman Empire": "ممثلون ذكور من الدولة العثمانية في القرن 19",
    "19th-century male musicians from the Russian Empire": "موسيقيون ذكور من الإمبراطورية الروسية في القرن 19",
    "19th-century male singers from the Russian Empire": "مغنون ذكور من الإمبراطورية الروسية في القرن 19",
    "18th-century male musicians from Bohemia": "موسيقيون ذكور من بوهيميا في القرن 18",
    "18th-century male musicians from the Holy Roman Empire": "موسيقيون ذكور من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century male musicians from the Russian Empire": "موسيقيون ذكور من الإمبراطورية الروسية في القرن 18",
    "18th-century male writers from the Russian Empire": "كتاب ذكور من الإمبراطورية الروسية في القرن 18",

}


@pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
@pytest.mark.slow
def test_year_job_origin_resolver_new_1(category: str, expected: str) -> None:
    """Test resolve year job from countries function for test_data_standard."""
    result1 = resolve_year_job_from_countries(category)
    assert result1 == expected

    result2 = resolve_label_ar(category)
    assert result2 == expected
