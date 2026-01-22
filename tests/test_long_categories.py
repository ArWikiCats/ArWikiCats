#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_1_list = [
    (
        "lists of Yugoslav non-fiction writers people executed of 2020 of Nazi concentration camps by city and year templates",
        "قوالب قوائم كتاب غير روائيين يوغسلافيون أعدموا في معسكرات الاعتقال النازية في 2020 حسب المدينة والسنة",
    ),
    (
        "lists of Yugoslav non-fiction writers people executed in 2020 at Nazi concentration camps by city and year templates",
        "قوالب قوائم كتاب غير روائيين يوغسلافيون أعدموا في معسكرات الاعتقال النازية في 2020 حسب المدينة والسنة",
    ),
    (
        "lists of Yugoslav non-fiction writers people executed in Nazi concentration camps by city and year",
        "قوائم كتاب غير روائيين يوغسلافيون أعدموا في معسكرات الاعتقال النازية حسب المدينة والسنة",
    ),
    (
        "lists of Yugoslav non-fiction writers people executed in Nazi concentration camps by city and year templates",
        "قوالب قوائم كتاب غير روائيين يوغسلافيون أعدموا في معسكرات الاعتقال النازية حسب المدينة والسنة",
    ),
    (
        "Yugoslav people executed in Nazi concentration camps by city templates",
        "قوالب يوغسلافيون أعدموا في معسكرات الاعتقال النازية حسب المدينة",
    ),
    (
        "lists of Yugoslav people executed in Nazi concentration camps by city templates",
        "قوالب قوائم يوغسلافيون أعدموا في معسكرات الاعتقال النازية حسب المدينة",
    ),
]

data_1 = {item[0]: item[1] for item in data_1_list}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
def test_long_categories_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data([("test_long_categories_1", data_1)], resolve_label_ar, run_same=True)
