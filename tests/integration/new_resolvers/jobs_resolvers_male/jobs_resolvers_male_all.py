"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers import all_new_resolvers
from utils.dump_runner import make_dump_test_name_data_callback

te4_2018_jobs_data = {
    "egyptian male sport shooters": "لاعبو رماية ذكور مصريون",
    "russian male voice actors": "ممثلو أداء صوتي ذكور روس",
    "scottish male golfers": "لاعبو غولف ذكور إسكتلنديون",
    "paraguayan male actors": "ممثلون ذكور بارغوايانيون",
    "macedonian male taekwondo practitioners": "لاعبو تايكوندو ذكور مقدونيون",
    "moroccan male mixed martial artists": "مقاتلو فنون قتالية مختلطة ذكور مغاربة",
    "irish male musicians": "موسيقيون ذكور أيرلنديون",
    "israeli male stage actors": "ممثلو مسرح ذكور إسرائيليون",
    "italian male mixed martial artists": "مقاتلو فنون قتالية مختلطة ذكور إيطاليون",
    "hungarian male opera singers": "مغنو أوبرا ذكور مجريون",
    "greek male dancers": "راقصون ذكور يونانيون",
    "german male pianists": "عازفو بيانو ذكور ألمان",
    "french male painters": "رسامون ذكور فرنسيون",
    "french male singer-songwriters": "مغنون وكتاب أغاني ذكور فرنسيون",
    "south korean male biathletes": "لاعبو بياثلون ذكور كوريون جنوبيون",
    "soviet male figure skaters": "متزلجون فنيون ذكور سوفيت",
    "spanish male biographers": "كتاب سيرة ذكور إسبان",
    "sri lankan male kabaddi players": "لاعبو كابادي ذكور سريلانكيون",
    "swedish male archers": "نبالون ذكور سويديون",
    "tunisian male fencers": "مبارزون ذكور تونسيون",
    "venezuelan male poets": "شعراء ذكور فنزويليون",
    "icelandic male athletes": "لاعبو قوى ذكور آيسلنديون",
    "icelandic male runners": "عداؤون ذكور آيسلنديون",
    "icelandic male steeplechase runners": "عداؤو موانع ذكور آيسلنديون",
    "moroccan male middle-distance runners": "عداؤو مسافات متوسطة ذكور مغاربة",
    "norwegian male pair skaters": "متزلجون فنيون على الجليد ذكور نرويجيون",
    "albanian male tennis players": "لاعبو كرة مضرب ذكور ألبان",
    "norwegian male single skaters": "متزلجون فرديون ذكور نرويجيون",
    "bulgarian male opera singers": "مغنو أوبرا ذكور بلغاريون",
    "beninese male boxers": "ملاكمون ذكور بنينيون",
    "australian male sculptors": "نحاتون ذكور أستراليون",
    "australian male sprinters": "عداؤون سريعون ذكور أستراليون",
    "canadian male biathletes": "لاعبو بياثلون ذكور كنديون",
    "canadian male kickboxers": "مقاتلو كيك بوكسنغ ذكور كنديون",
}


@pytest.mark.parametrize("category, expected", te4_2018_jobs_data.items(), ids=te4_2018_jobs_data.keys())
@pytest.mark.fast
def test_jobs_resolvers_male_all(category: str, expected: str) -> None:
    label = all_new_resolvers(category)
    assert label == expected


to_test = [
    ("jobs_resolvers_male_all", te4_2018_jobs_data, all_new_resolvers),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
