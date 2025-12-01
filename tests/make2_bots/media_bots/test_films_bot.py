"""
Tests
"""

import pytest

from ArWikiCats.make_bots.media_bots.films_bot import te_films

fast_data_drama = {
    "belgian drama films": "أفلام درامية بلجيكية",
    "burmese romantic drama films": "أفلام دراما رومانسية بورمية",
    "canadian docudrama films": "أفلام درامية وثائقية كندية",
    "comedy-drama films": "أفلام كوميدية درامية",
    "dutch war drama films": "أفلام درامية حربية هولندية",
    "english-language political drama films": "أفلام دراما سياسية باللغة الإنجليزية",
    "english-language war drama films": "أفلام دراما حربية باللغة الإنجليزية",
    "hindi-language drama films": "أفلام دراما باللغة الهندية",
    "indian sports drama films": "أفلام درامية رياضية هندية",
    "iranian romantic drama films": "أفلام دراما رومانسية إيرانية",
    "korean-language historical drama films": "أفلام تاريخية درامية باللغة الكورية",
    "melodrama films": "أفلام ميلودراما",
    "nigerian musical drama films": "أفلام دراما موسيقية نيجيرية",
    "north korean drama films": "أفلام درامية كورية شمالية",
    "norwegian-language romantic drama films": "أفلام دراما رومانسية باللغة النرويجية",
    "portuguese-language biographical drama films": "أفلام سيرة ذاتية درامية باللغة البرتغالية",
    "russian sports drama films": "أفلام درامية رياضية روسية",
    "russian-language fantasy drama films": "أفلام فانتازيا درامية باللغة الروسية",
    "soviet drama films": "أفلام درامية سوفيتية",
    "spanish war drama films": "أفلام دراما حربية إسبانية",
    "spanish-language historical drama films": "أفلام تاريخية درامية باللغة الإسبانية",
}

