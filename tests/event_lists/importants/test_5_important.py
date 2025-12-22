#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_diff_text

from ArWikiCats import resolve_arabic_category_label

data0 = {
    "Category:Family of Socrates": "تصنيف:عائلة سقراط",
    "Category:Discoveries by WISE": "تصنيف:اكتشافات بواسطة وايز",
    "Category:Academic staff of University of Nigeria": "تصنيف:أعضاء هيئة تدريس جامعة نيجيريا",
    "Category:Early modern history of Portugal": "تصنيف:تاريخ البرتغال الحديث المبكر",
}

data1 = {
}


data_2 = {
}

data_3 = {
}

to_test = [
    ("test_5_data_0", data0),
    ("test_5_data_1", data1),
    ("test_5_data_3", data_3),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_5_data_0(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
def test_5_data_1(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
def test_5_data_3(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
