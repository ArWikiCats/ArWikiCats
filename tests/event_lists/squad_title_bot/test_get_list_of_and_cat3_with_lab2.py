"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar

list_data_0 = {
    "Bahrain AFC Asian Cup squad navigational boxes": "صناديق تصفح تشكيلات البحرين في كأس آسيا",
}

list_data = {
    # "1880 european competition for women's football squad templates": "قوالب تشكيلات منافسات أوروبية في كرة القدم للسيدات 1880",
    "1904 Summer Olympics football squad navigational boxes": "صناديق تصفح تشكيلات كرة القدم في الألعاب الأولمبية الصيفية 1904",
    "1984 AFC Asian Cup squad navigational boxes": "صناديق تصفح تشكيلات كأس آسيا 1984",
    "1952 Summer Olympics field hockey squad navigational boxes": "صناديق تصفح تشكيلات هوكي الميدان في الألعاب الأولمبية الصيفية 1952",
    "2022 European Women's Handball Championship squad templates": "قوالب تشكيلات بطولة أوروبا لكرة اليد للسيدات 2022",
    "1880 fifa women's world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم لكرة القدم للسيدات 1880",
    "1880 afc asian cup squad navigational boxes": "صناديق تصفح تشكيلات كأس آسيا 1880",
    "1880 afc women's asian cup squad navigational boxes": "صناديق تصفح تشكيلات كأس الأمم الآسيوية لكرة القدم للسيدات 1880",
    "1880 afc women's championship squad navigational boxes": "صناديق تصفح تشكيلات بطولة آسيا للسيدات 1880",
    "1880 africa cup-of-nations squad navigational boxes": "صناديق تصفح تشكيلات كأس الأمم الإفريقية 1880",
    "1880 african cup of nations squad navigational boxes": "صناديق تصفح تشكيلات كأس الأمم الإفريقية 1880",
    "1880 african women's championship squad navigational boxes": "صناديق تصفح تشكيلات كأس أمم إفريقيا لكرة القدم للسيدات 1880",
    "1880 basketball olympic squad templates": "قوالب تشكيلات كرة سلة أولمبية 1880",
    "1880 concacaf championships squad navigational boxes": "صناديق تصفح تشكيلات بطولات الكونكاكاف 1880",
    "1880 concacaf gold cup squad templates": "قوالب تشكيلات كأس الكونكاكاف الذهبية 1880",
    "1880 concacaf women's championship squad navigational boxes": "صناديق تصفح تشكيلات بطولة أمريكا الشمالية للسيدات 1880",
    "1880 copa américa femenina squad navigational boxes": "صناديق تصفح تشكيلات كوبا أمريكا فمنينا 1880",
    "1880 copa américa squad navigational boxes": "صناديق تصفح تشكيلات كوبا أمريكا 1880",
    "1880 cricket world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم للكريكت 1880",
    "1880 european men's handball championship squad templates": "قوالب تشكيلات بطولة أوروبا لكرة اليد للرجال 1880",
    "1880 european women's handball championship squad templates": "قوالب تشكيلات بطولة أوروبا لكرة اليد للسيدات 1880",
    "1880 fiba asia championship squad templates": "قوالب تشكيلات بطولة أمم آسيا لكرة السلة 1880",
    "1880 fiba asia cup squad templates": "قوالب تشكيلات كأس أمم آسيا لكرة السلة 1880",
    "1880 fiba basketball world cup squad templates": "قوالب تشكيلات كأس العالم لكرة السلة 1880",
    "1880 fiba women's basketball world cup squad templates": "قوالب تشكيلات كأس العالم لكرة السلة للسيدات 1880",
    "1880 fiba world championship for women squad templates": "قوالب تشكيلات بطولة كأس العالم لكرة السلة للسيدات 1880",
    "1880 fiba world championship squad templates": "قوالب تشكيلات بطولة كأس العالم لكرة السلة 1880",
    "1880 fiba world cup squad templates": "قوالب تشكيلات كأس العالم لكرة السلة 1880",
    "1880 fifa confederations cup squad navigational boxes": "صناديق تصفح تشكيلات كأس القارات 1880",
    "1880 men's hockey world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم للهوكي للرجال 1880",
    "1880 oceania cup squad navigational boxes": "صناديق تصفح تشكيلات كأس أوقيانوسيا 1880",
    "1880 ofc nations cup squad navigational boxes": "صناديق تصفح تشكيلات كأس أوقيانوسيا للأمم 1880",
    "1880 pan american games squad navigational boxes": "صناديق تصفح تشكيلات دورة الألعاب الأمريكية 1880",
    "1880 rugby league world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم لدوري الرجبي 1880",
    "1880 rugby world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم للرجبي 1880",
    "1880 rugby world cup squad templates": "قوالب تشكيلات كأس العالم للرجبي 1880",
    "1880 south american championship (argentina) squad navigational boxes": "صناديق تصفح تشكيلات كأس أمريكا الجنوبية (الأرجنتين) 1880",
    "1880 south american championship (ecuador) squad navigational boxes": "صناديق تصفح تشكيلات كأس أمريكا الجنوبية (الإكوادور) 1880",
    "1880 south american championship squad navigational boxes": "صناديق تصفح تشكيلات بطولة أمريكا الجنوبية 1880",
    "1880 summer olympics basketball squad navigational boxes": "صناديق تصفح تشكيلات كرة السلة في الألعاب الأولمبية الصيفية 1880",
    "1880 summer olympics field hockey squad navigational boxes": "صناديق تصفح تشكيلات هوكي الميدان في الألعاب الأولمبية الصيفية 1880",
    "1880 summer olympics football squad navigational boxes": "صناديق تصفح تشكيلات كرة القدم في الألعاب الأولمبية الصيفية 1880",
    "1880 summer olympics handball squad navigational boxes": "صناديق تصفح تشكيلات كرة اليد في الألعاب الأولمبية الصيفية 1880",
    "1880 summer olympics rugby sevens squad navigational boxes": "صناديق تصفح تشكيلات سباعيات الرجبي في الألعاب الأولمبية الصيفية 1880",
    "1880 summer olympics squad navigational boxes": "صناديق تصفح تشكيلات الألعاب الأولمبية الصيفية 1880",
    "1880 summer olympics volleyball squad navigational boxes": "صناديق تصفح تشكيلات كرة الطائرة في الألعاب الأولمبية الصيفية 1880",
    "1880 summer olympics water polo squad navigational boxes": "صناديق تصفح تشكيلات كرة الماء في الألعاب الأولمبية الصيفية 1880",
    "1880 women's cricket world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم للكريكت للسيدات 1880",
    "1880 women's field hockey world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم لهوكي الميدان للسيدات 1880",
    "1880 women's hockey world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم للهوكي للسيدات 1880",
    "1880 women's rugby world cup squad navigational boxes": "صناديق تصفح تشكيلات كأس العالم للرجبي للسيدات 1880",
    "1880 women's rugby world cup squad templates": "قوالب تشكيلات كأس العالم للرجبي للسيدات 1880",
    "1880 world men's handball championship squad templates": "قوالب تشكيلات بطولة العالم لكرة اليد للرجال 1880",
    "1880 world women's handball championship squad templates": "قوالب تشكيلات بطولة العالم لكرة اليد للسيدات 1880",
    "2004 summer olympics football squad navigational boxes": "صناديق تصفح تشكيلات كرة القدم في الألعاب الأولمبية الصيفية 2004",
}


@pytest.mark.parametrize("category, expected_key", list_data.items(), ids=list_data.keys())
@pytest.mark.fast
def test_list_data(category: str, expected_key: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected_key


@pytest.mark.parametrize("category, expected_key", list_data.items(), ids=list_data.keys())
@pytest.mark.fast
def test_squad_with_resolve(category: str, expected_key: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected_key


@pytest.mark.fast
def test_resolve_squads_labels_and_templates() -> None:
    # Test with a basic input
    result = resolve_label_ar("test category")
    assert isinstance(result, str)

    # Test with squad templates
    result_squad = resolve_label_ar("2020 squad templates")
    assert isinstance(result_squad, str)
    assert result_squad == "قوالب تشكيلات 2020"

    # Test with empty strings
    result_empty = resolve_label_ar("")
    assert isinstance(result_empty, str)
    assert result_empty == ""
