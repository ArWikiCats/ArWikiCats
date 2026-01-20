#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

examples = {
    "18th-century Dutch explorers": "مستكشفون هولنديون في القرن 18",
    "20th-century Albanian sports coaches": "مدربو رياضة ألبان في القرن 20",
    "19th-century actors": "ممثلون في القرن 19",
    "2000s American films": "أفلام أمريكية في عقد 2000",
    "2017 American television series debuts": "مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "2017 American television series endings": "مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "19th-century actors by religion": "ممثلون في القرن 19 حسب الدين",
    "19th-century people by religion": "أشخاص في القرن 19 حسب الدين",
}

TEMPORAL_CASES = [
    ("temporal_1", examples),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.skip2
def test_temporal_add_in(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_add_in(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected
