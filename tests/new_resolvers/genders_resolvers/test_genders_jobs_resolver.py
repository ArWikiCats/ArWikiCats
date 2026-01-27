"""
Tests
"""

import re

import pytest

from ArWikiCats.new_resolvers.genders_resolvers.jobs_and_genders_resolver import genders_jobs_resolver

test_job_bot_data = {
    "actors": "ممثلون وممثلات",
    "actresses": "ممثلات",
    "male actors": "ممثلون",
    "yemeni actresses": "ممثلات يمنيات",
    "yemeni actors": "ممثلون وممثلات يمنيون",
    "yemeni male actors": "ممثلون يمنيون",
    "boxers": "ملاكمون وملاكمات",
    "female boxers": "ملاكمات",
    "male boxers": "ملاكمون",
    "women boxers": "ملاكمات",
    "yemeni boxers": "ملاكمون وملاكمات يمنيون",
    "yemeni female boxers": "ملاكمات يمنيات",
    "yemeni male boxers": "ملاكمون يمنيون",
    "yemeni women's boxers": "ملاكمات يمنيات",
    "female singers": "مغنيات",
    "male singers": "مغنون",
    "singers": "مغنون ومغنيات",
    "women singers": "مغنيات",
    "yemeni male singers": "مغنون يمنيون",
    "yemeni singers": "مغنون ومغنيات يمنيون",
    "yemeni female singers": "مغنيات يمنيات",
    "yemeni women singers": "مغنيات يمنيات",
}

test_data2 = {
    "classical composers": "ملحنون وملحنات كلاسيكيون",
    "male classical singers": "مغنون كلاسيكيون",
    "female classical singers": "مغنيات كلاسيكيات",
    "yemeni male classical composers": "ملحنون كلاسيكيون يمنيون",
    "yemeni classical composers": "ملحنون وملحنات كلاسيكيون يمنيون",
    "yemeni female classical composers": "ملحنات كلاسيكيات يمنيات",
    # classical all keys (6 possibilities)
    "classical boxers": "ملاكمون وملاكمات كلاسيكيون",
    "male classical boxers": "ملاكمون كلاسيكيون",
    "female classical boxers": "ملاكمات كلاسيكيات",
    "yemeni male classical boxers": "ملاكمون كلاسيكيون يمنيون",
    "yemeni womens classical boxers": "ملاكمات كلاسيكيات يمنيات",
    "yemeni classical boxers": "ملاكمون وملاكمات كلاسيكيون يمنيون",
    # other keys
    "male guitarists": "عازفو قيثارة",
    "women guitarists": "عازفات قيثارة",
    "guitarists": "عازفو وعازفات قيثارة",
    "yemeni guitarists": "عازفو وعازفات قيثارة يمنيون",
    "yemeni male guitarists": "عازفو قيثارة يمنيون",
    "yemeni female guitarists": "عازفات قيثارة يمنيات",
    "male yemeni guitarists": "عازفو قيثارة يمنيون",
    "female yemeni guitarists": "عازفات قيثارة يمنيات",
}


@pytest.mark.parametrize("category, expected", test_job_bot_data.items(), ids=test_job_bot_data.keys())
@pytest.mark.fast
def test_job_bot(category: str, expected: str) -> None:
    label = genders_jobs_resolver(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data2.items(), ids=test_data2.keys())
@pytest.mark.fast
def test_job_bot2(category: str, expected: str) -> None:
    label = genders_jobs_resolver(category)
    assert label == expected
