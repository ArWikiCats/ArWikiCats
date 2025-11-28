#
import pytest
from load_one_data import dump_diff, one_dump_test

from src import resolve_arabic_category_label

data1 = {
    # "Category:yemeni presidential elections": "تصنيف:انتخابات اليمن الرئاسية",
    "Category:Adaptations of works by Greek writers": "تصنيف:أعمال مقتبسة عن أعمال كتاب يونانيون",
    "Category:Adaptations of works by Irish writers": "تصنيف:أعمال مقتبسة عن أعمال كتاب أيرلنديون",
    "Category:Adaptations of works by Italian writers": "تصنيف:أعمال مقتبسة عن أعمال كتاب إيطاليون",
    "Category:sieges of french invasion of egypt and syria": "تصنيف:حصارات الغزو الفرنسي لمصر وسوريا",
    "Category:1330 in men's international football": "تصنيف:كرة قدم دولية للرجال في 1330",
    "Category:2015 American television": "تصنيف:التلفزة الأمريكية 2015",
    "Category:2017 sports events": "تصنيف:أحداث 2017 الرياضية",
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
    "Category:military personnel of republic-of china": "تصنيف:أفراد عسكريون من جمهورية الصين",
    "Category:children of prime ministers of ukraine": "تصنيف:أطفال رؤساء وزراء أوكرانيا",
    # "Category:roman catholic bishops of fulda": "تصنيف:",
    "Category:men of poseidon": "تصنيف:رجال من بوسيدون",
    "Category:Olympic shooters of Egypt": "تصنيف:رماة أولمبيون من مصر",
    "Category:Olympic short track speed skaters of Japan": "تصنيف:متزلجون على مسار قصير أولمبيون من اليابان",
    "Category:Olympic figure skaters of Argentina": "تصنيف:متزلجون فنيون أولمبيون من الأرجنتين",
    "Category:Olympic figure skaters of Armenia": "تصنيف:متزلجون فنيون أولمبيون من أرمينيا",
    "Category:Olympic figure skaters of Australia": "تصنيف:متزلجون فنيون أولمبيون من أستراليا",
    # "Category:communists of bosnia and herzegovina politicians": "تصنيف:أحداث أكتوبر 1550 الرياضية في أوقيانوسيا",
}

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
    "Category:People associated with Nazarene universities and colleges": "",
}


