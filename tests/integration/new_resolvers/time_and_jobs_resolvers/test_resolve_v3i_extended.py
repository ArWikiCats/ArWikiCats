#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest

from ArWikiCats.new_resolvers.time_and_jobs_resolvers.year_job_origin_resolver import resolve_year_job_from_countries
from utils.dump_runner import make_dump_test_name_data

test_0 = {
    "21st-century people from Northern Ireland by occupation": "أشخاص من أيرلندا الشمالية حسب المهنة في القرن 21",
    "21st-century people from Georgia (country) by occupation": "أشخاص من جورجيا في القرن 21 حسب المهنة",
    "20th-century people from Northern Ireland by occupation": "أشخاص من أيرلندا الشمالية حسب المهنة في القرن 20",
    "20th-century people from Georgia (country) by occupation": "أشخاص من جورجيا في القرن 20 حسب المهنة",
    "19th-century people from the Ottoman Empire by conflict": "أشخاص من الدولة العثمانية في القرن 19 حسب النزاع",
    "19th-century people from the Russian Empire by occupation": "روس في القرن 19 حسب المهنة",
    "19th-century people from Ottoman Iraq by occupation": "عراقيون في القرن 19 حسب المهنة",
    "19th-century people from Georgia (country) by occupation": "أشخاص من جورجيا في القرن 19 حسب المهنة",
    "18th-century people from the Polish–Lithuanian Commonwealth by occupation": "أشخاص بولنديون في القرن 18 حسب المهنة",
    "18th-century people from the Russian Empire by occupation": "روس في القرن 18 حسب المهنة",
    "17th-century politicians from the Province of New York": "سياسيو ولاية نيويورك القرن 17",
    "11th-century people from the Savoyard State": "أشخاص من منطقة سافوا في القرن 11",
    "16th-century people from the Colony of Santo Domingo": "دومينيكانيون في القرن 16",
    "17th-century people from the Colony of Santo Domingo": "دومينيكانيون في القرن 17",
    "17th-century people from the Province of New York": "أشخاص من ولاية نيويورك في القرن 17",
    "18th-century people from the Savoyard State": "أشخاص من منطقة سافوا في القرن 18",
}


@pytest.mark.parametrize("category,expected", test_0.items(), ids=test_0.keys())
@pytest.mark.skip2
def test_year_job_origin_resolver_extended_1(category: str, expected: str) -> None:
    result = resolve_year_job_from_countries(category)
    assert result == expected


to_test = [
    ("test_year_job_origin_resolver_extended_1", test_0),
]

# test_dump_all = make_dump_test_name_data(to_test, resolve_year_job_from_countries, run_same=True)
