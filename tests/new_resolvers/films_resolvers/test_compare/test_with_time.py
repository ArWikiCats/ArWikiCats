"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels_and_time import get_films_key_tyty_new_and_time

novels_films_test_data_0 = {
    "1980s films": "أفلام إنتاج عقد 1980",
    "2026 films": "أفلام إنتاج 2026",
    "African films by country": "أفلام إفريقية حسب البلد",
    "African-American musical films": "أفلام موسيقية أمريكية إفريقية",
    "American war films": "أفلام حربية أمريكية",
    "Animated films set in 2050s": "أفلام رسوم متحركة تقع أحداثها في عقد 2050",
    "Animated films set in Manhattan": "أفلام رسوم متحركة تقع أحداثها في مانهاتن",
    "Animated films set in Monaco": "أفلام رسوم متحركة تقع أحداثها في موناكو",
    "Animated films set in Tanzania": "أفلام رسوم متحركة تقع أحداثها في تنزانيا",
    "Australian adult animated films": "أفلام رسوم متحركة للكبار أسترالية",
    "Australian fantasy films": "أفلام فانتازيا أسترالية",
    "Bangladeshi musical films": "أفلام موسيقية بنغلاديشية",
    "Belgian short films": "أفلام قصيرة بلجيكية",
    "Burkinabe independent films": "أفلام مستقلة بوركينابية",
    "Canadian psychological horror films": "أفلام رعب نفسي كندية",
    "Chinese sports films": "أفلام رياضية صينية",
    "Comedy films by year": "أفلام كوميدية حسب السنة",
    "Croatian comedy horror films": "أفلام كوميدية رعب كرواتية",
    "Danish films by studio": "أفلام دنماركية حسب استوديو الإنتاج",
    "Documentary films about David Lynch": "أفلام وثائقية عن ديفيد لينش",
    "Documentary films about film directors and producers": "أفلام وثائقية عن مخرجو أفلام ومنتجون",
    "Documentary films about immigration to Europe": "أفلام وثائقية عن الهجرة إلى أوروبا",
    "Documentary films about male prostitution": "أفلام وثائقية عن دعارة الذكور",
    "Documentary films about rape": "أفلام وثائقية عن الاغتصاب",
    "Documentary films about Werner Herzog": "أفلام وثائقية عن فرنر هرتزوغ",
    "Documentary films about women in United Kingdom": "أفلام وثائقية عن المرأة في المملكة المتحدة",
    "Films about mass shootings": "أفلام عن إطلاق نار عشوائي",
    "Films about poverty in France": "أفلام عن الفقر في فرنسا",
    "Films about racism in United Kingdom": "أفلام عن عنصرية في المملكة المتحدة",
    "Films based on American folklore": "أفلام مبنية على فلكور أمريكي",
    "Films based on Marvel Comics": "أفلام مبنية على مارفال كومكس",
    "Films based on operas by composer": "أفلام مبنية على أوبيرات حسب الملحن",
    "Films based on works by Albanian writers": "أفلام مبنية على أعمال كتاب ألبان",
    "Films based on works by Chrétien de Troyes": "أفلام مبنية على أعمال كريتيان دي تروا",
    "Films based on works by Estonian writers": "أفلام مبنية على أعمال كتاب إستونيون",
    "Films based on works by Nigerian writers": "أفلام مبنية على أعمال كتاب نيجيريون",
    "Films by Iraqi directors": "أفلام مخرجون عراقيون",
    "Films by Malaysian producers": "أفلام منتجون ماليزيون",
    "Films scored by Brazilian composers": "أفلام سجلها ملحنون برازيليون",
    "Films scored by French composers": "أفلام سجلها ملحنون فرنسيون",
    "Films set in 1670": "أفلام تقع أحداثها في 1670",
    "Films set in 1699": "أفلام تقع أحداثها في 1699",
    "Films set in 1719": "أفلام تقع أحداثها في 1719",
    "Films set in 1879": "أفلام تقع أحداثها في 1879",
    "Films set in 2026": "أفلام تقع أحداثها في 2026",
    "Films set in Bahamas": "أفلام تقع أحداثها في باهاماس",
    "Films set in castles": "أفلام تقع أحداثها في قلاع",
    "Films set in Chhattisgarh": "أفلام تقع أحداثها في تشاتيسغار",
    "Films set in Ibadan": "أفلام تقع أحداثها في إبادان",
    "Films set in Iowa": "أفلام تقع أحداثها في آيوا",
    "Films set in Suffolk": "أفلام تقع أحداثها في سوفولك",
    "Films shot in County Kildare": "أفلام مصورة في مقاطعة كيلدير",
    "Films shot in East Riding of Yorkshire": "أفلام مصورة في إيست رايدينج أوف يوركشير",
    "Films shot in Pennsylvania": "أفلام مصورة في بنسلفانيا",
    "Films shot in Sarthe": "أفلام مصورة في سارت (إقليم فرنسي)",
    "Films shot in Sindhudurg": "أفلام مصورة في سيندهودورج",
    "Films shot in South Carolina": "أفلام مصورة في كارولاينا الجنوبية",
    "Finnish films": "أفلام فنلندية",
    "French association football films": "أفلام كرة القدم الفرنسية",
    "Greenlandic documentary films": "أفلام وثائقية جرينلاندية",
    "Iranian silent films": "أفلام صامتة إيرانية",
    "Japanese works adapted into films": "أعمال يابانية تم تحويلها إلى أفلام",
    "Lists of 1920 films by language": "قوائم أفلام إنتاج 1920 حسب اللغة",
    "Lists of 1976 films by language": "قوائم أفلام إنتاج 1976 حسب اللغة",
    "Lists of 2000 films": "قوائم أفلام 2000",
    "Lists of 2026 films": "قوائم أفلام 2026",
    "Lists of anime films": "قوائم أفلام أنمي",
    "Lists of films by year and language": "قوائم أفلام حسب السنة واللغة",
    "Lists of French films by decade": "قوائم أفلام فرنسية حسب العقد",
    "Luxembourgian documentary films": "أفلام وثائقية لوكسمبورغية",
    "Novellas adapted into films": "روايات قصيرة تم تحويلها إلى أفلام",
    "Pakistani drama films": "أفلام درامية باكستانية",
    "Pakistani science fiction action films": "أفلام خيال علمي وحركة باكستانية",
    "Philippine black-and-white films": "أفلام أبيض وأسود فلبينية",
    "Polish films": "أفلام بولندية",
    "Romance films": "أفلام رومانسية",
    "Somalian documentary films": "أفلام وثائقية صومالية",
    "Somalian short films": "أفلام قصيرة صومالية",
    "South Korean children's films": "أفلام أطفال كورية جنوبية",
    "South Korean films by year": "أفلام كورية جنوبية حسب السنة",
    "South Korean political thriller films": "أفلام إثارة سياسية كورية جنوبية",
    "Swedish vampire films": "أفلام مصاصي دماء سويدية",
    "Taiwanese black comedy films": "أفلام كوميدية سوداء تايوانية",
    "Bangladeshi musical drama films": "أفلام موسيقية درامية بنغلاديشية",
    "Croatian crime drama films": "أفلام جريمة درامية كرواتية",
    "Philippine war drama films": "أفلام حربية درامية فلبينية",
}


