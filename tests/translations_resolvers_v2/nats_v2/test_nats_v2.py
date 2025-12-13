"""
Tests
"""

import pytest
from typing import Callable

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.translations_resolvers_v2.nats_v2 import resolve_by_nats

test_data_males = {
    # males - en_is_nat_ar_is_mens
    "yemeni non profit publishers": "ناشرون غير ربحيون يمنيون",
    "yemeni non-profit publishers": "ناشرون غير ربحيون يمنيون",
    "yemeni government officials": "مسؤولون حكوميون يمنيون",
    "saudi non profit publishers": "ناشرون غير ربحيون سعوديون",
    "egyptian government officials": "مسؤولون حكوميون مصريون",
}

test_data_ar = {
    # ar - en_is_nat_ar_is_P17
    "Bahraini King's Cup": "كأس ملك البحرين",
    "Yemeni King's Cup": "كأس ملك اليمن",
    "French Grand Prix": "جائزة فرنسا الكبرى",
    "Italian Grand Prix": "جائزة إيطاليا الكبرى",
    "French Open": "فرنسا المفتوحة",
    "Australian Open": "أستراليا المفتوحة",
    "French Ladies Open": "فرنسا المفتوحة للسيدات",
    "Canadian Cup": "كأس كندا",
    "Egyptian Independence": "استقلال مصر",
    "Syrian Independence": "استقلال سوريا",
    "Canadian National University": "جامعة كندا الوطنية",
    "Egyptian National University": "جامعة مصر الوطنية",
    "Canadian National University Alumni": "خريجو جامعة كندا الوطنية",
    "Egyptian National University Alumni": "خريجو جامعة مصر الوطنية",
    "Japanese national women's motorsports racing team": "منتخب اليابان لسباق رياضة المحركات للسيدات",
    "French national women's motorsports racing team": "منتخب فرنسا لسباق رياضة المحركات للسيدات",
}

test_data_the_male = {
    # the_male - en_is_nat_ar_is_al_mens
    "Iraqi President Cup": "كأس الرئيس العراقي",
    "Egyptian President Cup": "كأس الرئيس المصري",
    "Iraqi Federation Cup": "كأس الاتحاد العراقي",
    "Saudi Federation Cup": "كأس الاتحاد السعودي",
    "Iraqi FA Cup": "كأس الاتحاد العراقي",
    "Egyptian FA Cup": "كأس الاتحاد المصري",
    "Iraqi Occupation": "الاحتلال العراقي",
    "American Occupation": "الاحتلال الأمريكي",
    "Iraqi Super Cup": "كأس السوبر العراقي",
    "Egyptian Super Cup": "كأس السوبر المصري",
    "Saudi Elite Cup": "كأس النخبة السعودي",
    "Iraqi Referendum": "الاستفتاء العراقي",
    "Syrian Referendum": "الاستفتاء السوري",
    "American Involvement": "التدخل الأمريكي",
    "French Involvement": "التدخل الفرنسي",
    "Egyptian Census": "التعداد المصري",
    "Iraqi Census": "التعداد العراقي",
    "Iraqi Professional Football League": "دوري كرة القدم العراقي للمحترفين",
    "Saudi Professional Football League": "دوري كرة القدم السعودي للمحترفين",
    "Iraqi Premier Football League": "الدوري العراقي الممتاز لكرة القدم",
    "Egyptian Premier Football League": "الدوري المصري الممتاز لكرة القدم",
    "Iraqi National Super League": "دوري السوبر العراقي",
    "Egyptian National Super League": "دوري السوبر المصري",
    "Iraqi Super League": "دوري السوبر العراقي",
    "Saudi Super League": "دوري السوبر السعودي",
    "Iraqi Premier League": "الدوري العراقي الممتاز",
    "Egyptian Premier League": "الدوري المصري الممتاز",
    "Iraqi Premier Division": "الدوري العراقي الممتاز",
    "Saudi Premier Division": "الدوري السعودي الممتاز",
    "Iraqi amateur football league": "الدوري العراقي لكرة القدم للهواة",
    "Egyptian amateur football league": "الدوري المصري لكرة القدم للهواة",
    "Iraqi football league": "الدوري العراقي لكرة القدم",
    "Saudi football league": "الدوري السعودي لكرة القدم",
    "Egyptian Population Census": "التعداد السكاني المصري",
    "Iraqi Population Census": "التعداد السكاني العراقي",
    "Egyptian population and housing census": "التعداد المصري للسكان والمساكن",
    "Iraqi population and housing census": "التعداد العراقي للسكان والمساكن",
    "Egyptian National Party": "الحزب الوطني المصري",
    "Iraqi National Party": "الحزب الوطني العراقي",
    "Egyptian Criminal Law": "القانون الجنائي المصري",
    "Iraqi Criminal Law": "القانون الجنائي العراقي",
    "Egyptian Family Law": "قانون الأسرة المصري",
    "Iraqi Family Law": "قانون الأسرة العراقي",
    "Egyptian Labour Law": "قانون العمل المصري",
    "Iraqi Labour Law": "قانون العمل العراقي",
    "Egyptian Abortion Law": "قانون الإجهاض المصري",
    "American Abortion Law": "قانون الإجهاض الأمريكي",
    "French Rugby Union Leagues": "اتحاد دوري الرجبي الفرنسي",
    "Australian Rugby Union Leagues": "اتحاد دوري الرجبي الأسترالي",
    "French Women's Rugby Union": "اتحاد الرجبي الفرنسي للنساء",
    "Australian Women's Rugby Union": "اتحاد الرجبي الأسترالي للنساء",
    "French Rugby Union": "اتحاد الرجبي الفرنسي",
    "Australian Rugby Union": "اتحاد الرجبي الأسترالي",
    "American Presidential Pardons": "العفو الرئاسي الأمريكي",
    "Egyptian Presidential Pardons": "العفو الرئاسي المصري",
    "American Pardons": "العفو الأمريكي",
    "Egyptian Pardons": "العفو المصري",
}

