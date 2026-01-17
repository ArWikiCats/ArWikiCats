import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
from ArWikiCats.legacy_bots.ma_bots2.year_or_typeo import label_for_startwith_year_or_typeo

data_0 = {
}

data_1 = {
    "1960s Dutch-language films": "أفلام باللغة الهولندية في عقد 1960",
    "2010s French-language films": "أفلام باللغة الفرنسية في عقد 2010",
    "1960s in Dutch-language films": "أفلام باللغة الهولندية في عقد 1960",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
def test_year_or_typeo_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_year_or_typeo_1", data_1),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, expected, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
