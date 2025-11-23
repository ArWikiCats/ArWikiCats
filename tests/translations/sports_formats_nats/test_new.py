import pytest

# from src.translations.sports_formats_nats.new import create_label
from src.translations.sports_formats_nats.new import (
    create_label,
    create_nat_label,
    get_template_label_new,
    normalize_both,
    normalize_nat_label,
)

from src.translations.sports_formats_nats.sport_lab_with_nat import (
    Get_New_team_xo_with_nat,
    apply_pattern_replacement,
    get_template_label,
    format_labels_with_nat,
    match_sports_labels_with_nat,
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
    template_label1 = get_template_label_new("Yemeni", "Yemeni xoxo championships")
    template_label2 = get_template_label("Yemeni", "natar", "Yemeni xoxo championships", format_labels_with_nat)
    assert template_label1 == "بطولة natar xoxo"
    assert template_label1 == template_label2


@pytest.mark.fast
def test_create_nat_label() -> None:
    label = create_nat_label("Yemeni xoxo championships")
    assert label == "بطولة اليمن xoxo"


@pytest.mark.fast
def test_create_label() -> None:
    label = create_label("Yemeni football championships")
    assert label == "بطولة اليمن لكرة القدم"
