import pytest

from ArWikiCats.new_resolvers.sports_resolvers.sport_lab_nat import sport_lab_nat_load_new
from utils.dump_runner import make_dump_test_name_data

new_for_nat_female_xo_team_2_data = {
    "yemeni": "",
    "trinidad and tobago amateur basketball cup": "كأس ترنيدادية كرة سلة للهواة",
    "trinidad and tobago youth basketball cup": "كأس ترنيدادية كرة سلة للشباب",
    "trinidad and tobago mens basketball cup": "كأس ترنيدادية كرة سلة للرجال",
    "trinidad and tobago womens basketball cup": "كأس ترنيدادية كرة سلة للسيدات",
    "trinidad and tobago defunct basketball cup": "كؤوس كرة سلة ترنيدادية سابقة",
    "trinidad and tobago basketball cup": "كؤوس كرة سلة ترنيدادية",
    "trinidad and tobago domestic basketball cup": "كؤوس كرة سلة ترنيدادية محلية",
    # "yemeni football": "كرة قدم يمنية",
    # "new zealand basketball": "كرة سلة نيوزيلندية",  # Category:American_basketball
    "yemeni national football": "كرة قدم وطنية يمنية",
    "new zealand national basketball": "كرة سلة وطنية نيوزيلندية",
    "new zealand basketball teams": "فرق كرة سلة نيوزيلندية",
    "new zealand basketball national teams": "منتخبات كرة سلة نيوزيلندية",
    "new zealand domestic basketball": "كرة سلة نيوزيلندية محلية",
    "new zealand basketball championships": "بطولات كرة سلة نيوزيلندية",
    "new zealand national basketball championships": "بطولات كرة سلة وطنية نيوزيلندية",
    "new zealand national basketball champions": "أبطال كرة سلة وطنية نيوزيلندية",
    "trinidad and tobago basketball super leagues": "دوريات سوبر كرة سلة ترنيدادية",
    "trinidad and tobago womens basketball": "كرة سلة ترنيدادية نسائية",
    "trinidad and tobago current basketball seasons": "مواسم كرة سلة ترنيدادية حالية",
    # ---
    "trinidad and tobago professional basketball": "كرة سلة ترنيدادية للمحترفين",
    "trinidad and tobago domestic womens basketball": "كرة سلة ترنيدادية محلية للسيدات",
    "trinidad and tobago indoor basketball": "كرة سلة ترنيدادية داخل الصالات",
    "trinidad and tobago outdoor basketball": "كرة سلة ترنيدادية في الهواء الطلق",
    "trinidad and tobago defunct indoor basketball": "كرة سلة ترنيدادية داخل الصالات سابقة",
    "trinidad and tobago defunct outdoor basketball": "كرة سلة ترنيدادية في الهواء الطلق سابقة",
    "trinidad and tobago reserve basketball": "كرة سلة ترنيدادية احتياطية",
    "trinidad and tobago defunct basketball": "كرة سلة ترنيدادية سابقة",
    # tab[Category:Canadian domestic Soccer: "تصنيف:كرة قدم كندية محلية"
    # [european national womens volleyball teams] = "منتخبات كرة طائرة وطنية أوروبية للسيدات"
    "trinidad and tobago national womens basketball teams": "منتخبات كرة سلة وطنية ترنيدادية للسيدات",
    "trinidad and tobago national basketball teams": "منتخبات كرة سلة وطنية ترنيدادية",
    "trinidad and tobago national a basketball teams": "منتخبات كرة سلة محليين ترنيدادية",
    "trinidad and tobago national b basketball teams": "منتخبات كرة سلة رديفة ترنيدادية",
    "trinidad and tobago national reserve basketball teams": "منتخبات كرة سلة وطنية احتياطية ترنيدادية",
}

