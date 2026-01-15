#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "middle eastern traditional music": "موسيقى تقليدية شرق أوسطي",
    "korean traditional music": "موسيقى تقليدية كوري",
    "Christian rock songs": "تصنيف:أغاني روك مسيحي",
    "danish dance songs": "تصنيف:أغاني رقص دنماركي",
    "hong kong rock songs": "تصنيف:أغاني روك هونغ كونغي",
    "irish pop songs": "تصنيف:أغاني بوب أيرلندي",
    "taiwanese hip hop": "تصنيف:هيب هوب تايواني",
    "australian electronic dance music": "",
    "austrian rock": "تصنيف:روك نمساوي",
    "english country music": "تصنيف:كانتري إنجليزي",
    "Category:Bengali folk songs": "تصنيف:أغاني فولك بنغالي",
    "Category:Indian folk songs": "تصنيف:أغاني فولك هندي",
    "Category:American rock music": "تصنيف:موسيقى الروك أمريكي",
    "Category:Danish country music": "تصنيف:كانتري دنماركي",
    "Category:Estonian rock music": "تصنيف:موسيقى الروك إستوني",
    "Category:French electronic songs": "تصنيف:أغاني إليكترونيك فرنسي",
    "Category:Mongolian traditional music": "تصنيف:موسيقى تقليدية منغولي",
    "Category:Serbian hip-hop": "تصنيف:هيب هوب صربي",
    "Christian country music": "تصنيف:كانتري مسيحي",
    "Christian electronic dance music songs": "تصنيف:أغاني موسيقى الرقص الإلكترونية مسيحي",
    "Christian electronic dance music": "تصنيف:موسيقى الرقص الإلكترونية مسيحي",
    "Christian hip-hop songs": "تصنيف:أغاني هيب هوب مسيحي",
    "Christian hip-hop": "تصنيف:هيب هوب مسيحي",
    "Christian R&B": "تصنيف:ريذم أند بلوز مسيحي",
    "Jewish dance": "تصنيف:رقص يهودي",
    "Jewish folk songs": "تصنيف:أغاني فولك يهودي",
    "Jewish hip-hop": "تصنيف:هيب هوب يهودي",
    "Jewish rock songs": "تصنيف:أغاني روك يهودي",
    "Jewish rock": "تصنيف:روك يهودي",
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
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.skip2
def test_peoples(name: str, data: dict[str, str]) -> None:
    """
    Run a dumped comparison of resolved Arabic labels for a dataset and assert there are no differences.

    Parameters:
        name (str): Identifier used when writing the diff output.
        data (dict[str, str]): Mapping from English category strings to expected Arabic label strings.

    Raises:
        AssertionError: If the computed diff does not match the expected result.
    """
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
