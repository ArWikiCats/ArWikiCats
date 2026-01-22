#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_0 = {
    "construction and architecture": "بناء وهندسة معمارية",
    "novels and short stories": "روايات وقصص قصيرة",
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

data_1 = {
    "Women's universities and colleges in India": "جامعات وكليات نسائية في الهند",
    "women's universities and colleges": "جامعات وكليات نسائية",
    "Christian universities and colleges templates": "قوالب جامعات وكليات مسيحية",
    "Hindu philosophers and theologians": "فلاسفة ولاهوتيون هندوس",
    "17th-century_establishments_in_Närke_and_Värmland_County": "تأسيسات القرن 17 في مقاطعة ناركه وفارملاند",
    "17th_century_in_Närke_and_Värmland_County": "مقاطعة ناركه وفارملاند في القرن 17",
    "Centuries_in_Närke_and_Värmland_County": "قرون في مقاطعة ناركه وفارملاند",
    "Establishments_in_Närke_and_Värmland_County_by_century": "تأسيسات في مقاطعة ناركه وفارملاند حسب القرن",
    "Närke_and_Värmland_County": "مقاطعة ناركه وفارملاند",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.skip2
def test_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_0", data_0),
    ("test_1", data_1),
]


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
