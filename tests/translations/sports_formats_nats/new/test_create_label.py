import pytest

# from src.translations.sports_formats_nats.new import _create_label
from src.translations.sports_formats_nats.new import (
    both_bot,
    _create_label,
    _create_nat_label,
)

data = {
    "british softball championshipszz": "بطولة المملكة المتحدة للكرة اللينة",
    "ladies british softball tour": "بطولة المملكة المتحدة للكرة اللينة للسيدات",
    "british football tour": "بطولة المملكة المتحدة لكرة القدم",
    "Yemeni football championships": "بطولة اليمن لكرة القدم",
    "german figure skating championships": "بطولة ألمانيا للتزلج الفني",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_create_label(key, expected) -> None:
    template_label = _create_label(key)
    assert template_label != ""
    assert template_label == expected

    template_label2 = both_bot.create_label(key)
    assert template_label2 == expected


data2 = {
    "Yemeni xoxo championships": "بطولة اليمن xoxo",
}


@pytest.mark.parametrize("key,expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_create_nat_label(key, expected) -> None:
    template_label = _create_nat_label(key)
    assert template_label != ""
    assert template_label == expected

    template_label2 = both_bot.nat_bot.search(key)
    assert template_label2 == expected