fast_data = {
    "british films": "أفلام بريطانية",
    "american animated films": "أفلام رسوم متحركة أمريكية",
    "black comedy films": "أفلام كوميدية سوداء",
    "moldovan film actors": "ممثلو أفلام مولدوفيون",
    "malaysian sports films": "أفلام رياضية ماليزية",
    "japanese male film actors": "ممثلو أفلام ذكور يابانيون",
    "australian erotic thriller films": "أفلام إثارة جنسية أسترالية",
    "science fiction thriller films": "أفلام إثارة خيال علمي",
    "american superhero films": "أفلام خارقة أمريكية",
    "film directors": "مخرجو أفلام",
    "animated films": "أفلام رسوم متحركة",
    "documentary films": "أفلام وثائقية",
    "thriller films": "أفلام إثارة",
    "german disaster films": "أفلام كوارثية ألمانية",
    "fantasy films": "أفلام فانتازيا",
    "action films": "أفلام حركة",
    "ukrainian filmmakers": "صانعو أفلام أوكرانيون",
    "crime films": "أفلام جريمة",
    "moroccan musical films": "أفلام موسيقية مغربية",
    "venezuelan silent short films": "أفلام قصيرة صامته فنزويلية",
    "adventure films": "أفلام مغامرات",
    "nigerien film actors": "ممثلو أفلام نيجريون",
    "indonesian film actresses": "ممثلات أفلام إندونيسيات",
    "irish fantasy films": "أفلام فانتازيا أيرلندية",
    "american thriller films": "أفلام إثارة أمريكية",
    "chinese epic films": "أفلام ملحمية صينية",
    "swedish-language musical films": "أفلام موسيقية باللغة السويدية",
    "soviet films": "أفلام سوفيتية",
    "irish speculative fiction films": "أفلام خيالية تأملية أيرلندية",
    "emirati animated films": "أفلام رسوم متحركة إماراتية",
    "british mystery films": "أفلام غموض بريطانية",
    "ecuadorian science fiction films": "أفلام خيال علمي إكوادورية",
    "mexican independent films": "أفلام مستقلة مكسيكية",
    "comedy films": "أفلام كوميدية",
    "superhero films": "أفلام خارقة",
    "police procedural films": "أفلام إجراءات الشرطة",
    "romanian films": "أفلام رومانية",
    "japanese films": "أفلام يابانية",
    "ghanaian films": "أفلام غانية",
    "czech-language crime films": "أفلام جريمة باللغة التشيكية",
    "south korean sequel films": "أفلام متممة كورية جنوبية",
    "spanish documentary films": "أفلام وثائقية إسبانية",
    "spanish independent films": "أفلام مستقلة إسبانية",
    "dutch films": "أفلام هولندية",
    "parody films": "أفلام ساخرة",
    "indian crime films": "أفلام جريمة هندية",
    "malayalam-language films": "أفلام باللغة الماليالامية",
    "british robot films": "أفلام آلية بريطانية",
    "japanese heist films": "أفلام سرقة يابانية",
    "russian-language historical comedy films": "أفلام تاريخية كوميدية باللغة الروسية",
    "horror films": "أفلام رعب",
    "irish thriller films": "أفلام إثارة أيرلندية",
    "indonesian prequel films": "أفلام بادئة إندونيسية",
    "australian comedy thriller films": "أفلام كوميديا إثارة أسترالية",
    "albanian film directors": "مخرجو أفلام ألبان",
    "soviet short films": "أفلام قصيرة سوفيتية",
    "nepalese male film actors": "ممثلو أفلام ذكور نيباليون",
    "bruneian film producers": "منتجو أفلام برونيون",
    "kuwaiti short films": "أفلام قصيرة كويتية",
    "german-language films": "أفلام باللغة الألمانية",
    "american film directors": "مخرجو أفلام أمريكيون",
    "austrian silent short films": "أفلام قصيرة صامته نمساوية",
    "maldivian women film directors": "مخرجات أفلام مالديفيات",
    "czech silent film actors": "ممثلو أفلام صامتة تشيكيون",
    "croatian fantasy films": "أفلام فانتازيا كرواتية",
    "war films": "أفلام حربية",
    "epic films": "أفلام ملحمية",
    "english-language crime action films": "أفلام جريمة حركة باللغة الإنجليزية",
    "kosovan filmmakers": "صانعو أفلام كوسوفيون",
    "croatian biographical films": "أفلام سير ذاتية كرواتية",
    "japanese-language horror films": "أفلام رعب باللغة اليابانية",
    "french-language films": "أفلام باللغة الفرنسية",
    "philippine kung fu films": "أفلام كونغ فو فلبينية",
    "somalian film producers": "منتجو أفلام صوماليون",
    "buddy films": "أفلام رفقاء",
    "urdu-language films": "أفلام باللغة الأردية",
    "canadian war films": "أفلام حربية كندية",
    "portuguese adult animated films": "أفلام رسوم متحركة للكبار برتغالية",
    "portuguese musical comedy films": "أفلام كوميديا موسيقية برتغالية",
    "anthology films": "أفلام أنثولوجيا",
    "dutch short films": "أفلام قصيرة هولندية",
    "spanish-language historical films": "أفلام تاريخية باللغة الإسبانية",
    "croatian science fiction films": "أفلام خيال علمي كرواتية",
    "anime films": "أفلام أنمي",
    "swedish 3d films": "أفلام ثلاثية الأبعاد سويدية",
    "spanish films": "أفلام إسبانية",
    "cantonese-language speculative fiction films": "أفلام خيال تأملي باللغة الكانتونية",
    "finnish-language erotic films": "أفلام إغرائية باللغة الفنلندية",
    "bengali-language romantic comedy films": "أفلام رومانسية كوميدية باللغة البنغالية",
    "slovenian animated films": "أفلام رسوم متحركة سلوفينية",
    "mystery film series": "سلاسل أفلام غموض",
    "argentine film actors": "ممثلو أفلام أرجنتينيون",
    "welsh film producers": "منتجو أفلام ويلزيون",
    "french musical comedy films": "أفلام كوميديا موسيقية فرنسية",
    "telugu film directors": "مخرجو أفلام تيلوغويون",
    "iranian film actors": "ممثلو أفلام إيرانيون",
    "russian silent film actresses": "ممثلات أفلام صامتة روسيات",
    "indonesian zombie films": "أفلام زومبي إندونيسية",
    "indian dark fantasy films": "أفلام فانتازيا مظلمة هندية",
    "austrian films": "أفلام نمساوية",
    "french films": "أفلام فرنسية",
    "latvian films": "أفلام لاتفية",
    "australian films": "أفلام أسترالية",
    "spanish-language sex comedy films": "أفلام جنسية كوميدية باللغة الإسبانية",
    "irish films": "أفلام أيرلندية",
    "azerbaijani short films": "أفلام قصيرة أذربيجانية",
    "hungarian-language romance films": "أفلام رومانسية باللغة المجرية",
    "bangladeshi films": "أفلام بنغلاديشية",
    "thai film actors": "ممثلو أفلام تايلنديون",
    "italian zombie films": "أفلام زومبي إيطالية",
    "saudiarabian films": "أفلام سعودية",
    "iranian film producers": "منتجو أفلام إيرانيون",
    "dark fantasy films": "أفلام فانتازيا مظلمة",
    "italian comedy films": "أفلام كوميدية إيطالية",
}


@pytest.mark.parametrize("category, expected", fast_data_drama.items(), ids=list(fast_data_drama.keys()))
@pytest.mark.fast
def test_fast_data_drama(category: str, expected: str) -> None:
    label = te_films(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = te_films(category)
    assert label == expected


def test_test_films() -> None:
    # Test with a basic input
    result = te_films("action films")
    assert isinstance(result, str)

    result_empty = te_films("")
    assert isinstance(result_empty, str)

    # Test with reference category
    result_with_ref = te_films("drama movies")
    assert isinstance(result_with_ref, str)
