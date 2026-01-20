#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

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


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