novels_films_test_data = {
    "1940s Canadian animated films": "أفلام رسوم متحركة كندية في عقد 1940",
    "2000s Hong Kong films": "أفلام هونغ كونغية في عقد 2000",
    "2025 South Korean films": "أفلام كورية جنوبية في 2025",
    "1510s fantasy novels": "روايات فانتازيا في عقد 1510",
    "1530s fantasy novels": "روايات فانتازيا في عقد 1530",
    "1590s fantasy novels": "روايات فانتازيا في عقد 1590",
    "1610s fantasy novels": "روايات فانتازيا في عقد 1610",
    "1620s fantasy novels": "روايات فانتازيا في عقد 1620",
    "1630s science fiction novels": "روايات خيال علمي في عقد 1630",
    "1650s science fiction novels": "روايات خيال علمي في عقد 1650",
    "1680s fantasy novels": "روايات فانتازيا في عقد 1680",
    "1720s science fiction novels": "روايات خيال علمي في عقد 1720",
    "1895 fantasy novels": "روايات فانتازيا في 1895",
    "1910s mystery films": "أفلام غموض في عقد 1910",
    "1910s pornographic films": "أفلام إباحية في عقد 1910",
    "1928 American animated short films": "أفلام رسوم متحركة قصيرة أمريكية في 1928",
    "1950 comedy films": "أفلام كوميدية في 1950",
    "1950s comedy films": "أفلام كوميدية في عقد 1950",
    "1955 science fiction novels": "روايات خيال علمي في 1955",
    "1960 anime films": "أفلام أنمي في 1960",
    "1960 comedy-drama films": "أفلام كوميدية درامية في 1960",
    "1972 independent films": "أفلام مستقلة في 1972",
    "1976 fantasy films": "أفلام فانتازيا في 1976",
    "1978 martial arts films": "أفلام فنون قتال في 1978",
    "1979 anime films": "أفلام أنمي في 1979",
    "1980 crime thriller films": "أفلام إثارة وجريمة في 1980",
    "1983 American television seasons": "مواسم تلفزيونية أمريكية في 1983",
    "1986 comedy horror films": "أفلام كوميدية رعب في 1986",
    "1986 fantasy novels": "روايات فانتازيا في 1986",
    "1989 crime films": "أفلام جريمة في 1989",
    "1990 animated short films": "أفلام رسوم متحركة قصيرة في 1990",
    "1991 crime thriller films": "أفلام إثارة وجريمة في 1991",
    "1992 action comedy films": "أفلام حركة كوميدية في 1992",
    "2000s educational films": "أفلام تعليمية في عقد 2000",
    "2002 horror films": "أفلام رعب في 2002",
    "2003 fantasy films": "أفلام فانتازيا في 2003",
    "2003 psychological thriller films": "أفلام إثارة نفسية في 2003",
    "2003 Swedish television seasons": "مواسم تلفزيونية سويدية في 2003",
    "2009 science fiction action films": "أفلام خيال علمي وحركة في 2009",
    "2010 Hungarian television seasons": "مواسم تلفزيونية مجرية في 2010",
    "2011 Slovenian television seasons": "مواسم تلفزيونية سلوفينية في 2011",
    "2012 Danish television seasons": "مواسم تلفزيونية دنماركية في 2012",
    "2013 Czech television seasons": "مواسم تلفزيونية تشيكية في 2013",
    "2014 fantasy novels": "روايات فانتازيا في 2014",
    "2014 Norwegian television seasons": "مواسم تلفزيونية نرويجية في 2014",
    "2017 Vietnamese television seasons": "مواسم تلفزيونية فيتنامية في 2017",
    "2020 romance films": "أفلام رومانسية في 2020",
    "2020s slasher films": "أفلام تقطيع في عقد 2020",
    "2021 fantasy novels": "روايات فانتازيا في 2021",
    "2026 3D films": "أفلام ثلاثية الأبعاد في 2026",
    "2026 action films": "أفلام حركة في 2026",
    "2026 action thriller films": "أفلام إثارة حركة في 2026",
    "2026 American animated films": "أفلام رسوم متحركة أمريكية في 2026",
    "2026 animated films": "أفلام رسوم متحركة في 2026",
    "2026 anime films": "أفلام أنمي في 2026",
    "2026 comedy films": "أفلام كوميدية في 2026",
    "2026 computer-animated films": "أفلام حركة حاسوبية في 2026",
    "2026 drama films": "أفلام درامية في 2026",
    "2026 fantasy films": "أفلام فانتازيا في 2026",
    "2026 horror films": "أفلام رعب في 2026",
    "2026 science fiction action films": "أفلام خيال علمي وحركة في 2026",
    "2026 science fiction films": "أفلام خيال علمي في 2026",
    "2026 thriller films": "أفلام إثارة في 2026",
}


@pytest.mark.parametrize(
    "name,data,callback", [("get_films_key_tyty_new_and_time", novels_films_test_data, get_films_key_tyty_new_and_time)]
)
@pytest.mark.dump
def test_dump_2nd(monkeypatch: pytest.MonkeyPatch, name: str, data: dict[str, str], callback) -> None:
    """
    Run a comparison test of film-label resolution with time by patching its helper and asserting the output matches expected.

    Parameters:
        monkeypatch (pytest.MonkeyPatch): pytest fixture used to replace the module's helper with a controlled implementation.
        name (str): Identifier used for dump files and test output grouping.
        data (dict[str, str]): Mapping of source film-category keys to expected translations.
        callback: The function under test that processes `data` to produce comparison results.

    No return value. The test records differences and same/not-same items, and asserts that the produced diff equals the expected result.
    """
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
