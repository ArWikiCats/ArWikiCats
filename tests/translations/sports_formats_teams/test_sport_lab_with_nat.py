#!/usr/bin/python3
"""


"""
import pytest

from src.translations.sports_formats_nats.sport_lab_with_nat import (
    get_template_label,
    match_sports_labels_with_nat,
    match_sports_labels_with_nat_new,
    Get_New_team_xo_with_nat,
    apply_pattern_replacement,
)


@pytest.mark.skip
def test_1() -> None:
    label = Get_New_team_xo_with_nat("Yemeni national xoxo teams", "football")
    assert label == "New team xoxo with nat"


@pytest.mark.skip
def test_2() -> None:
    template_label1 = match_sports_labels_with_nat_new("Yemeni national xoxo teams", "softball")
    assert template_label1 == 'منتخبات xoxo وطنية natar'

    template_label2 = match_sports_labels_with_nat_new("national xoxo teams of yemen", "softball")
    assert template_label2 == ""


@pytest.mark.skip
def test_3() -> None:
    template_label1 = match_sports_labels_with_nat("yemeni national xoxo teams", "softball")
    assert template_label1 == 'منتخبات xoxo وطنية natar'

    template_label2 = match_sports_labels_with_nat("national xoxo teams of yemen", "softball")
    assert template_label2 == ""


def test_get_template_label() -> None:
    template_label = get_template_label("Yemeni", "natar", "Yemeni national teams", {"natar national teams": "تجربة"})
    assert template_label == "تجربة"


def test_apply_pattern_replacement() -> None:
    team_lab = apply_pattern_replacement("منتخب xoxo الوطني", "اليمن", "xoxo")
    assert team_lab == "منتخب اليمن الوطني"


@pytest.mark.skip
def test_all():

    _data_old = {
        "national youth women's under-14 softball leagues umpires": "حكام دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball teams trainers": "مدربو منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball leagues trainers": "مدربو دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball teams scouts": "كشافة منتخبات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball leagues scouts": "كشافة دوريات كرة لينة وطنية تحت 14 سنة للشابات",
        "national youth women's under-14 softball teams coaches": "مدربو منتخبات كرة لينة وطنية تحت 14 سنة للشابات",

        "football seventh tier leagues": "دوريات كرة قدم من الدرجة السابعة",
        "football chairmen and investors": "رؤساء ومسيرو كرة قدم",
        "defunct football cup competitions": "منافسات كؤوس كرة قدم سابقة",
        "football cup competitions": "منافسات كؤوس كرة قدم",
        "domestic football cup": "كؤوس كرة قدم محلية",
        "current football seasons": "مواسم كرة قدم حالية",
        "football cups": "كؤوس كرة قدم",
        "professional football cups": "كؤوس كرة قدم للمحترفين",
        "defunct football cups": "كؤوس كرة قدم سابقة",
        "domestic football": "كرة قدم محلية",
        "indoor football": "كرة قدم داخل الصالات",
        "defunct football clubs": "أندية كرة قدم سابقة",

        "national women's equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية للسيدات",
        "national men's equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية للرجال",
        "national equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية",
        "under-13 equestrian": "فروسية تحت 13 سنة",
        "national under-13 equestrian manager history": "تاريخ مدربو منتخبات فروسية تحت 13 سنة",
        "under-13 equestrian manager history": "تاريخ مدربو فرق فروسية تحت 13 سنة",
        "under-14 equestrian": "فروسية تحت 14 سنة",
        "national under-14 equestrian manager history": "تاريخ مدربو منتخبات فروسية تحت 14 سنة",
        "under-14 equestrian manager history": "تاريخ مدربو فرق فروسية تحت 14 سنة",
        "outdoor equestrian": "فروسية في الهواء الطلق",

    }
    data = {
        "under-13 baseball leagues finals": "",
        "Swiss under-13 baseball teams": "مراكز فرق كرة قاعدة تحت 13 سنة",
        "under-13 baseball leagues positions": "مراكز دوريات كرة قاعدة تحت 13 سنة",
        "under-13 baseball teams tournaments": "بطولات فرق كرة قاعدة تحت 13 سنة",
        "under-13 baseball leagues tournaments": "بطولات دوريات كرة قاعدة تحت 13 سنة",
        "under-13 baseball teams films": "أفلام فرق كرة قاعدة تحت 13 سنة",
        "under-13 baseball leagues films": "أفلام دوريات كرة قاعدة تحت 13 سنة",
    }

    for category, expected_key in data.items():
        result = Get_New_team_xo_with_nat(category, "baseball")
        assert result.strip() == expected_key, f"Mismatch for {category}"
