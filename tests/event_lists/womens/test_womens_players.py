#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data_1 = {
    # "Category:Fenerbahçe women's basketball players": "تصنيف:لاعبات فنربخشة لكرة السلة للسيدات",
}

data_2 = {
    "Category:Women's England Hockey League players": "تصنيف:لاعبات الدوري الإنجليزي للهوكي للسيدات",
    "Category:2022 Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات 2022",
    "Category:2023 FIFA Women's World Cup players": "تصنيف:لاعبات كأس العالم لكرة القدم للسيدات 2023",
    "Category:2024 Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات 2024",
    "Category:Armenian women's volleyball players": "تصنيف:لاعبات كرة طائرة أرمنيات",
    "Category:Association football players by women's under-20 national team": "تصنيف:لاعبات كرة قدم حسب المنتخب الوطني للسيدات تحت 20 سنة",
    "Category:Association football players by women's under-21 national team": "تصنيف:لاعبات كرة قدم حسب المنتخب الوطني للسيدات تحت 21 سنة",
    "Category:Association football players by women's under-23 national team": "تصنيف:لاعبات كرة قدم حسب المنتخب الوطني للسيدات تحت 23 سنة",
    "Category:Basketball players by women's national team": "تصنيف:لاعبات كرة سلة حسب منتخب السيدات الوطني",
    "Category:Canada women's national basketball team players": "تصنيف:لاعبات منتخب كندا لكرة السلة للسيدات",
    "Category:Chinese Taipei women's national basketball team players": "تصنيف:لاعبات منتخب تايبيه الصينية لكرة السلة للسيدات",
    "Category:Colombian women's volleyball players": "تصنيف:لاعبات كرة طائرة كولومبيات",
    "Category:European Women's Hockey League players": "تصنيف:لاعبات الدوري الأوروبي للهوكي للسيدات",
    "Category:Expatriate women's futsal players in Kuwait": "تصنيف:لاعبات كرة صالات مغتربات في الكويت",
    "Category:Expatriate women's futsal players in the Maldives": "تصنيف:لاعبات كرة صالات مغتربات في جزر المالديف",
    "Category:Female handball players in Turkey by club": "تصنيف:لاعبات كرة يد في تركيا حسب النادي",
    "Category:Galatasaray S.K. (women's basketball) players": "تصنيف:لاعبات نادي غلطة سراي لكرة السلة للسيدات",
    "Category:Handball players by women's national team": "تصنيف:لاعبات كرة يد حسب منتخب السيدات الوطني",
    "Category:Ireland women's national basketball team players": "تصنيف:لاعبات منتخب أيرلندا لكرة السلة للسيدات",
    "Category:Ireland women's national basketball team": "تصنيف:منتخب أيرلندا لكرة السلة للسيدات",
    "Category:Ireland women's national field hockey team coaches": "تصنيف:مدربو منتخب أيرلندا لهوكي الميدان للسيدات",
    "Category:Ireland women's national field hockey team": "تصنيف:منتخب أيرلندا لهوكي الميدان للسيدات",
    "Category:Ireland women's national rugby sevens team": "تصنيف:منتخب أيرلندا لسباعيات الرجبي للسيدات",
    "Category:Ireland women's national rugby union team coaches": "تصنيف:مدربو منتخب أيرلندا لاتحاد الرجبي للسيدات",
    "Category:Ireland women's national rugby union team": "تصنيف:منتخب أيرلندا لاتحاد الرجبي للسيدات",
    "Category:Israeli women's basketball players": "تصنيف:لاعبات كرة سلة إسرائيليات",
    "Category:Italian women's futsal players": "تصنيف:لاعبات كرة صالات إيطاليات",
    "Category:Kyrgyzstani women's basketball players": "تصنيف:لاعبات كرة سلة قيرغيزستانيات",
    "Category:Kyrgyzstani women's volleyball players": "تصنيف:لاعبات كرة طائرة قيرغيزستانيات",
    "Category:New Zealand women's national rugby league team players": "تصنيف:لاعبات منتخب نيوزيلندا لدوري الرجبي للسيدات",
    "Category:Northern Ireland women's national football team": "تصنيف:منتخب أيرلندا الشمالية لكرة القدم للسيدات",
    "Category:Northern Ireland women's national football teams": "تصنيف:منتخبات كرة قدم وطنية أيرلندية شمالية للسيدات",
    "Category:Republic of Ireland association football leagues": "تصنيف:دوريات كرة القدم الأيرلندية",
    "Category:Republic of Ireland women's association football": "تصنيف:كرة قدم أيرلندية للسيدات",
    "Category:Republic of Ireland women's association footballers": "تصنيف:لاعبات كرة قدم أيرلنديات",
    "Category:Republic of Ireland women's international footballers": "تصنيف:لاعبات كرة قدم دوليات أيرلنديات",
    "Category:Republic of Ireland women's international rugby union players": "تصنيف:لاعبات اتحاد رجبي دوليات من جمهورية أيرلندا",
    "Category:Republic of Ireland women's national football team managers": "تصنيف:مدربو منتخب جمهورية أيرلندا لكرة القدم للسيدات",
    "Category:Republic of Ireland women's national football team navigational boxes": "تصنيف:صناديق تصفح منتخب جمهورية أيرلندا لكرة القدم للسيدات",
    "Category:Republic of Ireland women's national football team": "تصنيف:منتخب جمهورية أيرلندا لكرة القدم للسيدات",
    "Category:Republic of Ireland women's national football teams": "تصنيف:منتخبات كرة قدم وطنية أيرلندية للسيدات",
    "Category:Republic of Ireland women's youth international footballers": "تصنيف:لاعبات منتخب جمهورية أيرلندا لكرة القدم للشابات",
    "Category:Rugby league players by women's national team": "تصنيف:لاعبات دوري رجبي حسب منتخب السيدات الوطني",
    "Category:Rugby union players by women's national team": "تصنيف:لاعبات اتحاد رجبي حسب منتخب السيدات الوطني",
    "Category:Scottish women's basketball players": "تصنيف:لاعبات كرة سلة إسكتلنديات",
    "Category:Surinamese women's basketball players": "تصنيف:لاعبات كرة سلة سوريناميات",
    "Category:Turkey women's national basketball team players": "تصنيف:لاعبات منتخب تركيا لكرة السلة للسيدات",
    "Category:UEFA Women's Euro 2017 players": "تصنيف:لاعبات بطولة أمم أوروبا لكرة القدم للسيدات 2017",
    "Category:UEFA Women's Euro 2022 players": "تصنيف:لاعبات بطولة أمم أوروبا لكرة القدم للسيدات 2022",
    "Category:UEFA Women's Euro 2025 players": "تصنيف:لاعبات بطولة أمم أوروبا لكرة القدم للسيدات 2025",
    "Category:Victorian Women's Football League players": "تصنيف:لاعبات الدوري الفيكتوري لكرة القدم للسيدات",
    "Category:Volleyball players by women's national team": "تصنيف:لاعبات كرة طائرة حسب منتخب السيدات الوطني",
    "Category:Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات",
    "Category:Women's basketball players in the United States by league": "تصنيف:لاعبات كرة سلة في الولايات المتحدة حسب الدوري",
    "Category:Women's Chinese Basketball Association players": "تصنيف:لاعبات الرابطة الصينية لكرة السلة للسيدات",
    "Category:Women's field hockey players in England": "تصنيف:لاعبات هوكي ميدان في إنجلترا",
    "Category:Women's field hockey players in Ireland": "تصنيف:لاعبات هوكي ميدان في أيرلندا",
    "Category:Women's futsal players in Kuwait": "تصنيف:لاعبات كرة صالات في الكويت",
    "Category:Women's futsal players in the Maldives": "تصنيف:لاعبات كرة صالات في جزر المالديف",
    "Category:Women's handball players": "تصنيف:لاعبات كرة يد",
    "Category:Women's hockey players": "تصنيف:لاعبات هوكي",
    "Category:Women's Irish Hockey League players": "تصنيف:لاعبات الدوري الأيرلندي للهوكي للسيدات",
    "Category:Women's Korean Basketball League players": "تصنيف:لاعبات الدوري الكوري لكرة السلة للسيدات",
    "Category:Women's lacrosse players": "تصنيف:لاعبات لاكروس",
    "Category:Women's National Basketball Association players from Belgium": "تصنيف:لاعبات الاتحاد الوطني لكرة السلة للسيدات من بلجيكا",
    "Category:Women's National Basketball Association players from Croatia": "تصنيف:لاعبات الاتحاد الوطني لكرة السلة للسيدات من كرواتيا",
    "Category:Women's National Basketball Association players from Serbia": "تصنيف:لاعبات الاتحاد الوطني لكرة السلة للسيدات من صربيا",
    "Category:Women's National Basketball Association players": "تصنيف:لاعبات الاتحاد الوطني لكرة السلة للسيدات",
    "Category:Women's National Basketball League players": "تصنيف:لاعبات الدوري الوطني لكرة السلة للسيدات",
    "Category:Women's National Basketball League teams": "تصنيف:فرق الدوري الوطني لكرة السلة للسيدات",
    "Category:Women's National Basketball League": "تصنيف:الدوري الوطني لكرة السلة للسيدات",
    "Category:Women's soccer players in Australia by competition": "تصنيف:لاعبات كرة قدم في أستراليا حسب المنافسة",
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
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    # dump_diff_text(expected, diff_result, name)

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
