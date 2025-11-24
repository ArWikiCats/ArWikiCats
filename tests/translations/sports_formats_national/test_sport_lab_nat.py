import pytest

from src.translations.sports_formats_national.sport_lab_nat import (
    Get_sport_formts_female_nat,
    sport_lab_nat_load,
)

data = {
    "under-13 baseball teams": "فرق كرة قاعدة {nat} تحت 13 سنة",
    "women's ice hockey": "هوكي جليد {nat} نسائية",
    "women's football": "كرة قدم {nat} نسائية",
    "football leagues": "دوريات كرة قدم {nat}",
    "football teams": "فرق كرة قدم {nat}",
    "basketball": "كرة سلة {nat}",
    "ice hockey leagues": "دوريات هوكي جليد {nat}",
    "ice hockey": "هوكي جليد {nat}",
    "football cups": "كؤوس كرة قدم {nat}",
    "cricket": "كريكت {nat}",
    "football chairmen and investors": "رؤساء ومسيرو كرة قدم {nat}",
    "swimming championships": "بطولات سباحة {nat}",
    "auto racing teams": "فرق سباق سيارات {nat}",
    "basketball leagues": "دوريات كرة سلة {nat}",
    "rugby union chairmen and investors": "رؤساء ومسيرو اتحاد رجبي {nat}",
    "domestic football cups": "كؤوس كرة قدم {nat} محلية",
    "national rugby union teams": "منتخبات اتحاد رجبي وطنية {nat}",
    "second tier ice hockey leagues": "دوريات هوكي جليد {nat} من الدرجة الثانية",
    "soccer leagues": "دوريات كرة قدم {nat}",
    "football competitions": "منافسات كرة قدم {nat}",
    "professional wrestling teams": "فرق مصارعة محترفين {nat}",
    "skiing": "تزلج {nat}",
    "handball": "كرة يد {nat}",
    "second tier basketball leagues": "دوريات كرة سلة {nat} من الدرجة الثانية",
    "table tennis championships": "بطولات كرة طاولة {nat}",
    "women's soccer": "كرة قدم {nat} نسائية",
    "athletics": "ألعاب قوى {nat}",
    "futsal": "كرة صالات {nat}",
    "women's cricket": "كريكت {nat} نسائية",
    "college": "كليات {nat}",
    "national youth football teams": "منتخبات كرة قدم وطنية {nat} للشباب",
    "women's sports": "رياضية {nat} نسائية",
    "national women's under-17 football teams": "منتخبات كرة قدم وطنية {nat} تحت 17 سنة للسيدات",
    "athletics championships": "بطولات ألعاب قوى {nat}",
    "speed skating championships": "بطولات تزلج سريع {nat}",
    "women's basketball": "كرة سلة {nat} نسائية",
    "artistic gymnastics championships": "بطولات جمباز فني {nat}",
    "football clubs": "أندية كرة قدم {nat}",
    "national football teams": "منتخبات كرة قدم وطنية {nat}",
    "skiing competitions": "منافسات تزلج {nat}",
    "volleyball championships": "بطولات كرة طائرة {nat}",
    "field hockey": "هوكي ميدان {nat}",
    "curling": "كيرلنغ {nat}",
    "handball competitions": "منافسات كرة يد {nat}",
    "futsal leagues": "دوريات كرة صالات {nat}",
    "national women's futsal teams": "منتخبات كرة صالات وطنية {nat} للسيدات",
    "rugby league competitions": "منافسات دوري رجبي {nat}",
    "national women's rugby union teams": "منتخبات اتحاد رجبي وطنية {nat} للسيدات",
    "water polo": "كرة ماء {nat}",
    "figure skating championships": "بطولات تزلج فني {nat}",
    "domestic cricket": "كريكت {nat} محلية",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_Get_sport_formts_female_nat(key, expected) -> None:
    template_label = Get_sport_formts_female_nat(key)
    assert template_label == expected


data2 = {
    "Yemeni under-13 baseball teams": "فرق كرة قاعدة يمنية تحت 13 سنة",
    "Canadian women's ice hockey": "هوكي جليد كندية نسائية",
    "samoan women's football": "كرة قدم ساموية نسائية",
    "indian basketball": "كرة سلة هندية",
}


@pytest.mark.parametrize("key,expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_sport_lab_nat_load(key, expected) -> None:
    result = sport_lab_nat_load(key)
    assert result == expected
