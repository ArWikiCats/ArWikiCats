"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_v2 import resolve_by_countries_names_v2

test_data = {
    "bahamas royal defence force": "قوات الدفاع الملكية البهامية",
    # -------------------------
    # government officials (males)
    # -------------------------
    "united states government officials": "مسؤولون حكوميون أمريكيون",
    "morocco government officials": "مسؤولون حكوميون مغاربة",
    "vanuatu government officials": "مسؤولون حكوميون فانواتيون",
    "vatican government officials": "مسؤولون حكوميون فاتيكانيون",
    "venezuela government officials": "مسؤولون حكوميون فنزويليون",
    "victoria-australia government officials": "مسؤولون حكوميون فيكتوريون",
    "vietnam government officials": "مسؤولون حكوميون فيتناميون",
    "wales government officials": "مسؤولون حكوميون ويلزيون",
    "west germany government officials": "مسؤولون حكوميون ألمانيون غربيون",
    "west india government officials": "مسؤولون حكوميون هنود غربيون",
    "western asia government officials": "مسؤولون حكوميون آسيويون غربيون",
    "western canada government officials": "مسؤولون حكوميون كنديون غربيون",
    "western sahara government officials": "مسؤولون حكوميون صحراويون",
    "yemen government officials": "مسؤولون حكوميون يمنيون",
    "yoruba government officials": "مسؤولون حكوميون يوروبيون",
    "yugoslavia government officials": "مسؤولون حكوميون يوغسلافيون",
    "zaire government officials": "مسؤولون حكوميون زائيريون",
    "zambia government officials": "مسؤولون حكوميون زامبيون",
    "zanzibar government officials": "مسؤولون حكوميون زنجباريون",
    "zimbabwe government officials": "مسؤولون حكوميون زيمبابويون",
    "zulu people government officials": "مسؤولون حكوميون زولو",
    # -------------------------
    # air force (women + article)
    # -------------------------
    "united states air force": "القوات الجوية الأمريكية",
    "new zealand royal air force": "القوات الجوية الملكية النيوزيلندية",
    "china air force": "القوات الجوية الصينية",
    "sri lanka air force": "القوات الجوية السريلانكية",
    "netherlands royal air force": "القوات الجوية الملكية الهولندية",
    "korea air force": "القوات الجوية الكورية",
    "vanuatu air force": "القوات الجوية الفانواتية",
    "vatican air force": "القوات الجوية الفاتيكانية",
    "venezuela air force": "القوات الجوية الفنزويلية",
    "victoria-australia air force": "القوات الجوية الفكتورية",
    "vietnam air force": "القوات الجوية الفيتنامية",
    "wales air force": "القوات الجوية الويلزية",
    "west germany air force": "القوات الجوية الألمانية الغربية",
    "west india air force": "القوات الجوية الهندية الغربية",
    "western asia air force": "القوات الجوية الآسيوية الغربية",
    "western canada air force": "القوات الجوية الكندية الغربية",
    "western sahara air force": "القوات الجوية الصحراوية",
    "yemen air force": "القوات الجوية اليمنية",
    "yoruba air force": "القوات الجوية اليوروبية",
    "yugoslavia air force": "القوات الجوية اليوغسلافية",
    "zaire air force": "القوات الجوية الزائيرية",
    "zambia air force": "القوات الجوية الزامبية",
    "zanzibar air force": "القوات الجوية الزنجبارية",
    "zimbabwe air force": "القوات الجوية الزيمبابوية",
    "zulu people air force": "القوات الجوية الزولية",
    # -------------------------
    # naval force / naval forces / navy / royal navy
    # كلها من قوالب النساء → تحتاج مؤنث + ال
    # -------------------------
    "united states navy": "البحرية الأمريكية",
    "china navy": "البحرية الصينية",
    "pakistan navy": "البحرية الباكستانية",
    "korea navy": "البحرية الكورية",
    "new zealand royal navy": "البحرية الملكية النيوزيلندية",
    "netherlands royal navy": "البحرية الملكية الهولندية",
    "iran navy": "البحرية الإيرانية",
    "sri lanka navy": "البحرية السريلانكية",
    "south yemen navy": "البحرية اليمنية الجنوبية",
    "japan navy": "البحرية اليابانية",
    "united arab emirates navy": "البحرية الإماراتية",
    "benin navy": "البحرية البنينية",
    "cyprus navy": "البحرية القبرصية",
    "brunei royal navy": "البحرية الملكية البرونية",
    "vietnam navy": "البحرية الفيتنامية",
    "yemen navy": "البحرية اليمنية",
    "venezuela navy": "البحرية الفنزويلية",
    "zambia naval force": "البحرية الزامبية",
    "zambia naval forces": "البحرية الزامبية",
    "west germany royal navy": "البحرية الملكية الألمانية الغربية",
    "western sahara navy": "البحرية الصحراوية",
    "yugoslavia naval force": "البحرية اليوغسلافية",
    "zimbabwe naval forces": "البحرية الزيمبابوية",
    # -------------------------
    # civil war (women + إضافة “ال”)
    # -------------------------
    "north yemen civil war": "الحرب الأهلية اليمنية الشمالية",
    "sierra leone civil war": "الحرب الأهلية السيراليونية",
    "myanmar civil war": "الحرب الأهلية الميانمارية",
    "yemen civil war": "الحرب الأهلية اليمنية",
    "vietnam civil war": "الحرب الأهلية الفيتنامية",
    "venezuela civil war": "الحرب الأهلية الفنزويلية",
    "western sahara civil war": "الحرب الأهلية الصحراوية",
    "zimbabwe civil war": "الحرب الأهلية الزيمبابوية",
}


@pytest.mark.parametrize("category, expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_get_p17_2(category: str, expected: str) -> None:
    label = resolve_by_countries_names_v2(category)
    assert label == expected
