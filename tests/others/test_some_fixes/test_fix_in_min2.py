#
import pytest

from ArWikiCats import resolve_label_ar

data_2 = {
    # NEED FIXING
    # "2020 Chinese Taipei international footballers from Hong Kong": "لاعبو منتخب تايبيه الصينية لكرة القدم من هونغ كونغ في 2020",
    "2020 Chinese Taipei international footballers from Hong Kong": "لاعبو كرة قدم دوليون تايبيون صينيون من هونغ كونغ في 2020",
    "14th-century writers from Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
    "14th-century writers from the Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
}


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_fix_in_min_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category, fix_label=False)
    assert label == expected
