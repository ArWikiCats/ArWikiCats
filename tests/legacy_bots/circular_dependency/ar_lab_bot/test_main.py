import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

fast_data = {
    "Commissioners for South Georgia and South Sandwich Islands": "مفوضين في جورجيا الجنوبية وجزر ساندويتش الجنوبية",
    "Founders of Norwegian schools and colleges": "مؤسسي مدارس وكليات نرويجية",
    "Golf tournaments in Guatemala": "بطولات الغولف في غواتيمالا",
    "Golf tournaments in Peru": "بطولات الغولف في بيرو",
    "Motorsport in North America": "رياضة المحركات في أمريكا الشمالية",
    "Motorsport in Tanzania": "رياضة المحركات في تنزانيا",
    "Music based on works by William Shakespeare": "موسيقى مبنية على أعمال وليم شكسبير",
    "Music by country subdivision": "موسيقى حسب تقسيم البلد",
    "Music organisations based in Democratic Republic of Congo": "منظمات موسيقية مقرها في جمهورية الكونغو الديمقراطية",
    "Music organisations based in Djibouti": "منظمات موسيقية مقرها في جيبوتي",
    "Music organisations based in Somalia": "منظمات موسيقية مقرها في الصومال",
    "Musical groups by time of reestablishment": "مجموعات موسيقية حسب وقت إعادة التأسيس",
    "Musical groups from Bern": "مجموعات موسيقية من برن",
    "Musical groups from Brussels": "مجموعات موسيقية من بروكسل",
    "Musical groups from County Clare": "مجموعات موسيقية من مقاطعة كلير",
    "Musical groups from Kiev": "مجموعات موسيقية من كييف",
    "Natural gas fields in China": "خطوط غاز طبيعي في الصين",
    "Natural gas pipelines by country": "خطوط أنابيب غاز حسب البلد",
    "Olympic competitors for Russian Empire": "منافسون في الألعاب الأولمبية من الإمبراطورية الروسية",
    "Running in Gabon": "الركض في الغابون",
    "Running in Mozambique": "الركض في موزمبيق",
    "Running in Suriname": "الركض في سورينام",
    "Sports at Asian Youth Games": "رياضات في الألعاب الآسيوية الشبابية",
    "Sports in Bemidji, Minnesota": "رياضات في بيميدجي (منيسوتا)",
    "Sports in Clarksburg, West Virginia": "رياضات في كلاركسبورغ (فرجينيا الغربية)",
    "Sports in Duluth, Minnesota": "رياضات في دولوث",
    "Sports in Mankato, Minnesota": "رياضات في مانكاتو (منيسوتا)",
    "Sports in Martinsburg, West Virginia": "رياضات في مرتينسبورغ (فرجينيا الغربية)",
    "Sports in Newburgh, New York": "رياضات في نيوبورغ (نيويورك)",
    "Sports in Niagara Falls, New York": "رياضات في نياجارا فولز (نيويورك)",
    "Sports in Olympia, Washington": "رياضات في أولمبيا (واشنطن)",
    "Sports in Parkersburg, West Virginia": "رياضات في باركرسبورغ (فرجينيا الغربية)",
    "Sports in Puerto Rico": "رياضات في بورتوريكو",
    "Sports in Rochester, Minnesota": "رياضات في روتشيستر (منيسوتا)",
    "Sports in St. Cloud, Minnesota": "رياضات في سانت كلاود (منيسوتا)",
    "Sports in Walla Walla, Washington": "رياضات في والا والا (واشنطن)",
    "Christian rock groups from Arizona": "فرق روك مسيحية من أريزونا",
    "Christian rock groups from California": "فرق روك مسيحية من كاليفورنيا",
    "Christian rock groups from Florida": "فرق روك مسيحية من فلوريدا",
    "Christian rock groups from Georgia (U.S. state)": "فرق روك مسيحية من ولاية جورجيا",
    "Christian rock groups from Illinois": "فرق روك مسيحية من إلينوي",
    "Christian rock groups from Iowa": "فرق روك مسيحية من آيوا",
    "Christian rock groups from Kentucky": "فرق روك مسيحية من كنتاكي",
    "Christian rock groups from Louisiana": "فرق روك مسيحية من لويزيانا",
    "Christian rock groups from Michigan": "فرق روك مسيحية من ميشيغان",
    "Christian rock groups from Minnesota": "فرق روك مسيحية من منيسوتا",
    "Christian rock groups from Ohio": "فرق روك مسيحية من أوهايو",
    "Christian rock groups from Oklahoma": "فرق روك مسيحية من أوكلاهوما",
    "Christian rock groups from South Carolina": "فرق روك مسيحية من كارولاينا الجنوبية",
    "Christian rock groups from Tennessee": "فرق روك مسيحية من تينيسي",
    "Christian rock groups from Texas": "فرق روك مسيحية من تكساس",
    "Christian rock groups from Washington (state)": "فرق روك مسيحية من ولاية واشنطن",
    "Christian rock groups from West Virginia": "فرق روك مسيحية من فرجينيا الغربية",
    "Cycling at Islamic Solidarity Games": "سباق الدراجات الهوائية في ألعاب التضامن الإسلامي",
    "Music based on works by Hans Christian Andersen": "موسيقى مبنية على أعمال هانس كريستيان أندرسن",
    "Sports at 2010 Islamic Solidarity Games": "رياضات في ألعاب التضامن الإسلامي 2010",
    "Sports at Islamic Solidarity Games": "رياضات في ألعاب التضامن الإسلامي",
    "1650s crimes": "جرائم عقد 1650",
    "1650s disasters": "كوارث عقد 1650",
    "1650s disestablishments": "انحلالات عقد 1650",
    "1650s establishments": "تأسيسات عقد 1650",
    "1st millennium bc establishments": "تأسيسات الألفية 1 ق م",
    "1st millennium disestablishments": "انحلالات الألفية 1",
    "20th century attacks": "هجمات القرن 20",
    "20th century clergy": "رجال دين في القرن 20",
    "20th century lawyers": "محامون في القرن 20",
    "20th century mathematicians": "رياضياتيون في القرن 20",
    "20th century north american people": "أمريكيون شماليون في القرن 20",
    "20th century norwegian people": "نرويجيون في القرن 20",
    "20th century people": "أشخاص في القرن 20",
    "20th century philosophers": "فلاسفة في القرن 20",
    "20th century photographers": "مصورون في القرن 20",
    "20th century roman catholic bishops": "أساقفة كاثوليك رومان في القرن 20",
    "20th century romanian people": "رومان في القرن 20",
    "march 1650 crimes": "جرائم مارس 1650",
    "september 1650 crimes": "جرائم سبتمبر 1650",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_event2_fast(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("fast_data", fast_data),
]

test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
