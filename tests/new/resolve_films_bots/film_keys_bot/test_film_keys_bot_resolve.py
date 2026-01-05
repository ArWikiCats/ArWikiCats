"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats.new.resolve_films_bots.film_keys_bot import resolve_films_with_nat, Films, resolve_films

fast_data_with_nat = {
    # "american superhero films": "أفلام أبطال خارقين أمريكية",
    "burmese romantic drama films": "أفلام درامية رومانسية بورمية",
    "dutch war drama films": "أفلام درامية حربية هولندية",
    "indian sports drama films": "أفلام درامية رياضية هندية",
    "iranian romantic drama films": "أفلام درامية رومانسية إيرانية",
    "nigerian musical drama films": "أفلام درامية موسيقية نيجيرية",
    "russian sports drama films": "أفلام درامية رياضية روسية",
    "spanish war drama films": "أفلام درامية حربية إسبانية",
    "australian films": "أفلام أسترالية",
    "austrian films": "أفلام نمساوية",
    "bangladeshi films": "أفلام بنغلاديشية",
    "british films": "أفلام بريطانية",
    "croatian biographical films": "أفلام سير ذاتية كرواتية",
    "dutch films": "أفلام هولندية",
    "french films": "أفلام فرنسية",
    "ghanaian films": "أفلام غانية",
    "irish films": "أفلام أيرلندية",
    "japanese films": "أفلام يابانية",
    "latvian films": "أفلام لاتفية",
    "moroccan musical films": "أفلام موسيقية مغربية",
    "romanian films": "أفلام رومانية",
    "saudiarabian films": "أفلام سعودية",
    "soviet films": "أفلام سوفيتية",
    "spanish films": "أفلام إسبانية",
    "belgian drama films": "أفلام درامية بلجيكية",
    "canadian docudrama films": "أفلام درامية وثائقية كندية",
    "soviet drama films": "أفلام درامية سوفيتية",
    "north korean drama films": "أفلام درامية كورية شمالية",
    "american animated films": "أفلام رسوم متحركة أمريكية",
    "american thriller films": "أفلام إثارة أمريكية",
    "australian comedy thriller films": "أفلام كوميدية إثارة أسترالية",
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
    "french musical comedy films": "أفلام كوميدية موسيقية فرنسية",
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
    "portuguese musical comedy films": "أفلام كوميدية موسيقية برتغالية",
    "slovenian animated films": "أفلام رسوم متحركة سلوفينية",
    "south korean sequel films": "أفلام متممة كورية جنوبية",
    "soviet short films": "أفلام قصيرة سوفيتية",
    "spanish documentary films": "أفلام وثائقية إسبانية",
    "spanish independent films": "أفلام مستقلة إسبانية",
    "swedish 3d films": "أفلام ثلاثية الأبعاد سويدية",
    "venezuelan silent short films": "أفلام قصيرة صامته فنزويلية"
}

fast_data_no_nat1 = {
    "action films": "أفلام حركة",
    "adventure films": "أفلام مغامرات",
    "animated films": "أفلام رسوم متحركة",
    "anime films": "أفلام أنمي",
    "anthology films": "أفلام أنثولوجيا",
    "black comedy films": "أفلام كوميدية سوداء",
    "buddy films": "أفلام رفقاء",
    "comedy films": "أفلام كوميدية",
    "crime films": "أفلام جريمة",
    "dark fantasy films": "أفلام فانتازيا مظلمة",
    "documentary films": "أفلام وثائقية",
    "epic films": "أفلام ملحمية",
    "fantasy films": "أفلام فانتازيا",
    "horror films": "أفلام رعب",
    "mystery film series": "سلاسل أفلام غموض",
    "parody films": "أفلام ساخرة",
    "police procedural films": "أفلام إجراءات الشرطة",
    "science fiction thriller films": "أفلام إثارة خيال علمي",
    "thriller films": "أفلام إثارة",
    "war films": "أفلام حربية",
    "melodrama films": "أفلام ميلودراما"
}

fast_data_no_nat = {
    # "chinese sports executives": "مدربو رياضية صينية",
    "danish adventure television series": "مسلسلات تلفزيونية مغامرات دنماركية",
    "danish black-and-white films": "أفلام أبيض وأسود دنماركية",
    "dutch television-seasons": "مواسم تلفزيونية هولندية",
    "colombian children's animated television series": "مسلسلات تلفزيونية رسوم متحركة أطفال كولومبية",
    "american zombie novels": "روايات زومبي أمريكية",
    "argentine adult animated television series": "مسلسلات تلفزيونية رسوم متحركة للكبار أرجنتينية",
    "austrian television series-endings": "مسلسلات تلفزيونية نمساوية انتهت في",
    "british mystery television series": "مسلسلات تلفزيونية غموض بريطانية",
    "canadian television series-endings": "مسلسلات تلفزيونية كندية انتهت في",
    "chilean television series-endings": "مسلسلات تلفزيونية تشيلية انتهت في",
    "spanish television series-debuts": "مسلسلات تلفزيونية إسبانية بدأ عرضها في",
    "spanish action films": "أفلام حركة إسبانية",
    "serbian crime television series": "مسلسلات تلفزيونية جريمة صربية",
    "portuguese fantasy films": "أفلام فانتازيا برتغالية",
    "puerto rican television series-debuts": "مسلسلات تلفزيونية بورتوريكية بدأ عرضها في",
    "polish crime thriller films": "أفلام إثارة وجريمة بولندية",
    "polish epic films": "أفلام ملحمية بولندية",
    "polish television series-debuts": "مسلسلات تلفزيونية بولندية بدأ عرضها في",
    "polish television-seasons": "مواسم تلفزيونية بولندية",
    "norwegian comedy-drama films": "أفلام كوميدية درامية نرويجية",
    "mexican crime thriller films": "أفلام إثارة وجريمة مكسيكية",
    "mexican television series-endings": "مسلسلات تلفزيونية مكسيكية انتهت في",
}


@pytest.mark.parametrize("category, expected", fast_data_with_nat.items(), ids=fast_data_with_nat.keys())
@pytest.mark.fast
def test_resolve_films_with_nat(category: str, expected: str) -> None:
    label = resolve_films_with_nat(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data_no_nat.items(), ids=fast_data_no_nat.keys())
@pytest.mark.fast
def test_resolve_films_no_nat(category: str, expected: str) -> None:
    label = Films(category)
    assert label == expected


to_test = [
    ("test_resolve_films_with_nat", fast_data_with_nat, resolve_films_with_nat),
    ("test_resolve_films_no_nat", fast_data_no_nat, Films),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_resolve_films_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
