#
import pytest

from ArWikiCats import resolve_arabic_category_label

data = {
    # "Category:History of the Royal Air Force": "تصنيف:تاريخ القوات الجوية الملكية",
    # "Category:History of the Royal Navy": "تصنيف:تاريخ البحرية الملكية",
    "Category:Afghan criminal law": "تصنيف:القانون الجنائي الأفغاني",
    "Category:Archaeology of Europe by period": "تصنيف:علم الآثار في أوروبا حسب الحقبة",
    "Category:Award winners by nationality": "تصنيف:حائزو جوائز حسب الجنسية",
    "Category:Government of Saint Barthélemy": "تصنيف:حكومة سان بارتيلمي",
    "Category:Historical novels": "تصنيف:روايات تاريخية",
    "Category:Historical poems": "تصنيف:قصائد تاريخية",
    "Category:Historical short stories": "تصنيف:قصص قصيرة تاريخية",
    # "Category:History of the British Army": "تصنيف:تاريخ الجيش البريطاني",
    "Category:History of the British National Party": "تصنيف:تاريخ الحزب الوطني البريطاني",
    "Category:Military alliances involving Japan": "تصنيف:تحالفات عسكرية تشمل اليابان",
    "Category:Military alliances involving Yemen": "تصنيف:تحالفات عسكرية تشمل اليمن",
    "Category:Penal system in Afghanistan": "تصنيف:قانون العقوبات في أفغانستان",
    "Category:Prehistory of Venezuela": "تصنيف:فنزويلا ما قبل التاريخ",
    "Category:American award winners": "تصنيف:حائزو جوائز أمريكيون",
    "Category:Treaties extended to Curaçao": "تصنيف:اتفاقيات امتدت إلى كوراساو",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_politics_and_history(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
