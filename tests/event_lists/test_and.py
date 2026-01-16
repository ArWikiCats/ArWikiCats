#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_label_ar

data0 = {
    "construction and architecture": "بناء وهندسة معمارية",
    "novels and short stories": "روايات وقصص قصيرة",
    "Women's universities and colleges in India": "جامعات نسائية وكليات في الهند",
    "women's universities and colleges": "جامعات نسائية وكليات",
    "qatar and united nations": "قطر والأمم المتحدة",
    "villages and municipalities": "قرى وبلديات",
    "Films about Olympic swimming and diving": "أفلام عن سباحة أولمبية والغطس",
    "olympic swimming and diving": "سباحة أولمبية والغطس",
    "films about olympic swimming and diving": "أفلام عن سباحة أولمبية والغطس",
    "criminal groups and organizations": "مجموعات إجرامية ومنظمات",
    "cherokee and united states treaties": "شيروكي ومعاهدات الولايات المتحدة",
    "European Union and science and technology": "الاتحاد الأوروبي والعلوم والتقانة",
    "british empire and commonwealth games": "الإمبراطورية البريطانية وألعاب الكومنولث",
    "Russia and Soviet Union political leader navigational boxes": "روسيا وصناديق تصفح قادة سياسيون سوفيت",
    "Papua New Guinea and the United Nations": "بابوا غينيا الجديدة والأمم المتحدة",
    "Christian theology and politics": "اللاهوت المسيحي وسياسة",
    "Christian universities and colleges templates": "جامعات مسيحية وقوالب كليات",
    "Hindu philosophers and theologians": "فلاسفة هندوس ولاهوتيون",
    "Jewish Persian and Iranian history": "فرس يهود وتاريخ إيراني",
    "Jewish Russian and Soviet history": "روس يهود وتاريخ سوفيتي",
    "Jewish universities and colleges by country": "جامعات يهودية وكليات حسب البلد",
    "Jewish universities and colleges in United Kingdom": "جامعات يهودية وكليات في المملكة المتحدة",
    "Jewish universities and colleges in United States": "جامعات يهودية وكليات في الولايات المتحدة",
    "Jewish universities and colleges": "جامعات يهودية وكليات",
    "Lists of Anglican bishops and archbishops": "قوائم أساقفة أنجليكيون ورؤساء أساقفة",
    "Lists of Protestant bishops and archbishops": "قوائم أساقفة بروتستانتيون ورؤساء أساقفة",
    "Nazi Germany and Catholicism": "ألمانيا النازية والكاثوليكية",
    "Nazi Germany and Christianity": "ألمانيا النازية والمسيحية",
    "Nazi Germany and Protestantism": "ألمانيا النازية والبروتستانتية",
    "1940 shipwrecks and maritime incidents navigational boxes": "حطام سفن وصناديق تصفح حوادث بحرية 1940",
    "Bishops of Ripon and Leeds": "أساقفة من ريبون (شمال يوركشير) وليدز",
    "Communications and media organizations based in China": "منظمات الاتصالات ووسائل الإعلام مقرها في الصين",
    "Gender and education": "الجنس وتعليم",
    "Gender and religion": "الجنس والدين",
    "Mathematics and art": "الرياضيات والفن",
    "South and Central American Men's Handball Championship": "الجنوب وبطولة أمريكا الوسطى لكرة اليد للرجال",
    "Turkey and United Nations": "تركيا والأمم المتحدة",
    "Games and sports introduced in 2026": "ألعاب وألعاب رياضية عرضت في 2026",
    "Conservatism and left-wing politics": "اتجاه محافظ وسياسة يسارية",
    "Religion and disability": "الدين وإعاقة",
    "University and college association football clubs in Spain": "جامعة وأندية كرة القدم الأمريكية الجامعية في إسبانيا",
    "Argentina and United Nations": "الأرجنتين والأمم المتحدة",
    "Games and sports introduced in 1977": "ألعاب وألعاب رياضية عرضت في 1977",
    "Singapore history and events templates": "تاريخ سنغافوري وقوالب أحداث",
}

data_1 = {}

data_2 = {
    "Category:17th-century_establishments_in_Närke_and_Värmland_County": "تأسيسات القرن 17 في مقاطعة ناركه وفارملاند",
    "Category:17th_century_in_Närke_and_Värmland_County": "مقاطعة ناركه وفارملاند في القرن 17",
    "Category:Centuries_in_Närke_and_Värmland_County": "قرون في مقاطعة ناركه وفارملاند",
    "Category:Establishments_in_Närke_and_Värmland_County_by_century": "تأسيسات في مقاطعة ناركه وفارملاند حسب القرن",
    "Category:Närke_and_Värmland_County": "مقاطعة ناركه وفارملاند",
}

data_3 = {}


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    # ("test_1", data_1),
    # ("test_2", data_2),
    ("test_3", data_3),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
@pytest.mark.skip2
def test_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
