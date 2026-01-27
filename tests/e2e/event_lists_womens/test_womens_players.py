#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_1 = {
    # "Fenerbahçe women's basketball players": "لاعبات فنربخشة لكرة السلة للسيدات",
}

data_2 = {
    "Women's England Hockey League players": "لاعبات الدوري الإنجليزي للهوكي للسيدات",
    "2022 Women's Africa Cup of Nations players": "لاعبات كأس الأمم الإفريقية للسيدات 2022",
    "2023 FIFA Women's World Cup players": "لاعبات كأس العالم لكرة القدم للسيدات 2023",
    "2024 Women's Africa Cup of Nations players": "لاعبات كأس الأمم الإفريقية للسيدات 2024",
    "Armenian women's volleyball players": "لاعبات كرة طائرة أرمنيات",
    "Association football players by women's under-20 national team": "لاعبات كرة قدم حسب المنتخب الوطني للسيدات تحت 20 سنة",
    "Association football players by women's under-21 national team": "لاعبات كرة قدم حسب المنتخب الوطني للسيدات تحت 21 سنة",
    "Association football players by women's under-23 national team": "لاعبات كرة قدم حسب المنتخب الوطني للسيدات تحت 23 سنة",
    "Basketball players by women's national team": "لاعبات كرة سلة حسب منتخب السيدات الوطني",
    "Canada women's national basketball team players": "لاعبات منتخب كندا لكرة السلة للسيدات",
    "Chinese Taipei women's national basketball team players": "لاعبات منتخب تايبيه الصينية لكرة السلة للسيدات",
    "Colombian women's volleyball players": "لاعبات كرة طائرة كولومبيات",
    "European Women's Hockey League players": "لاعبات الدوري الأوروبي للهوكي للسيدات",
    "Expatriate women's futsal players in Kuwait": "لاعبات كرة صالات مغتربات في الكويت",
    "Expatriate women's futsal players in the Maldives": "لاعبات كرة صالات مغتربات في جزر المالديف",
    "Female handball players in Turkey by club": "لاعبات كرة يد في تركيا حسب النادي",
    "Galatasaray S.K. (women's basketball) players": "لاعبات نادي غلطة سراي لكرة السلة للسيدات",
    "Handball players by women's national team": "لاعبات كرة يد حسب منتخب السيدات الوطني",
    "Ireland women's national basketball team players": "لاعبات منتخب أيرلندا لكرة السلة للسيدات",
    "Ireland women's national basketball team": "منتخب أيرلندا لكرة السلة للسيدات",
    "Ireland women's national field hockey team coaches": "مدربو منتخب أيرلندا لهوكي الميدان للسيدات",
    "Ireland women's national field hockey team": "منتخب أيرلندا لهوكي الميدان للسيدات",
    "Ireland women's national rugby sevens team": "منتخب أيرلندا لسباعيات الرجبي للسيدات",
    "Ireland women's national rugby union team coaches": "مدربو منتخب أيرلندا لاتحاد الرجبي للسيدات",
    "Ireland women's national rugby union team": "منتخب أيرلندا لاتحاد الرجبي للسيدات",
    "Israeli women's basketball players": "لاعبات كرة سلة إسرائيليات",
    "Italian women's futsal players": "لاعبات كرة صالات إيطاليات",
    "Kyrgyzstani women's basketball players": "لاعبات كرة سلة قيرغيزستانيات",
    "Kyrgyzstani women's volleyball players": "لاعبات كرة طائرة قيرغيزستانيات",
    "New Zealand women's national rugby league team players": "لاعبات منتخب نيوزيلندا لدوري الرجبي للسيدات",
    "Northern Ireland women's national football team": "منتخب أيرلندا الشمالية لكرة القدم للسيدات",
    "Northern Ireland women's national football teams": "منتخبات كرة قدم وطنية أيرلندية شمالية للسيدات",
    "Republic of Ireland association football leagues": "دوريات كرة القدم الأيرلندية",
    "Republic of Ireland women's association football": "كرة قدم أيرلندية للسيدات",
    "Republic of Ireland women's association footballers": "لاعبات كرة قدم أيرلنديات",
    "Republic of Ireland women's international footballers": "لاعبات كرة قدم دوليات أيرلنديات",
    "Republic of Ireland women's international rugby union players": "لاعبات اتحاد رجبي دوليات من جمهورية أيرلندا",
    "Republic of Ireland women's national football team managers": "مدربو منتخب جمهورية أيرلندا لكرة القدم للسيدات",
    "Republic of Ireland women's national football team navigational boxes": "صناديق تصفح منتخب جمهورية أيرلندا لكرة القدم للسيدات",
    "Republic of Ireland women's national football team": "منتخب جمهورية أيرلندا لكرة القدم للسيدات",
    "Republic of Ireland women's national football teams": "منتخبات كرة قدم وطنية أيرلندية للسيدات",
    "Republic of Ireland women's youth international footballers": "لاعبات منتخب جمهورية أيرلندا لكرة القدم للشابات",
    "Rugby league players by women's national team": "لاعبات دوري رجبي حسب منتخب السيدات الوطني",
    "Rugby union players by women's national team": "لاعبات اتحاد رجبي حسب منتخب السيدات الوطني",
    "Scottish women's basketball players": "لاعبات كرة سلة إسكتلنديات",
    "Surinamese women's basketball players": "لاعبات كرة سلة سوريناميات",
    "Turkey women's national basketball team players": "لاعبات منتخب تركيا لكرة السلة للسيدات",
    "UEFA Women's Euro 2017 players": "لاعبات بطولة أمم أوروبا لكرة القدم للسيدات 2017",
    "UEFA Women's Euro 2022 players": "لاعبات بطولة أمم أوروبا لكرة القدم للسيدات 2022",
    "UEFA Women's Euro 2025 players": "لاعبات بطولة أمم أوروبا لكرة القدم للسيدات 2025",
    "Victorian Women's Football League players": "لاعبات الدوري الفيكتوري لكرة القدم للسيدات",
    "Volleyball players by women's national team": "لاعبات كرة طائرة حسب منتخب السيدات الوطني",
    "Women's Africa Cup of Nations players": "لاعبات كأس الأمم الإفريقية للسيدات",
    "Women's basketball players in the United States by league": "لاعبات كرة سلة في الولايات المتحدة حسب الدوري",
    "Women's Chinese Basketball Association players": "لاعبات الرابطة الصينية لكرة السلة للسيدات",
    "Women's field hockey players in England": "لاعبات هوكي ميدان في إنجلترا",
    "Women's field hockey players in Ireland": "لاعبات هوكي ميدان في أيرلندا",
    "Women's futsal players in Kuwait": "لاعبات كرة صالات في الكويت",
    "Women's futsal players in the Maldives": "لاعبات كرة صالات في جزر المالديف",
    "Women's handball players": "لاعبات كرة يد",
    "Women's hockey players": "لاعبات هوكي",
    "Women's Irish Hockey League players": "لاعبات الدوري الأيرلندي للهوكي للسيدات",
    "Women's Korean Basketball League players": "لاعبات الدوري الكوري لكرة السلة للسيدات",
    "Women's lacrosse players": "لاعبات لاكروس",
    "Women's National Basketball Association players from Belgium": "لاعبات الاتحاد الوطني لكرة السلة للسيدات من بلجيكا",
    "Women's National Basketball Association players from Croatia": "لاعبات الاتحاد الوطني لكرة السلة للسيدات من كرواتيا",
    "Women's National Basketball Association players from Serbia": "لاعبات الاتحاد الوطني لكرة السلة للسيدات من صربيا",
    "Women's National Basketball Association players": "لاعبات الاتحاد الوطني لكرة السلة للسيدات",
    "Women's National Basketball League players": "لاعبات الدوري الوطني لكرة السلة للسيدات",
    "Women's National Basketball League teams": "فرق الدوري الوطني لكرة السلة للسيدات",
    "Women's National Basketball League": "الدوري الوطني لكرة السلة للسيدات",
    "Women's soccer players in Australia by competition": "لاعبات كرة قدم في أستراليا حسب المنافسة",
}
data_3 = {}
data_4 = {}

to_test = [
    ("test_womens_players_1", data_1),
    ("test_womens_players_2", data_2),
    ("test_womens_players_3", data_3),
    ("test_womens_ireland_4", data_4),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_womens_players_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
