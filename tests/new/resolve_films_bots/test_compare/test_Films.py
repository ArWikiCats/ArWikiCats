
"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats.new.resolve_films_bots.film_keys_bot import Films
from ArWikiCats.new.resolve_films_bots.resolve_films_labels import _get_films_key_tyty_new

test_data = {

    "3d comics": "قصص مصورة ثلاثية الأبعاد",
    "3d film series": "سلاسل أفلام ثلاثية الأبعاد",
    "3d soap opera": "مسلسلات طويلة ثلاثية الأبعاد",
    "3d television episodes": "حلقات تلفزيونية ثلاثية الأبعاد",
    "3d television films": "أفلام تلفزيونية ثلاثية الأبعاد",
    "3d television miniseries": "مسلسلات قصيرة ثلاثية الأبعاد",
    "3d television news": "أخبار تلفزيونية ثلاثية الأبعاد",
    "3d television programmes": "برامج تلفزيونية ثلاثية الأبعاد",
    "3d television programs": "برامج تلفزيونية ثلاثية الأبعاد",
    "3d television series": "مسلسلات تلفزيونية ثلاثية الأبعاد",
    "3d video games": "ألعاب فيديو ثلاثية الأبعاد",
    "3d web series": "مسلسلات ويب ثلاثية الأبعاد",
    "4d comics": "قصص مصورة رباعية الأبعاد",
    "4d film series": "سلاسل أفلام رباعية الأبعاد",
    "4d soap opera": "مسلسلات طويلة رباعية الأبعاد",
    "4d television episodes": "حلقات تلفزيونية رباعية الأبعاد",
    "4d television films": "أفلام تلفزيونية رباعية الأبعاد",
    "4d television miniseries": "مسلسلات قصيرة رباعية الأبعاد",
    "4d television news": "أخبار تلفزيونية رباعية الأبعاد",
    "4d television programmes": "برامج تلفزيونية رباعية الأبعاد",
    "4d television programs": "برامج تلفزيونية رباعية الأبعاد",
    "4d television series": "مسلسلات تلفزيونية رباعية الأبعاد",
    "4d video games": "ألعاب فيديو رباعية الأبعاد",
    "4d web series": "مسلسلات ويب رباعية الأبعاد",
    "action comedy comics": "قصص مصورة حركة كوميدية",
    "action comedy film series": "سلاسل أفلام حركة كوميدية",
    "action comedy soap opera": "مسلسلات طويلة حركة كوميدية",
    "action comedy television episodes": "حلقات تلفزيونية حركة كوميدية",
    "action comedy television films": "أفلام تلفزيونية حركة كوميدية",
    "action comedy television miniseries": "مسلسلات قصيرة حركة كوميدية",
    "action comedy television news": "أخبار تلفزيونية حركة كوميدية",
    "action comedy television programmes": "برامج تلفزيونية حركة كوميدية",
    "action comedy television programs": "برامج تلفزيونية حركة كوميدية",
    "action comedy television series": "مسلسلات تلفزيونية حركة كوميدية",
    "action comedy video games": "ألعاب فيديو حركة كوميدية",
    "action comedy web series": "مسلسلات ويب حركة كوميدية",
    "action comics": "قصص مصورة حركة",
    "action film series": "سلاسل أفلام حركة",
    "action films": "أفلام حركة",
    "action soap opera": "مسلسلات طويلة حركة",
    "action television episodes": "حلقات تلفزيونية حركة",
    "action television films": "أفلام تلفزيونية حركة",
    "action television miniseries": "مسلسلات قصيرة حركة",
    "action television news": "أخبار تلفزيونية حركة",
    "action television programmes": "برامج تلفزيونية حركة",
    "action television programs": "برامج تلفزيونية حركة",
    "action television series": "مسلسلات تلفزيونية حركة",
    "action thriller comics": "قصص مصورة إثارة حركة",
    "action thriller film series": "سلاسل أفلام إثارة حركة",
    "action thriller soap opera": "مسلسلات طويلة إثارة حركة",
    "adventure films": "أفلام مغامرات",
    "animated films": "أفلام رسوم متحركة",
    "animation": "رسوم متحركة",
    "anime and manga characters": "شخصيات أنمي ومانغا",
    "anime films": "أفلام أنمي",
    "anthology films": "أفلام أنثولوجيا",
    "black comedy films": "أفلام كوميدية سوداء",
    "buddy films": "أفلام رفقاء",
    "clubs": "أندية",
    "comedy films": "أفلام كوميدية",
    "comics characters": "شخصيات قصص مصورة",
    "comics images": "صور قصص مصورة",
    "crime films": "أفلام جريمة",
    "dark fantasy films": "أفلام فانتازيا مظلمة",
    "documentary films": "أفلام وثائقية",
    "epic films": "أفلام ملحمية",
    "fantasy films": "أفلام فانتازيا",
    "horror films": "أفلام رعب",
    "melodrama films": "أفلام ميلودراما",
    "music": "موسيقى",
    "mystery film series": "سلاسل أفلام غموض",
    "parody films": "أفلام ساخرة",
    "police procedural films": "أفلام إجراءات الشرطة",
    "science fiction thriller films": "أفلام إثارة خيال علمي",
    "soap opera": "مسلسلات طويلة",
    "thriller films": "أفلام إثارة",
    "war films": "أفلام حربية",
    "webcomic": "ويب كومكس",
}


@pytest.mark.parametrize("category, expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_Films(category: str, expected: str) -> None:
    label = Films(category)
    assert label == expected


to_test = [
    ("test_Films", test_data, Films),
    ("test_Films_tyty", test_data, _get_films_key_tyty_new),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_resolve_films_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
