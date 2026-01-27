"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.films_resolvers import main_films_resolvers
from utils.dump_runner import make_dump_test_name_data_callback

fast_data_with_nat0 = {
    "mexican television series-endings": "مسلسلات تلفزيونية مكسيكية انتهت في",
    "austrian television series-endings": "مسلسلات تلفزيونية نمساوية انتهت في",
    "canadian television series-endings": "مسلسلات تلفزيونية كندية انتهت في",
    "chilean television series-endings": "مسلسلات تلفزيونية تشيلية انتهت في",
    "spanish television series-debuts": "مسلسلات تلفزيونية إسبانية بدأ عرضها في",
    "polish television series-debuts": "مسلسلات تلفزيونية بولندية بدأ عرضها في",
    "puerto rican television series-debuts": "مسلسلات تلفزيونية بورتوريكية بدأ عرضها في",
}

fast_data_with_nat = {
    # "american superhero films": "أفلام أبطال خارقين أمريكية",
    "american animated films": "أفلام رسوم متحركة أمريكية",
    "american thriller films": "أفلام إثارة أمريكية",
    "american zombie novels": "روايات زومبي أمريكية",
    "argentine adult animated television series": "مسلسلات تلفزيونية رسوم متحركة للكبار أرجنتينية",
    "australian comedy thriller films": "أفلام كوميدية إثارة أسترالية",
    "australian erotic thriller films": "أفلام إثارة جنسية أسترالية",
    "australian films": "أفلام أسترالية",
    "austrian films": "أفلام نمساوية",
    "austrian silent short films": "أفلام قصيرة صامته نمساوية",
    "azerbaijani short films": "أفلام قصيرة أذربيجانية",
    "bangladeshi films": "أفلام بنغلاديشية",
    "belgian drama films": "أفلام درامية بلجيكية",
    "british films": "أفلام بريطانية",
    "british mystery films": "أفلام غموض بريطانية",
    "british mystery television series": "مسلسلات تلفزيونية غموض بريطانية",
    "british robot films": "أفلام آلية بريطانية",
    "burmese romantic drama films": "أفلام رومانسية درامية بورمية",
    "canadian docudrama films": "أفلام درامية وثائقية كندية",
    "canadian war films": "أفلام حربية كندية",
    "chinese epic films": "أفلام ملحمية صينية",
    "colombian children's animated television series": "مسلسلات تلفزيونية رسوم متحركة أطفال كولومبية",
    "croatian biographical films": "أفلام سير ذاتية كرواتية",
    "croatian fantasy films": "أفلام فانتازيا كرواتية",
    "croatian science fiction films": "أفلام خيال علمي كرواتية",
    "danish adventure television series": "مسلسلات تلفزيونية مغامرات دنماركية",
    "danish black-and-white films": "أفلام أبيض وأسود دنماركية",
    "dutch films": "أفلام هولندية",
    "dutch short films": "أفلام قصيرة هولندية",
    "dutch television-seasons": "مواسم تلفزيونية هولندية",
    "dutch war drama films": "أفلام حربية درامية هولندية",
    "ecuadorian science fiction films": "أفلام خيال علمي إكوادورية",
    "emirati animated films": "أفلام رسوم متحركة إماراتية",
    "french films": "أفلام فرنسية",
    "french musical comedy films": "أفلام كوميدية موسيقية فرنسية",
    "german disaster films": "أفلام كوارثية ألمانية",
    "ghanaian films": "أفلام غانية",
    "indian crime films": "أفلام جريمة هندية",
    "indian dark fantasy films": "أفلام فانتازيا مظلمة هندية",
    "indian sports drama films": "أفلام رياضية درامية هندية",
    "indonesian prequel films": "أفلام بادئة إندونيسية",
    "indonesian zombie films": "أفلام زومبي إندونيسية",
    "iranian romantic drama films": "أفلام رومانسية درامية إيرانية",
    "irish fantasy films": "أفلام فانتازيا أيرلندية",
    "irish films": "أفلام أيرلندية",
    "irish speculative fiction films": "أفلام خيالية تأملية أيرلندية",
    "irish thriller films": "أفلام إثارة أيرلندية",
    "italian comedy films": "أفلام كوميدية إيطالية",
    "italian zombie films": "أفلام زومبي إيطالية",
    "japanese films": "أفلام يابانية",
    "japanese heist films": "أفلام سرقة يابانية",
    "kuwaiti short films": "أفلام قصيرة كويتية",
    "latvian films": "أفلام لاتفية",
    "malaysian sports films": "أفلام رياضية ماليزية",
    "mexican crime thriller films": "أفلام إثارة وجريمة مكسيكية",
    "mexican independent films": "أفلام مستقلة مكسيكية",
    "moroccan musical films": "أفلام موسيقية مغربية",
    "nigerian musical drama films": "أفلام موسيقية درامية نيجيرية",
    "north korean drama films": "أفلام درامية كورية شمالية",
    "norwegian comedy-drama films": "أفلام كوميدية درامية نرويجية",
    "philippine kung fu films": "أفلام كونغ فو فلبينية",
    "polish crime thriller films": "أفلام إثارة وجريمة بولندية",
    "polish epic films": "أفلام ملحمية بولندية",
    "polish television-seasons": "مواسم تلفزيونية بولندية",
    "portuguese adult animated films": "أفلام رسوم متحركة للكبار برتغالية",
    "portuguese fantasy films": "أفلام فانتازيا برتغالية",
    "portuguese musical comedy films": "أفلام كوميدية موسيقية برتغالية",
    "romanian films": "أفلام رومانية",
    "russian sports drama films": "أفلام رياضية درامية روسية",
    "saudiarabian films": "أفلام سعودية",
    "serbian crime television series": "مسلسلات تلفزيونية جريمة صربية",
    "slovenian animated films": "أفلام رسوم متحركة سلوفينية",
    "south korean sequel films": "أفلام متممة كورية جنوبية",
    "soviet drama films": "أفلام درامية سوفيتية",
    "soviet films": "أفلام سوفيتية",
    "soviet short films": "أفلام قصيرة سوفيتية",
    "spanish action films": "أفلام حركة إسبانية",
    "spanish documentary films": "أفلام وثائقية إسبانية",
    "spanish films": "أفلام إسبانية",
    "spanish independent films": "أفلام مستقلة إسبانية",
    "spanish war drama films": "أفلام حربية درامية إسبانية",
    "swedish 3d films": "أفلام ثلاثية الأبعاد سويدية",
    "venezuelan silent short films": "أفلام قصيرة صامته فنزويلية",
}

fast_data_no_nat = {
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
    "melodrama films": "أفلام ميلودراما",
}


@pytest.mark.parametrize("category, expected", fast_data_no_nat.items(), ids=fast_data_no_nat.keys())
@pytest.mark.fast
def test_resolve_films_no_nat(category: str, expected: str) -> None:
    label = main_films_resolvers(category)
    assert label == expected


to_test = [
    ("with_nat_tyty", fast_data_with_nat, main_films_resolvers),
    ("no_nat_tyty", fast_data_no_nat, main_films_resolvers),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
