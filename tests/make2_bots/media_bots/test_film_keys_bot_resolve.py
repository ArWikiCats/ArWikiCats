"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.films_bot import resolve_films

fast_data = {
    "burmese romantic drama films": "أفلام رومانسية درامية بورمية",
    "dutch war drama films": "أفلام حربية درامية هولندية",
    "indian sports drama films": "أفلام رياضية درامية هندية",
    "iranian romantic drama films": "أفلام رومانسية درامية إيرانية",
    "nigerian musical drama films": "أفلام موسيقية درامية نيجيرية",
    "russian sports drama films": "أفلام رياضية درامية روسية",
    "spanish war drama films": "أفلام حربية درامية إسبانية",
    "soviet drama films": "أفلام درامية سوفيتية",
    "melodrama films": "أفلام ميلودراما",
    "north korean drama films": "أفلام درامية كورية شمالية",

}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_resolve_films(category: str, expected: str) -> None:
    label = resolve_films(category)
    assert label == expected


to_test = [
    ("test_resolve_films", fast_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_resolve_films_all(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_films)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
