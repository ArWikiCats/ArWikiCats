"""
Tests
"""

import pytest
import re
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.genders_resolvers.nat_genders_pattern_multi import sports_resolver, jobs_resolver

test_sport_bot_data= {
    "footballers": "لاعبو ولاعبات كرة قدم",
    "mens footballers": "لاعبو كرة قدم",
    "softball players": "لاعبو ولاعبات كرة لينة",
    "male beach soccer players": "لاعبو كرة قدم شاطئية",
    "male squash players": "لاعبو اسكواش",
    "male submission wrestling players": "لاعبو مصارعة خضوع",
    "male sumo players": "لاعبو سومو",
    "male surfing players": "لاعبو ركمجة",
    "male swimming players": "لاعبو سباحة",
    "male synchronised swimming players": "لاعبو سباحة متزامنة",
    "male synchronized swimming players": "لاعبو سباحة متزامنة",
    "female players of american-football": "لاعبات كرة قدم أمريكية",
    "male players of american-football": "لاعبو كرة قدم أمريكية",
    "players of american-football": "لاعبو ولاعبات كرة قدم أمريكية",
}


@pytest.mark.parametrize("category, expected", test_sport_bot_data.items(), ids=test_sport_bot_data.keys())
@pytest.mark.fast
def test_sport_bot(category: str, expected: str) -> None:
    label = sports_resolver(category)
    assert label == expected


test_job_bot_data= {
    "actors": "ممثلون وممثلات",
    "actresses": "ممثلات",
    "boxers": "ملاكمون وملاكمات",
    "female boxers": "ملاكمات",
    "female singers": "مغنيات",
    "male actors": "ممثلون",
    "male boxers": "ملاكمون",
    "male singers": "مغنون",
    "singers": "مغنون ومغنيات",
    "women boxers": "ملاكمات",
    "women singers": "مغنيات",

    "yemeni actresses": "ممثلات يمنيات",
    "yemeni actors": "ممثلون وممثلات يمنيون",
    "yemeni boxers": "ملاكمون وملاكمات يمنيون",
    "yemeni female boxers": "ملاكمات يمنيات",
    "yemeni female singers": "مغنيات يمنيات",
    "yemeni male actors": "ممثلون يمنيون",
    "yemeni male boxers": "ملاكمون يمنيون",
    "yemeni male singers": "مغنون يمنيون",
    "yemeni singers": "مغنون ومغنيات يمنيون",
    "yemeni women's boxers": "ملاكمات يمنيات",
    "yemeni women singers": "مغنيات يمنيات",
}


@pytest.mark.parametrize("category, expected", test_job_bot_data.items(), ids=test_job_bot_data.keys())
@pytest.mark.fast
def test_job_bot(category: str, expected: str) -> None:
    label = jobs_resolver(category)
    assert label == expected
