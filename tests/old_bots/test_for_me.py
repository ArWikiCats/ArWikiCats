""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar as Work_for_me_main
# from ArWikiCats.old_bots.for_me import Work_for_me_main

data_1 = {
    "american country music groups": "فرق كانتري أمريكية",
    "american doom metal musical groups": "فرق موسيقى دوم ميتال أمريكية",
    "american rock music groups": "فرق موسيقى الروك أمريكية",
    "slovak eurodance groups": "فرق يورودانس سلوفاكية",
    "swedish ska groups": "فرق سكا سويدية",
    "jewish folk rock groups": "فرق فولك روك يهودية",
    "japanese indie pop groups": "فرق إيندي بوب يابانية",
    "iranian indie rock groups": "فرق إيندي روك إيرانية",
    "chinese hip hop groups": "فرق هيب هوب صينية",
    "chinese hip-hop groups": "فرق هيب هوب صينية",
    "jewish hip hop groups": "فرق هيب هوب يهودية",
    "Jewish hip-hop groups": "فرق هيب هوب يهودية",
    "armenian world music groups": "فرق موسيقى العالم أرمينية",
    "australian black metal musical groups": "فرق موسيقى بلاك ميتال أسترالية",
    "australian electronic dance music groups": "فرق موسيقى الرقص الإلكترونية أسترالية",
    "australian musicals": "مسرحيات غنائية أسترالية",
    "australian world music groups": "فرق موسيقى العالم أسترالية",
    "azerbaijani heavy metal musical groups": "فرق موسيقى هيفي ميتال أذربيجانية",
    "british black metal musical groups": "فرق موسيقى بلاك ميتال بريطانية",
    "canadian contemporary r&b musical groups": "فرق موسيقى آر أند بي معاصر كندية",
    "czech rock music groups": "فرق موسيقى الروك تشيكية",
    "czech thrash metal musical groups": "فرق موسيقى ثراش ميتال تشيكية",
    "french gothic metal musical groups": "فرق موسيقى غوثيك ميتال فرنسية",
    "icelandic pop music groups": "فرق موسيقى بوب آيسلندية",
    "indian funk musical groups": "فرق موسيقى فانك هندية",
    "indonesian rock music groups": "فرق موسيقى الروك إندونيسية",
    "italian black metal musical groups": "فرق موسيقى بلاك ميتال إيطالية",
    "malagasy world music groups": "فرق موسيقى العالم مدغشقرية",
    "mauritian folk music groups": "فرق موسيقى تقليدية موريشيوسية",
    "mexican blues musical groups": "فرق موسيقى بلوز مكسيكية",
    "norwegian folk music groups": "فرق موسيقى تقليدية نرويجية",
    "salvadoran reggae musical groups": "فرق موسيقى ريغيه سلفادورية",
    "saudiarabian black metal musical groups": "فرق موسيقى بلاك ميتال سعودية",
    "serbian reggae musical groups": "فرق موسيقى ريغيه صربية",
    "slovenian rock music groups": "فرق موسيقى الروك سلوفينية",
    "sri lankan heavy metal musical groups": "فرق موسيقى هيفي ميتال سريلانكية",
    "Swedish heavy metal musical groups by genre": "فرق موسيقى هيفي ميتال سويدية حسب النوع الفني",
    "swedish heavy metal musical groups": "فرق موسيقى هيفي ميتال سويدية",
    "syrian rock music groups": "فرق موسيقى الروك سورية",
    "tajikistani rock music groups": "فرق موسيقى الروك طاجيكستانية",
}

data_2 = {
    "christian alternative metal groups": "فرق ميتال بديل مسيحية",
    "christian bibliographies": "ببليوجرافيات مسيحية",
    "christian conferences": "مؤتمرات مسيحية",
    "christian contemporary r&b groups": "فرق آر أند بي معاصر مسيحية",
    "christian metal musical groups": "فرق موسيقى ميتال مسيحية",
    "christian music awards": "جوائز موسيقى مسيحية",
    "christian pop groups": "فرق بوب مسيحية",
    "christian rhythm and blues groups": "فرق ريذم أند بلوز مسيحية",
    "christian socialist organizations": "منظمات اشتراكية مسيحية"
}

data_2018 = {
    "american christian metal musical groups": "فرق موسيقى ميتال مسيحي أمريكية",
    "american christian rock groups": "فرق روك مسيحي أمريكية",
    "arab christian communities": "مجتمعات مسيحية عربية",
    "australian christian metal musical groups": "فرق موسيقى ميتال مسيحي أسترالية",
    "australian christian rock groups": "فرق روك مسيحي أسترالية",
    "brazilian christian metal musical groups": "فرق موسيقى ميتال مسيحي برازيلية",
    "brazilian christian rock groups": "فرق روك مسيحي برازيلية",
    "british christian rock groups": "فرق روك مسيحي بريطانية",
    "canadian christian metal musical groups": "فرق موسيقى ميتال مسيحي كندية",
    "canadian christian rock groups": "فرق روك مسيحي كندية",
    "english christian rock groups": "فرق روك مسيحي إنجليزية",
    "finnish christian metal musical groups": "فرق موسيقى ميتال مسيحي فنلندية",
    "german christian metal musical groups": "فرق موسيقى ميتال مسيحي ألمانية",
    "norwegian christian metal musical groups": "فرق موسيقى ميتال مسيحي نرويجية",
    "palestinian christian communities": "مجتمعات مسيحية فلسطينية",
    "swedish christian metal musical groups": "فرق موسيقى ميتال مسيحي سويدية",
    "swiss christian metal musical groups": "فرق موسيقى ميتال مسيحي سويسرية",
}


@pytest.mark.parametrize("category, expected_key", data_1.items(), ids=data_1.keys())
@pytest.mark.skip2
def test_Work_for_data1(category: str, expected_key: str) -> None:
    """
    Verify that Work_for_me_main produces the expected Arabic label for a given category string.

    Parameters:
        category (str): The input category or phrase to resolve.
        expected_key (str): The expected Arabic label string to compare against.
    """
    label1 = Work_for_me_main(category)
    assert label1 == expected_key


@pytest.mark.parametrize("category, expected_key", data_2018.items(), ids=data_2018.keys())
@pytest.mark.skip2
def test_Work_for_data_2018(category: str, expected_key: str) -> None:
    label1 = Work_for_me_main(category)
    assert label1 == expected_key


to_test = [
    ("test_Work_for_data1", data_1),
    ("test_Work_for_data2", data_2),
    ("test_Work_for_data_2018", data_2018),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    """
    """
    expected, diff_result = one_dump_test(data, Work_for_me_main)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
