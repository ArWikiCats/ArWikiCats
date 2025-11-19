#
from load_one_data import dump_diff, ye_test_one_dataset

from src import new_func_lab_final_label

data = {
    "Category:2015 American television": "تصنيف:التلفزة الأمريكية 2015",
    "Category:2017 sports events": "تصنيف:أحداث رياضية 2017",
    "Category:2017 American television series": "تصنيف:مسلسلات تلفزيونية أمريكية 2017",
    "Category:Cross-country skiers at the 1992 Winter Paralympics": "تصنيف:متزحلقون ريفيون في الألعاب البارالمبية الشتوية 1992",
    "Category:2017 American television episodes": "تصنيف:حلقات تلفزيونية أمريكية 2017",
    "Category:2017 American television seasons": "تصنيف:مواسم تلفزيونية أمريكية 2017",
    "Category:Roller skaters at the 2003 Pan American Games": "تصنيف:متزلجون بالعجلات في دورة الألعاب الأمريكية 2003",
    "Category:Ski jumpers at the 2007 Winter Universiade": "تصنيف:متزلجو قفز في الألعاب الجامعية الشتوية 2007",
    "Category:Figure skaters at the 2002 Winter Olympics": "تصنيف:متزلجون فنيون في الألعاب الأولمبية الشتوية 2002",
    "Category:Figure skaters at the 2003 Asian Winter Games": "تصنيف:متزلجون فنيون في الألعاب الآسيوية الشتوية 2003",
    "Category:Figure skaters at the 2007 Winter Universiade": "تصنيف:متزلجون فنيون في الألعاب الجامعية الشتوية 2007",
    "Category:Nations at the 2010 Summer Youth Olympics": "تصنيف:بلدان في الألعاب الأولمبية الشبابية الصيفية 2010",
}


def test_2():
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_2")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