data_list_bad = {
    "Category:20th century synagogues in switzerland": "تصنيف:كنس في سويسرا القرن 20",
    "Category:20th century roman catholic archbishops in colombia": "تصنيف:رؤساء أساقفة رومان كاثوليك في كولومبيا القرن 20",
    "Category:20th century people from al-andalus": "تصنيف:أشخاص من الأندلس في القرن 20",
    "Category:20th century churches in ethiopia": "تصنيف:كنائس في إثيوبيا القرن 20",
    "Category:20th century churches in nigeria": "تصنيف:كنائس في نيجيريا القرن 20",
    "Category:20th century members of maine legislature": "تصنيف:أعضاء هيئة مين التشريعية في القرن 20",
    "Category:20th century prime ministers of japan": "تصنيف:رؤساء وزراء اليابان القرن 20",
    "Category:september 1550 sorts-events in germany": "تصنيف:أحداث سبتمبر 1550 الرياضية في ألمانيا",
    "Category:1550s disestablishments in yugoslavia": "تصنيف:انحلالات عقد 1550 في يوغوسلافيا",
    "Category:20th century disestablishments in the united kingdom": "تصنيف:انحلالات القرن 20 في المملكة المتحدة",
    "Category:november 1550 sorts-events in north america": "تصنيف:أحداث نوفمبر 1550 الرياضية في أمريكا الشمالية",
    "Category:1550s establishments in wisconsin": "تصنيف:تأسيسات عقد 1550 في ويسكونسن",
    "Category:20th century disestablishments in sri lanka": "تصنيف:انحلالات القرن 20 في سريلانكا",
    "Category:3rd millennium disestablishments in england": "تصنيف:انحلالات الألفية 3 في إنجلترا",
    "Category:may 1550 sorts-events in the united states": "تصنيف:أحداث مايو 1550 الرياضية في الولايات المتحدة",
    "Category:december 1550 sorts-events in the united states": "تصنيف:أحداث ديسمبر 1550 الرياضية في الولايات المتحدة",
    "Category:1550s crimes in pakistan": "تصنيف:جرائم عقد 1550 في باكستان",
    "Category:2nd millennium establishments in rhode island": "تصنيف:تأسيسات الألفية 2 في رود آيلاند",
    "Category:1550s establishments in chile": "تصنيف:تأسيسات عقد 1550 في تشيلي",
    "Category:1550s disestablishments in southeast asia": "تصنيف:انحلالات عقد 1550 في جنوب شرق آسيا",
    "Category:december 1550 sorts-events in the united kingdom": "تصنيف:أحداث ديسمبر 1550 الرياضية في المملكة المتحدة",
    "Category:20th century american people by occupation": "تصنيف:أمريكيون في القرن 20 حسب المهنة",
    "Category:1550s establishments in jamaica": "تصنيف:تأسيسات عقد 1550 في جامايكا",
    "Category:march 1550 sorts-events in belgium": "تصنيف:أحداث مارس 1550 الرياضية في بلجيكا",
    "Category:20th century disasters in afghanistan": "تصنيف:كوارث القرن 20 في أفغانستان",
    "Category:april 1550 sorts-events in the united kingdom": "تصنيف:أحداث أبريل 1550 الرياضية في المملكة المتحدة",
    "Category:1550s disestablishments in mississippi": "تصنيف:انحلالات عقد 1550 في مسيسيبي",
    "Category:1550s establishments in maine": "تصنيف:تأسيسات عقد 1550 في مين",
    "Category:1550s establishments in sweden": "تصنيف:تأسيسات عقد 1550 في السويد",
    "Category:20th century disestablishments in newfoundland and labrador": "تصنيف:انحلالات القرن 20 في نيوفاوندلاند واللابرادور",
    "Category:20th century disestablishments in the danish colonial empire": "تصنيف:انحلالات القرن 20 في الإمبراطورية الاستعمارية الدنماركية",
    "Category:20th century establishments in french guiana": "تصنيف:تأسيسات القرن 20 في غويانا الفرنسية",
    "Category:20th century establishments in ireland": "تصنيف:تأسيسات القرن 20 في أيرلندا",
    "Category:20th century monarchs by country": "تصنيف:ملكيون في القرن 20 حسب البلد",
    "Category:august 1550 sorts-events in france": "تصنيف:أحداث أغسطس 1550 الرياضية في فرنسا",
    "Category:february 1550 sorts-events in germany": "تصنيف:أحداث فبراير 1550 الرياضية في ألمانيا",
    "Category:july 1550 crimes by continent": "تصنيف:جرائم يوليو 1550 حسب القارة",
    "Category:july 1550 sorts-events in north america": "تصنيف:أحداث يوليو 1550 الرياضية في أمريكا الشمالية",
    "Category:june 1550 sorts-events in malaysia": "تصنيف:أحداث يونيو 1550 الرياضية في ماليزيا",
    "Category:march 1550 sorts-events in thailand": "تصنيف:أحداث مارس 1550 الرياضية في تايلاند",
    "Category:november 1550 sorts-events in europe": "تصنيف:أحداث نوفمبر 1550 الرياضية في أوروبا",
    "Category:november 1550 sorts-events in the united kingdom": "تصنيف:أحداث نوفمبر 1550 الرياضية في المملكة المتحدة",
    "Category:october 1550 sorts-events in oceania": "تصنيف:أحداث أكتوبر 1550 الرياضية في أوقيانوسيا",
}


to_test = [
    ("test_1", data1),
    ("test_2", data_test2),
    ("test_2_new_bug_check", data_list_bad),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=list(data1.keys()))
@pytest.mark.fast
def test_1(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("category, expected", data_test2.items(), ids=list(data_test2.keys()))
@pytest.mark.fast
def test_2(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("category, expected", data_list_bad.items(), ids=list(data_list_bad.keys()))
@pytest.mark.fast
def test_2_new_bug_check(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.slow
def test_peoples(name, data):

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
