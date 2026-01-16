"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.countries_names_resolvers.geo_names_formats import resolve_by_geo_names

data_0 = {
    "military history of estonia": "تاريخ إستونيا العسكري",
    "Category:Political history of West Virginia": "تصنيف:تاريخ فرجينيا الغربية السياسي",

    "Category:Military history of the Tsardom of Russia": "تصنيف:تاريخ روسيا القيصرية العسكري",
    "Category:Banks of Zambia": "تصنيف:بنوك زامبيا",
    "Category:Military history of Amhara Region": "تصنيف:تاريخ أمهرة العسكري",
    "Category:Military history of Hubei": "تصنيف:تاريخ خوبي العسكري",
    "Category:Military history of republic of Venice": "تصنيف:تاريخ جمهورية البندقية العسكري",
    "Category:Military history of West Virginia": "تصنيف:تاريخ فرجينيا الغربية العسكري",
    "Category:Political history of Manitoba": "تصنيف:تاريخ مانيتوبا السياسي",
    "Category:Political history of Tamil Nadu": "تصنيف:تاريخ تامل نادو السياسي",
    "Category:Political history of Texas": "تصنيف:تاريخ تكساس السياسي",
    "Category:Military history of Bologna": "تصنيف:تاريخ بولونيا العسكري",
    "Category:Political history of Kurdistan": "تصنيف:تاريخ كردستان السياسي",
}

data_1 = {
}


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
