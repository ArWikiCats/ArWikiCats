#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_diff_text

from ArWikiCats import resolve_arabic_category_label

data_1 = {
    "Category:2019 FIFA Women's World Cup players": "تصنيف:لاعبو كأس العالم للسيدات 2019",
    "Category:Rugby league players by women's national team": "تصنيف:لاعبو دوري رغبي حسب منتخب السيدات الوطني",
    "Category:Rugby union players by women's national team": "تصنيف:لاعبو اتحاد رغبي حسب منتخب السيدات الوطني",
    "Category:UEFA Women's Euro 2017 players": "تصنيف:لاعبو بطولة أمم أوروبا للسيدات 2017",
    "Category:Volleyball players by women's national team": "تصنيف:لاعبو كرة طائرة حسب المنتخب الوطني للنساء",
    "Category:Women's Chinese Basketball Association players": "تصنيف:لاعبو الدوري الصيني لكرة السلة للسيدات",
    "Category:Fenerbahçe women's basketball players": "تصنيف:لاعبو نادي فنربخشة لكرة السلة للسيدات",
}
data_2 = {
    "Category:2022 Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس إفريقيا نسائية في بلدان 2022",
    "Category:2023 FIFA Women's World Cup players": "تصنيف:لاعبو كأس العالم لكرة القدم للسيدات 2023",
    "Category:2024 Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس الأمم الإفريقية نسائية 2024",
    "Category:Armenian women's volleyball players": "تصنيف:لاعبو كرة طائرة أرمينية نسائية",
    "Category:Association football players by women's under-20 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للسيدات تحت 20 سنة",
    "Category:Association football players by women's under-21 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للسيدات تحت 21 سنة",
    "Category:Association football players by women's under-23 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للسيدات تحت 23 سنة",
    "Category:Basketball players by women's national team": "تصنيف:لاعبو كرة سلة حسب منتخب السيدات الوطني",
    "Category:Canada women's national basketball team players": "تصنيف:لاعبو منتخب كندا الوطني لكرة السلة للسيدات",
    "Category:Chinese Taipei women's national basketball team players": "تصنيف:لاعبو منتخب تايبيه الصينية لكرة السلة للسيدات",
    "Category:Colombian women's volleyball players": "تصنيف:لاعبو كرة طائرة كولومبية نسائية",
    "Category:European Women's Hockey League players": "تصنيف:لاعبو الدوري الأوروبي للهوكي للسيدات",
    "Category:Expatriate women's futsal players in Kuwait": "تصنيف:لاعبو كرة صالات للسيدات مغتربون في الكويت",
    "Category:Expatriate women's futsal players in the Maldives": "تصنيف:لاعبو كرة صالات للسيدات مغتربون في جزر المالديف",
    "Category:Galatasaray S.K. (women's basketball) players": "تصنيف:لاعبو نادي غلطة سراي لكرة السلة للسيدات",
    "Category:Israeli women's basketball players": "تصنيف:لاعبو كرة سلة إسرائيلية نسائية",
    "Category:Italian women's futsal players": "تصنيف:لاعبو كرة صالات إيطالية نسائية",
    "Category:Kyrgyzstani women's basketball players": "تصنيف:لاعبو كرة سلة قرغيزستانية نسائية",
    "Category:Kyrgyzstani women's volleyball players": "تصنيف:لاعبو كرة طائرة قرغيزستانية نسائية",
    "Category:Lists of FIFA Women's World Cup players": "تصنيف:قوائم لاعبو كأس العالم لكرة القدم للسيدات",
    "Category:New Zealand women's national rugby league team players": "تصنيف:لاعبو منتخب نيوزيلندا لدوري الرغبي للسيدات",
    "Category:Scottish women's basketball players": "تصنيف:لاعبو كرة سلة إسكتلندية نسائية",
    "Category:Surinamese women's basketball players": "تصنيف:لاعبو كرة سلة سورينامية نسائية",
    "Category:Turkey women's national basketball team players": "تصنيف:لاعبو منتخب تركيا الوطني لكرة السلة للسيدات",
    "Category:UEFA Women's Euro 2022 players": "تصنيف:لاعبو بطولة أمم أوروبا لكرة القدم للسيدات 2022",
    "Category:UEFA Women's Euro 2025 players": "تصنيف:لاعبو بطولة أمم أوروبا لكرة القدم للسيدات 2025",
    "Category:Victorian Women's Football League players": "تصنيف:لاعبو الدوري الفيكتوري لكرة القدم للسيدات",
    "Category:Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس أمم إفريقيا لكرة القدم للسيدات",
    "Category:Women's basketball players in the United States by league": "تصنيف:لاعبو كرة سلة نسائية في الولايات المتحدة حسب الدوري",
    "Category:Women's England Hockey League players": "تصنيف:لاعبو دوري إنجلترا للهوكي نسائية",
    "Category:Women's hockey players": "تصنيف:لاعبو هوكي نسائية",
    "Category:Women's Irish Hockey League players": "تصنيف:لاعبو الدوري الأيرلندي للهوكي نسائية",
    "Category:Women's Korean Basketball League players": "تصنيف:لاعبو الدوري الكوري لكرة السلة نسائية",
    "Category:Women's lacrosse players": "تصنيف:لاعبو لاكروس نسائية",
    "Category:Women's National Basketball Association players from Croatia": "تصنيف:لاعبو الاتحاد الوطني لكرة السلة النسائية من كرواتيا",
    "Category:Women's National Basketball Association players from Serbia": "تصنيف:لاعبو الاتحاد الوطني لكرة السلة النسائية من صربيا",
    "Category:Women's National Basketball League players": "تصنيف:لاعبو الدوري الوطني لكرة السلة للسيدات",
    "Category:Women's soccer players in Australia by competition": "تصنيف:لاعبو كرة قدم نسائية في أستراليا حسب المنافسة",
}

