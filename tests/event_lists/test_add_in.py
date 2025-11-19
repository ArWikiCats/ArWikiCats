#
import pytest

from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

examples = {
    "Category:18th-century Dutch explorers": "تصنيف:مستكشفون هولنديون في القرن 18",
    "Category:20th-century Albanian sports coaches": "تصنيف:مدربو رياضة ألبان في القرن 20",
    "Category:19th-century actors": "تصنيف:ممثلون في القرن 19",
    "Category:2000s American films": "تصنيف:أفلام أمريكية في عقد 2000",
    "Category:2017 American television series debuts": "تصنيف:مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "Category:2017 American television series endings": "تصنيف:مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "Category:Paralympic competitors for Cape Verde": "تصنيف:منافسون في الألعاب البارالمبية من الرأس الأخضر",
    "Category:19th-century actors by religion": "تصنيف:ممثلون في القرن 19 حسب الدين",
    "Category:19th-century people by religion": "تصنيف:أشخاص في القرن 19 حسب الدين",
    "Category:20th-century railway accidents": "تصنيف:حوادث سكك حديد في القرن 20",
}

TEMPORAL_CASES = [
    ("temporal_1", examples),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
def _test_temporal(name, data):
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_add_in(category: str, expected: str) -> None:

    assert new_func_lab_final_label(category) == expected