end_key_mappings_data = {
    # "yemeni football finals": "نهائيات كرة قدم يمنية",
    # "yemeni football": "كرة قدم يمنية",
    "yemeni national football": "كرة قدم وطنية يمنية",
    "yemeni national football home stadiums": "ملاعب كرة قدم وطنية يمنية",
    "yemeni national football teams fifth tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الخامسة",
    "yemeni national football teams first tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الأولى",
    "yemeni national football teams fourth tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الرابعة",
    "yemeni national football teams premier": "منتخبات كرة قدم وطنية يمنية من الدرجة الممتازة",
    "yemeni national football teams second tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الثانية",
    "yemeni national football teams seventh tier": "منتخبات كرة قدم وطنية يمنية من الدرجة السابعة",
    "yemeni national football teams sixth tier": "منتخبات كرة قدم وطنية يمنية من الدرجة السادسة",
    "yemeni national football teams third tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الثالثة",
    "yemeni national football teams top tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الأولى",
    "yemeni football teams fifth tier": "فرق كرة قدم يمنية من الدرجة الخامسة",
    "yemeni football teams first tier": "فرق كرة قدم يمنية من الدرجة الأولى",
    "yemeni football teams fourth tier": "فرق كرة قدم يمنية من الدرجة الرابعة",
    "yemeni football teams premier": "فرق كرة قدم يمنية من الدرجة الممتازة",
    "yemeni football teams second tier": "فرق كرة قدم يمنية من الدرجة الثانية",
    "yemeni football teams seventh tier": "فرق كرة قدم يمنية من الدرجة السابعة",
    "yemeni football teams sixth tier": "فرق كرة قدم يمنية من الدرجة السادسة",
    "yemeni football teams third tier": "فرق كرة قدم يمنية من الدرجة الثالثة",
    "yemeni football teams top tier": "فرق كرة قدم يمنية من الدرجة الأولى",
}

additional_keys_data = {
    "yemeni national amateur under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة للهواة",
    "yemeni national amateur under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة للهواة",
    "yemeni national amateur under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة للهواة",
    "yemeni national amateur under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة للهواة",
    "yemeni national amateur under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة للهواة",
    "yemeni national amateur under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة للهواة",
    "yemeni national amateur under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة للهواة",
    "yemeni national amateur under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة للهواة",
    "yemeni national amateur under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة للهواة",
    "yemeni national amateur under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة للهواة",
    "yemeni national amateur under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة للهواة",
    "yemeni national amateur basketball teams": "منتخبات كرة سلة وطنية يمنية للهواة",
    "yemeni national junior mens under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة للناشئين",
    "yemeni national junior mens under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة للناشئين",
    "yemeni national junior mens under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة للناشئين",
    "yemeni national junior mens under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة للناشئين",
    "yemeni national junior mens under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة للناشئين",
    "yemeni national junior mens under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة للناشئين",
    "yemeni national junior mens under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة للناشئين",
    "yemeni national junior mens under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة للناشئين",
    "yemeni national junior mens under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة للناشئين",
    "yemeni national junior mens under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة للناشئين",
    "yemeni national junior mens under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة للناشئين",
    "yemeni national junior mens basketball teams": "منتخبات كرة سلة وطنية يمنية للناشئين",
    "yemeni national junior womens under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة للناشئات",
    "yemeni national junior womens under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة للناشئات",
    "yemeni national junior womens under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة للناشئات",
    "yemeni national junior womens under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة للناشئات",
    "yemeni national junior womens under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة للناشئات",
    "yemeni national junior womens under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة للناشئات",
    "yemeni national junior womens under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة للناشئات",
    "yemeni national junior womens under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة للناشئات",
    "yemeni national junior womens under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة للناشئات",
    "yemeni national junior womens under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة للناشئات",
    "yemeni national junior womens under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة للناشئات",
    "yemeni national junior womens basketball teams": "منتخبات كرة سلة وطنية يمنية للناشئات",
    "yemeni national mens under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة للرجال",
    "yemeni national mens under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة للرجال",
    "yemeni national mens under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة للرجال",
    "yemeni national mens under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة للرجال",
    "yemeni national mens under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة للرجال",
    "yemeni national mens under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة للرجال",
    "yemeni national mens under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة للرجال",
    "yemeni national mens under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة للرجال",
    "yemeni national mens under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة للرجال",
    "yemeni national mens under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة للرجال",
    "yemeni national mens under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة للرجال",
    "yemeni national mens basketball teams": "منتخبات كرة سلة وطنية يمنية للرجال",
    "yemeni national under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة",
    "yemeni national under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة",
    "yemeni national under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة",
    "yemeni national under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة",
    "yemeni national under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة",
    "yemeni national under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة",
    "yemeni national under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة",
    "yemeni national under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة",
    "yemeni national under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة",
    "yemeni national under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة",
    "yemeni national under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة",
    "yemeni national womens under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة للسيدات",
    "yemeni national womens under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة للسيدات",
    "yemeni national womens under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة للسيدات",
    "yemeni national womens under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة للسيدات",
    "yemeni national womens under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة للسيدات",
    "yemeni national womens under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة للسيدات",
    "yemeni national womens under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة للسيدات",
    "yemeni national womens under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة للسيدات",
    "yemeni national womens under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة للسيدات",
    "yemeni national womens under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة للسيدات",
    "yemeni national womens under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة للسيدات",
    "yemeni national womens basketball teams": "منتخبات كرة سلة وطنية يمنية للسيدات",
    "yemeni national youth under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة للشباب",
    "yemeni national youth under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة للشباب",
    "yemeni national youth under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة للشباب",
    "yemeni national youth under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة للشباب",
    "yemeni national youth under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة للشباب",
    "yemeni national youth under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة للشباب",
    "yemeni national youth under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة للشباب",
    "yemeni national youth under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة للشباب",
    "yemeni national youth under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة للشباب",
    "yemeni national youth under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة للشباب",
    "yemeni national youth under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة للشباب",
    "yemeni national youth womens under-13 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 13 سنة للشابات",
    "yemeni national youth womens under-14 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 14 سنة للشابات",
    "yemeni national youth womens under-15 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 15 سنة للشابات",
    "yemeni national youth womens under-16 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 16 سنة للشابات",
    "yemeni national youth womens under-17 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 17 سنة للشابات",
    "yemeni national youth womens under-18 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 18 سنة للشابات",
    "yemeni national youth womens under-19 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 19 سنة للشابات",
    "yemeni national youth womens under-20 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 20 سنة للشابات",
    "yemeni national youth womens under-21 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 21 سنة للشابات",
    "yemeni national youth womens under-23 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 23 سنة للشابات",
    "yemeni national youth womens under-24 basketball teams": "منتخبات كرة سلة وطنية يمنية تحت 24 سنة للشابات",
    "yemeni national youth womens basketball teams": "منتخبات كرة سلة وطنية يمنية للشابات",
    "yemeni national youth basketball teams": "منتخبات كرة سلة وطنية يمنية للشباب",
    "yemeni under-13 basketball": "كرة سلة يمنية تحت 13 سنة",
    "yemeni under-14 basketball": "كرة سلة يمنية تحت 14 سنة",
    "yemeni under-15 basketball": "كرة سلة يمنية تحت 15 سنة",
    "yemeni under-16 basketball": "كرة سلة يمنية تحت 16 سنة",
    "yemeni under-17 basketball": "كرة سلة يمنية تحت 17 سنة",
    "yemeni under-18 basketball": "كرة سلة يمنية تحت 18 سنة",
    "yemeni under-19 basketball": "كرة سلة يمنية تحت 19 سنة",
    "yemeni under-20 basketball": "كرة سلة يمنية تحت 20 سنة",
    "yemeni under-21 basketball": "كرة سلة يمنية تحت 21 سنة",
    "yemeni under-23 basketball": "كرة سلة يمنية تحت 23 سنة",
    "yemeni under-24 basketball": "كرة سلة يمنية تحت 24 سنة",
}


