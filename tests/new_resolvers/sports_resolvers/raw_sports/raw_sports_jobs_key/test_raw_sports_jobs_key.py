#!/usr/bin/python3
""" """

import pytest

from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import resolve_sport_label_unified

jobs_data_only = {
    "defunct national football teams": "منتخبات كرة قدم وطنية سابقة",
    "national football teams": "منتخبات كرة قدم وطنية",
    "national football": "كرة قدم وطنية",
}


@pytest.mark.parametrize("category, expected", jobs_data_only.items(), ids=jobs_data_only.keys())
@pytest.mark.fast
def test_find_jobs_bot(category: str, expected: str) -> None:
    label1 = resolve_sport_label_unified(category)
    assert isinstance(label1, str)
    assert label1 == expected
