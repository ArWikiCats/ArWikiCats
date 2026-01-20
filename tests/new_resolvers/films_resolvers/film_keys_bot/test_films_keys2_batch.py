#
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.films_resolvers import main_films_resolvers

data_1 = {
    "3d comics": "قصص مصورة ثلاثية الأبعاد",
    "3d film series": "سلاسل أفلام ثلاثية الأبعاد",
    "3d soap opera": "مسلسلات طويلة ثلاثية الأبعاد",
    "3d television episodes": "حلقات تلفزيونية ثلاثية الأبعاد",
    "3d television films": "أفلام تلفزيونية ثلاثية الأبعاد",
    "3d television miniseries": "مسلسلات قصيرة تلفزيونية ثلاثية الأبعاد",
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
    "4d television miniseries": "مسلسلات قصيرة تلفزيونية رباعية الأبعاد",
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
    "action comedy television miniseries": "مسلسلات قصيرة تلفزيونية حركة كوميدية",
    "action comedy television news": "أخبار تلفزيونية حركة كوميدية",
    "action comedy television programmes": "برامج تلفزيونية حركة كوميدية",
    "action comedy television programs": "برامج تلفزيونية حركة كوميدية",
    "action comedy television series": "مسلسلات تلفزيونية حركة كوميدية",
    "action comedy video games": "ألعاب فيديو حركة كوميدية",
    "action comedy web series": "مسلسلات ويب حركة كوميدية",
    "action comics": "قصص مصورة حركة",
    "action film series": "سلاسل أفلام حركة",
    "action soap opera": "مسلسلات طويلة حركة",
    "action television episodes": "حلقات تلفزيونية حركة",
    "action television films": "أفلام تلفزيونية حركة",
    "action television miniseries": "مسلسلات قصيرة تلفزيونية حركة",
    "action television news": "أخبار تلفزيونية حركة",
    "action television programmes": "برامج تلفزيونية حركة",
    "action television programs": "برامج تلفزيونية حركة",
    "action television series": "مسلسلات تلفزيونية حركة",
    "action thriller comics": "قصص مصورة إثارة حركة",
    "action thriller film series": "سلاسل أفلام إثارة حركة",
    "action thriller soap opera": "مسلسلات طويلة إثارة حركة",
}

data_2 = {
    "yemeni children's-animated-adventure-television films": "أفلام مغامرات رسوم متحركة تلفزيونية يمنية للأطفال",
    "children's-animated-adventure-television films": "أفلام مغامرات رسوم متحركة تلفزيونية للأطفال",
    "action television characters": "شخصيات تلفزيونية حركة",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_films_keys2_batch_1(category: str, expected: str) -> None:
    label = main_films_resolvers(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_films_keys2_batch_1", data_1, main_films_resolvers),
    # ("test_films_keys2_batch_2", data_1, resolve_label_ar),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: callable) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
