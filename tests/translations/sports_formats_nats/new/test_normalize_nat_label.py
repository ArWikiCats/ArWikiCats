import pytest

from src.translations.sports_formats_nats.new import (
    normalize_nat_label,
)

data = {
    "Yemeni national football teams": "natar national football teams",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_normalize_nat_label(key, expected) -> None:
    template_label = normalize_nat_label(key)
    assert template_label != ""
    assert template_label == expected
