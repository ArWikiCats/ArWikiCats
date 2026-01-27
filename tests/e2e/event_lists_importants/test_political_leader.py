#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_0 = {
    "World War II political leaders": "زعماء الحرب العالمية الثانية",
    "Vanuatu political leader navigational boxes": "صناديق تصفح قادة فانواتو السياسيون",
    "Somaliland political leader navigational boxes": "صناديق تصفح قادة أرض الصومال السياسيون",
    "Republic of the Congo political leader navigational boxes": "صناديق تصفح قادة جمهورية الكونغو السياسيين",
    "Northern Mariana Islands political leader navigational boxes": "صناديق تصفح قادة جزر ماريانا الشمالية السياسيون",
    "Ireland political leader navigational boxes": "قوالب تصفح قادة سياسيين أيرلنديين",
    "European Union political leader navigational boxes": "صناديق تصفح قائد سياسي الاتحاد الأوروبي",
}

data_fast = {
    "Zimbabwe political leader navigational boxes": "صناديق تصفح قادة سياسيون زيمبابويون",
    "Yemen political leader navigational boxes": "صناديق تصفح قادة سياسيون يمنيون",
    "Vietnam political leader navigational boxes": "صناديق تصفح قادة سياسيون فيتناميون",
    "United States political leader templates": "قوالب قادة سياسيون أمريكيون",
    "United States political leader navigational boxes": "صناديق تصفح قادة سياسيون أمريكيون",
    "United Kingdom political leader templates": "قوالب قادة سياسيون بريطانيون",
    "United Kingdom political leader navigational boxes": "صناديق تصفح قادة سياسيون بريطانيون",
    "United Arab Emirates political leader navigational boxes": "صناديق تصفح قادة سياسيون إماراتيون",
    "Ukraine political leader navigational boxes": "صناديق تصفح قادة سياسيون أوكرانيون",
    "Uganda political leader navigational boxes": "صناديق تصفح قادة سياسيون أوغنديون",
    "Turkey political leader navigational boxes": "صناديق تصفح قادة سياسيون أتراك",
    "Tunisia political leader navigational boxes": "صناديق تصفح قادة سياسيون تونسيون",
}

