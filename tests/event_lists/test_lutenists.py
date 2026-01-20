#
import pytest
from load_one_data import dump_diff, dump_diff_text, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar

test_lutenists_1 = {
    "Lutenists": "عازفو آلات وترية",
    "German lutenists": "عازفو آلات وترية ألمان",
    "American lutenists": "عازفو آلات وترية أمريكيون",
    "Spanish lutenists": "عازفو آلات وترية إسبان",
    "English lutenists": "عازفو آلات وترية إنجليز",
    "Portuguese lutenists": "عازفو آلات وترية برتغاليون",
    "British lutenists": "عازفو آلات وترية بريطانيون",
    "Polish lutenists": "عازفو آلات وترية بولنديون",
    "Lutenists by nationality": "عازفو آلات وترية حسب الجنسية",
    "Danish lutenists": "عازفو آلات وترية دنماركيون",
    "Russian lutenists": "عازفو آلات وترية روس",
    "French lutenists": "عازفو آلات وترية فرنسيون",
    "Dutch lutenists": "عازفو آلات وترية هولنديون",
}
to_test = [
    ("test_lutenists_1", test_lutenists_1),
]


@pytest.mark.parametrize("category, expected", test_lutenists_1.items(), ids=test_lutenists_1.keys())
@pytest.mark.fast
def test_data_lutenists_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    # dump_diff_text (expected, diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, True)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
