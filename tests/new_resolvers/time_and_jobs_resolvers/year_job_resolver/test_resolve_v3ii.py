#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest

from ArWikiCats.new_resolvers.time_and_jobs_resolvers.year_job_resolver import resolve_year_job_countries

test_data = {
    "18th-century princes": "أمراء في القرن 18",
    "18th-century nobility": "نبلاء في القرن 18",
    "21st-century yemeni writers": "كتاب يمنيون في القرن 21",
    "21st-century New Zealand writers": "كتاب نيوزيلنديون في القرن 21",
    # "20th century american people": "أمريكيون في القرن 20",
    "20th century american people": "أمريكيون في القرن 20",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_year_job_resolver(category: str, expected: str) -> None:
    """
    pytest tests/time_and_jobs_resolvers/test_year_job_resolver.py::test_data
    """
    result = resolve_year_job_countries(category)
    assert result == expected
