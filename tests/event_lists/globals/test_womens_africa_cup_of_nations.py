#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_label_ar

data1 = {
    "2016 Women's Africa Cup of Nations squad navigational boxes": "صناديق تصفح تشكيلات كأس الأمم الإفريقية للسيدات 2016",
    "2016 Women's Africa Cup of Nations": "كأس الأمم الإفريقية للسيدات 2016",
    "2018 Women's Africa Cup of Nations squad navigational boxes": "صناديق تصفح تشكيلات كأس الأمم الإفريقية للسيدات 2018",
    "2018 Women's Africa Cup of Nations": "كأس الأمم الإفريقية للسيدات 2018",
    "2022 Women's Africa Cup of Nations players": "لاعبات كأس الأمم الإفريقية للسيدات 2022",
    "2022 Women's Africa Cup of Nations squad navigational boxes": "صناديق تصفح تشكيلات كأس الأمم الإفريقية للسيدات 2022",
    "2022 Women's Africa Cup of Nations": "كأس الأمم الإفريقية للسيدات 2022",
    "2024 Women's Africa Cup of Nations players": "لاعبات كأس الأمم الإفريقية للسيدات 2024",
    "2024 Women's Africa Cup of Nations": "كأس الأمم الإفريقية للسيدات 2024",
    "Women's Africa Cup of Nations players": "لاعبات كأس الأمم الإفريقية للسيدات",
    "Women's Africa Cup of Nations qualification": "تصفيات كأس الأمم الإفريقية للسيدات",
    "Women's Africa Cup of Nations tournaments": "بطولات كأس الأمم الإفريقية للسيدات",
    "Women's Africa Cup of Nations": "كأس الأمم الإفريقية للسيدات",
}

data_2 = {
    "Women's Africa Cup of Nations squad navigational boxes by competition": "صناديق تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات حسب المنافسة",
    "Women's Africa Cup of Nations squad navigational boxes by nation": "صناديق تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات حسب الموطن",
}

to_test = [
    ("test_womens_africa_cup_of_nations_1", data1),
    # ("test_womens_africa_cup_of_nations_2", data_2),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_womens_africa_cup_of_nations_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)

    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
