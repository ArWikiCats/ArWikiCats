"""
Tests
"""

import re

import pytest

from ArWikiCats.new_resolvers.genders_resolvers import resolve_nat_genders_pattern_v2
from utils.dump_runner import make_dump_test_name_data_callback

test_data_ar = {
    "yemeni softball players": "لاعبو ولاعبات كرة لينة يمنيون",
    "yemeni men's softball players": "لاعبو كرة لينة يمنيون",
    "yemeni male softball players": "لاعبو كرة لينة يمنيون",
    "yemeni women's softball players": "لاعبات كرة لينة يمنيات",
    "Serbian men's footballers": "لاعبو كرة قدم صرب",
    "Russian men's futsal players": "لاعبو كرة صالات روس",
    "Scottish male badminton players": "لاعبو تنس ريشة إسكتلنديون",
    "irish actors": "ممثلون وممثلات أيرلنديون",
    "irish male actors": "ممثلون أيرلنديون",
    "irish actresses": "ممثلات أيرلنديات",
    "Albanian women's volleyball players": "لاعبات كرة طائرة ألبانيات",
    "yemeni women's footballers": "لاعبات كرة قدم يمنيات",
    "yemeni female footballers": "لاعبات كرة قدم يمنيات",
    "American women baseball players": "لاعبات كرة قاعدة أمريكيات",
    "Andorran female tennis players": "لاعبات كرة مضرب أندوريات",
    "Welsh players of Australian rules football": "لاعبو ولاعبات كرة قدم أسترالية ويلزيون",
    "Irish female players of Australian rules football": "لاعبات كرة قدم أسترالية أيرلنديات",
    "Welsh players of american-football": "لاعبو ولاعبات كرة قدم أمريكية ويلزيون",
    "Irish female players of american-football": "لاعبات كرة قدم أمريكية أيرلنديات",
    "Irish female players of american football": "لاعبات كرة قدم أمريكية أيرلنديات",
}

test_data_2 = {}


@pytest.mark.parametrize("category, expected", test_data_ar.items(), ids=test_data_ar.keys())
@pytest.mark.fast
def test_nat_genders_pattern_1(category: str, expected: str) -> None:
    label = resolve_nat_genders_pattern_v2(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_2.items(), ids=test_data_2.keys())
@pytest.mark.fast
def test_nat_genders_pattern_2(category: str, expected: str) -> None:
    label = resolve_nat_genders_pattern_v2(category)
    assert label == expected


to_test = [
    ("test_nat_genders_pattern_1", test_data_ar, resolve_nat_genders_pattern_v2),
    ("test_nat_genders_pattern_2", test_data_2, resolve_nat_genders_pattern_v2),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
