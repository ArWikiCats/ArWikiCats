#
import pytest

from ArWikiCats import resolve_label_ar

data = {
    # "History of the Royal Air Force": "تاريخ القوات الجوية الملكية",
    # "History of the Royal Navy": "تاريخ البحرية الملكية",
    "Afghan criminal law": "القانون الجنائي الأفغاني",
    "Archaeology of Europe by period": "علم الآثار في أوروبا حسب الحقبة",
    "Award winners by nationality": "حائزو جوائز حسب الجنسية",
    "Government of Saint Barthélemy": "حكومة سان بارتيلمي",
    "Historical novels": "روايات تاريخية",
    "Historical poems": "قصائد تاريخية",
    "Historical short stories": "قصص قصيرة تاريخية",
    # "History of the British Army": "تاريخ الجيش البريطاني",
    "History of the British National Party": "تاريخ الحزب الوطني البريطاني",
    "Military alliances involving Japan": "تحالفات عسكرية تشمل اليابان",
    "Military alliances involving Yemen": "تحالفات عسكرية تشمل اليمن",
    "Penal system in Afghanistan": "قانون العقوبات في أفغانستان",
    "Prehistory of Venezuela": "فنزويلا ما قبل التاريخ",
    "American award winners": "حائزو جوائز أمريكيون",
    "Treaties extended to Curaçao": "اتفاقيات امتدت إلى كوراساو",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_politics_and_history(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
