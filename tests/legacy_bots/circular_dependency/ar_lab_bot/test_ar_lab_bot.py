"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.resolvers.arabic_label_builder import CountryResolver


@pytest.mark.fast
def test_get_con_lab_data_one() -> None:
    label = CountryResolver.resolve_labels(" of ", "11th government of turkey")
    assert label != "حكومة تركيا"


data_1 = [
    # ("for", "for national teams", "للمنتخبات الوطنية"),
    ("for", "for argentina", "الأرجنتين"),
    ("for", "for australia", "أستراليا"),
    ("for", "for germany", "ألمانيا"),
    ("from", "northern ireland of canadian descent", "أيرلندا الشمالية من أصل كندي"),
    ("in", "1420 all-africa games", "ألعاب عموم إفريقيا 1420"),
    ("in", "1420 world games", "دورة الألعاب العالمية 1420"),
    ("in", "german novels of 20th century", "روايات ألمانية في القرن 20"),
    ("named after", "populated places in latvia", "أماكن مأهولة في لاتفيا"),
    ("named after", "populated places in portugal", "أماكن مأهولة في البرتغال"),
    ("of", "prime ministers of malaysia", "رؤساء وزراء ماليزيا"),
    ("to", "united states house-of-representatives from missouri territory", "مجلس النواب الأمريكي من إقليم ميزوري"),
    ("by", "by city in colombia", "حسب المدينة في كولومبيا"),
    ("by", "by city in northern-ireland", "حسب المدينة في أيرلندا الشمالية"),
    ("by", "by county in taiwan", "حسب المقاطعة في تايوان"),
    ("by", "by educational institution in derbyshire", "حسب الهيئة التعليمية في داربيشير"),
    ("by", "by league in the united states", "حسب الدوري في الولايات المتحدة"),
    ("by", "by team in the united states", "حسب الفريق في الولايات المتحدة"),
    ("by", "by university or college in beijing", "حسب الجامعة أو الكلية في بكين"),
    ("by", "by university or college in guatemala", "حسب الجامعة أو الكلية في غواتيمالا"),
    ("by", "by university or college in india", "حسب الجامعة أو الكلية في الهند"),
    ("by", "by university or college in mauritius", "حسب الجامعة أو الكلية في موريشيوس"),
    ("by", "by university or college in nebraska", "حسب الجامعة أو الكلية في نبراسكا"),
    ("by", "by university or college in north carolina", "حسب الجامعة أو الكلية في كارولاينا الشمالية"),
    ("for", "for malta ", "مالطا"),
    ("for", "for the british virgin islands", "جزر العذراء البريطانية"),
    ("for", "for the russian empire", "الإمبراطورية الروسية"),
    ("for", "for the soviet union", "الاتحاد السوفيتي"),
    ("for", "for the united states", "الولايات المتحدة"),
    ("in", "1789 asian winter games", "الألعاب الآسيوية الشتوية 1789"),
    ("in", "1789 british empire games", "دورة ألعاب الإمبراطورية البريطانية 1789"),
    ("in", "1789 fifa women's world cup", "كأس العالم لكرة القدم للسيدات 1789"),
    ("in", "1789 fifa world cup", "كأس العالم لكرة القدم 1789"),
    ("in", "1789 pan american games", "دورة الألعاب الأمريكية 1789"),
    ("in", "buildings and structures in africa", "مبان ومنشآت في إفريقيا"),
    ("in", "real estate industry", "صناعة عقارية"),
    ("in", "university of galway", "جامعة جلوي"),
    ("named after", "organizations based in gabon", "منظمات مقرها في الغابون"),
    ("named after", "populated places in uruguay", "أماكن مأهولة في أوروغواي"),
    ("named after", "universities and colleges in ghana", "جامعات وكليات في غانا"),
    ("named after", "universities and colleges in uruguay", "جامعات وكليات في أوروغواي"),
    ("of", " kingdom-of italy (1789–1789)", "مملكة إيطاليا (1789–1789)"),
    ("of", "companies of georgia (country)", "شركات في جورجيا"),
    ("of", "companies of southeast asia", "شركات في جنوب شرق آسيا"),
    ("of", "indigenous peoples of americas", "شعوب أصلية في الأمريكتين"),
    ("of", "parliament of england 1789", "برلمان إنجلترا 1789"),
    ("of", "parliament of northern ireland 1789–1789", "برلمان أيرلندا الشمالية 1789–1789"),
    (
        "of",
        "verkhovna rada of ukrainian soviet socialist republic",
        "المجلس الأعلى الأوكراني في جمهورية أوكرانيا السوفيتية الاشتراكية",
    ),
    ("of", "water of coquimbo region", "مياه في إقليم كوكيمبو"),
    ("of", "water of hambantota district", "مياه في مديرية هامبانتوتا"),
    ("of", "water of matale district", "مياه في مديرية ماتال"),
    ("of", "water of wilkes land", "مياه في ويلكس لاند"),
    ("to", "united nations in geneva", "الأمم المتحدة في جنيف"),
    ("transferred-from", "united states navy to the royal navy", "البحرية الأمريكية إلى البحرية الملكية"),
]


@pytest.mark.parametrize("separator, country, output", data_1, ids=[x[1] for x in data_1])
# @pytest.mark.fast
def test_get_con_lab_data(separator: str, country: str, output: str) -> None:
    preposition = f" {separator} "
    label = CountryResolver.resolve_labels(preposition, country)
    assert label == output
