#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "Category:2016 Women's Africa Cup of Nations squad navigational boxes": "تصنيف:صناديق تصفح تشكيلات كأس الأمم الإفريقية للسيدات 2016",
    "Category:2016 Women's Africa Cup of Nations": "تصنيف:كأس الأمم الإفريقية للسيدات 2016",
    "Category:2018 Women's Africa Cup of Nations squad navigational boxes": "تصنيف:صناديق تصفح تشكيلات كأس الأمم الإفريقية للسيدات 2018",
    "Category:2018 Women's Africa Cup of Nations": "تصنيف:كأس الأمم الإفريقية للسيدات 2018",
    "Category:2022 Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات 2022",
    "Category:2022 Women's Africa Cup of Nations squad navigational boxes": "تصنيف:صناديق تصفح تشكيلات كأس الأمم الإفريقية للسيدات 2022",
    "Category:2022 Women's Africa Cup of Nations": "تصنيف:كأس الأمم الإفريقية للسيدات 2022",
    "Category:2024 Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات 2024",
    "Category:2024 Women's Africa Cup of Nations": "تصنيف:كأس الأمم الإفريقية للسيدات 2024",
    "Category:Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات",
    "Category:Women's Africa Cup of Nations qualification": "تصنيف:تصفيات كأس الأمم الإفريقية للسيدات",
    "Category:Women's Africa Cup of Nations tournaments": "تصنيف:بطولات كأس الأمم الإفريقية للسيدات",
    "Category:Women's Africa Cup of Nations": "تصنيف:كأس الأمم الإفريقية للسيدات",
}

data_2 = {
    "Category:Women's Africa Cup of Nations squad navigational boxes by competition": "تصنيف:صناديق تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات حسب المنافسة",
    "Category:Women's Africa Cup of Nations squad navigational boxes by nation": "تصنيف:صناديق تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات حسب الموطن",
}

to_test = [
    ("test_womens_africa_cup_of_nations_1", data1),
    # ("test_womens_africa_cup_of_nations_2", data_2),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_womens_africa_cup_of_nations_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