data_3 = {
    "Category:Women's futsal players in Kuwait": "تصنيف:لاعبات كرة صالات في الكويت",
    "Category:Women's futsal players in the Maldives": "تصنيف:لاعبات كرة صالات في جزر المالديف",
    "Category:Women's field hockey players in England": "تصنيف:لاعبات هوكي ميدان في إنجلترا",
    "Category:Women's field hockey players in Ireland": "تصنيف:لاعبات هوكي ميدان في أيرلندا",

    "Category:Women's National Basketball League": "تصنيف:الدوري الوطني لكرة السلة للسيدات",
    "Category:Women's National Basketball League players": "تصنيف:لاعبو الدوري الوطني لكرة السلة للسيدات",
    "Category:Women's National Basketball League teams": "تصنيف:فرق الدوري الوطني لكرة السلة للسيدات",
    "Category:Women's lacrosse players": "تصنيف:لاعبات لاكروس",
    "Category:Women's hockey players": "تصنيف:لاعبات هوكي",
    "Category:Israeli women's basketball players": "تصنيف:لاعبات كرة سلة إسرائيليات",
    "Category:Female handball players in Turkey by club": "تصنيف:لاعبات كرة يد في تركيا حسب النادي",
    "Category:Colombian women's volleyball players": "تصنيف:لاعبات كرة طائرة كولومبيات",
    "Category:Armenian women's volleyball players": "تصنيف:لاعبات كرة طائرة أرمنيات",
    "Category:2024 Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات 2024",
    "Category:2022 Women's Africa Cup of Nations players": "تصنيف:لاعبات كأس الأمم الإفريقية للسيدات 2022",
    "Category:Kyrgyzstani women's basketball players": "تصنيف:لاعبات كرة سلة قيرغيزستانيات",
    "Category:Kyrgyzstani women's volleyball players": "تصنيف:لاعبات كرة طائرة قيرغيزستانيات",
    "Category:Italian women's futsal players": "تصنيف:لاعبات كرة صالات إيطاليات",
    "Category:Surinamese women's basketball players": "تصنيف:لاعبات كرة سلة سوريناميات",
    "Category:Scottish women's basketball players": "تصنيف:لاعبات كرة سلة إسكتلنديات",
}

