"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.countries_names_resolvers.geo_names_formats import resolve_by_geo_names

data_0 = {
    "foreign relations of fatimid caliphate": "علاقات الدولة الفاطمية الخارجية",
    "Banks of bologna": "بنوك بولونيا",
    "Military history of Amhara Region": "تاريخ أمهرة العسكري",
    "Military history of Bologna": "تاريخ بولونيا العسكري",
    "Military history of Hubei": "تاريخ خوبي العسكري",
    "Military history of republic of Venice": "تاريخ جمهورية البندقية العسكري",
    "Military history of the Tsardom of Russia": "تاريخ روسيا القيصرية العسكري",
    "Military history of West Virginia": "تاريخ فرجينيا الغربية العسكري",
    "Political history of Kurdistan": "تاريخ كردستان السياسي",
    "Political history of Manitoba": "تاريخ مانيتوبا السياسي",
    "Political history of Tamil Nadu": "تاريخ تامل نادو السياسي",
    "Political history of Texas": "تاريخ تكساس السياسي",
    "Political history of West Virginia": "تاريخ فرجينيا الغربية السياسي",
}

data_1 = {}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_geo_data_0(category: str, expected: str) -> None:
    label = resolve_by_geo_names(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.fast
def test_geo_data_1(category: str, expected: str) -> None:
    label = resolve_by_geo_names(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_geo_data_0", data_0, resolve_by_geo_names),
    ("test_geo_data_1", data_1, resolve_by_geo_names),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
