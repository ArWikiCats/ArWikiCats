""" """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.jobs_resolvers.relegin_jobs_new import new_religions_jobs_with_suffix

test_religions_data = {
    "painters shi'a muslims": "رسامون مسلمون شيعة",
    "painters shia muslims": "رسامون مسلمون شيعة",
    "painters male muslims": "رسامون ذكور مسلمون",
    "muslims painters": "رسامون مسلمون",
    "painters muslims": "رسامون مسلمون",
}

test_religions_female_data = {
    "female painters shi'a muslims": "رسامات مسلمات شيعيات",
    "painters female shia muslims": "رسامات مسلمات شيعيات",
    "painters women's muslims": "رسامات مسلمات",
    "painters female muslims": "رسامات مسلمات",
    "women's painters muslims": "رسامات مسلمات",
}


@pytest.mark.parametrize("category,expected", test_religions_data.items(), ids=test_religions_data.keys())
@pytest.mark.fast
def test_religions_jobs_1(category: str, expected: str) -> None:
    result = new_religions_jobs_with_suffix(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_religions_female_data.items(), ids=test_religions_female_data.keys())
@pytest.mark.fast
def test_religions_females(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = new_religions_jobs_with_suffix(category)
    assert result == expected


TEMPORAL_CASES = [
    ("test_religions_jobs_1", test_religions_data, new_religions_jobs_with_suffix),
    ("test_religions_females", test_religions_female_data, new_religions_jobs_with_suffix),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
