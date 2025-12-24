#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest

from ArWikiCats.new_resolvers.translations_resolvers_v3i.resolve_v3ii import resolve_year_job_countries

test_data = {
    "18th-century princes": "أمراء في القرن 18",
    "18th-century nobility": "نبلاء في القرن 18",
    "21st-century yemeni writers": "كتاب يمنيون في القرن 21",
    "21st-century New Zealand writers": "كتاب نيوزيلنديون في القرن 21",
    # "20th century american people": "أمريكيون في القرن 20",
    "20th century american people": "أمريكيون في القرن 20",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_resolve_v3ii(category: str, expected: str) -> None:
    """
    pytest tests/translations_resolvers_v3i/test_resolve_v3ii.py::test_data
    """
    result = resolve_year_job_countries(category)
    assert result == expected
