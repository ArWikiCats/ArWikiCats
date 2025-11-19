"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.te4_bots.for_me import Work_for_New_2018_men_Keys_with_all, Work_for_me, add_all


fast_data = {
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = add_all(category)
    assert label.strip() == expected


with_all_data = [
    {"cate": "african rugby union", "nat": "african", "con_3": "rugby union", "output": "اتحاد الرجبي الإفريقي"},
    {"cate": "american basketball league", "nat": "american", "con_3": "basketball league", "output": "الدوري الأمريكي لكرة السلة"},
    {"cate": "american football league", "nat": "american", "con_3": "football league", "output": "الدوري الأمريكي لكرة القدم"},
    {"cate": "american indoor soccer league", "nat": "american", "con_3": "indoor soccer league", "output": "الدوري الأمريكي لكرة القدم داخل الصالات"},
    {"cate": "american rugby league players", "nat": "american", "con_3": "rugby league players", "output": "لاعبو الدوري الأمريكي للرجبي"},
    {"cate": "american rugby union", "nat": "american", "con_3": "rugby union", "output": "اتحاد الرجبي الأمريكي"},
    {"cate": "arab league", "nat": "arab", "con_3": "league", "output": "الدوري العربي"},
    {"cate": "argentine army", "nat": "argentine", "con_3": "army", "output": "الجيش الأرجنتيني"},
    {"cate": "argentine military", "nat": "argentine", "con_3": "military", "output": "الجيش الأرجنتيني"},
    {"cate": "argentine rugby union", "nat": "argentine", "con_3": "rugby union", "output": "اتحاد الرجبي الأرجنتيني"},
    {"cate": "asian rugby union", "nat": "asian", "con_3": "rugby union", "output": "اتحاد الرجبي الآسيوي"},
    {"cate": "australian hockey league", "nat": "australian", "con_3": "hockey league", "output": "الدوري الأسترالي للهوكي"},
    {"cate": "australian involvement", "nat": "australian", "con_3": "involvement", "output": "التدخل الأسترالي"},
    {"cate": "australian rugby league players", "nat": "australian", "con_3": "rugby league players", "output": "لاعبو الدوري الأسترالي للرجبي"},
    {"cate": "australian rugby league", "nat": "australian", "con_3": "rugby league", "output": "الدوري الأسترالي للرجبي"},
    {"cate": "australian rugby union", "nat": "australian", "con_3": "rugby union", "output": "اتحاد الرجبي الأسترالي"},
    {"cate": "australian women's ice hockey league", "nat": "australian", "con_3": "women's ice hockey league", "output": "الدوري الأسترالي لهوكي الجليد للسيدات"},
    {"cate": "belgian hockey league", "nat": "belgian", "con_3": "hockey league", "output": "الدوري البلجيكي للهوكي"},
    {"cate": "belgian rugby union", "nat": "belgian", "con_3": "rugby union", "output": "اتحاد الرجبي البلجيكي"},
    {"cate": "beninese presidential pardons", "nat": "beninese", "con_3": "presidential pardons", "output": "العفو الرئاسي البنيني"},
    {"cate": "bohemian football league", "nat": "bohemian", "con_3": "football league", "output": "الدوري البوهيمي لكرة القدم"},
    {"cate": "bosnia and herzegovina hockey league", "nat": "bosnia and herzegovina", "con_3": "hockey league", "output": "الدوري البوسني للهوكي"},
    {"cate": "brazilian rugby league players", "nat": "brazilian", "con_3": "rugby league players", "output": "لاعبو الدوري البرازيلي للرجبي"},
    {"cate": "british army", "nat": "british", "con_3": "army", "output": "الجيش البريطاني"},
    {"cate": "british hockey league", "nat": "british", "con_3": "hockey league", "output": "الدوري البريطاني للهوكي"},
    {"cate": "british national party", "nat": "british", "con_3": "national party", "output": "الحزب الوطني البريطاني"},
    {"cate": "british rugby union", "nat": "british", "con_3": "rugby union", "output": "اتحاد الرجبي البريطاني"},
    {"cate": "canadian army", "nat": "canadian", "con_3": "army", "output": "الجيش الكندي"},
    {"cate": "canadian football league", "nat": "canadian", "con_3": "football league", "output": "الدوري الكندي لكرة القدم"},
    {"cate": "canadian military", "nat": "canadian", "con_3": "military", "output": "الجيش الكندي"},
    {"cate": "canadian premier league", "nat": "canadian", "con_3": "premier league", "output": "الدوري الكندي الممتاز"},
    {"cate": "canadian rugby union", "nat": "canadian", "con_3": "rugby union", "output": "اتحاد الرجبي الكندي"},
    {"cate": "canadian women's hockey league", "nat": "canadian", "con_3": "women's hockey league", "output": "الدوري الكندي للهوكي للسيدات"},
    {"cate": "celtic league", "nat": "celtic", "con_3": "league", "output": "الدوري الكلتي"},
    {"cate": "chinese football league", "nat": "chinese", "con_3": "football league", "output": "الدوري الصيني لكرة القدم"},
    {"cate": "chinese professional baseball league", "nat": "chinese", "con_3": "professional baseball league", "output": "دوري كرة القاعدة الصيني للمحترفين"},
    {"cate": "cuban league", "nat": "cuban", "con_3": "league", "output": "الدوري الكوبي"},
    {"cate": "czech military", "nat": "czech", "con_3": "military", "output": "الجيش التشيكي"},
    {"cate": "dominican professional baseball league", "nat": "dominican", "con_3": "professional baseball league", "output": "دوري كرة القاعدة الدومينيكي للمحترفين"},
    {"cate": "egyptian league", "nat": "egyptian", "con_3": "league", "output": "الدوري المصري"},
    {"cate": "egyptian military", "nat": "egyptian", "con_3": "military", "output": "الجيش المصري"},
    {"cate": "english football league", "nat": "english", "con_3": "football league", "output": "الدوري الإنجليزي لكرة القدم"},
    {"cate": "english rugby league players", "nat": "english", "con_3": "rugby league players", "output": "لاعبو الدوري الإنجليزي للرجبي"},
    {"cate": "english rugby league", "nat": "english", "con_3": "rugby league", "output": "الدوري الإنجليزي للرجبي"},
    {"cate": "english rugby union leagues", "nat": "english", "con_3": "rugby union leagues", "output": "اتحاد دوري الرجبي الإنجليزي"},
    {"cate": "english rugby union", "nat": "english", "con_3": "rugby union", "output": "اتحاد الرجبي الإنجليزي"},
    {"cate": "eritrean premier league", "nat": "eritrean", "con_3": "premier league", "output": "الدوري الإريتري الممتاز"},
    {"cate": "european league", "nat": "european", "con_3": "league", "output": "الدوري الأوروبي"},
    {"cate": "european rugby union leagues", "nat": "european", "con_3": "rugby union leagues", "output": "اتحاد دوري الرجبي الأوروبي"},
    {"cate": "european rugby union", "nat": "european", "con_3": "rugby union", "output": "اتحاد الرجبي الأوروبي"},
    {"cate": "european women's hockey league", "nat": "european", "con_3": "women's hockey league", "output": "الدوري الأوروبي للهوكي للسيدات"},
    {"cate": "european women's rugby union", "nat": "european", "con_3": "women's rugby union", "output": "اتحاد الرجبي الأوروبي للنساء"},
    {"cate": "fijian rugby union", "nat": "fijian", "con_3": "rugby union", "output": "اتحاد الرجبي الفيجي"},
    {"cate": "french military", "nat": "french", "con_3": "military", "output": "الجيش الفرنسي"},
    {"cate": "french rugby league", "nat": "french", "con_3": "rugby league", "output": "الدوري الفرنسي للرجبي"},
    {"cate": "french rugby union leagues", "nat": "french", "con_3": "rugby union leagues", "output": "اتحاد دوري الرجبي الفرنسي"},
    {"cate": "french rugby union", "nat": "french", "con_3": "rugby union", "output": "اتحاد الرجبي الفرنسي"},
    {"cate": "german army", "nat": "german", "con_3": "army", "output": "الجيش الألماني"},
    {"cate": "german family law", "nat": "german", "con_3": "family law", "output": "قانون الأسرة الألماني"},
    {"cate": "german football league", "nat": "german", "con_3": "football league", "output": "الدوري الألماني لكرة القدم"},
    {"cate": "german occupation", "nat": "german", "con_3": "occupation", "output": "الاحتلال الألماني"},
    {"cate": "german rugby league players", "nat": "german", "con_3": "rugby league players", "output": "لاعبو الدوري الألماني للرجبي"},
    {"cate": "german rugby union", "nat": "german", "con_3": "rugby union", "output": "اتحاد الرجبي الألماني"},
    {"cate": "hong kong fa cup", "nat": "hong kong", "con_3": "fa cup", "output": "كأس الاتحاد الهونغ الكونغي"},
    {"cate": "hong kong labour law", "nat": "hong kong", "con_3": "labour law", "output": "قانون العمل الهونغ الكونغي"},
    {"cate": "indian army", "nat": "indian", "con_3": "army", "output": "الجيش الهندي"},
    {"cate": "indian federation cup", "nat": "indian", "con_3": "federation cup", "output": "كأس الاتحاد الهندي"},
    {"cate": "indian premier league", "nat": "indian", "con_3": "premier league", "output": "الدوري الهندي الممتاز"},
    {"cate": "iranian futsal super league", "nat": "iranian", "con_3": "futsal super league", "output": "دوري السوبر كرة صالات الإيراني"},
    {"cate": "irish rugby union", "nat": "irish", "con_3": "rugby union", "output": "اتحاد الرجبي الأيرلندي"},
    {"cate": "israeli beach soccer league", "nat": "israeli", "con_3": "beach soccer league", "output": "الدوري الإسرائيلي لكرة القدم الشاطئية"},
    {"cate": "israeli futsal league", "nat": "israeli", "con_3": "futsal league", "output": "الدوري الإسرائيلي لكرة الصالات"},
    {"cate": "italian rugby union", "nat": "italian", "con_3": "rugby union", "output": "اتحاد الرجبي الإيطالي"},
    {"cate": "jamaican rugby league", "nat": "jamaican", "con_3": "rugby league", "output": "الدوري الجامايكي للرجبي"},
    {"cate": "japanese army", "nat": "japanese", "con_3": "army", "output": "الجيش الياباني"},
    {"cate": "japanese criminal law", "nat": "japanese", "con_3": "criminal law", "output": "القانون الجنائي الياباني"},
    {"cate": "japanese occupation", "nat": "japanese", "con_3": "occupation", "output": "الاحتلال الياباني"},
    {"cate": "japanese rugby union", "nat": "japanese", "con_3": "rugby union", "output": "اتحاد الرجبي الياباني"},
    {"cate": "jewish rugby league players", "nat": "jewish", "con_3": "rugby league players", "output": "لاعبو الدوري اليهودي للرجبي"},
    {"cate": "jordanian involvement", "nat": "jordanian", "con_3": "involvement", "output": "التدخل الأردني"},
    {"cate": "kenyan super cup", "nat": "kenyan", "con_3": "super cup", "output": "كأس السوبر الكيني"},
    {"cate": "lebanese federation cup", "nat": "lebanese", "con_3": "federation cup", "output": "كأس الاتحاد اللبناني"},
    {"cate": "lebanese involvement", "nat": "lebanese", "con_3": "involvement", "output": "التدخل اللبناني"},
    {"cate": "lebanese premier league", "nat": "lebanese", "con_3": "premier league", "output": "الدوري اللبناني الممتاز"},
    {"cate": "lithuanian women's handball league", "nat": "lithuanian", "con_3": "women's handball league", "output": "الدوري الليتواني لكرة اليد للسيدات"},
    {"cate": "malaysian army", "nat": "malaysian", "con_3": "army", "output": "الجيش الماليزي"},
    {"cate": "malaysian rugby union", "nat": "malaysian", "con_3": "rugby union", "output": "اتحاد الرجبي الماليزي"},
    {"cate": "maltese rugby league players", "nat": "maltese", "con_3": "rugby league players", "output": "لاعبو الدوري المالطي للرجبي"},
    {"cate": "mexican league", "nat": "mexican", "con_3": "league", "output": "الدوري المكسيكي"},
    {"cate": "mexican softball league players", "nat": "mexican", "con_3": "softball league players", "output": "لاعبو الدوري المكسيكي للكرة اللينة"},
    {"cate": "moroccan army", "nat": "moroccan", "con_3": "army", "output": "الجيش المغربي"},
    {"cate": "namibian labour law", "nat": "namibian", "con_3": "labour law", "output": "قانون العمل الناميبي"},
    {"cate": "nicaraguan professional baseball league", "nat": "nicaraguan", "con_3": "professional baseball league", "output": "دوري كرة القاعدة النيكاراغوي للمحترفين"},
    {"cate": "nigerian military", "nat": "nigerian", "con_3": "military", "output": "الجيش النيجيري"},
    {"cate": "north american football league", "nat": "north american", "con_3": "football league", "output": "الدوري الأمريكي الشمالي لكرة القدم"},
    {"cate": "north american hockey league", "nat": "north american", "con_3": "hockey league", "output": "الدوري الأمريكي الشمالي للهوكي"},
    {"cate": "north american rugby union", "nat": "north american", "con_3": "rugby union", "output": "اتحاد الرجبي الأمريكي الشمالي"},
    {"cate": "north american soccer league", "nat": "north american", "con_3": "soccer league", "output": "الدوري الأمريكي الشمالي لكرة القدم"},
    {"cate": "north korean pardons", "nat": "north korean", "con_3": "pardons", "output": "العفو الكوري الشمالي"},
    {"cate": "oceanian rugby union", "nat": "oceanian", "con_3": "rugby union", "output": "اتحاد الرجبي الأوقيانوسي"},
    {"cate": "pakistani criminal law", "nat": "pakistani", "con_3": "criminal law", "output": "القانون الجنائي الباكستاني"},
    {"cate": "palestinian solidarity movement", "nat": "palestinian", "con_3": "solidarity movement", "output": "حركة التضامن الفلسطيني"},
    {"cate": "peruvian army", "nat": "peruvian", "con_3": "army", "output": "الجيش البيروي"},
    {"cate": "romanian hockey league", "nat": "romanian", "con_3": "hockey league", "output": "الدوري الروماني للهوكي"},
    {"cate": "romanian military", "nat": "romanian", "con_3": "military", "output": "الجيش الروماني"},
    {"cate": "romanian rugby union", "nat": "romanian", "con_3": "rugby union", "output": "اتحاد الرجبي الروماني"},
    {"cate": "russian futsal super league", "nat": "russian", "con_3": "futsal super league", "output": "دوري السوبر كرة صالات الروسي"},
    {"cate": "russian invasion", "nat": "russian", "con_3": "invasion", "output": "الغزو الروسي"},
    {"cate": "russian presidential pardons", "nat": "russian", "con_3": "presidential pardons", "output": "العفو الرئاسي الروسي"},
    {"cate": "russian rugby union", "nat": "russian", "con_3": "rugby union", "output": "اتحاد الرجبي الروسي"},
    {"cate": "samoan rugby league", "nat": "samoan", "con_3": "rugby league", "output": "الدوري الساموي للرجبي"},
    {"cate": "samoan rugby union", "nat": "samoan", "con_3": "rugby union", "output": "اتحاد الرجبي الساموي"},
    {"cate": "saudi federation cup", "nat": "saudi", "con_3": "federation cup", "output": "كأس الاتحاد السعودي"},
    {"cate": "scottish football league", "nat": "scottish", "con_3": "football league", "output": "الدوري الإسكتلندي لكرة القدم"},
    {"cate": "scottish league", "nat": "scottish", "con_3": "league", "output": "الدوري الإسكتلندي"},
    {"cate": "scottish national party", "nat": "scottish", "con_3": "national party", "output": "الحزب الوطني الإسكتلندي"},
    {"cate": "scottish rugby union", "nat": "scottish", "con_3": "rugby union", "output": "اتحاد الرجبي الإسكتلندي"},
    {"cate": "singapore league", "nat": "singapore", "con_3": "league", "output": "الدوري السنغافوري"},
    {"cate": "slovenian ice hockey league", "nat": "slovenian", "con_3": "ice hockey league", "output": "الدوري السلوفيني لهوكي الجليد"},
    {"cate": "south african rugby union", "nat": "south african", "con_3": "rugby union", "output": "اتحاد الرجبي الجنوب الإفريقي"},
    {"cate": "south american rugby union", "nat": "south american", "con_3": "rugby union", "output": "اتحاد الرجبي الأمريكي الجنوبي"},
    {"cate": "south korean army", "nat": "south korean", "con_3": "army", "output": "الجيش الكوري الجنوبي"},
    {"cate": "soviet invasion", "nat": "soviet", "con_3": "invasion", "output": "الغزو السوفيتي"},
    {"cate": "spanish football league", "nat": "spanish", "con_3": "football league", "output": "الدوري الإسباني لكرة القدم"},
    {"cate": "spanish military", "nat": "spanish", "con_3": "military", "output": "الجيش الإسباني"},
    {"cate": "spanish rugby union leagues", "nat": "spanish", "con_3": "rugby union leagues", "output": "اتحاد دوري الرجبي الإسباني"},
    {"cate": "swedish hockey league", "nat": "swedish", "con_3": "hockey league", "output": "الدوري السويدي للهوكي"},
    {"cate": "swiss league", "nat": "swiss", "con_3": "league", "output": "الدوري السويسري"},
    {"cate": "tongan rugby union", "nat": "tongan", "con_3": "rugby union", "output": "اتحاد الرجبي التونغاني"},
    {"cate": "turkish army", "nat": "turkish", "con_3": "army", "output": "الجيش التركي"},
    {"cate": "turkish invasion", "nat": "turkish", "con_3": "invasion", "output": "الغزو التركي"},
    {"cate": "vanuatuan rugby league players", "nat": "vanuatuan", "con_3": "rugby league players", "output": "لاعبو الدوري الفانواتي للرجبي"},
    {"cate": "venezuelan professional baseball league", "nat": "venezuelan", "con_3": "professional baseball league", "output": "دوري كرة القاعدة الفنزويلي للمحترفين"},
    {"cate": "welsh football league", "nat": "welsh", "con_3": "football league", "output": "الدوري الويلزي لكرة القدم"},
    {"cate": "welsh rugby league", "nat": "welsh", "con_3": "rugby league", "output": "الدوري الويلزي للرجبي"},
    {"cate": "welsh rugby union", "nat": "welsh", "con_3": "rugby union", "output": "اتحاد الرجبي الويلزي"},
]


@pytest.mark.parametrize(
    "data",
    with_all_data,
    ids=lambda x: x["cate"]
)
@pytest.mark.fast
def test_work_for_new_2018_men_keys_with_all(data) -> None:

    label = Work_for_New_2018_men_Keys_with_all(data["cate"], data["nat"], data["con_3"])
    assert label == data["output"]


@pytest.mark.skip
def test_work_for_me():
    # Test with basic inputs using a valid country code
    result = Work_for_me("test category", "united states", "players")
    assert isinstance(result, str)

    result_empty = Work_for_me("", "", "")
    assert isinstance(result_empty, str)

    # Test with various inputs using valid country codes
    result_various = Work_for_me("sports", "france", "athletes")
    assert isinstance(result_various, str)


def test_add_all():
    # Test with a basic input
    result = add_all("test label")
    assert isinstance(result, str)
    assert "ال" in result  # The function adds "ال" prefix

    # Test with empty string
    result_empty = add_all("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = add_all("another label")
    assert isinstance(result_various, str)
