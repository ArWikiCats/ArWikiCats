""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar as Work_for_me_main
# from ArWikiCats.old_bots.for_me import Work_for_me_main

data_1 = {}

data_2 = {
}

data_2018 = {
}


@pytest.mark.parametrize("category, expected_key", data_1.items(), ids=data_1.keys())
@pytest.mark.skip2
def test_Work_for_data1(category: str, expected_key: str) -> None:
    label1 = Work_for_me_main(category)
    assert label1 == expected_key


@pytest.mark.parametrize("category, expected_key", data_2018.items(), ids=data_2018.keys())
@pytest.mark.skip2
def test_Work_for_data_2018(category: str, expected_key: str) -> None:
    label1 = Work_for_me_main(category)
    assert label1 == expected_key


to_test = [
    ("test_Work_for_data1", data_1),
    ("test_Work_for_data2", data_2),
    ("test_Work_for_data_2018", data_2018),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    """
    """
    expected, diff_result = one_dump_test(data, Work_for_me_main)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
