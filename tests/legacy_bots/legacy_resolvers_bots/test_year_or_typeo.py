import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.legacy_bots.legacy_resolvers_bots.year_or_typeo import label_for_startwith_year_or_typeo
from utils.dump_runner import make_dump_test_name_data

data_0 = {}

data_1 = {}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
def test_year_or_typeo_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_year_or_typeo_1", data_1),
]


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
