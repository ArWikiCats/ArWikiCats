#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

data ={
    "Category:Afghan criminal law": "تصنيف:القانون الجنائي الأفغاني",
    "Category:Archaeology of Europe by period": "تصنيف:علم الآثار في أوروبا حسب الحقبة",
    "Category:Award winners by nationality": "تصنيف:حائزو جوائز حسب الجنسية",
    "Category:Government of Saint Barthélemy": "تصنيف:حكومة سان بارتيلمي",
    "Category:Historical novels": "تصنيف:روايات تاريخية",
    "Category:Historical poems": "تصنيف:قصائد تاريخية",
    "Category:Historical short stories": "تصنيف:قصص قصيرة تاريخية",
    "Category:History of the British Army": "تصنيف:تاريخ الجيش البريطاني",
    "Category:History of the British National Party": "تصنيف:تاريخ الحزب الوطني البريطاني",
    "Category:History of the Royal Air Force": "تصنيف:تاريخ القوات الجوية الملكية",
    "Category:History of the Royal Navy": "تصنيف:تاريخ البحرية الملكية",
    "Category:Military alliances involving Japan": "تصنيف:تحالفات عسكرية تشمل اليابان",
    "Category:Military alliances involving Yemen": "تصنيف:تحالفات عسكرية تشمل اليمن",
    "Category:Penal system in Afghanistan": "تصنيف:قانون العقوبات في أفغانستان",
    "Category:Prehistory of Venezuela": "تصنيف:فنزويلا ما قبل التاريخ",
}


def test_politics_and_history():
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_politics_and_history")
    assert diff == org, f"Differences found: {len(diff)}"


def test_politics_and_history():
    data = {
        "Category:American award winners": "تصنيف:حائزو جوائز أمريكيون",
        "Category:Treaties extended to Curaçao": "تصنيف:اتفاقيات امتدت إلى كوراساو"
    }
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_politics_and_history")
    assert diff == org, f"Differences found: {len(diff)}"
