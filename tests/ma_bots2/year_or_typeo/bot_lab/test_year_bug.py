import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.ma_bots2.year_or_typeo.bot_lab import (
    label_for_startwith_year_or_typeo,
)

examples = {
    "April 1983 sports events": "أحداث أبريل 1983 الرياضية",
    "1370s conflicts": "نزاعات عقد 1370",
    # "8th parliament of la rioja": "برلمان منطقة لا ريوخا الثامن",
}

examples_century = {
    # "18th-century Dutch explorers": "مستكشفون هولنديون في القرن 18",
    # "20th-century Albanian sports coaches": "مدربو رياضة ألبان في القرن 20",
    "1st-millennium architecture": "عمارة الألفية 1",
    "1st-millennium literature": "أدب الألفية 1",
    "1st-century architecture": "عمارة القرن 1",
    "10th-century BC architecture": "عمارة القرن 10 ق م",
}


TEMPORAL_CASES = [
    ("test_label_for_startwith_year_or_typeo", examples),
    ("test_label_for_startwith_year_or_typeo_centuries", examples_century),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, label_for_startwith_year_or_typeo)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.parametrize("category, expected", examples.items(), ids=examples.keys())
@pytest.mark.fast
def test_label_for_startwith_year_or_typeo(category: str, expected: str) -> None:
    label = label_for_startwith_year_or_typeo(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", examples_century.items(), ids=examples_century.keys())
@pytest.mark.fast
def test_label_for_startwith_year_or_typeo_centuries(category: str, expected: str) -> None:
    label = label_for_startwith_year_or_typeo(category)
    assert label == expected