test_data_male = {
    # male - en_is_nat_ar_is_man
    "Egyptian descent": "أصل مصري",
    "Iraqi descent": "أصل عراقي",
    "American military occupations": "احتلال عسكري أمريكي",
    "Iraqi military occupations": "احتلال عسكري عراقي",
    "French integration": "تكامل فرنسي",
    "Egyptian integration": "تكامل مصري",
    "Japanese innovation": "ابتكار ياباني",
    "American innovation": "ابتكار أمريكي",
    "Italian design": "تصميم إيطالي",
    "French design": "تصميم فرنسي",
    "French contemporary art": "فن معاصر فرنسي",
    "American contemporary art": "فن معاصر أمريكي",
    "Italian art": "فن إيطالي",
    "French art": "فن فرنسي",
    "Italian cuisine": "مطبخ إيطالي",
    "French cuisine": "مطبخ فرنسي",
    "Japanese calendar": "تقويم ياباني",
    "Chinese calendar": "تقويم صيني",
    "American non fiction literature": "أدب غير خيالي أمريكي",
    "French non fiction literature": "أدب غير خيالي فرنسي",
    "British non-fiction literature": "أدب غير خيالي بريطاني",
    "American non-fiction literature": "أدب غير خيالي أمريكي",
    "Russian literature": "أدب روسي",
    "French literature": "أدب فرنسي",
    "Indian caste system": "نظام طبقي هندي",
    "Pakistani caste system": "نظام طبقي باكستاني",
    "American law": "قانون أمريكي",
    "French law": "قانون فرنسي",
    "French wine": "نبيذ فرنسي",
    "Italian wine": "نبيذ إيطالي",
    "Egyptian history": "تاريخ مصري",
    "Iraqi history": "تاريخ عراقي",
    "American nuclear history": "تاريخ نووي أمريكي",
    "French nuclear history": "تاريخ نووي فرنسي",
    "American military history": "تاريخ عسكري أمريكي",
    "French military history": "تاريخ عسكري فرنسي",
    "Palestinian diaspora": "شتات فلسطيني",
    "Syrian diaspora": "شتات سوري",
    "Indian traditions": "تراث هندي",
    "Chinese traditions": "تراث صيني",
    "Irish folklore": "فلكور أيرلندي",
    "Scottish folklore": "فلكور إسكتلندي",
}

test_data_female = {
    # female - en_is_nat_ar_is_women
    "American airstrikes": "ضربات جوية أمريكية",
    "American autobiographies": "ترجمة ذاتية أمريكية",
    "American awards and decorations": "جوائز وأوسمة أمريكية",
    "American awards": "جوائز أمريكية",
    "American companies": "شركات أمريكية",
    "American crimes against humanity": "جرائم ضد الإنسانية أمريكية",
    "American crimes": "جرائم أمريكية",
    "American elections": "انتخابات أمريكية",
    "American music": "موسيقى أمريكية",
    "American newspapers": "صحف أمريكية",
    "American organizations": "منظمات أمريكية",
    "american television series": "مسلسلات تلفزيونية أمريكية",
    "American universities": "جامعات أمريكية",
    "American war crimes": "جرائم حرب أمريكية",
    "American wars": "حروب أمريكية",
    "British autobiographies": "ترجمة ذاتية بريطانية",
    "British newspapers": "صحف بريطانية",
    "British universities": "جامعات بريطانية",
    "French architecture": "عمارة فرنسية",
    "French awards and decorations": "جوائز وأوسمة فرنسية",
    "French awards": "جوائز فرنسية",
    "French culture": "ثقافة فرنسية",
    "French elections": "انتخابات فرنسية",
    "French music": "موسيقى فرنسية",
    "French organizations": "منظمات فرنسية",
    "French phonologies": "تصريفات صوتية فرنسية",
    "French wars": "حروب فرنسية",
    "German automotive": "سيارات ألمانية",
    "Greek archipelagoes": "أرخبيلات يونانية",
    "Greek mythology": "أساطير يونانية",
    "Indonesian archipelagoes": "أرخبيلات إندونيسية",
    "Iraqi crimes": "جرائم عراقية",
    "Israeli airstrikes": "ضربات جوية إسرائيلية",
    "Israeli crimes against humanity": "جرائم ضد الإنسانية إسرائيلية",
    "Israeli war crimes": "جرائم حرب إسرائيلية",
    "Japanese architecture": "عمارة يابانية",
    "Japanese automotive": "سيارات يابانية",
    "Japanese companies": "شركات يابانية",
    "Japanese culture": "ثقافة يابانية",
    "non american television series": "مسلسلات تلفزيونية غير أمريكية",
    "non yemeni television series": "مسلسلات تلفزيونية غير يمنية",
    "non-american television series": "مسلسلات تلفزيونية غير أمريكية",
    "non-yemeni television series": "مسلسلات تلفزيونية غير يمنية",
    "Roman mythology": "أساطير رومانية",
}

