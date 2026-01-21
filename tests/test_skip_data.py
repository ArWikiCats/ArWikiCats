#
import pytest
from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

fast_data_1 = {
    "Scheduled sports events": "أحداث رياضية مقررة",
}

to_test = [
    ("test_sports_events_2", fast_data_1),
]


@pytest.mark.parametrize("category, expected", fast_data_1.items(), ids=fast_data_1.keys())
@pytest.mark.skip2
def test_fast_data_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


# test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
