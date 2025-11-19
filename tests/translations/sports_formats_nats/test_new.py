import pytest

# from src.translations.sports_formats_nats.new import create_label
from src.translations.sports_formats_nats.new import (
    create_label,
    create_nat_label,
    get_template_label_new,
    normalize_both,
    normalize_nat_label,
)


@pytest.mark.fast
def test_normalize_both() -> None:
    match_1 = normalize_both("Yemeni national football teams")
    assert match_1 == "natar national xoxo teams"


@pytest.mark.fast
def test_normalize_nat_label() -> None:
    match_1 = normalize_nat_label("Yemeni national football teams")
    assert match_1 == "natar national football teams"


@pytest.mark.fast
def test_get_template_label_new() -> None:
    template_label = get_template_label_new("Yemeni", "Yemeni xoxo championships")
    assert template_label == "بطولة natar xoxo"


@pytest.mark.fast
def test_create_nat_label() -> None:
    label = create_nat_label("Yemeni xoxo championships")
    assert label == "بطولة اليمن xoxo"


@pytest.mark.fast
def test_create_label() -> None:
    label = create_label("Yemeni football championships")
    assert label == "بطولة اليمن لكرة القدم"