test_data_the_female = {
    # the_female - en_is_nat_ar_is_al_women
    "British royal air force": "القوات الجوية الملكية البريطانية",
    "Saudi royal air force": "القوات الجوية الملكية السعودية",
    "American air force": "القوات الجوية الأمريكية",
    "French air force": "القوات الجوية الفرنسية",
    "British royal defence force": "قوات الدفاع الملكية البريطانية",
    "Saudi royal defence force": "قوات الدفاع الملكية السعودية",
    "British royal navy": "البحرية الملكية البريطانية",
    "Saudi royal navy": "البحرية الملكية السعودية",
    "American naval force": "البحرية الأمريكية",
    "French naval force": "البحرية الفرنسية",
    "American naval forces": "البحرية الأمريكية",
    "French naval forces": "البحرية الفرنسية",
    "American navy": "البحرية الأمريكية",
    "French navy": "البحرية الفرنسية",
    "British airways accidents and incidents": "حوادث الخطوط الجوية البريطانية",
    "American airways accidents and incidents": "حوادث الخطوط الجوية الأمريكية",
    "British airways": "الخطوط الجوية البريطانية",
    "American airways": "الخطوط الجوية الأمريكية",
    "French youth games": "الألعاب الفرنسية الشبابية",
    "Egyptian youth games": "الألعاب المصرية الشبابية",
    "American financial crisis": "الأزمة المالية الأمريكية",
    "Greek financial crisis": "الأزمة المالية اليونانية",
    "Egyptian presidential crisis": "الأزمة الرئاسية المصرية",
    "American presidential crisis": "الأزمة الرئاسية الأمريكية",
    "Egyptian military academy": "الأكاديمية العسكرية المصرية",
    "American military academy": "الأكاديمية العسكرية الأمريكية",
    "Egyptian military college": "الكلية العسكرية المصرية",
    "American military college": "الكلية العسكرية الأمريكية",
    "Greek crisis": "الأزمة اليونانية",
    "American crisis": "الأزمة الأمريكية",
    "American energy crisis": "أزمة الطاقة الأمريكية",
    "European energy crisis": "أزمة الطاقة الأوروبية",
    "American constitutional crisis": "الأزمة الدستورية الأمريكية",
    "Egyptian constitutional crisis": "الأزمة الدستورية المصرية",
    "French games competitors": "منافسون في الألعاب الفرنسية",
    "Egyptian games competitors": "منافسون في الألعاب المصرية",
    "American television people": "شخصيات التلفزة الأمريكية",
    "British television people": "شخصيات التلفزة البريطانية",
    "American presidential primaries": "الانتخابات الرئاسية التمهيدية الأمريكية",
    "French presidential primaries": "الانتخابات الرئاسية التمهيدية الفرنسية",
    "Egyptian legislative election": "الانتخابات التشريعية المصرية",
    "French legislative election": "الانتخابات التشريعية الفرنسية",
    "British parliamentary election": "الانتخابات البرلمانية البريطانية",
    "Egyptian parliamentary election": "الانتخابات البرلمانية المصرية",
    "American general election": "الانتخابات العامة الأمريكية",
    "British general election": "الانتخابات العامة البريطانية",
    "French presidential election": "انتخابات الرئاسة الفرنسية",
    "American presidential election": "انتخابات الرئاسة الأمريكية",
}


@pytest.mark.parametrize("category, expected", test_data_males.items(), ids=test_data_males.keys())
@pytest.mark.fast
def test_resolve_males(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_ar.items(), ids=test_data_ar.keys())
@pytest.mark.fast
def test_resolve_ar(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_the_male.items(), ids=test_data_the_male.keys())
@pytest.mark.fast
def test_resolve_the_male(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_male.items(), ids=test_data_male.keys())
@pytest.mark.fast
def test_resolve_male(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_female.items(), ids=test_data_female.keys())
@pytest.mark.fast
def test_resolve_female(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_the_female.items(), ids=test_data_the_female.keys())
@pytest.mark.fast
def test_resolve_the_female(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_males", test_data_males, resolve_by_nats),
    ("test_resolve_ar", test_data_ar, resolve_by_nats),
    ("test_resolve_the_male", test_data_the_male, resolve_by_nats),
    ("test_resolve_male", test_data_male, resolve_by_nats),
    ("test_resolve_female", test_data_female, resolve_by_nats),
    ("test_resolve_the_female", test_data_the_female, resolve_by_nats),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
