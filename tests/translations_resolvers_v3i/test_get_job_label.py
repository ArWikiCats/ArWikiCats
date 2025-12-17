#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_diff_text
from ArWikiCats.translations_resolvers_v3i.resolve_v3i import get_job_label

test_0 = {
}

test_data_standard = {
    "botanists": "علماء نبات",
    "actors": "x",
    "actresses": "x",
    "architects": "x",
    "artisans": "x",
    "artists": "x",
    "astronomers": "x",
    "autobiographers": "x",
    "ballet dancers": "x",
    "bass guitarists": "x",
    "biographers": "x",
    "biologists": "x",
    "businesspeople": "x",
    "businesswomen": "x",
    "chemists": "x",
    "chess players": "x",
    "civil servants": "x",
    "classical composers": "x",
    "classical musicians": "x",
    "classical pianists": "x",
    "clergy": "x",
    "comedians": "x",
    "composers": "x",
    "criminals": "x",
    "dancers": "x",
    "deaths": "x",
    "diarists": "x",
    "diplomats": "x",
    "dramatists and playwrights": "x",
    "drummers": "x",
    "educators": "x",
    "engineers": "x",
    "engravers": "x",
    "explorers": "x",
    "folk musicians": "x",
    "guitarists": "x",
    "historians": "x",
    "illustrators": "x",
    "Jews": "x",
    "journalists": "x",
    "jurists": "x",
    "landowners": "x",
    "lawyers": "x",
    "LGBTQ people": "x",
    "male actors": "x",
    "male artists": "x",
    "male composers": "x",
    "male musicians": "x",
    "male singers": "x",
    "male writers": "x",
    "mathematicians": "x",
    "medical doctors": "x",
    "memoirists": "x",
    "men": "x",
    "military personnel": "x",
    "musicians": "x",
    "naturalists": "x",
    "nobility": "x",
    "non-fiction writers": "x",
    "novelists": "x",
    "opera singers": "x",
    "painters": "x",
    "people": "x",
    "people": "أشخاص",
    "philosophers": "x",
    "photographers": "x",
    "physicians": "x",
    "physicists": "x",
    "pianists": "x",
    "poets": "x",
    "politicians": "x",
    "princes": "x",
    "publishers (people)": "x",
    "rabbis": "x",
    "scholars": "x",
    "scientists": "x",
    "screenwriters": "x",
    "sculptors": "x",
    "short story writers": "x",
    "singer-songwriters": "x",
    "singers": "x",
    "songwriters": "x",
    "sportsmen": "x",
    "sportspeople": "x",
    "sportswomen": "x",
    "translators": "x",
    "violinists": "x",
    "women artists": "x",
    "women composers": "x",
    "women educators": "x",
    "women journalists": "x",
    "women lawyers": "x",
    "women medical doctors": "x",
    "women musicians": "x",
    "women opera singers": "x",
    "women painters": "x",
    "women politicians": "x",
    "women scientists": "x",
    "women singers": "x",
    "women writers": "x",
    "women": "x",
    "writers": "x",
    "zoologists": "x",
}


@pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
def test_get_job_label_1(category: str, expected: str) -> None:
    """
    Test
    """
    result = get_job_label(category)
    assert result == expected


to_test = [
    ("test_get_job_label_1", test_data_standard),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, get_job_label)
    dump_diff(diff_result, name)
    dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
