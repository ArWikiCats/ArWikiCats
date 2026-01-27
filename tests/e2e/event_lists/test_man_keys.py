""" """

import pytest

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
    "japanese folklore": "فلكور ياباني",
    "iraqi diaspora": "شتات عراقي",
    "hungarian diaspora": "شتات مجري",
    "finnish descent": "أصل فنلندي",
    "coptic calendar": "تقويم قبطي",
    "croatian diaspora": "شتات كرواتي",
    "chilean law": "قانون تشيلي",
    "austrian descent": "أصل نمساوي",
    "north korean literature": "أدب كوري شمالي",
    "german literature": "أدب ألماني",
    "russian literature": "أدب روسي",
    "indian literature": "أدب هندي",
}


@pytest.mark.parametrize("category, expected_key", data_n.items(), ids=data_n.keys())
@pytest.mark.fast
def test_data_n(category: str, expected_key: str) -> None:
    label1 = resolve_label_ar(category)
    assert label1 == expected_key