data_slow = {
    "Thailand political leader navigational boxes": "صناديق تصفح قادة سياسيون تايلنديون",
    "Taiwan political leader navigational boxes": "صناديق تصفح قادة سياسيون تايوانيون",
    "Syria political leader navigational boxes": "صناديق تصفح قادة سياسيون سوريون",
    "Sweden political leader navigational boxes": "صناديق تصفح قادة سياسيون سويديون",
    "Suriname political leader navigational boxes": "صناديق تصفح قادة سياسيون سوريناميون",
    "Sudan political leader navigational boxes": "صناديق تصفح قادة سياسيون سودانيون",
    "Spain political leader navigational boxes": "صناديق تصفح قادة سياسيون إسبان",
    "South Sudan political leader navigational boxes": "صناديق تصفح قادة سياسيون سودانيون جنوبيون",
    "South Korea political leader navigational boxes": "صناديق تصفح قادة سياسيون كوريون جنوبيون",
    "South America political leader navigational boxes": "صناديق تصفح قادة سياسيون أمريكيون جنوبيون",
    "Somalia political leader navigational boxes": "صناديق تصفح قادة سياسيون صوماليون",
    "Slovakia political leader navigational boxes": "صناديق تصفح قادة سياسيون سلوفاكيون",
    "Sierra Leone political leader navigational boxes": "صناديق تصفح قادة سياسيون سيراليونيون",
    "Senegal political leader navigational boxes": "صناديق تصفح قادة سياسيون سنغاليون",
    "Saudi Arabia political leader navigational boxes": "صناديق تصفح قادة سياسيون سعوديون",
    "Rwanda political leader navigational boxes": "صناديق تصفح قادة سياسيون روانديون",
    "Romania political leader navigational boxes": "صناديق تصفح قادة سياسيون رومان",
    "Portugal political leader navigational boxes": "صناديق تصفح قادة سياسيون برتغاليون",
    "Philippines political leader navigational boxes": "صناديق تصفح قادة سياسيون فلبينيون",
    "Pakistan political leader navigational boxes": "صناديق تصفح قادة سياسيون باكستانيون",
    "Ottoman Empire political leader navigational boxes": "صناديق تصفح قادة سياسيون عثمانيون",
    "Oman political leader navigational boxes": "صناديق تصفح قادة سياسيون عمانيون",
    "Oceania political leader navigational boxes": "صناديق تصفح قادة سياسيون أوقيانوسيون",
    "North Macedonia political leader navigational boxes": "صناديق تصفح قادة سياسيون مقدونيون شماليون",
    "North America political leader navigational boxes": "صناديق تصفح قادة سياسيون أمريكيون شماليون",
    "Nigeria political leader navigational boxes": "صناديق تصفح قادة سياسيون نيجيريون",
    "Niger political leader navigational boxes": "صناديق تصفح قادة سياسيون نيجريون",
    "New Zealand political leader navigational boxes": "صناديق تصفح قادة سياسيون نيوزيلنديون",
    "Netherlands political leader navigational boxes": "صناديق تصفح قادة سياسيون هولنديون",
    "Namibia political leader navigational boxes": "صناديق تصفح قادة سياسيون ناميبيون",
    "Myanmar political leader navigational boxes": "صناديق تصفح قادة سياسيون ميانماريون",
    "Mozambique political leader navigational boxes": "صناديق تصفح قادة سياسيون موزمبيقيون",
    "Montenegro political leader navigational boxes": "صناديق تصفح قادة سياسيون مونتينيغريون",
    "Moldova political leader navigational boxes": "صناديق تصفح قادة سياسيون مولدوفيون",
    "Middle East political leader navigational boxes": "صناديق تصفح قادة سياسيون شرقيون أوسطيون",
    "Mexico political leader navigational boxes": "صناديق تصفح قادة سياسيون مكسيكيون",
    "Mauritania political leader navigational boxes": "صناديق تصفح قادة سياسيون موريتانيون",
    "Mali political leader navigational boxes": "صناديق تصفح قادة سياسيون ماليون",
    "Madagascar political leader navigational boxes": "صناديق تصفح قادة سياسيون مدغشقريون",
    "Luxembourg political leader navigational boxes": "صناديق تصفح قادة سياسيون لوكسمبورغيون",
    "Lithuania political leader navigational boxes": "صناديق تصفح قادة سياسيون ليتوانيون",
    "Libya political leader navigational boxes": "صناديق تصفح قادة سياسيون ليبيون",
    "Liberia political leader navigational boxes": "صناديق تصفح قادة سياسيون ليبيريون",
    "Lebanon political leader navigational boxes": "صناديق تصفح قادة سياسيون لبنانيون",
    "Laos political leader navigational boxes": "صناديق تصفح قادة سياسيون لاوسيون",
    "Kosovo political leader navigational boxes": "صناديق تصفح قادة سياسيون كوسوفيون",
    "Kazakhstan political leader navigational boxes": "صناديق تصفح قادة سياسيون كازاخستانيون",
    "Jordan political leader navigational boxes": "صناديق تصفح قادة سياسيون أردنيون",
    "Japan political leader navigational boxes": "صناديق تصفح قادة سياسيون يابانيون",
    "Ivory Coast political leader navigational boxes": "صناديق تصفح قادة سياسيون إيفواريون",
    "Italy political leader templates": "قوالب قادة سياسيون إيطاليون",
    "Italy political leader navigational boxes": "صناديق تصفح قادة سياسيون إيطاليون",
    "Israel political leader navigational boxes": "صناديق تصفح قادة سياسيون إسرائيليون",
    "Iraq political leader navigational boxes": "صناديق تصفح قادة سياسيون عراقيون",
    "Iran political leader templates": "قوالب قادة سياسيون إيرانيون",
    "Iran political leader navigational boxes": "صناديق تصفح قادة سياسيون إيرانيون",
    "Indonesia political leader templates": "قوالب قادة سياسيون إندونيسيون",
    "India political leader navigational boxes": "صناديق تصفح قادة سياسيون هنود",
    "Iceland political leader navigational boxes": "صناديق تصفح قادة سياسيون آيسلنديون",
    "Hungary political leader navigational boxes": "صناديق تصفح قادة سياسيون مجريون",
    "Guyana political leader navigational boxes": "صناديق تصفح قادة سياسيون غيانيون",
    "Guinea political leader navigational boxes": "صناديق تصفح قادة سياسيون غينيون",
    "Guinea-Bissau political leader navigational boxes": "صناديق تصفح قادة سياسيون غينيون بيساويون",
    "Guatemala political leader navigational boxes": "صناديق تصفح قادة سياسيون غواتيماليون",
    "Guam political leader navigational boxes": "صناديق تصفح قادة سياسيون غواميون",
    "Greece political leader navigational boxes": "صناديق تصفح قادة سياسيون يونانيون",
    "Germany political leader templates": "قوالب قادة سياسيون ألمان",
    "Germany political leader navigational boxes": "صناديق تصفح قادة سياسيون ألمان",
    "Gabon political leader navigational boxes": "صناديق تصفح قادة سياسيون غابونيون",
    "France political leader navigational boxes": "صناديق تصفح قادة سياسيون فرنسيون",
    "Finland political leader navigational boxes": "صناديق تصفح قادة سياسيون فنلنديون",
    "Fiji political leader navigational boxes": "صناديق تصفح قادة سياسيون فيجيون",
    "Europe political leader navigational boxes": "صناديق تصفح قادة سياسيون أوروبيون",
    "Estonia political leader navigational boxes": "صناديق تصفح قادة سياسيون إستونيون",
    "Egypt political leader navigational boxes": "صناديق تصفح قادة سياسيون مصريون",
    "Democratic Republic of the Congo political leader navigational boxes": "صناديق تصفح قادة سياسيون كونغويون ديمقراطيون",
    "Czechoslovakia political leader navigational boxes": "صناديق تصفح قادة سياسيون تشيكوسلوفاكيون",
    "Czech Republic political leader navigational boxes": "صناديق تصفح قادة سياسيون تشيكيون",
    "Croatia political leader navigational boxes": "صناديق تصفح قادة سياسيون كروات",
    "Colombia political leader navigational boxes": "صناديق تصفح قادة سياسيون كولومبيون",
    "Chad political leader navigational boxes": "صناديق تصفح قادة سياسيون تشاديون",
    "Central African Republic political leader navigational boxes": "صناديق تصفح قادة سياسيون أفارقة أوسطيون",
    "Caribbean political leader navigational boxes": "صناديق تصفح قادة سياسيون كاريبيون",
    "Cape Verde political leader navigational boxes": "صناديق تصفح قادة سياسيون أخضريون",
    "Cameroon political leader navigational boxes": "صناديق تصفح قادة سياسيون كاميرونيون",
    "Cambodia political leader navigational boxes": "صناديق تصفح قادة سياسيون كمبوديون",
    "Burundi political leader navigational boxes": "صناديق تصفح قادة سياسيون بورونديون",
    "Burkina Faso political leader navigational boxes": "صناديق تصفح قادة سياسيون بوركينابيون",
    "Bulgaria political leader navigational boxes": "صناديق تصفح قادة سياسيون بلغاريون",
    "Brazil political leader navigational boxes": "صناديق تصفح قادة سياسيون برازيليون",
    "Botswana political leader navigational boxes": "صناديق تصفح قادة سياسيون بوتسوانيون",
    "Bosnia and Herzegovina political leader navigational boxes": "صناديق تصفح قادة سياسيون بوسنيون",
    "Benin political leader navigational boxes": "صناديق تصفح قادة سياسيون بنينيون",
    "Bangladesh political leader navigational boxes": "صناديق تصفح قادة سياسيون بنغلاديشيون",
    "Azerbaijan political leader navigational boxes": "صناديق تصفح قادة سياسيون أذربيجانيون",
    "Austria political leader navigational boxes": "صناديق تصفح قادة سياسيون نمساويون",
    "Asia political leader navigational boxes": "صناديق تصفح قادة سياسيون آسيويون",
    "Armenia political leader navigational boxes": "صناديق تصفح قادة سياسيون أرمن",
    "Argentina political leader navigational boxes": "صناديق تصفح قادة سياسيون أرجنتينيون",
    "Angola political leader navigational boxes": "صناديق تصفح قادة سياسيون أنغوليون",
    "Algeria political leader navigational boxes": "صناديق تصفح قادة سياسيون جزائريون",
    "Albania political leader navigational boxes": "صناديق تصفح قادة سياسيون ألبان",
    "Africa political leader navigational boxes": "صناديق تصفح قادة سياسيون أفارقة",
    "Afghanistan political leader navigational boxes": "صناديق تصفح قادة سياسيون أفغان",
}

to_test = [
    ("test_political_leader_1", data_fast),
    ("test_political_leader_slow", data_slow),
]


@pytest.mark.parametrize("category, expected", data_fast.items(), ids=data_fast.keys())
@pytest.mark.fast
def test_political_leader_1(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data_slow.items(), ids=data_slow.keys())
@pytest.mark.slow
def test_political_leader_slow(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
