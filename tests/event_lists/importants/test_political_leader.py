#
import pytest
from load_one_data import dump_diff, dump_diff_text, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data_0 = {
    "Category:World War II political leaders": "تصنيف:زعماء الحرب العالمية الثانية",
    "Category:Vanuatu political leader navigational boxes": "تصنيف:صناديق تصفح قادة فانواتو السياسيون",
    "Category:Somaliland political leader navigational boxes": "تصنيف:صناديق تصفح قادة أرض الصومال السياسيون",
    "Category:Republic of the Congo political leader navigational boxes": "تصنيف:صناديق تصفح قادة جمهورية الكونغو السياسيين",
    "Category:Northern Mariana Islands political leader navigational boxes": "تصنيف:صناديق تصفح قادة جزر ماريانا الشمالية السياسيون",
    "Category:Ireland political leader navigational boxes": "تصنيف:قوالب تصفح قادة سياسيين أيرلنديين",
    "Category:European Union political leader navigational boxes": "تصنيف:صناديق تصفح قائد سياسي الاتحاد الأوروبي",
}

data_fast = {
    "Category:Zimbabwe political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون زيمبابويون",
    "Category:Yemen political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون يمنيون",
    "Category:Vietnam political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون فيتناميون",
    "Category:United States political leader templates": "تصنيف:قوالب قادة سياسيون أمريكيون",
    "Category:United States political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أمريكيون",
    "Category:United Kingdom political leader templates": "تصنيف:قوالب قادة سياسيون بريطانيون",
    "Category:United Kingdom political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بريطانيون",
    "Category:United Arab Emirates political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون إماراتيون",
    "Category:Ukraine political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أوكرانيون",
    "Category:Uganda political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أوغنديون",
    "Category:Turkey political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أتراك",
    "Category:Tunisia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون تونسيون",
}

