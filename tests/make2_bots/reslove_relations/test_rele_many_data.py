#
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.relations_resolver import new_relations_resolvers
from ArWikiCats.make_bots.reslove_relations.rele import resolve_relations_label

data_0 = {
    "africanamerican–asian-american relations": "العلاقات الأمريكية الآسيوية الأمريكية الإفريقية",
    "africanamerican–jewish relations": "العلاقات الأمريكية الإفريقية اليهودية",
    "african–native american relations": "العلاقات الأمريكية الأصلية الإفريقية",
    "algerian–tunisian wars": "الحروب التونسية الجزائرية",
    "arab–american relations": "العلاقات الأمريكية العربية",
    "arab–byzantine wars": "الحروب البيزنطية العربية",
    "bulgarian–ottoman wars": "الحروب البلغارية العثمانية",
    "bulgarian–serbian wars": "الحروب البلغارية الصربية",
    "byzantine–bulgarian wars": "الحروب البلغارية البيزنطية",
    "byzantine–georgian wars": "الحروب البيزنطية الجورجية",
    "byzantine–hungarian wars": "الحروب البيزنطية المجرية",
    "byzantine–ottoman wars": "الحروب البيزنطية العثمانية",
    "byzantine–sasanian wars": "الحروب البيزنطية الساسانية",
    "byzantine–turkish wars": "الحروب البيزنطية التركية",
    "cambodian–vietnamese war": "الحرب الفيتنامية الكمبودية",
    "canada–oceanian relations": "العلاقات الأوقيانوسية الكندية",
    "chadian–libyan war": "الحرب التشادية الليبية",
    "democratic-republic-of-congo–republic-of ireland relations": "العلاقات الأيرلندية الكونغوية الديمقراطية",
    "dutch–portuguese war": "الحرب البرتغالية الهولندية",
    "ecuadorian–peruvian war": "الحرب الإكوادورية البيروية",
    "ecuadorian–peruvian wars": "الحروب الإكوادورية البيروية",
    "egyptian–ottoman war": "الحرب العثمانية المصرية",
    "eritrean–ethiopian war": "الحرب الإثيوبية الإريترية",
    "german–romania military relations": "العلاقات الألمانية الرومانية العسكرية",
    "hungarian–czechoslovak war": "الحرب التشيكوسلوفاكية المجرية",
    "hungarian–ottoman wars": "الحروب العثمانية المجرية",
    "hungarian–romanian war": "الحرب الرومانية المجرية",
    "jewish–roman wars": "الحروب الرومانية اليهودية",
    "mexican–american war": "الحرب الأمريكية المكسيكية",
    "native american–jewish relations": "العلاقات الأمريكية الأصلية اليهودية",
    "ottoman–persian wars": "الحروب العثمانية الفارسية",
    "ottoman–serbian wars": "الحروب الصربية العثمانية",
    "philippine–american war": "الحرب الأمريكية الفلبينية",
    "polish–lithuanian war": "الحرب البولندية الليتوانية",
    "polish–ottoman wars": "الحروب البولندية العثمانية",
    "polish–russian wars": "الحروب البولندية الروسية",
    "polish–soviet war": "الحرب البولندية السوفيتية",
    "polish–ukrainian war": "الحرب الأوكرانية البولندية",
    "polish–ukrainian wars": "الحروب الأوكرانية البولندية",
    "republic-of ireland–united kingdom border crossings": "معابر الحدود الأيرلندية البريطانية",
    "republic-of ireland–united kingdom border": "الحدود الأيرلندية البريطانية",
    "roman–greek wars": "الحروب الرومانية اليونانية",
    "roman–iranian relations": "العلاقات الإيرانية الرومانية",
    "roman–parthian wars": "الحروب الرومانية الفرثية",
    "roman–persian wars": "الحروب الرومانية الفارسية",
    "roman–sasanian wars": "الحروب الرومانية الساسانية",
    "russian–ukrainian wars": "الحروب الأوكرانية الروسية",
    "scottish–norwegian war": "الحرب الإسكتلندية النرويجية",
    "sinhalese–portuguese war": "الحرب البرتغالية السنهالية",
    "slovak–hungarian war": "الحرب السلوفاكية المجرية",
    "soviet–afghan war": "الحرب الأفغانية السوفيتية",
    "spanish–american war": "الحرب الأمريكية الإسبانية",
    "swedish–norwegian war": "الحرب السويدية النرويجية",
    "ukrainian–soviet war": "الحرب الأوكرانية السوفيتية",
    "united kingdom–asian relations": "العلاقات الآسيوية البريطانية",
    "united kingdom–middle eastern relations": "العلاقات البريطانية الشرقية الأوسطية",
    "united kingdom–oceanian relations": "العلاقات الأوقيانوسية البريطانية",
    "united states–asian relations": "العلاقات الآسيوية الأمريكية",
    "united states–central american relations": "العلاقات الأمريكية الأمريكية الأوسطية",
    "united states–european relations": "العلاقات الأمريكية الأوروبية",
    "united states–middle eastern relations": "العلاقات الأمريكية الشرقية الأوسطية",
    "united states–north american relations": "العلاقات الأمريكية الأمريكية الشمالية",
    "united states–oceanian relations": "العلاقات الأمريكية الأوقيانوسية",
    "united states–south american relations": "العلاقات الأمريكية الأمريكية الجنوبية"
}

