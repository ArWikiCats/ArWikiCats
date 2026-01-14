""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar as Work_for_me_main
# from ArWikiCats.old_bots.for_me import Work_for_me_main

data0 = {
    "10th-century Christian texts": "نصوص مسيحية في القرن 10",
    "11th-century Christian texts": "نصوص مسيحية في القرن 11",
    "12th-century Christian texts": "نصوص مسيحية في القرن 12",
    "13th-century Christian texts": "نصوص مسيحية في القرن 13",
    "13th-century Jewish texts": "نصوص يهودية في القرن 13",
    "14th-century Christian texts": "نصوص مسيحية في القرن 14",
    "15th-century Christian texts": "نصوص مسيحية في القرن 15",
    "16th-century Christian texts": "نصوص مسيحية في القرن 16",
    "17th-century Christian texts": "نصوص مسيحية في القرن 17",
    "18th-century Christian texts": "نصوص مسيحية في القرن 18",
    "19th-century Christian texts": "نصوص مسيحية في القرن 19",
    "1st-century Christian texts": "نصوص مسيحية في القرن 1",
    "1st-millennium Christian texts": "نصوص مسيحية في الألفية 1",
    "2006 in Northern Ireland sport": "رياضة أيرلندية شمالية في 2006",
    "20th-century Christian texts": "نصوص مسيحية في القرن 20",
    "21st-century Christian texts": "نصوص مسيحية في القرن 21",
    "2nd-century Christian texts": "نصوص مسيحية في القرن 2",
    "2nd-millennium Christian texts": "نصوص مسيحية في الألفية 2",
    "3rd-century Christian texts": "نصوص مسيحية في القرن 3",
    "3rd-millennium Christian texts": "نصوص مسيحية في الألفية 3",
    "4th-century Christian texts": "نصوص مسيحية في القرن 4",
    "5th-century Christian texts": "نصوص مسيحية في القرن 5",
    "6th-century Christian texts": "نصوص مسيحية في القرن 6",
    "7th-century Christian texts": "نصوص مسيحية في القرن 7",
    "8th-century Christian texts": "نصوص مسيحية في القرن 8",
    "9th-century Christian texts": "نصوص مسيحية في القرن 9",
    "american christian metal musical groups": "فرق موسيقى ميتال مسيحي أمريكية",
    "american christian rock groups": "فرق روك مسيحي أمريكية",
    "american country music groups": "فرق كانتري أمريكية",
    "american doom metal musical groups": "فرق موسيقى دوم ميتال أمريكية",
    "american international schools": "مدارس دولية أمريكية",
    "american rock music groups": "فرق موسيقى الروك أمريكية",
    "Arab Christian communities in Israel": "مجتمعات مسيحية عربية في إسرائيل",
    "arab christian communities": "مجتمعات مسيحية عربية",
    "armenian world music groups": "فرق موسيقى العالم أرمينية",
    "australian black metal musical groups": "فرق موسيقى بلاك ميتال أسترالية",
    "australian christian metal musical groups": "فرق موسيقى ميتال مسيحي أسترالية",
    "australian christian rock groups": "فرق روك مسيحي أسترالية",
    "australian electronic dance music groups": "فرق موسيقى الرقص الإلكترونية أسترالية",
    "australian musicals": "مسرحيات غنائية أسترالية",
    "australian world music groups": "فرق موسيقى العالم أسترالية",
    "azerbaijani heavy metal musical groups": "فرق موسيقى هيفي ميتال أذربيجانية",
    "belgian children's books": "كتب أطفال بلجيكية",
    "bengali hindu festivals": "مهرجانات هندوسية بنغالية",
    "brazilian christian metal musical groups": "فرق موسيقى ميتال مسيحي برازيلية",
    "brazilian christian rock groups": "فرق روك مسيحي برازيلية",
    "british black metal musical groups": "فرق موسيقى بلاك ميتال بريطانية",
    "british christian rock groups": "فرق روك مسيحي بريطانية",
    "british international schools": "مدارس دولية بريطانية",
    "canadian christian metal musical groups": "فرق موسيقى ميتال مسيحي كندية",
    "canadian christian rock groups": "فرق روك مسيحي كندية",
    "canadian contemporary r&b musical groups": "فرق موسيقى آر أند بي معاصر كندية",
    "canadian documentaries": "وثائقيات كندية",
    "chinese cookbooks": "كتب طبخ صينية",
    "chinese hip hop groups": "فرق هيب هوب صينية",
    "chinese hip-hop groups": "فرق هيب هوب صينية",
    "christian alternative metal groups": "فرق ميتال بديل مسيحية",
    "christian bibliographies": "ببليوجرافيات مسيحية",
    "christian children's books": "كتب أطفال مسيحية",
    "christian children's magazines": "مجلات أطفال مسيحية",
    "christian conferences": "مؤتمرات مسيحية",
    "christian contemporary r&b groups": "فرق آر أند بي معاصر مسيحية",
    "christian hip hop groups": "فرق هيب هوب مسيحية",
    "Christian hip-hop groups": "فرق هيب هوب مسيحية",
    "christian illuminated manuscripts": "مخطوطات مذهبة مسيحية",
    "christian manuscripts": "مخطوطات مسيحية",
    "christian metal musical groups": "فرق موسيقى ميتال مسيحية",
    "christian music awards": "جوائز موسيقى مسيحية",
    "christian new religious movements": "حركات دينية جديدة مسيحية",
    "christian paintings": "لوحات مسيحية",
    "Christian political parties by country": "أحزاب سياسية مسيحية حسب البلد",
    "Christian political parties in Australia": "أحزاب سياسية مسيحية في أستراليا",
    "Christian political parties in Canada": "أحزاب سياسية مسيحية في كندا",
    "Christian political parties in Germany": "أحزاب سياسية مسيحية في ألمانيا",
    "Christian political parties in Hungary": "أحزاب سياسية مسيحية في المجر",
    "Christian political parties in Lebanon": "أحزاب سياسية مسيحية في لبنان",
    "Christian political parties in Montenegro": "أحزاب سياسية مسيحية في الجبل الأسود",
    "Christian political parties in New Zealand": "أحزاب سياسية مسيحية في نيوزيلندا",
    "Christian political parties in Papua New Guinea": "أحزاب سياسية مسيحية في بابوا غينيا الجديدة",
    "Christian political parties in Poland": "أحزاب سياسية مسيحية في بولندا",
    "Christian political parties in Quebec": "أحزاب سياسية مسيحية في كيبك",
    "Christian political parties in South Africa": "أحزاب سياسية مسيحية في جنوب إفريقيا",
    "Christian political parties in Ukraine": "أحزاب سياسية مسيحية في أوكرانيا",
    "Christian political parties in United Kingdom": "أحزاب سياسية مسيحية في المملكة المتحدة",
    "Christian political parties in United States": "أحزاب سياسية مسيحية في الولايات المتحدة",
    "christian political parties": "أحزاب سياسية مسيحية",
    "christian pop groups": "فرق بوب مسيحية",
    "Christian religious orders by century of establishment": "أخويات دينية مسيحية حسب قرن التأسيس",
    "Christian religious orders established in 11th century": "أخويات دينية مسيحية أسست في القرن 11",
    "Christian religious orders established in 12th century": "أخويات دينية مسيحية أسست في القرن 12",
    "Christian religious orders established in 13th century": "أخويات دينية مسيحية أسست في القرن 13",
    "Christian religious orders established in 14th century": "أخويات دينية مسيحية أسست في القرن 14",
    "Christian religious orders established in 15th century": "أخويات دينية مسيحية أسست في القرن 15",
    "Christian religious orders established in 16th century": "أخويات دينية مسيحية أسست في القرن 16",
    "Christian religious orders established in 17th century": "أخويات دينية مسيحية أسست في القرن 17",
    "Christian religious orders established in 18th century": "أخويات دينية مسيحية أسست في القرن 18",
    "Christian religious orders established in 19th century": "أخويات دينية مسيحية أسست في القرن 19",
    "Christian religious orders established in 20th century": "أخويات دينية مسيحية أسست في القرن 20",
    "Christian religious orders established in 21st century": "أخويات دينية مسيحية أسست في القرن 21",
    "Christian religious orders established in 5th century": "أخويات دينية مسيحية أسست في القرن 5",
    "Christian religious orders established in 6th century": "أخويات دينية مسيحية أسست في القرن 6",
    "christian religious orders": "أخويات دينية مسيحية",
    "christian rhythm and blues groups": "فرق ريذم أند بلوز مسيحية",
    "christian ska groups": "فرق سكا مسيحية",
    "christian socialist organizations": "منظمات اشتراكية مسيحية",
    "Christian texts by century": "نصوص مسيحية حسب القرن",
    "Christian texts by genre": "نصوص مسيحية حسب النوع الفني",
    "Christian texts by medium": "نصوص مسيحية حسب الوسط",
    "Christian texts by millennium": "نصوص مسيحية حسب الألفية",
    "Christian texts by period": "نصوص مسيحية حسب الحقبة",
    "christian texts": "نصوص مسيحية",
    "czech rock music groups": "فرق موسيقى الروك تشيكية",
    "czech thrash metal musical groups": "فرق موسيقى ثراش ميتال تشيكية",
    "english christian rock groups": "فرق روك مسيحي إنجليزية",
    "English tennis commentators": "معلقو كرة مضرب إنجليزية",
    "european political websites": "مواقع ويب سياسية أوروبية",
    "finnish christian metal musical groups": "فرق موسيقى ميتال مسيحي فنلندية",
    "french comic": "قصص مصورة فرنسية",
    "french gothic metal musical groups": "فرق موسيقى غوثيك ميتال فرنسية",
    "german christian metal musical groups": "فرق موسيقى ميتال مسيحي ألمانية",
    "greek organized crime": "جريمة منظمة يونانية",
    "greek paintings": "لوحات يونانية",
    "icelandic pop music groups": "فرق موسيقى بوب آيسلندية",
    "indian funk musical groups": "فرق موسيقى فانك هندية",
    "indonesian online encyclopedias": "موسوعات إنترنت إندونيسية",
    "indonesian rock music groups": "فرق موسيقى الروك إندونيسية",
    "iranian indie rock groups": "فرق إيندي روك إيرانية",
    "iranian paintings": "لوحات إيرانية",
    "irish paintings": "لوحات أيرلندية",
    "israeli architecture awards": "جوائز عمارة إسرائيلية",
    "italian black metal musical groups": "فرق موسيقى بلاك ميتال إيطالية",
    "japanese indie pop groups": "فرق إيندي بوب يابانية",
    "jewish children's magazines": "مجلات أطفال يهودية",
    "jewish ethnic groups": "مجموعات عرقية يهودية",
    "Jewish feminist organizations in United States": "منظمات نسوية يهودية في الولايات المتحدة",
    "jewish feminist organizations": "منظمات نسوية يهودية",
    "jewish folk rock groups": "فرق فولك روك يهودية",
    "jewish hip hop groups": "فرق هيب هوب يهودية",
    "Jewish hip-hop groups": "فرق هيب هوب يهودية",
    "jewish illuminated manuscripts": "مخطوطات مذهبة يهودية",
    "jewish manuscripts": "مخطوطات يهودية",
    "jewish medical organizations": "منظمات طبية يهودية",
    "jewish military units and formations": "وحدات وتشكيلات عسكرية يهودية",
    "jewish new religious movements": "حركات دينية جديدة يهودية",
    "jewish political movements": "حركات سياسية يهودية",
    "jewish political parties": "أحزاب سياسية يهودية",
    "jewish religious movements": "حركات دينية يهودية",
    "jewish rock groups": "فرق روك يهودية",
    "Jewish texts by century": "نصوص يهودية حسب القرن",
    "jewish texts": "نصوص يهودية",
    "korean international schools": "مدارس دولية كورية",
    "malagasy world music groups": "فرق موسيقى العالم مدغشقرية",
    "mauritian folk music groups": "فرق موسيقى تقليدية موريشيوسية",
    "Members of Christian religious orders": "أعضاء أخويات دينية مسيحية",
    "mexican blues musical groups": "فرق موسيقى بلوز مكسيكية",
    "norwegian christian metal musical groups": "فرق موسيقى ميتال مسيحي نرويجية",
    "norwegian folk music groups": "فرق موسيقى تقليدية نرويجية",
    "palestinian christian communities": "مجتمعات مسيحية فلسطينية",
    "palestinian political parties": "أحزاب سياسية فلسطينية",
    "polish biographical dictionaries": "قواميس سير ذاتية بولندية",
    "Politicians of Christian political parties": "سياسيون من أحزاب سياسية مسيحية",
    "Politicians of Jewish political parties": "سياسيون من أحزاب سياسية يهودية",
    "portuguese international schools": "مدارس دولية برتغالية",
    "salvadoran reggae musical groups": "فرق موسيقى ريغيه سلفادورية",
    "saudiarabian black metal musical groups": "فرق موسيقى بلاك ميتال سعودية",
    "serbian cultural organizations": "منظمات ثقافية صربية",
    "serbian reggae musical groups": "فرق موسيقى ريغيه صربية",
    "slovak eurodance groups": "فرق يورودانس سلوفاكية",
    "slovenian rock music groups": "فرق موسيقى الروك سلوفينية",
    "sri lankan heavy metal musical groups": "فرق موسيقى هيفي ميتال سريلانكية",
    "swedish christian metal musical groups": "فرق موسيقى ميتال مسيحي سويدية",
    "Swedish heavy metal musical groups by genre": "فرق موسيقى هيفي ميتال سويدية حسب النوع الفني",
    "swedish heavy metal musical groups": "فرق موسيقى هيفي ميتال سويدية",
    "swedish ska groups": "فرق سكا سويدية",
    "swiss christian metal musical groups": "فرق موسيقى ميتال مسيحي سويسرية",
    "syrian rock music groups": "فرق موسيقى الروك سورية",
    "tajikistani rock music groups": "فرق موسيقى الروك طاجيكستانية",
    "thai buddhist temples": "معابد بوذية تايلندية",
    "turkish cookbooks": "كتب طبخ تركية",
}

data_2018 = {
    "christian events": "أحداث مسيحية",
    "christian political organizations": "منظمات سياسية مسيحية",
    "christian rock groups": "فرق روك مسيحية",
    "jewish history organizations": "منظمات تاريخ يهودية",
    "jewish political organizations": "منظمات سياسية يهودية",
    "jewish religious organizations": "منظمات دينية يهودية",
    "Kurdish Islamic organisations": "منظمات إسلامية كردية",
    "kurdish islamic organizations": "منظمات إسلامية كردية",

}


@pytest.mark.parametrize("category, expected_key", data0.items(), ids=data0.keys())
@pytest.mark.skip2
def test_Work_for_data0(category: str, expected_key: str) -> None:
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
    ("test_Work_for_data0", data0),
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
