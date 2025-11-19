"""
Tests
"""
import pytest

from src.make2_bots.o_bots.popl import work_peoples, make_people_lab, work_peoples_old

fast_data = {
    "christina aguilera video albums": "ألبومات فيديو كريستينا أغيليرا",
    "ed sheeran albums": "ألبومات إد شيران",
    "a. r. rahman albums": "ألبومات أي.أر. رحمان",
    "george h. w. bush administration cabinet members": "أعضاء مجلس وزراء إدارة جورج بوش الأب",
    "george h. w. bush administration personnel": "موظفو إدارة جورج بوش الأب",
    "george w. bush administration cabinet members": "أعضاء مجلس وزراء إدارة جورج دبليو بوش",
    "george w. bush administration personnel": "موظفو إدارة جورج دبليو بوش",
    "john quincy adams administration cabinet members": "أعضاء مجلس وزراء إدارة جون كوينسي آدامز",
    "john quincy adams administration personnel": "موظفو إدارة جون كوينسي آدامز",
    "lyndon b. johnson administration cabinet members": "أعضاء مجلس وزراء إدارة ليندون جونسون",
    "lyndon b. johnson administration personnel": "موظفو إدارة ليندون جونسون",
    "nusrat fateh ali khan albums": "ألبومات نصرت فتح علي خان",
    "pope john paul ii albums": "ألبومات يوحنا بولس الثاني",
    "william henry harrison administration cabinet members": "أعضاء مجلس وزراء إدارة ويليام هنري هاريسون",
    "william henry harrison administration personnel": "موظفو إدارة ويليام هنري هاريسون",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = work_peoples(category)
    assert label.strip() == expected

    label2 = work_peoples_old(category)
    assert label == label2


def test_work_peoples():
    # Test with a basic input
    result = work_peoples("test people")
    assert isinstance(result, str)

    result_empty = work_peoples("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = work_peoples("some suffix")
    assert isinstance(result_various, str)


def test_make_people_lab():
    # Test with a basic input
    result = make_people_lab("people")
    assert isinstance(result, str)

    result_empty = make_people_lab("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = make_people_lab("actors")
    assert isinstance(result_various, str)
