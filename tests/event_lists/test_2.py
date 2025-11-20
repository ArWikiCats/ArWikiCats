#
from load_one_data import dump_diff, ye_test_one_dataset

from src import new_func_lab_final_label

data = {
    "Category:sieges of french invasion of egypt and syria": "تصنيف:حصارات الغزو الفرنسي لمصر وسوريا",
    "Category:1330 in men's international football": "تصنيف:كرة قدم دولية للرجال في 1330",
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


data_test2 = {
    "Category:Schools for the deaf in New York (state)": "تصنيف:مدارس للصم في ولاية نيويورك",
    "Category:Cabinets involving the Liberal Party (Norway)": "",
    "Category:Television plays directed by William Sterling (director)": "",
    "Category:Television plays filmed in Brisbane": "",
    "Category:Television personalities from Yorkshire": "تصنيف:شخصيات تلفزيون من يوركشاير",
    "Category:Cabinets involving the Progress Party (Norway)": "تصنيف:مجالس وزراء تشمل حزب التقدم (النرويج)",
    "Category:People convicted of drug offenses by nationality": "تصنيف:مدانون ب جرائم المخدرات حسب الجنسية",
    "Category:People convicted of embezzlement": "تصنيف:مدانون ب الاختلاس",
    "Category:People convicted of espionage in Indonesia": "تصنيف:مدانون بالتجسس في إندونيسيا",
    "Category:People convicted of espionage in Iran": "تصنيف:مدانون بالتجسس في إيران",
    "Category:People convicted of espionage in Pakistan": "تصنيف:مدانون بالتجسس في باكستان",

    "Category:100 metres at the African Championships in Athletics": "",
    "Category:100 metres at the IAAF World Youth Championships in Athletics": "",
    "Category:100 metres at the World Para Athletics Championships": "",
    "Category:Documentary films about the 2011 Tōhoku earthquake and tsunami": "",
    "Category:People accused of lèse majesté in Thailand": "",
    "Category:People accused of lèse majesté in Thailand since 2020": "",
    "Category:People associated with former colleges of the University of London": "",
    "Category:People associated with Nazarene universities and colleges": ""
}


def test_2_new():
    expected, diff_result = ye_test_one_dataset(data_test2, new_func_lab_final_label)

    dump_diff(diff_result, "test_2_new")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
