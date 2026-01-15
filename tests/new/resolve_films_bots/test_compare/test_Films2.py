"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new.resolve_films_bots.film_keys_bot import Films
from ArWikiCats.new.resolve_films_bots.resolve_films_labels import _get_films_key_tyty_new

test_data3 = {
    "animated short film comics": "قصص مصورة رسوم متحركة قصيرة",
    "animated short film film series": "سلاسل أفلام رسوم متحركة قصيرة",
    "animated short film soap opera": "مسلسلات طويلة رسوم متحركة قصيرة",
    "animated short film television episodes": "حلقات تلفزيونية رسوم متحركة قصيرة",
    "animated short film television films": "أفلام تلفزيونية رسوم متحركة قصيرة",
    "animated short film television news": "أخبار تلفزيونية رسوم متحركة قصيرة",
    "animated short film television programmes": "برامج تلفزيونية رسوم متحركة قصيرة",
    "animated short film television programs": "برامج تلفزيونية رسوم متحركة قصيرة",
    "animated short film television series": "مسلسلات تلفزيونية رسوم متحركة قصيرة",
    "animated short film video games": "ألعاب فيديو رسوم متحركة قصيرة",
    "animated short film web series": "مسلسلات ويب رسوم متحركة قصيرة",
    "comic science fiction comics": "قصص مصورة خيالية علمية كوميدية",
    "comic science fiction film series": "سلاسل أفلام خيالية علمية كوميدية",
    "comic science fiction soap opera": "مسلسلات طويلة خيالية علمية كوميدية",
    "comic science fiction television episodes": "حلقات تلفزيونية خيالية علمية كوميدية",
    "comic science fiction television films": "أفلام تلفزيونية خيالية علمية كوميدية",
    "comic science fiction television news": "أخبار تلفزيونية خيالية علمية كوميدية",
    "comic science fiction television programmes": "برامج تلفزيونية خيالية علمية كوميدية",
    "comic science fiction television programs": "برامج تلفزيونية خيالية علمية كوميدية",
    "comic science fiction television series": "مسلسلات تلفزيونية خيالية علمية كوميدية",
    "comic science fiction video games": "ألعاب فيديو خيالية علمية كوميدية",
    "comic science fiction web series": "مسلسلات ويب خيالية علمية كوميدية",
    "television comics": "قصص مصورة تلفزيونية",
    "television episodes": "حلقات تلفزيونية",
    "television film series": "سلاسل أفلام تلفزيونية",
    "television films": "أفلام تلفزيونية",
    "television miniseries": "مسلسلات قصيرة تلفزيونية",
    "television news": "أخبار تلفزيونية",
    "television programmes": "برامج تلفزيونية",
    "television programs": "برامج تلفزيونية",
    "television series": "مسلسلات تلفزيونية",
    "television soap opera": "مسلسلات طويلة تلفزيونية",
    "television video games": "ألعاب فيديو تلفزيونية",
    "television web series": "مسلسلات ويب تلفزيونية",
    "comics": "قصص مصورة",
    "film series": "سلاسل أفلام",
    "soap opera": "مسلسلات طويلة",
    "video games": "ألعاب فيديو",
    "web series": "مسلسلات ويب",
}


@pytest.mark.parametrize("category, expected", test_data3.items(), ids=test_data3.keys())
@pytest.mark.fast
def test_Films(category: str, expected: str) -> None:
    label = Films(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data3.items(), ids=test_data3.keys())
@pytest.mark.fast
def test_get_films_key_tyty_new(category: str, expected: str) -> None:
    label = _get_films_key_tyty_new(category)
    assert label == expected


to_test = [
    ("test_Films", test_data3, Films),
    ("test_Films_tyty", test_data3, _get_films_key_tyty_new),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_resolve_films_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
