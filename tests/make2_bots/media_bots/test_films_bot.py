"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.films_bot import te_films, resolve_films

fast_data_drama = {
    "comedy-drama films": "أفلام كوميدية درامية",
    "english-language political drama films": "أفلام دراما سياسية باللغة الإنجليزية",
    "english-language war drama films": "أفلام دراما حربية باللغة الإنجليزية",
    "hindi-language drama films": "أفلام دراما باللغة الهندية",
    "norwegian-language romantic drama films": "أفلام دراما رومانسية باللغة النرويجية",

    "belgian drama films": "أفلام درامية بلجيكية",
    "canadian docudrama films": "أفلام درامية وثائقية كندية",
    "korean-language historical drama films": "أفلام تاريخية درامية باللغة الكورية",
    "portuguese-language biographical drama films": "أفلام سيرة ذاتية درامية باللغة البرتغالية",
    "russian-language fantasy drama films": "أفلام فانتازيا درامية باللغة الروسية",
    "spanish-language historical drama films": "أفلام تاريخية درامية باللغة الإسبانية",
}

fast_data = {
    "action films": "أفلام حركة",
    "adventure films": "أفلام مغامرات",
    "albanian film directors": "مخرجو أفلام ألبان",
    "american animated films": "أفلام رسوم متحركة أمريكية",
    "american film directors": "مخرجو أفلام أمريكيون",
    "american superhero films": "أفلام خارقة أمريكية",
    "american thriller films": "أفلام إثارة أمريكية",
    "animated films": "أفلام رسوم متحركة",
    "anime films": "أفلام أنمي",
    "anthology films": "أفلام أنثولوجيا",
    "argentine film actors": "ممثلو أفلام أرجنتينيون",
    "australian comedy thriller films": "أفلام كوميديا إثارة أسترالية",
    "australian erotic thriller films": "أفلام إثارة جنسية أسترالية",
    "australian films": "أفلام أسترالية",
    "austrian films": "أفلام نمساوية",
    "austrian silent short films": "أفلام قصيرة صامته نمساوية",
    "azerbaijani short films": "أفلام قصيرة أذربيجانية",
    "bangladeshi films": "أفلام بنغلاديشية",
    "bengali-language romantic comedy films": "أفلام رومانسية كوميدية باللغة البنغالية",
    "black comedy films": "أفلام كوميدية سوداء",
    "british films": "أفلام بريطانية",
    "british mystery films": "أفلام غموض بريطانية",
    "british robot films": "أفلام آلية بريطانية",
    "bruneian film producers": "منتجو أفلام برونيون",
    "buddy films": "أفلام رفقاء",
    "canadian war films": "أفلام حربية كندية",
    "cantonese-language speculative fiction films": "أفلام خيال تأملي باللغة الكانتونية",
    "chinese epic films": "أفلام ملحمية صينية",
    "comedy films": "أفلام كوميدية",
    "crime films": "أفلام جريمة",
    "croatian biographical films": "أفلام سير ذاتية كرواتية",
    "croatian fantasy films": "أفلام فانتازيا كرواتية",
    "croatian science fiction films": "أفلام خيال علمي كرواتية",
    "czech silent film actors": "ممثلو أفلام صامتة تشيكيون",
    "czech-language crime films": "أفلام جريمة باللغة التشيكية",
    "dark fantasy films": "أفلام فانتازيا مظلمة",
    "documentary films": "أفلام وثائقية",
    "dutch films": "أفلام هولندية",
    "dutch short films": "أفلام قصيرة هولندية",
    "ecuadorian science fiction films": "أفلام خيال علمي إكوادورية",
    "emirati animated films": "أفلام رسوم متحركة إماراتية",
    "english-language crime action films": "أفلام جريمة حركة باللغة الإنجليزية",
    "epic films": "أفلام ملحمية",
    "fantasy films": "أفلام فانتازيا",
    "film directors": "مخرجو أفلام",
    "finnish-language erotic films": "أفلام إغرائية باللغة الفنلندية",
    "french films": "أفلام فرنسية",
    "french musical comedy films": "أفلام كوميديا موسيقية فرنسية",
    "french-language films": "أفلام باللغة الفرنسية",
    "german disaster films": "أفلام كوارثية ألمانية",
    "german-language films": "أفلام باللغة الألمانية",
    "ghanaian films": "أفلام غانية",
    "horror films": "أفلام رعب",
    "hungarian-language romance films": "أفلام رومانسية باللغة المجرية",
    "indian crime films": "أفلام جريمة هندية",
    "indian dark fantasy films": "أفلام فانتازيا مظلمة هندية",
    "indonesian film actresses": "ممثلات أفلام إندونيسيات",
    "indonesian prequel films": "أفلام بادئة إندونيسية",
    "indonesian zombie films": "أفلام زومبي إندونيسية",
    "iranian film actors": "ممثلو أفلام إيرانيون",
    "iranian film producers": "منتجو أفلام إيرانيون",
    "irish fantasy films": "أفلام فانتازيا أيرلندية",
    "irish films": "أفلام أيرلندية",
    "irish speculative fiction films": "أفلام خيالية تأملية أيرلندية",
    "irish thriller films": "أفلام إثارة أيرلندية",
    "italian comedy films": "أفلام كوميدية إيطالية",
    "italian zombie films": "أفلام زومبي إيطالية",
    "japanese films": "أفلام يابانية",
    "japanese heist films": "أفلام سرقة يابانية",
    "japanese male film actors": "ممثلو أفلام ذكور يابانيون",
    "japanese-language horror films": "أفلام رعب باللغة اليابانية",
    "kosovan filmmakers": "صانعو أفلام كوسوفيون",
    "kuwaiti short films": "أفلام قصيرة كويتية",
    "latvian films": "أفلام لاتفية",
    "malayalam-language films": "أفلام باللغة الماليالامية",
    "malaysian sports films": "أفلام رياضية ماليزية",
    "maldivian women film directors": "مخرجات أفلام مالديفيات",
    "mexican independent films": "أفلام مستقلة مكسيكية",
    "moldovan film actors": "ممثلو أفلام مولدوفيون",
    "moroccan musical films": "أفلام موسيقية مغربية",
    "mystery film series": "سلاسل أفلام غموض",
    "nepalese male film actors": "ممثلو أفلام ذكور نيباليون",
    "nigerien film actors": "ممثلو أفلام نيجريون",
    "parody films": "أفلام ساخرة",
    "philippine kung fu films": "أفلام كونغ فو فلبينية",
    "police procedural films": "أفلام إجراءات الشرطة",
    "portuguese adult animated films": "أفلام رسوم متحركة للكبار برتغالية",
    "portuguese musical comedy films": "أفلام كوميديا موسيقية برتغالية",
    "romanian films": "أفلام رومانية",
    "russian silent film actresses": "ممثلات أفلام صامتة روسيات",
    "russian-language historical comedy films": "أفلام تاريخية كوميدية باللغة الروسية",
    "saudiarabian films": "أفلام سعودية",
    "science fiction thriller films": "أفلام إثارة خيال علمي",
    "slovenian animated films": "أفلام رسوم متحركة سلوفينية",
    "somalian film producers": "منتجو أفلام صوماليون",
    "south korean sequel films": "أفلام متممة كورية جنوبية",
    "soviet films": "أفلام سوفيتية",
    "soviet short films": "أفلام قصيرة سوفيتية",
    "spanish documentary films": "أفلام وثائقية إسبانية",
    "spanish films": "أفلام إسبانية",
    "spanish independent films": "أفلام مستقلة إسبانية",
    "spanish-language historical films": "أفلام تاريخية باللغة الإسبانية",
    "spanish-language sex comedy films": "أفلام جنسية كوميدية باللغة الإسبانية",
    "superhero films": "أفلام خارقة",
    "swedish 3d films": "أفلام ثلاثية الأبعاد سويدية",
    "swedish-language musical films": "أفلام موسيقية باللغة السويدية",
    "telugu film directors": "مخرجو أفلام تيلوغويون",
    "thai film actors": "ممثلو أفلام تايلنديون",
    "thriller films": "أفلام إثارة",
    "ukrainian filmmakers": "صانعو أفلام أوكرانيون",
    "urdu-language films": "أفلام باللغة الأردية",
    "venezuelan silent short films": "أفلام قصيرة صامته فنزويلية",
    "war films": "أفلام حربية",
    "welsh film producers": "منتجو أفلام ويلزيون",
}


@pytest.mark.parametrize("category, expected", fast_data_drama.items(), ids=list(fast_data_drama.keys()))
@pytest.mark.fast
def test_fast_data_drama(category: str, expected: str) -> None:
    label = te_films(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data_films(category: str, expected: str) -> None:
    label = te_films(category)
    assert label == expected


to_test = [
    ("test_fast_data_drama", fast_data_drama, te_films),
    ("test_fast_data_films", fast_data, resolve_films),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:

    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_test_films() -> None:
    # Test with a basic input
    result = te_films("action films")
    assert isinstance(result, str)

    result_empty = te_films("")
    assert isinstance(result_empty, str)

    # Test with reference category
    result_with_ref = te_films("drama movies")
    assert isinstance(result_with_ref, str)
