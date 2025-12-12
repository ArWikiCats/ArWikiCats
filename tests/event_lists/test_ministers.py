#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

examples = {
    "Category:Housing ministers of Abkhazia": "تصنيف:وزراء إسكان أبخازيا",
    "Category:Ministers of Housing of Abkhazia": "تصنيف:وزراء إسكان أبخازيا",
    "Category:Ministers for Housing of Abkhazia": "تصنيف:وزراء إسكان أبخازيا",
    "Category:Public works ministers of Catalonia": "تصنيف:وزراء أشغال عامة في كتالونيا",
    "Category:Ministers for Public Works of Luxembourg": "تصنيف:وزراء أشغال عامة في لوكسمبورغ",
    "Category:Ministers of Economics of Latvia": "تصنيف:وزراء الاقتصاد في لاتفيا",
    "Category:Economy ministers of Latvia": "تصنيف:وزراء اقتصاد لاتفيا",
    "Category:Religious affairs ministers of Yemen": "تصنيف:وزراء شؤون دينية في اليمن",
    "Category:Ministers of Religious Affairs of the Netherlands": "تصنيف:وزراء شؤون دينية في هولندا",
    "Category:Women government ministers of Latvia": "تصنيف:وزيرات لاتفيا",
    "Category:Women's ministers of Fiji": "تصنيف:وزيرات فيجي",
    "Category:Ministers for Foreign Affairs of Abkhazia": "تصنيف:وزراء شؤون خارجية في أبخازيا",
    "Category:Ministers for Foreign Affairs of Singapore": "تصنيف:وزراء شؤون خارجية في سنغافورة",
    "Category:Ministers for Foreign Affairs of Luxembourg": "تصنيف:وزراء شؤون خارجية في لوكسمبورغ",
    "Category:Ministers for Internal Affairs of Abkhazia": "تصنيف:وزراء شؤون داخلية في أبخازيا",
    "Category:Ministers of Labour and Social Security of Turkey": "تصنيف:وزراء عمل وضمان اجتماعي في تركيا"
}

TEMPORAL_CASES = [
    ("test_ministers", examples),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.fast
def test_ministers(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
