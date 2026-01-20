#!/usr/bin/python3

import pytest

from ArWikiCats.new_resolvers.time_and_jobs_resolvers.year_job_origin_resolver import get_label_new

r"""
Integration tests for the get_label_new function.

# "Category:((?:January|February|March|April|May|June|July|August|September|October|November|December)?\s*(\d+[−–\-]\d+|(\d{1,4})s\s*(BCE|BC)?|\d{1,4}\s*(?:BCE|BC)?)|(\d+)(?:st|nd|rd|th)(?:[−–\- ])(century|millennium)\s*(BCE|BC)?) (.*?) from (.*?)"

"""

test_data_standard = {
    "writers from Crown of Aragon": "كتاب من تاج أرغون",
    "writers from yemen": "كتاب من اليمن",
}


@pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
def test_get_label_new(category: str, expected: str) -> None:
    """
    Test
    """
    result = get_label_new(category)
    assert result == expected
