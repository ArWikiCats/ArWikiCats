#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

test_1 = {
    "New Zealand women non-fiction writers": "كاتبات غير روائيات نيوزيلنديات",
    "Non-fiction books about Italian-American organized crime": "كتب غير خيالية عن جريمة منظمة أمريكية إيطالية",
    "Non-fiction books about Native Americans": "كتب غير خيالية عن أمريكيون أصليون",
    "Non-fiction works about the United States military": "أعمال غير خيالية عن الجيش الأمريكي",
    "21st-century New Zealand non-fiction writers": "كتاب غير روائيين نيوزيلنديون في القرن 21",
    "20th-century New Zealand non-fiction writers": "كتاب غير روائيين نيوزيلنديون في القرن 20",
    "New Zealand non-fiction writers": "كتاب غير روائيين نيوزيلنديون",
    "New Zealand non-fiction writers by century": "كتاب غير روائيين نيوزيلنديون حسب القرن",
    "New Zealand non-fiction books": "كتب نيوزيلندية غير خيالية",
}

to_test = [
    ("test_1", test_1),
]


@pytest.mark.parametrize("category, expected", test_1.items(), ids=test_1.keys())
@pytest.mark.fast
def test_data_empty_result(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
