#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

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


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
