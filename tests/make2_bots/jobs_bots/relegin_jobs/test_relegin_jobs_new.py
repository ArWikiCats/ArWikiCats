""" """

import pytest

from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.jobs_bots.relegin_jobs import try_religions_jobs_with_suffix
# from ArWikiCats.make_bots.jobs_bots.relegin_jobs_new import new_religions_jobs_with_suffix as try_religions_jobs_with_suffix

test_religions_data = {
    "Category:Yemeni shi'a muslims": "تصنيف:يمنيون مسلمون شيعة",
    "Category:Yemeni shia muslims": "تصنيف:يمنيون مسلمون شيعة",
    "Category:Yemeni male muslims": "تصنيف:يمنيون مسلمون ذكور",
    "Category:Yemeni muslims male": "تصنيف:يمنيون مسلمون ذكور",
    "Category:Yemeni muslims": "تصنيف:يمنيون مسلمون",
    "Category:Yemeni people muslims": "تصنيف:يمنيون مسلمون",
    "Category:Pakistani expatriate footballers": "تصنيف:لاعبو كرة قدم باكستانيون مغتربون",
}


@pytest.mark.parametrize("category,expected", test_religions_data.items(), ids=test_religions_data.keys())
@pytest.mark.skip2
def test_religions_jobs_1(category: str, expected: str) -> None:
    result = try_religions_jobs_with_suffix(category)
    assert result == expected


test_religions_female_data = {
    "Category:female Yemeni shi'a muslims": "تصنيف:يمنيات مسلمات شيعيات",
    "Category:Yemeni female shia muslims": "تصنيف:يمنيات مسلمات شيعيات",
    "Category:Yemeni women's muslims": "تصنيف:يمنيات مسلمات",
    "Category:Yemeni female muslims": "تصنيف:يمنيات مسلمات",
    "Category:women's Yemeni muslims": "تصنيف:يمنيات مسلمات",
}


@pytest.mark.parametrize("category,expected", test_religions_female_data.items(), ids=test_religions_female_data.keys())
@pytest.mark.skip2
def test_religions_females(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    # result = new_religions_jobs_with_suffix(category)
    result = try_religions_jobs_with_suffix(category)
    assert result == expected


TEMPORAL_CASES = [
    ("test_religions_jobs_1", test_religions_data, try_religions_jobs_with_suffix),
    ("test_religions_females", test_religions_female_data, try_religions_jobs_with_suffix),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
