"""
Tests
"""

import pytest

from ArWikiCats.patterns_resolvers.country_nat_pattern import resolve_country_nat_pattern
from utils.dump_runner import make_dump_test_name_data_callback

test_data_1 = {
    "Polish spies for Nazi Germany": "جواسيس بولنديون لصالح ألمانيا النازية",
    "Hungarian spies for the Soviet Union": "جواسيس مجريون لصالح الاتحاد السوفيتي",
    "Dutch spies for Nazi Germany": "جواسيس هولنديون لصالح ألمانيا النازية",
    "Danish spies for Nazi Germany": "جواسيس دنماركيون لصالح ألمانيا النازية",
    "Swedish spies for the Soviet Union": "جواسيس سويديون لصالح الاتحاد السوفيتي",
    "Polish spies for the Soviet Union": "جواسيس بولنديون لصالح الاتحاد السوفيتي",
    "Italian spies for the Soviet Union": "جواسيس إيطاليون لصالح الاتحاد السوفيتي",
    "Canadian spies for the Soviet Union": "جواسيس كنديون لصالح الاتحاد السوفيتي",
    "Romanian spies for the Soviet Union": "جواسيس رومان لصالح الاتحاد السوفيتي",
    "Norwegian spies for Nazi Germany": "جواسيس نرويجيون لصالح ألمانيا النازية",
    "Japanese spies for the Soviet Union": "جواسيس يابانيون لصالح الاتحاد السوفيتي",
    "Austrian spies for the Soviet Union": "جواسيس نمساويون لصالح الاتحاد السوفيتي",
    "South African spies for the Soviet Union": "جواسيس جنوب إفريقيون لصالح الاتحاد السوفيتي",
    "Swiss spies for Nazi Germany": "جواسيس سويسريون لصالح ألمانيا النازية",
    "Irish spies for the Soviet Union": "جواسيس أيرلنديون لصالح الاتحاد السوفيتي",
    "Belgian spies for Nazi Germany": "جواسيس بلجيكيون لصالح ألمانيا النازية",
    "Finnish spies for the Soviet Union": "جواسيس فنلنديون لصالح الاتحاد السوفيتي",
    "American spies for the Soviet Union": "جواسيس أمريكيون لصالح الاتحاد السوفيتي",
    "British spies for the Soviet Union": "جواسيس بريطانيون لصالح الاتحاد السوفيتي",
    "West German spies for East Germany": "جواسيس ألمانيون غربيون لصالح ألمانيا الشرقية",
    "German spies for the Soviet Union": "جواسيس ألمان لصالح الاتحاد السوفيتي",
    "Israeli spies for the Soviet Union": "جواسيس إسرائيليون لصالح الاتحاد السوفيتي",
    "French spies for Nazi Germany": "جواسيس فرنسيون لصالح ألمانيا النازية",
    "British spies for Nazi Germany": "جواسيس بريطانيون لصالح ألمانيا النازية",
    "Ukrainian spies for the Soviet Union": "جواسيس أوكرانيون لصالح الاتحاد السوفيتي",
    "American spies for Nazi Germany": "جواسيس أمريكيون لصالح ألمانيا النازية",
}

test_data_2 = {}


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.fast
def test_country_nat_pattern_1(category: str, expected: str) -> None:
    label = resolve_country_nat_pattern(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_2.items(), ids=test_data_2.keys())
@pytest.mark.fast
def test_country_nat_pattern_2(category: str, expected: str) -> None:
    label = resolve_country_nat_pattern(category)
    assert label == expected


to_test = [
    ("test_country_nat_pattern_1", test_data_1, resolve_country_nat_pattern),
    ("test_country_nat_pattern_2", test_data_2, resolve_country_nat_pattern),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