@pytest.mark.parametrize(
    "key,expected", new_for_nat_female_xo_team_2_data.items(), ids=new_for_nat_female_xo_team_2_data.keys()
)
@pytest.mark.unit
def test_new_for_nat_female_xo_team_2_data(key: str, expected: str) -> None:
    result2 = sport_lab_nat_load_new(key)
    assert result2 == expected


@pytest.mark.parametrize("key,expected", end_key_mappings_data.items(), ids=end_key_mappings_data.keys())
@pytest.mark.unit
def test_end_key_mappings_data(key: str, expected: str) -> None:
    result2 = sport_lab_nat_load_new(key)
    assert result2 == expected


@pytest.mark.parametrize("key,expected", additional_keys_data.items(), ids=additional_keys_data.keys())
@pytest.mark.unit
def test_additional_keys_data(key: str, expected: str) -> None:
    result2 = sport_lab_nat_load_new(key)
    assert result2 == expected


to_test = [
    ("test_new_for_nat_female_xo_team_2_data", new_for_nat_female_xo_team_2_data),
    ("test_end_key_mappings_data", end_key_mappings_data),
    ("test_additional_keys_data", additional_keys_data),
]


test_dump_all = make_dump_test_name_data(to_test, sport_lab_nat_load_new, run_same=False)