data_1 = {
    "artsakh–united states relations": "علاقات أرتساخ والولايات المتحدة",
    "australia–niue relations": "علاقات أستراليا ونييوي",
    "byzantine empire–carolingian empire relations": "علاقات الإمبراطورية البيزنطية والإمبراطورية الكارولنجية",
    "byzantine empire–empire of trebizond relations": "علاقات إمبراطورية طرابزون والإمبراطورية البيزنطية",
    "byzantine empire–first bulgarian empire relations": "علاقات الإمبراطورية البلغارية الأولى والإمبراطورية البيزنطية",
    "china–russian empire relations": "علاقات الإمبراطورية الروسية والصين",
    "djibouti–somaliland relations": "علاقات أرض الصومال وجيبوتي",
    "east asia–united states relations": "علاقات الولايات المتحدة وشرق آسيا",
    "ethiopia–somaliland relations": "علاقات أرض الصومال وإثيوبيا",
    "france–hawaii relations": "علاقات فرنسا وهاواي",
    "gaza–israel conflict": "صراع إسرائيل وغزة",
    "germany–somaliland relations": "علاقات أرض الصومال وألمانيا",
    "hawaii–united kingdom relations": "علاقات المملكة المتحدة وهاواي",
    "israel–somaliland relations": "علاقات أرض الصومال وإسرائيل",
    "japan–hawaii relations": "علاقات اليابان وهاواي",
    "japan–niue relations": "علاقات اليابان ونييوي",
    "japan–south vietnam relations": "علاقات اليابان وفيتنام الجنوبية",
    "jersey–united kingdom relations": "علاقات المملكة المتحدة وجيرزي",
    "lithuania–second polish republic relations": "علاقات الجمهورية البولندية الثانية وليتوانيا",
    "new zealand–niue relations": "علاقات نيوزيلندا ونييوي",
    "new zealand–pacific relations": "علاقات باسيفيك ونيوزيلندا",
    "niue–european union relations": "علاقات الاتحاد الأوروبي ونييوي",
    "niue–united kingdom relations": "علاقات المملكة المتحدة ونييوي",
    "niue–united states relations": "علاقات الولايات المتحدة ونييوي",
    "ottoman empire–russian empire relations": "علاقات الإمبراطورية الروسية والدولة العثمانية",
    "philippines–south vietnam relations": "علاقات الفلبين وفيتنام الجنوبية",
    "poland–saxony relations": "علاقات بولندا وساكسونيا",
    "russian empire–united states relations": "علاقات الإمبراطورية الروسية والولايات المتحدة",
    "russia–transnistria relations": "علاقات ترانسنيستريا وروسيا",
    "second polish republic–soviet union relations": "علاقات الاتحاد السوفيتي والجمهورية البولندية الثانية",
    "sint maarten–united states relations": "علاقات الولايات المتحدة وسينت مارتن",
    "somaliland–taiwan relations": "علاقات أرض الصومال وتايوان",
    "somaliland–united arab emirates relations": "علاقات أرض الصومال والإمارات العربية المتحدة",
    "somaliland–united kingdom relations": "علاقات أرض الصومال والمملكة المتحدة",
    "somaliland–united states relations": "علاقات أرض الصومال والولايات المتحدة",
    "south korea–south vietnam relations": "علاقات فيتنام الجنوبية وكوريا الجنوبية",
    "south vietnam–taiwan relations": "علاقات تايوان وفيتنام الجنوبية",
    "south vietnam–united states relations": "علاقات الولايات المتحدة وفيتنام الجنوبية",
    "transnistria–ukraine relations": "علاقات أوكرانيا وترانسنيستريا",
    "transnistria–united states relations": "علاقات الولايات المتحدة وترانسنيستريا",
}

data_3 = {
}


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.fast
def test_data_0(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_data_1(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_data_3(category: str, expected: str) -> None:
    label = new_relations_resolvers(category)
    assert label == expected


to_test = [
    # ("test_relations_0", data_0),
    ("test_relations_1", data_1),
    # ("test_relations_3", data_3),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, new_relations_resolvers)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
