"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar

data_fast = {
    "4th senate of spain": "مجلس شيوخ إسبانيا",
    "19th government of turkey": "حكومة تركيا",
    "11th government of turkey": "حكومة تركيا",
    "1330 in men's international football": "كرة قدم دولية رجالية في 1340",
}


@pytest.mark.parametrize("category, not_expected", data_fast.items(), ids=data_fast.keys())
@pytest.mark.fast
def test_get_country2_one(category: str, not_expected: str) -> None:
    label = resolve_label_ar(category)
    assert label != not_expected
