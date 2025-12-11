#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "Category:2016 Women's Africa Cup of Nations squad navigational boxes": "تصنيف:قوالب تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات 2016",
    "Category:2016 Women's Africa Cup of Nations": "تصنيف:كأس أمم إفريقيا لكرة القدم للسيدات 2016",
    "Category:2018 Women's Africa Cup of Nations squad navigational boxes": "تصنيف:قوالب تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات 2018",
    "Category:2018 Women's Africa Cup of Nations": "تصنيف:كأس أمم إفريقيا لكرة القدم للسيدات 2018",
    "Category:2022 Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس إفريقيا نسائية في بلدان 2022",
    "Category:2022 Women's Africa Cup of Nations squad navigational boxes": "تصنيف:كأس إفريقيا نسائية في صناديق تصفح تشكيلات بلدان 2022",
    "Category:2022 Women's Africa Cup of Nations": "تصنيف:كأس إفريقيا نسائية في بلدان 2022",
    "Category:2024 Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس الأمم الإفريقية نسائية 2024",
    "Category:2024 Women's Africa Cup of Nations": "تصنيف:كأس الأمم الإفريقية نسائية 2024",
    "Category:Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس أمم إفريقيا لكرة القدم للسيدات",
    "Category:Women's Africa Cup of Nations qualification": "تصنيف:تصفيات كأس أمم إفريقيا لكرة القدم للسيدات",
    "Category:Women's Africa Cup of Nations squad navigational boxes by competition": "تصنيف:صناديق تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات حسب المنافسة",
    "Category:Women's Africa Cup of Nations squad navigational boxes by nation": "تصنيف:صناديق تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات حسب الموطن",
    "Category:Women's Africa Cup of Nations tournaments": "تصنيف:بطولات كأس أمم إفريقيا لكرة القدم للسيدات",
    "Category:Women's Africa Cup of Nations": "تصنيف:كأس أمم إفريقيا لكرة القدم للسيدات",
}

data_2 = {

}

to_test = [
    ("test_womens_africa_cup_of_nations_1", data1),
    ("test_womens_africa_cup_of_nations_2", data_2),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=list(data1.keys()))
@pytest.mark.fast
def test_womens_africa_cup_of_nations_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    save3 = [
        f"* {{{{وب:طنت/سطر|{v.replace('تصنيف:', '')}|{diff_result[x].replace('تصنيف:', '')}|سبب النقل=تصحيح ArWikiCats}}}}"
        for x, v in expected.items()
        if v and x in diff_result
    ]
    dump_diff(save3, f"{name}_d", _sort=False)

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
