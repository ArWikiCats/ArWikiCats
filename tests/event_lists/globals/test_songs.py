#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data1 = {
    "middle eastern traditional music": "موسيقى تقليدية شرق أوسطي",
    "korean traditional music": "موسيقى تقليدية كوري",
    "Christian rock songs": "أغاني روك مسيحي",
    "danish dance songs": "أغاني رقص دنماركي",
    "hong kong rock songs": "أغاني روك هونغ كونغي",
    "irish pop songs": "أغاني بوب أيرلندي",
    "taiwanese hip hop": "هيب هوب تايواني",
    "australian electronic dance music": "",
    "austrian rock": "روك نمساوي",
    "english country music": "كانتري إنجليزي",
    "Bengali folk songs": "أغاني فولك بنغالي",
    "Indian folk songs": "أغاني فولك هندي",
    "American rock music": "موسيقى الروك أمريكي",
    "Danish country music": "كانتري دنماركي",
    "Estonian rock music": "موسيقى الروك إستوني",
    "French electronic songs": "أغاني إليكترونيك فرنسي",
    "Mongolian traditional music": "موسيقى تقليدية منغولي",
    "Serbian hip-hop": "هيب هوب صربي",
    "Christian country music": "كانتري مسيحي",
    "Christian electronic dance music songs": "أغاني موسيقى الرقص الإلكترونية مسيحي",
    "Christian electronic dance music": "موسيقى الرقص الإلكترونية مسيحي",
    "Christian hip-hop songs": "أغاني هيب هوب مسيحي",
    "Christian hip-hop": "هيب هوب مسيحي",
    "Christian R&B": "ريذم أند بلوز مسيحي",
    "Jewish dance": "رقص يهودي",
    "Jewish folk songs": "أغاني فولك يهودي",
    "Jewish hip-hop": "هيب هوب يهودي",
    "Jewish rock songs": "أغاني روك يهودي",
    "Jewish rock": "روك يهودي",
}

to_test = [
    ("test_songs_1", data1),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.skip2
def test_songs_1(category: str, expected: str) -> None:
    """
    Run a single assertion that resolving the Arabic category label for `category` matches `expected`.

    Parameters:
        category (str): English category string to resolve.
        expected (str): Expected Arabic label for `category`.

    """
    label = resolve_label_ar(category)
    assert label == expected


from utils.dump_runner import make_dump_test_name_data

test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
