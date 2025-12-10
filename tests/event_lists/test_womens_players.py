#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {"Category:Women's Irish Hockey League players": "تصنيف:لاعبو الدوري الأيرلندي للهوكي نسائية",
         "Category:Women's Korean Basketball League players": "تصنيف:لاعبو الدوري الكوري لكرة السلة نسائية",
         "Category:Women's National Basketball League players": "تصنيف:لاعبو الدوري الوطني لكرة السلة نسائية",
         "Category:Women's basketball players in the United States by league": "تصنيف:لاعبو كرة سلة نسائية في الولايات المتحدة حسب الدوري",
         "Category:Women's lacrosse players": "تصنيف:لاعبو لاكروس نسائية",
         "Category:Women's hockey players": "تصنيف:لاعبو هوكي نسائية",
         "Category:Women's futsal players in Kuwait": "تصنيف:لاعبو كرة صالات نسائية في الكويت",
         "Category:Women's futsal players in the Maldives": "تصنيف:لاعبو كرة صالات نسائية في جزر المالديف",
         "Category:Women's field hockey players in England": "تصنيف:لاعبو هوكي ميدان نسائية في إنجلترا",
         "Category:Women's field hockey players in Ireland": "تصنيف:لاعبو هوكي ميدان نسائية في أيرلندا",
         "Category:Israeli women's basketball players": "تصنيف:لاعبو كرة سلة إسرائيلية نسائية",
         "Category:Female handball players in Turkey by club": "تصنيف:لاعبو كرة يد نسائية في تركيا حسب النادي",
         "Category:Colombian women's volleyball players": "تصنيف:لاعبو كرة طائرة كولومبية نسائية",
         "Category:Armenian women's volleyball players": "تصنيف:لاعبو كرة طائرة أرمينية نسائية",
         "Category:2024 Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس الأمم الإفريقية نسائية 2024",
         "Category:2022 Women's Africa Cup of Nations players": "تصنيف:لاعبو كأس إفريقيا نسائية في بلدان 2022",
         "Category:Women's soccer players in Australia by competition": "تصنيف:لاعبو كرة قدم نسائية في أستراليا حسب المنافسة",
         "Category:Kyrgyzstani women's basketball players": "تصنيف:لاعبو كرة سلة قرغيزستانية نسائية",
         "Category:Kyrgyzstani women's volleyball players": "تصنيف:لاعبو كرة طائرة قرغيزستانية نسائية",
         "Category:Italian women's futsal players": "تصنيف:لاعبو كرة صالات إيطالية نسائية",
         "Category:Women's England Hockey League players": "تصنيف:لاعبو دوري إنجلترا للهوكي نسائية",
         "Category:Surinamese women's basketball players": "تصنيف:لاعبو كرة سلة سورينامية نسائية",
         "Category:Scottish women's basketball players": "تصنيف:لاعبو كرة سلة إسكتلندية نسائية",
         "Category:Liga MX Femenil players": "تصنيف:لاعبو أول شعبة نسائية بالمكسيك",

         }

data_2 = {

}

to_test = [
    ("test_womens_players_1", data1),
    ("test_womens_players_2", data_2),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=list(data1.keys()))
@pytest.mark.fast
def test_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
