#!/usr/bin/python3
""" """

import pytest

from src.translations.sports_formats_teams.sport_lab import (
    Get_New_team_xo,
    Get_Sport_Format_xo_en_ar_is_P17,
)

Get_New_team_xo_data = {
    "acrobatic gymnastics junior world championships": "بطولة العالم الجمباز الاكروباتيكي للناشئين",
    "acrobatic gymnastics world championships": "بطولة العالم الجمباز الاكروباتيكي",
    "beach volleyball world championships": "بطولة العالم لكرة الطائرة الشاطئية",
    "biathlon world cup": "كأس العالم للبياثلون",
    "cross-country skiing world championships": "بطولة العالم للتزلج الريفي",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "domestic football leagues": "دوريات كرة قدم محلية",
    "domestic football": "كرة قدم محلية",
    "domestic handball leagues": "دوريات كرة يد محلية",
    "domestic women's football leagues": "دوريات كرة قدم محلية للسيدات",
    "domestic women's handball leagues": "دوريات كرة يد محلية للسيدات",
    "esports world cup": "كأس العالم للرياضة إلكترونية",
    "football league": "دوري كرة القدم",
    "indoor hockey": "هوكي داخل الصالات",
    "men's hockey world cup": "كأس العالم للهوكي للرجال",
    "men's international basketball": "كرة سلة دولية للرجال",
    "men's international football": "كرة قدم دولية للرجال",
    "men's rugby world cup": "كأس العالم للرجبي للرجال",
    "motocross world championship": "بطولة العالم للموتو كروس",
    "national football team results": "نتائج منتخبات كرة قدم وطنية",
    "national tennis league": "دوريات كرة مضرب وطنية",
    "netball world cup": "كأس العالم لكرة الشبكة",
    "racquetball world championships": "بطولة العالم لكرة الراح",
    "rugby league world cup": "كأس العالم لدوري الرجبي",
    "sailing world championships": "بطولة العالم للإبحار",
    "summer olympics basketball": "كرة السلة في الألعاب الأولمبية الصيفية",
    "summer olympics field hockey": "هوكي الميدان في الألعاب الأولمبية الصيفية",
    "summer olympics football": "كرة القدم في الألعاب الأولمبية الصيفية",
    "summer olympics handball": "كرة اليد في الألعاب الأولمبية الصيفية",
    "summer olympics rugby sevens": "سباعيات الرجبي في الألعاب الأولمبية الصيفية",
    "summer olympics volleyball": "كرة الطائرة في الألعاب الأولمبية الصيفية",
    "summer olympics water polo": "كرة الماء في الألعاب الأولمبية الصيفية",
    "wheelchair basketball world championships": "بطولة العالم لكرة السلة على الكراسي المتحركة",
    "women's cricket world cup": "كأس العالم للكريكت للسيدات",
    "women's field hockey world cup": "كأس العالم لهوكي الميدان للسيدات",
    "women's hockey world cup": "كأس العالم للهوكي للسيدات",
    "women's international basketball": "كرة سلة دولية للسيدات",
    "women's international football": "كرة قدم دولية للسيدات",
    "women's softball world cup": "كأس العالم للكرة اللينة للسيدات",
    "women's world wheelchair basketball championship": "بطولة العالم لكرة السلة على الكراسي المتحركة للسيدات",
    "world amateur boxing championships": "بطولة العالم للبوكسينغ للهواة",
    "world archery championships": "بطولة العالم للنبالة",
    "world athletics championships": "بطولة العالم لألعاب القوى",
    "world boxing championships": "بطولة العالم للبوكسينغ",
    "world junior ice hockey championships": "بطولة العالم لهوكي الجليد للناشئين",
    "world junior short track speed skating championships": "بطولة العالم للتزلج على مسار قصير للناشئين",
    "world junior wrestling championships": "بطولة العالم للمصارعة للناشئين",
    "world netball championship": "بطولة العالم لكرة الشبكة",
    "world netball championships": "بطولة العالم لكرة الشبكة",
    "world outdoor bowls championship": "بطولة العالم للبولينج في الهواء الطلق",
    "world taekwondo championships": "بطولة العالم للتايكوندو",
    "world wrestling championships": "بطولة العالم للمصارعة",
    "wrestling world cup": "كأس العالم للمصارعة",
}


@pytest.mark.parametrize("category, expected", Get_New_team_xo_data.items(), ids=list(Get_New_team_xo_data.keys()))
@pytest.mark.fast
def test_Get_New_team_xo_data(category, expected) -> None:
    label = Get_New_team_xo(category)
    assert isinstance(label, str)
    assert label.strip() == expected


@pytest.mark.fast
def test_Get_New_team_xo() -> None:
    label = Get_New_team_xo("national softball teams")
    assert label == "منتخبات كرة لينة وطنية"


data = {
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
    "under-13 baseball leagues finals": "نهائيات دوريات كرة قاعدة تحت 13 سنة",
    "under-13 baseball teams positions": "مراكز فرق كرة قاعدة تحت 13 سنة",
    "under-13 baseball leagues positions": "مراكز دوريات كرة قاعدة تحت 13 سنة",
    "under-13 baseball teams tournaments": "بطولات فرق كرة قاعدة تحت 13 سنة",
    "under-13 baseball leagues tournaments": "بطولات دوريات كرة قاعدة تحت 13 سنة",
    "under-13 baseball teams films": "أفلام فرق كرة قاعدة تحت 13 سنة",
    "under-13 baseball leagues films": "أفلام دوريات كرة قاعدة تحت 13 سنة",
}


@pytest.mark.fast
@pytest.mark.parametrize("category, expected_key", data.items(), ids=list(data.keys()))
def test_all(category, expected_key):
    result = Get_New_team_xo(category)
    assert result.strip() == expected_key, f"Mismatch for {category}"


data2 = {
    "national women's soccer team": "منتخب {} لكرة القدم للسيدات",
    "winter olympics softball": "كرة لينة {} في الألعاب الأولمبية الشتوية",
}


@pytest.mark.parametrize("category, expected_key", data2.items(), ids=list(data2.keys()))
@pytest.mark.fast
def test_Get_Sport_Format_xo_en_ar_is_P17(category, expected_key) -> None:
    label = Get_Sport_Format_xo_en_ar_is_P17(category)
    assert label.strip() == expected_key


def test_mens_softball_world_cup_regression() -> None:
    """The resolver should correctly translate the softball world cup query."""

    result = Get_New_team_xo("men's softball world cup")
    assert result == "كأس العالم للكرة اللينة للرجال"


def test_returns_default_for_unknown_category() -> None:
    """Unmapped categories should return the provided default value."""

    assert Get_New_team_xo("mystery sport") == ""
