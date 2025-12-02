"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.media_bots.films_bot import resolve_films

fast_data = {
    "action films": "أفلام حركة",
    "adventure films": "أفلام مغامرات",
    "animated films": "أفلام رسوم متحركة",
    "anime films": "أفلام أنمي",
    "anthology films": "أفلام أنثولوجيا",
    "australian films": "أفلام أسترالية",
    "austrian films": "أفلام نمساوية",
    "bangladeshi films": "أفلام بنغلاديشية",
    "black comedy films": "أفلام كوميدية سوداء",
    "british films": "أفلام بريطانية",
    "buddy films": "أفلام رفقاء",
    "comedy films": "أفلام كوميدية",
    "crime films": "أفلام جريمة",
    "croatian biographical films": "أفلام سير ذاتية كرواتية",
    "dark fantasy films": "أفلام فانتازيا مظلمة",
    "documentary films": "أفلام وثائقية",
    "dutch films": "أفلام هولندية",
    "epic films": "أفلام ملحمية",
    "fantasy films": "أفلام فانتازيا",
    "french films": "أفلام فرنسية",
    "ghanaian films": "أفلام غانية",
    "horror films": "أفلام رعب",
    "irish films": "أفلام أيرلندية",
    "japanese films": "أفلام يابانية",
    "latvian films": "أفلام لاتفية",
    "moroccan musical films": "أفلام موسيقية مغربية",
    "mystery film series": "سلاسل أفلام غموض",
    "parody films": "أفلام ساخرة",
    "police procedural films": "أفلام إجراءات الشرطة",
    "romanian films": "أفلام رومانية",
    "saudiarabian films": "أفلام سعودية",
    "science fiction thriller films": "أفلام إثارة خيال علمي",
    "soviet films": "أفلام سوفيتية",
    "spanish films": "أفلام إسبانية",
    "superhero films": "أفلام خارقة",
    "thriller films": "أفلام إثارة",
    "war films": "أفلام حربية",

    "belgian drama films": "أفلام درامية بلجيكية",
    "canadian docudrama films": "أفلام درامية وثائقية كندية",
    "burmese romantic drama films": "أفلام رومانسية درامية بورمية",
    "dutch war drama films": "أفلام حربية درامية هولندية",
    "indian sports drama films": "أفلام رياضية درامية هندية",
    "iranian romantic drama films": "أفلام رومانسية درامية إيرانية",
    "nigerian musical drama films": "أفلام موسيقية درامية نيجيرية",
    "russian sports drama films": "أفلام رياضية درامية روسية",
    "spanish war drama films": "أفلام حربية درامية إسبانية",
    "soviet drama films": "أفلام درامية سوفيتية",
    "melodrama films": "أفلام ميلودراما",
    "north korean drama films": "أفلام درامية كورية شمالية",
    "american animated films": "أفلام رسوم متحركة أمريكية",
    "american superhero films": "أفلام خارقة أمريكية",
    "american thriller films": "أفلام إثارة أمريكية",
    "australian comedy thriller films": "أفلام كوميديا إثارة أسترالية",
    "australian erotic thriller films": "أفلام إثارة جنسية أسترالية",
    "austrian silent short films": "أفلام قصيرة صامته نمساوية",
    "azerbaijani short films": "أفلام قصيرة أذربيجانية",
    "british mystery films": "أفلام غموض بريطانية",
    "british robot films": "أفلام آلية بريطانية",
    "canadian war films": "أفلام حربية كندية",
    "chinese epic films": "أفلام ملحمية صينية",
    "croatian fantasy films": "أفلام فانتازيا كرواتية",
    "croatian science fiction films": "أفلام خيال علمي كرواتية",
    "dutch short films": "أفلام قصيرة هولندية",
    "ecuadorian science fiction films": "أفلام خيال علمي إكوادورية",
    "emirati animated films": "أفلام رسوم متحركة إماراتية",
    "french musical comedy films": "أفلام كوميديا موسيقية فرنسية",
    "german disaster films": "أفلام كوارثية ألمانية",
    "indian crime films": "أفلام جريمة هندية",
    "indian dark fantasy films": "أفلام فانتازيا مظلمة هندية",
    "indonesian prequel films": "أفلام بادئة إندونيسية",
    "indonesian zombie films": "أفلام زومبي إندونيسية",
    "irish fantasy films": "أفلام فانتازيا أيرلندية",
    "irish speculative fiction films": "أفلام خيالية تأملية أيرلندية",
    "irish thriller films": "أفلام إثارة أيرلندية",
    "italian comedy films": "أفلام كوميدية إيطالية",
    "italian zombie films": "أفلام زومبي إيطالية",
    "japanese heist films": "أفلام سرقة يابانية",
    "kuwaiti short films": "أفلام قصيرة كويتية",
    "malaysian sports films": "أفلام رياضية ماليزية",
    "mexican independent films": "أفلام مستقلة مكسيكية",
    "philippine kung fu films": "أفلام كونغ فو فلبينية",
    "portuguese adult animated films": "أفلام رسوم متحركة للكبار برتغالية",
    "portuguese musical comedy films": "أفلام كوميديا موسيقية برتغالية",
    "slovenian animated films": "أفلام رسوم متحركة سلوفينية",
    "south korean sequel films": "أفلام متممة كورية جنوبية",
    "soviet short films": "أفلام قصيرة سوفيتية",
    "spanish documentary films": "أفلام وثائقية إسبانية",
    "spanish independent films": "أفلام مستقلة إسبانية",
    "swedish 3d films": "أفلام ثلاثية الأبعاد سويدية",
    "venezuelan silent short films": "أفلام قصيرة صامته فنزويلية",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_resolve_films(category: str, expected: str) -> None:
    label = resolve_films(category)
    assert label == expected


to_test = [
    ("test_resolve_films", fast_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_resolve_films_all(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_films)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
