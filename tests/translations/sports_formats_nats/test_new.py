import pytest

# from src.translations.sports_formats_nats.new import create_label
from src.translations.sports_formats_nats.new import (
    create_label,
    create_nat_label,
    normalize_both,
    normalize_nat_label,
)

data = {
    "british softball championshipszz": "بطولة المملكة المتحدة للكرة اللينة",
    "ladies british softball tour": "بطولة المملكة المتحدة للكرة اللينة للسيدات",
    "british football tour": "بطولة المملكة المتحدة لكرة القدم",
    "Yemeni football championships": "بطولة اليمن لكرة القدم",
    "german figure skating championships": "بطولة ألمانيا للتزلج الفني",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.skip2
def test_create_label(key, expected) -> None:
    template_label = create_label(key)
    assert template_label != ""
    assert template_label == expected


@pytest.mark.fast
def test_normalize_both() -> None:
    match_1 = normalize_both("Yemeni national football teams")
    assert match_1 == "natar national xoxo teams"


@pytest.mark.fast
def test_normalize_nat_label() -> None:
    match_1 = normalize_nat_label("Yemeni national football teams")
    assert match_1 == "natar national football teams"


@pytest.mark.fast
def test_create_nat_label() -> None:
    label = create_nat_label("Yemeni xoxo championships")
    assert label == "بطولة اليمن xoxo"
