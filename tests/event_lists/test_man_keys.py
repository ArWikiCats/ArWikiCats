""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar

data_n = {
    "brazilian design": "تصميم برازيلي",
    "british descent": "أصل بريطاني",
    "burkinabe design": "تصميم بوركينابي",
    "cypriot descent": "أصل قبرصي",
    "dutch diaspora": "شتات هولندي",
    "ecuadorian descent": "أصل إكوادوري",
    "filipino descent": "أصل فلبيني",
    "french descent": "أصل فرنسي",
    "greek descent": "أصل يوناني",
    "guatemalan diaspora": "شتات غواتيمالي",
    "hong kong descent": "أصل هونغ كونغي",
    "icelandic descent": "أصل آيسلندي",
    "indian descent": "أصل هندي",
    "indian literature": "أدب هندي",
    "iraqi descent": "أصل عراقي",
    "irish folklore": "فلكور أيرلندي",
    "japanese descent": "أصل ياباني",
    "kazakhstani descent": "أصل كازاخستاني",
    "kurdish folklore": "فلكور كردي",
    "lithuanian art": "فن ليتواني",
    "maldivian descent": "أصل مالديفي",
    "montserratian descent": "أصل مونتسراتي",
    "ossetian diaspora": "شتات أوسيتي",
    "pakistani descent": "أصل باكستاني",
    "pakistani law": "قانون باكستاني",
    "russian literature": "أدب روسي",
    "singaporean art": "فن سنغافوري",
    "singaporean descent": "أصل سنغافوري",
    "south american descent": "أصل أمريكي جنوبي",
    "spanish diaspora": "شتات إسباني",
    "tamil diaspora": "شتات تاميلي",
    "thai diaspora": "شتات تايلندي",
    "ukrainian diaspora": "شتات أوكراني",
    "welsh descent": "أصل ويلزي",
    "yemeni descent": "أصل يمني",
    "yoruba descent": "أصل يوروبي",
    "yugoslav descent": "أصل يوغسلافي",
    "zimbabwean descent": "أصل زيمبابوي",
    "zulu history": "تاريخ زولي",
    "ukrainian descent": "أصل أوكراني",
    "samoan diaspora": "شتات ساموي",
    "peruvian descent": "أصل بيروي",
    "ossetian descent": "أصل أوسيتي",
    "north korean literature": "أدب كوري شمالي",
    "japanese folklore": "فلكور ياباني",
    "iraqi diaspora": "شتات عراقي",
    "hungarian diaspora": "شتات مجري",
    "german literature": "أدب ألماني",
    "finnish descent": "أصل فنلندي",
    "coptic calendar": "تقويم قبطي",
    "croatian diaspora": "شتات كرواتي",
    "chilean law": "قانون تشيلي",
    "austrian descent": "أصل نمساوي",
    "Category:20th-century Ghanaian literature": "أدب غاني القرن 20",
    "Category:20th-century Mexican literature": "أدب مكسيكي القرن 20",
    "Category:20th-century Taiwanese literature": "أدب تايواني القرن 20",
    "Category:20th-century Zimbabwean literature": "أدب زيمبابوي القرن 20",
    "Category:21st-century Ghanaian literature": "أدب غاني القرن 21",
    "Category:21st-century Moroccan literature": "أدب مغربي القرن 21",
    "Category:21st-century Taiwanese literature": "أدب تايواني القرن 21",
    "Category:21st-century Zimbabwean literature": "أدب زيمبابوي القرن 21"
}


@pytest.mark.parametrize("category, expected_key", data_n.items(), ids=data_n.keys())
@pytest.mark.fast
def test_data_n(category: str, expected_key: str) -> None:
    label1 = resolve_label_ar(category)
    assert label1 == expected_key
