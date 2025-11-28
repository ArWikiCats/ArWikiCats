"""
Tests
"""

import pytest

from ArWikiCats.make_bots.ma_bots.squad_title_bot import get_squad_title

get_squad_title_data = {
    "1970 afc asian cup": "تشكيلات كأس آسيا 1970",
    "1970 afc women's asian cup": "تشكيلات كأس الأمم الآسيوية لكرة القدم للسيدات 1970",
    "1970 afc women's championship": "تشكيلات بطولة آسيا للسيدات 1970",
    "1970 africa cup-of-nations": "تشكيلات كأس الأمم الإفريقية 1970",
    "1970 african cup of nations": "تشكيلات كأس إفريقيا في بلدان 1970",
    "1970 african women's championship": "تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات 1970",
    "1970 basketball olympic": "تشكيلات كرة سلة أولمبية 1970",
    "1970 concacaf championships": "تشكيلات بطولات الكونكاكاف 1970",
    "1970 concacaf gold cup": "تشكيلات كأس الكونكاكاف الذهبية 1970",
    "1970 concacaf women's championship": "تشكيلات بطولة أمريكا الشمالية للسيدات 1970",
    "1970 copa américa femenina": "تشكيلات كوبا أمريكا فمنينا 1970",
    "1970 copa américa": "تشكيلات كوبا أمريكا 1970",
    "1970 cricket world cup": "تشكيلات كأس العالم للكريكيت 1970",
    "1970 european competition for women's football": "تشكيلات منافسات أوروبية في كرة القدم للسيدات 1970",
    "1970 european men's handball championship": "تشكيلات بطولة أوروبا لكرة اليد للرجال 1970",
    "1970 european women's handball championship": "تشكيلات بطولة أوروبا لكرة اليد للسيدات 1970",
    "1970 fiba asia championship": "تشكيلات بطولة أمم آسيا لكرة السلة 1970",
    "1970 fiba asia cup": "تشكيلات كأس أمم آسيا لكرة السلة 1970",
    "1970 fiba basketball world cup": "تشكيلات كأس العالم لكرة السلة 1970",
    "1970 fiba women's basketball world cup": "تشكيلات كأس العالم لكرة السلة للسيدات 1970",
    "1970 fiba world championship for women": "تشكيلات بطولة كأس العالم لكرة السلة للسيدات 1970",
    "1970 fiba world championship": "تشكيلات بطولة كأس العالم لكرة السلة 1970",
    "1970 fiba world cup": "تشكيلات كأس العالم لكرة السلة 1970",
    "1970 fifa confederations cup": "تشكيلات كأس القارات 1970",
    "1970 fifa women's world cup": "تشكيلات كأس العالم لكرة القدم للسيدات 1970",
    "1970 fifa world cup": "تشكيلات كأس العالم لكرة القدم 1970",
    "1970 men's hockey world cup": "تشكيلات كأس العالم للهوكي للرجال 1970",
    "1970 oceania cup": "تشكيلات كأس أوقيانوسيا 1970",
    "1970 ofc nations cup": "تشكيلات كأس أوقيانوسيا للأمم 1970",
    "1970 pan american games": "تشكيلات دورة الألعاب الأمريكية 1970",
    "1970 rugby league world cup": "تشكيلات كأس العالم لدوري الرجبي 1970",
    "1970 rugby world cup": "تشكيلات كأس العالم للرجبي 1970",
    "1970 south american championship (argentina)": "تشكيلات كأس أمريكا الجنوبية (الأرجنتين) 1970",
    "1970 south american championship (ecuador)": "تشكيلات كأس أمريكا الجنوبية (الإكوادور) 1970",
    "1970 south american championship": "تشكيلات بطولة أمريكا الجنوبية 1970",
    "1970 south american women's football championship": "تشكيلات كوبا أمريكا فمنينا 1970",
    "1970 summer olympics basketball": "تشكيلات كرة السلة في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics field hockey": "تشكيلات هوكي الميدان في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics football": "تشكيلات كرة القدم في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics handball": "تشكيلات كرة اليد في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics rugby sevens": "تشكيلات سباعيات الرجبي في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics volleyball": "تشكيلات كرة الطائرة في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics water polo": "تشكيلات كرة الماء في الألعاب الأولمبية الصيفية 1970",
    "1970 summer olympics": "تشكيلات الألعاب الأولمبية الصيفية 1970",
    "1970 women's cricket world cup": "تشكيلات كأس العالم للكريكت للسيدات 1970",
    "1970 women's field hockey world cup": "تشكيلات كأس العالم لهوكي الميدان للسيدات 1970",
    "1970 women's hockey world cup": "تشكيلات كأس العالم للهوكي للسيدات 1970",
    "1970 women's rugby world cup": "تشكيلات كأس العالم للرجبي للسيدات 1970",
    "1970 world men's handball championship": "تشكيلات بطولة العالم لكرة اليد للرجال 1970",
    "1970 world women's handball championship": "تشكيلات بطولة العالم لكرة اليد للسيدات 1970",
}


@pytest.mark.parametrize("category, expected_key", get_squad_title_data.items(), ids=list(get_squad_title_data.keys()))
@pytest.mark.fast
def test_get_squad_title_data(category, expected_key) -> None:
    label = get_squad_title(category)
    assert label == expected_key


def test_get_squad_title():
    # Test with a basic input
    result = get_squad_title("test squad")
    assert isinstance(result, str)

    result_empty = get_squad_title("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_squad_title("football team")
    assert isinstance(result_various, str)