data_4 = {
    "Category:Republic of Ireland association football leagues": "تصنيف:دوريات كرة قدم أيرلندية",
    "Category:Republic of Ireland association football": "تصنيف:كرة قدم أيرلندية",
    "Category:Republic of Ireland women's association football": "تصنيف:كرة قدم أيرلندية نسائية",
    "Category:Ireland women's international rugby union players": "تصنيف:لاعبات اتحاد رغبي دوليات من أيرلندا",
    "Category:Ireland women's national basketball team players": "تصنيف:لاعبو منتخب أيرلندا الوطني لكرة السلة للسيدات",
    "Category:Ireland women's national basketball team": "تصنيف:منتخب أيرلندا الوطني لكرة السلة للسيدات",
    "Category:Ireland women's national field hockey team coaches": "تصنيف:مدربو منتخب أيرلندا لهوكي الميدان للسيدات",
    "Category:Ireland women's national field hockey team": "تصنيف:منتخب أيرلندا لهوكي الميدان للسيدات",
    "Category:Ireland women's national rugby sevens team": "تصنيف:منتخب أيرلندا الوطني لسباعيات الرغبي للسيدات",
    "Category:Ireland women's national rugby union team coaches": "تصنيف:مدربو منتخب أيرلندا الوطني لاتحاد الرغبي للسيدات",
    "Category:Ireland women's national rugby union team": "تصنيف:منتخب أيرلندا الوطني لاتحاد الرغبي للسيدات",
    "Category:Northern Ireland women's international footballers": "تصنيف:لاعبات منتخب أيرلندا الشمالية لكرة القدم للسيدات",
    "Category:Northern Ireland women's national football team": "تصنيف:منتخب أيرلندا الشمالية الوطني لكرة القدم للنساء",
    "Category:Northern Ireland women's national football teams": "تصنيف:منتخبات كرة قدم وطنية أيرلندية شمالية للسيدات",
    "Category:Republic of Ireland women's association footballers": "تصنيف:لاعبات كرة قدم أيرلنديات",
    "Category:Republic of Ireland women's international footballers": "تصنيف:لاعبات منتخب جمهورية أيرلندا لكرة القدم للنساء",
    "Category:Republic of Ireland women's national football team managers": "تصنيف:مدراء منتخب جمهورية أيرلندا الوطني لكرة القدم للسيدات",
    "Category:Republic of Ireland women's national football team navigational boxes": "تصنيف:قوالب منتخب جمهورية أيرلندا لكرة القدم للسيدات",
    "Category:Republic of Ireland women's national football team": "تصنيف:منتخب جمهورية أيرلندا الوطني لكرة القدم للنساء",
    "Category:Republic of Ireland women's national football teams": "تصنيف:منتخبات كرة قدم وطنية أيرلندية للسيدات",
    "Category:Republic of Ireland women's youth international footballers": "تصنيف:لاعبات منتخب جمهورية أيرلندا لكرة القدم للشابات",
}

to_test = [
    # ("test_womens_players_1", data_1),
    ("test_womens_players_2", data_2),
    ("test_womens_players_3", data_3),
    ("test_womens_ireland_4", data_4),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=list(data_2.keys()))
@pytest.mark.fast
def test_womens_players_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    save3 = [
        f"* {{{{وب:طنت/سطر|{v.replace('تصنيف:', '')}|{diff_result[x].replace('تصنيف:', '')}|سبب النقل=تصحيح ArWikiCats}}}}"
        for x, v in expected.items()
        if v and x in diff_result
    ]
    dump_diff_text(save3, f"{name}_d")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
