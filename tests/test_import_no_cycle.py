"""
Tests
"""

import pytest

from src.make2_bots.ma_bots.ar_lab import get_con_lab
from src.make2_bots.ma_bots.country2_bot import Get_country2


@pytest.mark.fast
def test_get_con_lab_data_one():
    label = get_con_lab(preposition=" of ", country="11th government of turkey", start_get_country2=True)
    assert label != "حكومة تركيا"


data_fast = {
    "4th senate of spain": "مجلس شيوخ إسبانيا",
    "19th government of turkey": "حكومة تركيا",
    "11th government of turkey": "حكومة تركيا",
    "1330 in men's international football": "كرة قدم دولية رجالية في 1330",
}


@pytest.mark.parametrize("category, not_expected", data_fast.items(), ids=list(data_fast.keys()))
@pytest.mark.fast
def test_get_country2_one(category, not_expected) -> None:
    label = Get_country2(category)
    assert label.strip() != not_expected
