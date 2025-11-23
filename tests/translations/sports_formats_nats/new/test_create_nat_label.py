import pytest

from src.translations.sports_formats_nats.new import (
    create_nat_label,
)

data = {
    "Yemeni xoxo championships": "بطولة اليمن xoxo",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_create_nat_label(key, expected) -> None:
    template_label = create_nat_label(key)
    assert template_label != ""
    assert template_label == expected
