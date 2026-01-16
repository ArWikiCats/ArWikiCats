"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.o_bots.peoples_resolver import make_people_lab, work_peoples, work_peoples_old

fast_data = {
    "andrew johnson administration cabinet members": "أعضاء مجلس وزراء إدارة أندرو جونسون",
    "andrew johnson administration personnel": "موظفو إدارة أندرو جونسون",
    "william henry harrison administration cabinet members": "أعضاء مجلس وزراء إدارة ويليام هنري هاريسون",
    "william henry harrison administration personnel": "موظفو إدارة ويليام هنري هاريسون",
    "woodrow wilson administration cabinet members": "أعضاء مجلس وزراء إدارة وودرو ويلسون",
    "woodrow wilson administration personnel": "موظفو إدارة وودرو ويلسون",
    "adele video albums": "ألبومات فيديو أديل",
    "adriano celentano albums": "ألبومات أدريانو تشيلنتانو",
    "ai weiwei albums": "ألبومات آي ويوي",
    "akon albums": "ألبومات إيكون",
    "alanis morissette albums": "ألبومات ألانيس موريسيت",
    "alanis morissette video albums": "ألبومات فيديو ألانيس موريسيت",
    "aldous huxley albums": "ألبومات ألدوس هكسلي",
    "alexandra stan albums": "ألبومات ألكسندرا ستان",
    "alice cooper albums": "ألبومات أليس كوبر",
    "james brown albums": "ألبومات جيمس براون",
    "james taylor albums": "ألبومات جيمس تايلور",
    "james taylor video albums": "ألبومات فيديو جيمس تايلور",
    "jamie foxx albums": "ألبومات جيمي فوكس",
    "janet jackson albums": "ألبومات جانيت جاكسون",
    "janet jackson video albums": "ألبومات فيديو جانيت جاكسون",
    "janis joplin albums": "ألبومات جانيس جوبلين",
    "jason derulo albums": "ألبومات جيسون ديرولو",
    "jason mraz albums": "ألبومات جيسون مراز",
    "alicia keys albums": "ألبومات أليشيا كيز",
    "christina aguilera video albums": "ألبومات فيديو كريستينا أغيليرا",
    "ed sheeran albums": "ألبومات إد شيران",
    "a. r. rahman albums": "ألبومات أي.أر. رحمان",
    "george h. w. bush administration cabinet members": "أعضاء مجلس وزراء إدارة جورج بوش الأب",
    "george h. w. bush administration personnel": "موظفو إدارة جورج بوش الأب",
    "george w. bush administration cabinet members": "أعضاء مجلس وزراء إدارة جورج بوش الابن",
    "george w. bush administration personnel": "موظفو إدارة جورج بوش الابن",
    "john quincy adams administration cabinet members": "أعضاء مجلس وزراء إدارة جون كوينسي آدامز",
    "john quincy adams administration personnel": "موظفو إدارة جون كوينسي آدامز",
    "lyndon b. johnson administration cabinet members": "أعضاء مجلس وزراء إدارة ليندون جونسون",
    "lyndon b. johnson administration personnel": "موظفو إدارة ليندون جونسون",
    "nusrat fateh ali khan albums": "ألبومات نصرت فتح علي خان",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = work_peoples(category)
    assert label == expected

    label2 = work_peoples_old(category)
    assert label == label2


def test_work_peoples() -> None:
    # Test with a basic input
    result = work_peoples("test people")
    assert isinstance(result, str)

    result_empty = work_peoples("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = work_peoples("some suffix")
    assert isinstance(result_various, str)


def test_make_people_lab() -> None:
    # Test with a basic input
    result = make_people_lab("people")
    assert isinstance(result, str)

    result_empty = make_people_lab("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = make_people_lab("actors")
    assert isinstance(result_various, str)
