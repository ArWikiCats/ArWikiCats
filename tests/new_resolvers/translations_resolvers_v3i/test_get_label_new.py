#!/usr/bin/python3
r"""
Integration tests for the get_label_new function.

# "Category:((?:January|February|March|April|May|June|July|August|September|October|November|December)?\s*(\d+[−–\-]\d+|(\d{1,4})s\s*(BCE|BC)?|\d{1,4}\s*(?:BCE|BC)?)|(\d+)(?:st|nd|rd|th)(?:[−–\- ])(century|millennium)\s*(BCE|BC)?) (.*?) from (.*?)"

"""

import pytest

from ArWikiCats.new_resolvers.translations_resolvers_v3i.resolve_v3i import get_label_new

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
