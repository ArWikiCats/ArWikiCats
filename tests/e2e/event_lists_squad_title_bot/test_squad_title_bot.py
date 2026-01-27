"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar

get_squad_title_data = {
    "1970 fiba women's basketball world cup": "كأس العالم لكرة السلة للسيدات 1970",
    "1970 fiba world championship for women": "بطولة كأس العالم لكرة السلة للسيدات 1970",
    "1970 fiba women's world championship": "بطولة كأس العالم لكرة السلة للسيدات 1970",
    "1970 afc asian cup": "كأس آسيا 1970",
    "1970 afc women's asian cup": "كأس الأمم الآسيوية لكرة القدم للسيدات 1970",
    "1970 afc women's championship": "بطولة آسيا للسيدات 1970",
    "1970 africa cup-of-nations": "كأس الأمم الإفريقية 1970",
    "1970 african cup of nations": "كأس الأمم الإفريقية 1970",
    "1970 african women's championship": "كأس أمم إفريقيا لكرة القدم للسيدات 1970",
    "1970 basketball olympic": "كرة سلة أولمبية 1970",
    "1970 concacaf championships": "بطولات الكونكاكاف 1970",
    "1970 concacaf gold cup": "كأس الكونكاكاف الذهبية 1970",
    "1970 concacaf women's championship": "بطولة أمريكا الشمالية للسيدات 1970",
    "1970 copa américa femenina": "كوبا أمريكا فمنينا 1970",
    "1970 copa américa": "كوبا أمريكا 1970",
    "1970 cricket world cup": "كأس العالم للكريكت 1970",
    "1970 european men's handball championship": "بطولة أوروبا لكرة اليد للرجال 1970",
    "1970 european women's handball championship": "بطولة أوروبا لكرة اليد للسيدات 1970",
    "1970 fiba asia championship": "بطولة أمم آسيا لكرة السلة 1970",
    "1970 fiba asia cup": "كأس أمم آسيا لكرة السلة 1970",
    "1970 fiba basketball world cup": "كأس العالم لكرة السلة 1970",
    "1970 fiba world championship": "بطولة كأس العالم لكرة السلة 1970",
    "1970 fiba world cup": "كأس العالم لكرة السلة 1970",
    "1970 fifa confederations cup": "كأس القارات 1970",
    "1970 fifa women's world cup": "كأس العالم لكرة القدم للسيدات 1970",
    "1970 men's hockey world cup": "كأس العالم للهوكي للرجال 1970",
    "1970 oceania cup": "كأس أوقيانوسيا 1970",
    "1970 ofc nations cup": "كأس أوقيانوسيا للأمم 1970",
    "1970 pan american games": "دورة الألعاب الأمريكية 1970",
    "1970 rugby league world cup": "كأس العالم لدوري الرجبي 1970",
    "1970 rugby world cup": "كأس العالم للرجبي 1970",
    "1970 south american championship (argentina)": "كأس أمريكا الجنوبية (الأرجنتين) 1970",
    "1970 south american championship (ecuador)": "كأس أمريكا الجنوبية (الإكوادور) 1970",
    "1970 south american championship": "بطولة أمريكا الجنوبية 1970",
    "1970 summer olympics basketball": "كرة السلة في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics field hockey": "هوكي الميدان في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics football": "كرة القدم في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics handball": "كرة اليد في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics rugby sevens": "سباعيات الرجبي في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics volleyball": "كرة الطائرة في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics water polo": "كرة الماء في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics": "الألعاب الأولمبية الصيفية 1970",
    "1970 women's cricket world cup": "كأس العالم للكريكت للسيدات 1970",
    "1970 women's field hockey world cup": "كأس العالم لهوكي الميدان للسيدات 1970",
    "1970 women's hockey world cup": "كأس العالم للهوكي للسيدات 1970",
    "1970 women's rugby world cup": "كأس العالم للرجبي للسيدات 1970",
    "1970 world men's handball championship": "بطولة العالم لكرة اليد للرجال 1970",
    "1970 world women's handball championship": "بطولة العالم لكرة اليد للسيدات 1970",
}


@pytest.mark.parametrize("category, expected_key", get_squad_title_data.items(), ids=get_squad_title_data.keys())
@pytest.mark.fast
def test_get_squad_title_data(category: str, expected_key: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected_key


def test_get_squad_title() -> None:
    # Test with a basic input
    result = resolve_label_ar("test squad")
    assert isinstance(result, str)

    result_empty = resolve_label_ar("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = resolve_label_ar("football team")
    assert isinstance(result_various, str)
