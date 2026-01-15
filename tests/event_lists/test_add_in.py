#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

examples = {
    "Category:18th-century Dutch explorers": "تصنيف:مستكشفون هولنديون في القرن 18",
    "Category:20th-century Albanian sports coaches": "تصنيف:مدربو رياضة ألبان في القرن 20",
    "Category:19th-century actors": "تصنيف:ممثلون في القرن 19",
    "Category:2000s American films": "تصنيف:أفلام أمريكية في عقد 2000",
    "Category:2017 American television series debuts": "تصنيف:مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "Category:2017 American television series endings": "تصنيف:مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "Category:19th-century actors by religion": "تصنيف:ممثلون في القرن 19 حسب الدين",
    "Category:19th-century people by religion": "تصنيف:أشخاص في القرن 19 حسب الدين",
}

TEMPORAL_CASES = [
    ("temporal_1", examples),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.skip2
def test_temporal_add_in(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_add_in(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected
