import pytest

from src.translations.sports_formats_national.sport_lab_nat import (
    Get_sport_formts_female_nat,
)

data = {
    "under-13 baseball teams": "فرق كرة قاعدة {nat} تحت 13 سنة",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_create_label(key, expected) -> None:
    template_label = Get_sport_formts_female_nat(key)
    assert template_label != ""
    assert template_label == expected
