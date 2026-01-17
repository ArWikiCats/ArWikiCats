"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.films_resolvers import main_films_resolvers

data_0 = {
    "music albums": "ألبومات موسيقية",
    "christmas albums": "ألبومات عيد الميلاد",
    "science fiction works": "أعمال خيال علمي",
    "sports clubs": "أندية رياضية",
    "sports competitions": "منافسات رياضية",
    "sports executives": "مدراء رياضية",
    "sports films": "أفلام رياضية",
    "sports logos": "شعارات رياضية",
    "television logos": "شعارات تلفزيونية",
    "sailing competitions": "منافسات إبحار",
    "speculative fiction works": "أعمال خيالية تأملية",
    "sports television series": "مسلسلات تلفزيونية رياضية",
    "religious organizations": "منظمات دينية",
    "speculative fiction short stories": "قصص قصيرة خيالية تأملية",
}

fast_data_drama_cao = {
    "3d films": "أفلام ثلاثية الأبعاد",
    "action films": "أفلام حركة",
    "adult animated films": "أفلام رسوم متحركة للكبار",
    "adventure films": "أفلام مغامرات",
    "adventure novels": "روايات مغامرات",
    "animated films": "أفلام رسوم متحركة",
    "anime films": "أفلام أنمي",
    "anthology films": "أفلام أنثولوجيا",
    "apocalyptic television episodes": "حلقات تلفزيونية نهاية العالم",
    "black comedy films": "أفلام كوميدية سوداء",
    "buddy films": "أفلام رفقاء",
    "children's animated television series": "مسلسلات تلفزيونية رسوم متحركة أطفال",
    "children's television series": "مسلسلات تلفزيونية أطفال",
    "children's television shows": "عروض تلفزيونية أطفال",
    "comedy drama television series": "مسلسلات تلفزيونية كوميدية درامية",
    "comedy films": "أفلام كوميدية",
    "comedy television series": "مسلسلات تلفزيونية كوميدية",
    "comedy thriller films": "أفلام كوميدية إثارة",
    "comedy-drama films": "أفلام كوميدية درامية",
    "crime films": "أفلام جريمة",
    "dark fantasy films": "أفلام فانتازيا مظلمة",
    "disaster films": "أفلام كوارثية",
    "docudrama films": "أفلام درامية وثائقية",
    "documentary films": "أفلام وثائقية",
    "drama films": "أفلام درامية",
    "drama television series": "مسلسلات تلفزيونية درامية",
    "epic films": "أفلام ملحمية",
    "epic television series": "مسلسلات تلفزيونية ملحمية",
    "erotic thriller films": "أفلام إثارة جنسية",
    "fantasy films": "أفلام فانتازيا",
    "fantasy novels": "روايات فانتازيا",
    "heist films": "أفلام سرقة",
    "horror films": "أفلام رعب",
    "horror novels": "روايات رعب",
    "horror television series": "مسلسلات تلفزيونية رعب",
    "independent films": "أفلام مستقلة",
    "kung fu films": "أفلام كونغ فو",
    "live television shows": "عروض تلفزيونية مباشرة",
    "melodrama films": "أفلام ميلودراما",
    "military television series": "مسلسلات تلفزيونية عسكرية",
    "music television series": "مسلسلات تلفزيونية موسيقية",
    "music television shows": "عروض تلفزيونية موسيقية",
    "musical comedy films": "أفلام كوميدية موسيقية",
    "mystery film series": "سلاسل أفلام غموض",
    "mystery films": "أفلام غموض",
    "mystery television series": "مسلسلات تلفزيونية غموض",
    "parody films": "أفلام ساخرة",
    "police procedural films": "أفلام إجراءات الشرطة",
    "police procedural television series": "مسلسلات تلفزيونية إجراءات الشرطة",
    "political television series": "مسلسلات تلفزيونية سياسية",
    "prequel films": "أفلام بادئة",
    "reality television series": "مسلسلات تلفزيونية واقعية",
    "robot films": "أفلام آلية",
    "science fiction films": "أفلام خيال علمي",
    "science fiction novels": "روايات خيال علمي",
    "science fiction thriller films": "أفلام إثارة خيال علمي",
    "sequel films": "أفلام متممة",
    "short films": "أفلام قصيرة",
    "silent short films": "أفلام قصيرة صامته",
    "speculative fiction films": "أفلام خيالية تأملية",
    "speculative fiction novels": "روايات خيالية تأملية",
    "teen television series": "مسلسلات تلفزيونية مراهقة",
    "thriller films": "أفلام إثارة",
    "thriller novels": "روايات إثارة",
    "war films": "أفلام حربية",
    "war television series": "مسلسلات تلفزيونية حربية",
    "zombie films": "أفلام زومبي",
}


@pytest.mark.parametrize("category, expected", fast_data_drama_cao.items(), ids=fast_data_drama_cao.keys())
@pytest.mark.fast
def test_get_films_key_cao(category: str, expected: str) -> None:
    label = main_films_resolvers(category)
    assert label == expected
