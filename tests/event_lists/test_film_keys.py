#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data0 = {
    "Category:Mongolian film actors": "تصنيف:ممثلو أفلام منغوليون",
    "Category:Mongolian film directors": "تصنيف:مخرجو أفلام منغوليون",
    "Category:Mongolian documentary filmmakers": "تصنيف:صانعو أفلام وثائقية منغوليون",
    "Category:Mongolian film producers": "تصنيف:منتجو أفلام منغوليون",
    "Category:Mongolian screenwriters": "تصنيف:كتاب سيناريو منغوليون",
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
    "Category:Bissau-Guinean film people": "تصنيف:أعلام أفلام غينيون بيساويون",
}

data_1 = {
    "Category:Film people from Andhra Pradesh": "تصنيف:أعلام أفلام من أندرا برديش",
    "Category:Film people from Assam": "تصنيف:أعلام أفلام من أسام",
    "Category:Film people from Athens": "تصنيف:أعلام أفلام من أثينا",
    "Category:Film people from Baden-Württemberg": "تصنيف:أعلام أفلام من بادن-فورتمبيرغ",
    "Category:Film people from Baku": "تصنيف:أعلام أفلام من باكو",
    "Category:Film people from Bavaria": "تصنيف:أعلام أفلام من بافاريا",
    "Category:Film people from Belgrade": "تصنيف:أعلام أفلام من بلغراد",
    "Category:Film people from Bergamo": "تصنيف:أعلام أفلام من مدينة بيرغامو",
    "Category:Film people from Berlin": "تصنيف:أعلام أفلام من برلين",
    "Category:Film people from Besançon": "تصنيف:أعلام أفلام من بيزنسون",
    "Category:Film people from Beverly Hills, California": "تصنيف:أعلام أفلام من بيفرلي هيلز",
    "Category:Film people from Bihar": "تصنيف:أعلام أفلام من بيهار",
    "Category:Film people from Bologna": "تصنيف:أعلام أفلام من بولونيا",
    "Category:Film people from Brandenburg": "تصنيف:أعلام أفلام من براندنبورغ",
    "Category:Film people from Bratislava": "تصنيف:أعلام أفلام من براتيسلافا",
    "Category:Film people from Bremen (state)": "تصنيف:أعلام أفلام من ولاية بريمن",
    "Category:Film people from Brest, France": "تصنيف:أعلام أفلام من بريست (فرنسا)",
    "Category:Film people from Bristol": "تصنيف:أعلام أفلام من بريستول",
    "Category:Film people from Brno": "تصنيف:أعلام أفلام من برنو",
    "Category:Film people from Bucharest": "تصنيف:أعلام أفلام من بوخارست",
    "Category:Film people from Budapest": "تصنيف:أعلام أفلام من بودابست",
    "Category:Film people from Buenos Aires": "تصنيف:أعلام أفلام من بوينس آيرس",
    "Category:Film people from Bydgoszcz": "تصنيف:أعلام أفلام من بيدغوشتش",
    "Category:Film people from Cairo": "تصنيف:أعلام أفلام من القاهرة",
    "Category:Film people from California": "تصنيف:أعلام أفلام من كاليفورنيا",
    "Category:Film people from Catania": "تصنيف:أعلام أفلام من قطانية",
    "Category:Film people from České Budějovice": "تصنيف:أعلام أفلام من تشيسكي بوديوفيتسه",
    "Category:Film people from Chicago": "تصنيف:أعلام أفلام من شيكاغو",
    "Category:Film people from Chișinău": "تصنيف:أعلام أفلام من كيشيناو",
    "Category:Film people from Cleveland": "تصنيف:أعلام أفلام من كليفلاند",
    "Category:Film people from Cluj-Napoca": "تصنيف:أعلام أفلام من كلوج نابوك",
    "Category:Film people from Cologne": "تصنيف:أعلام أفلام من كولونيا",
    "Category:Film people from Copenhagen": "تصنيف:أعلام أفلام من كوبنهاغن",
    "Category:Film people from Delhi": "تصنيف:أعلام أفلام من دلهي",
    "Category:Film people from Dnipro": "تصنيف:أعلام أفلام من دنيبروبتروفسك",
    "Category:Film people from Dortmund": "تصنيف:أعلام أفلام من دورتموند",
    "Category:Film people from Dresden": "تصنيف:أعلام أفلام من درسدن",
    "Category:Film people from Dublin (city)": "تصنيف:أعلام أفلام من دبلن",
    "Category:Film people from Düsseldorf": "تصنيف:أعلام أفلام من دوسلدورف",
    "Category:Film people from Edinburgh": "تصنيف:أعلام أفلام من إدنبرة",
    "Category:Film people from Essen": "تصنيف:أعلام أفلام من إسن",
    "Category:Film people from Florence": "تصنيف:أعلام أفلام من فلورنسا",
    "Category:Film people from Frankfurt": "تصنيف:أعلام أفلام من فرانكفورت",
    "Category:Film people from Freiburg im Breisgau": "تصنيف:أعلام أفلام من فرايبورغ",
    "Category:Film people from Gdańsk": "تصنيف:أعلام أفلام من غدانسك",
    "Category:Film people from Geneva": "تصنيف:أعلام أفلام من جنيف",
    "Category:Film people from Genoa": "تصنيف:أعلام أفلام من جنوة",
    "Category:Film people from Georgia (country)": "تصنيف:أعلام أفلام من جورجيا",
    "Category:Film people from Glasgow": "تصنيف:أعلام أفلام من غلاسكو",
    "Category:Film people from Graz": "تصنيف:أعلام أفلام من غراتس",
    "Category:Film people from Gujarat": "تصنيف:أعلام أفلام من غوجارات",
    "Category:Film people from Hamburg": "تصنيف:أعلام أفلام من هامبورغ",
    "Category:Film people from Hanover": "تصنيف:أعلام أفلام من هانوفر",
    "Category:Film people from Haryana": "تصنيف:أعلام أفلام من هاريانا",
    "Category:Film people from Helsinki": "تصنيف:أعلام أفلام من هلسنكي",
    "Category:Film people from Hesse": "تصنيف:أعلام أفلام من هسن",
    "Category:Film people from Himachal Pradesh": "تصنيف:أعلام أفلام من هيماجل برديش",
    "Category:Film people from Iași": "تصنيف:أعلام أفلام من ياش",
    "Category:Film people from Innsbruck": "تصنيف:أعلام أفلام من إنسبروك",
    "Category:Film people from Isfahan": "تصنيف:أعلام أفلام من أصفهان",
    "Category:Film people from Istanbul": "تصنيف:أعلام أفلام من إسطنبول",
    "Category:Film people from Jammu and Kashmir": "تصنيف:أعلام أفلام من جامو وكشمير",
    "Category:Film people from Jerusalem": "تصنيف:أعلام أفلام من القدس",
    "Category:Film people from Jharkhand": "تصنيف:أعلام أفلام من جهارخاند",
    "Category:Film people from Karnataka": "تصنيف:أعلام أفلام من كارناتاكا",
    "Category:Film people from Kaunas": "تصنيف:أعلام أفلام من كاوناس",
    "Category:Film people from Kerala": "تصنيف:أعلام أفلام من كيرلا",
    "Category:Film people from Kharkiv": "تصنيف:أعلام أفلام من خاركيف",
    "Category:Film people from Kraków": "تصنيف:أعلام أفلام من كراكوف",
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
    "Category:Asian film awards": "تصنيف:جوائز الأفلام الآسيوية",
    "Category:Asian Film Awards": "تصنيف:جوائز الأفلام الآسيوية",
    "Category:Asian Film Awards navigational boxes": "تصنيف:صناديق تصفح جوائز الأفلام الآسيوية",
    "Category:Canadian women film critics": "تصنيف:ناقدات أفلام كنديات",
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
    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