data_slow = {
    "Category:Thailand political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون تايلنديون",
    "Category:Taiwan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون تايوانيون",
    "Category:Syria political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سوريون",
    "Category:Sweden political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سويديون",
    "Category:Suriname political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سوريناميون",
    "Category:Sudan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سودانيون",
    "Category:Spain political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون إسبان",
    "Category:South Sudan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سودانيون جنوبيون",
    "Category:South Korea political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كوريون جنوبيون",
    "Category:South America political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أمريكيون جنوبيون",
    "Category:Somalia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون صوماليون",
    "Category:Slovakia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سلوفاكيون",
    "Category:Sierra Leone political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سيراليونيون",
    "Category:Senegal political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سنغاليون",
    "Category:Saudi Arabia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون سعوديون",
    "Category:Rwanda political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون روانديون",
    "Category:Romania political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون رومان",
    "Category:Portugal political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون برتغاليون",
    "Category:Philippines political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون فلبينيون",
    "Category:Pakistan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون باكستانيون",
    "Category:Ottoman Empire political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون عثمانيون",
    "Category:Oman political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون عمانيون",
    "Category:Oceania political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أوقيانوسيون",
    "Category:North Macedonia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون مقدونيون شماليون",
    "Category:North America political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أمريكيون شماليون",
    "Category:Nigeria political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون نيجيريون",
    "Category:Niger political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون نيجريون",
    "Category:New Zealand political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون نيوزيلنديون",
    "Category:Netherlands political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون هولنديون",
    "Category:Namibia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ناميبيون",
    "Category:Myanmar political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ميانماريون",
    "Category:Mozambique political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون موزمبيقيون",
    "Category:Montenegro political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون مونتينيغريون",
    "Category:Moldova political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون مولدوفيون",
    "Category:Middle East political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون شرقيون أوسطيون",
    "Category:Mexico political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون مكسيكيون",
    "Category:Mauritania political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون موريتانيون",
    "Category:Mali political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ماليون",
    "Category:Madagascar political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون مدغشقريون",
    "Category:Luxembourg political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون لوكسمبورغيون",
    "Category:Lithuania political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ليتوانيون",
    "Category:Libya political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ليبيون",
    "Category:Liberia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ليبيريون",
    "Category:Lebanon political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون لبنانيون",
    "Category:Laos political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون لاوسيون",
    "Category:Kosovo political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كوسوفيون",
    "Category:Kazakhstan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كازاخستانيون",
    "Category:Jordan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أردنيون",
    "Category:Japan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون يابانيون",
    "Category:Ivory Coast political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون إيفواريون",
    "Category:Italy political leader templates": "تصنيف:قوالب قادة سياسيون إيطاليون",
    "Category:Italy political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون إيطاليون",
    "Category:Israel political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون إسرائيليون",
    "Category:Iraq political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون عراقيون",
    "Category:Iran political leader templates": "تصنيف:قوالب قادة سياسيون إيرانيون",
    "Category:Iran political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون إيرانيون",
    "Category:Indonesia political leader templates": "تصنيف:قوالب قادة سياسيون إندونيسيون",
    "Category:India political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون هنود",
    "Category:Iceland political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون آيسلنديون",
    "Category:Hungary political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون مجريون",
    "Category:Guyana political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون غيانيون",
    "Category:Guinea political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون غينيون",
    "Category:Guinea-Bissau political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون غينيون بيساويون",
    "Category:Guatemala political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون غواتيماليون",
    "Category:Guam political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون غواميون",
    "Category:Greece political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون يونانيون",
    "Category:Germany political leader templates": "تصنيف:قوالب قادة سياسيون ألمان",
    "Category:Germany political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ألمان",
    "Category:Gabon political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون غابونيون",
    "Category:France political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون فرنسيون",
    "Category:Finland political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون فنلنديون",
    "Category:Fiji political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون فيجيون",
    "Category:Europe political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أوروبيون",
    "Category:Estonia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون إستونيون",
    "Category:Egypt political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون مصريون",
    "Category:Democratic Republic of the Congo political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كونغويون ديمقراطيون",
    "Category:Czechoslovakia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون تشيكوسلوفاكيون",
    "Category:Czech Republic political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون تشيكيون",
    "Category:Croatia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كروات",
    "Category:Colombia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كولومبيون",
    "Category:Chad political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون تشاديون",
    "Category:Central African Republic political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أفارقة أوسطيون",
    "Category:Caribbean political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كاريبيون",
    "Category:Cape Verde political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أخضريون",
    "Category:Cameroon political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كاميرونيون",
    "Category:Cambodia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون كمبوديون",
    "Category:Burundi political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بورونديون",
    "Category:Burkina Faso political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بوركينابيون",
    "Category:Bulgaria political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بلغاريون",
    "Category:Brazil political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون برازيليون",
    "Category:Botswana political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بوتسوانيون",
    "Category:Bosnia and Herzegovina political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بوسنيون",
    "Category:Benin political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بنينيون",
    "Category:Bangladesh political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون بنغلاديشيون",
    "Category:Azerbaijan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أذربيجانيون",
    "Category:Austria political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون نمساويون",
    "Category:Asia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون آسيويون",
    "Category:Armenia political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أرمن",
    "Category:Argentina political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أرجنتينيون",
    "Category:Angola political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أنغوليون",
    "Category:Algeria political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون جزائريون",
    "Category:Albania political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون ألبان",
    "Category:Africa political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أفارقة",
    "Category:Afghanistan political leader navigational boxes": "تصنيف:صناديق تصفح قادة سياسيون أفغان",
}

to_test = [
    ("test_political_leader_1", data_fast),
    ("test_political_leader_slow", data_slow),
]


@pytest.mark.parametrize("category, expected", data_fast.items(), ids=data_fast.keys())
@pytest.mark.fast
def test_political_leader_1(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data_slow.items(), ids=data_slow.keys())
@pytest.mark.slow
def test_political_leader_slow(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    # dump_diff_text(expected, diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, just_dump=True)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
