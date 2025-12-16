#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_diff_text

from ArWikiCats import resolve_arabic_category_label

data0 = {
    "Category:American film people": "تصنيف:أعلام أفلام أمريكيون",
    "Category:Yemeni film people": "تصنيف:أعلام أفلام يمنيون",
    "Category:Ugandan film people": "تصنيف:أعلام أفلام أوغنديون",
    "Category:Turkish film people": "تصنيف:أعلام أفلام أتراك",
    "Category:Tunisian film people": "تصنيف:أعلام أفلام تونسيون",
    "Category:Saudi Arabian film people": "تصنيف:أعلام أفلام سعوديون",
    "Category:Rwandan film people": "تصنيف:أعلام أفلام روانديون",
    "Category:Republic of the Congo film people": "تصنيف:أعلام أفلام كونغويون",
    "Category:Palestinian film people": "تصنيف:أعلام أفلام فلسطينيون",
    "Category:Nigerien film people": "تصنيف:أعلام أفلام نيجريون",
    "Category:Malian film people": "تصنيف:أعلام أفلام ماليون",
    "Category:Ivorian film people": "تصنيف:أعلام أفلام إيفواريون",
    "Category:Gambian film people": "تصنيف:أعلام أفلام غامبيون",
    "Category:Gabonese film people": "تصنيف:أعلام أفلام غابونيون",
    "Category:Film people": "تصنيف:أعلام أفلام",
    "Category:Film people by nationality": "تصنيف:أعلام أفلام حسب الجنسية",
    "Category:Film people by role": "تصنيف:أعلام أفلام حسب الدور",
    "Category:Ethiopian film people": "تصنيف:أعلام أفلام إثيوبيون",
    "Category:Canadian film people": "تصنيف:أعلام أفلام كنديون",
    "Category:Bulgarian film people": "تصنيف:أعلام أفلام بلغاريون",
    "Category:Bissau-Guinean film people": "تصنيف:أعلام أفلام غينيون بيساويون"
}

data_1 = {
    "Category:Zimbabwean film posters": "",
    "Category:1890s French film templates": "",
    "Category:Asian Film Awards ceremonies": "",
    "Category:Canadian women film score composers": "",
    "Category:Film people from Andhra Pradesh": "x",
    "Category:Film people from Assam": "x",
    "Category:Film people from Athens": "x",
    "Category:Film people from Baden-Württemberg": "x",
    "Category:Film people from Baku": "x",
    "Category:Film people from Bavaria": "x",
    "Category:Film people from Belgrade": "x",
    "Category:Film people from Bergamo": "x",
    "Category:Film people from Berlin": "x",
    "Category:Film people from Besançon": "x",
    "Category:Film people from Beverly Hills, California": "x",
    "Category:Film people from Bihar": "x",
    "Category:Film people from Bologna": "x",
    "Category:Film people from Brandenburg": "x",
    "Category:Film people from Bratislava": "x",
    "Category:Film people from Bremen (state)": "x",
    "Category:Film people from Brest, France": "x",
    "Category:Film people from Bristol": "x",
    "Category:Film people from Brno": "x",
    "Category:Film people from Bucharest": "x",
    "Category:Film people from Budapest": "x",
    "Category:Film people from Buenos Aires": "x",
    "Category:Film people from Bydgoszcz": "x",
    "Category:Film people from Cairo": "x",
    "Category:Film people from California": "x",
    "Category:Film people from Catania": "x",
    "Category:Film people from České Budějovice": "x",
    "Category:Film people from Chicago": "x",
    "Category:Film people from Chișinău": "x",
    "Category:Film people from Cleveland": "x",
    "Category:Film people from Cluj-Napoca": "x",
    "Category:Film people from Cologne": "x",
    "Category:Film people from Copenhagen": "x",
    "Category:Film people from Delhi": "x",
    "Category:Film people from Dnipro": "x",
    "Category:Film people from Dortmund": "x",
    "Category:Film people from Dresden": "x",
    "Category:Film people from Dublin (city)": "x",
    "Category:Film people from Düsseldorf": "x",
    "Category:Film people from Edinburgh": "x",
    "Category:Film people from Essen": "x",
    "Category:Film people from Florence": "x",
    "Category:Film people from Frankfurt": "x",
    "Category:Film people from Freiburg im Breisgau": "x",
    "Category:Film people from Gdańsk": "x",
    "Category:Film people from Geneva": "x",
    "Category:Film people from Genoa": "x",
    "Category:Film people from Georgia (country)": "x",
    "Category:Film people from Glasgow": "x",
    "Category:Film people from Graz": "x",
    "Category:Film people from Gujarat": "x",
    "Category:Film people from Hamburg": "x",
    "Category:Film people from Hanover": "x",
    "Category:Film people from Haryana": "x",
    "Category:Film people from Helsinki": "x",
    "Category:Film people from Hesse": "x",
    "Category:Film people from Himachal Pradesh": "x",
    "Category:Film people from Iași": "x",
    "Category:Film people from Innsbruck": "x",
    "Category:Film people from Isfahan": "x",
    "Category:Film people from Istanbul": "x",
    "Category:Film people from Jammu and Kashmir": "x",
    "Category:Film people from Jerusalem": "x",
    "Category:Film people from Jharkhand": "x",
    "Category:Film people from Karnataka": "x",
    "Category:Film people from Kaunas": "x",
    "Category:Film people from Kerala": "x",
    "Category:Film people from Kharkiv": "x",
    "Category:Film people from Kraków": "x",
}

data_2 = {
    "Category:Asian Film Award winners": "تصنيف:فائزون بجائزة الأفلام الآسيوية",
    "Category:Zimbabwean film people": "تصنيف:أعلام أفلام زيمبابويون",
    "Category:Zimbabwean film actors": "تصنيف:ممثلو أفلام زيمبابويون",
    "Category:Zimbabwean film actresses": "تصنيف:ممثلات أفلام زيمبابويات",
    "Category:Zimbabwean film directors": "تصنيف:مخرجو أفلام زيمبابويون",
    "Category:Zimbabwean filmmakers": "تصنيف:صانعو أفلام زيمبابويون",
    "Category:Zimbabwean male film actors": "تصنيف:ممثلو أفلام ذكور زيمبابويون",
    "Category:Zimbabwean women film directors": "تصنيف:مخرجات أفلام زيمبابويات",
    "Category:Zombie film series": "تصنيف:سلاسل أفلام زومبي",
    "Category:Zombie film series navigational boxes": "تصنيف:صناديق تصفح سلاسل أفلام زومبي",
    "Category:1880s in film by country": "تصنيف:أفلام في عقد 1880 حسب البلد",
    "Category:Asian film awards": "تصنيف:جوائز الأفلام الآسيوية",
    "Category:Asian Film Awards": "تصنيف:جوائز الأفلام الآسيوية",
    "Category:Asian Film Awards navigational boxes": "تصنيف:صناديق تصفح جوائز الأفلام الآسيوية",
    "Category:Canadian women film critics": "تصنيف:ناقدات أفلام كنديات",
    "Category:Canadian women film directors": "تصنيف:مخرجات أفلام كنديات",
    "Category:Canadian women film editors": "تصنيف:محررات أفلام كنديات",
    "Category:Canadian women film producers": "تصنيف:منتجات أفلام كنديات",
}

to_test = [
    ("test_film_keys_0", data0),
    ("test_film_keys_1", data_1),
    ("test_film_keys_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_film_keys_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
