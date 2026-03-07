"""
Tests
"""

import pytest

# from ArWikiCats.new_resolvers.jobs_resolvers.mens import mens_resolver_labels
from ArWikiCats import resolve_label_ar


test_data2 = {
    "19th-century American male singers": "مغنون ذكور أمريكيون في القرن 19",
    "19th-century Austrian male musicians": "موسيقيون ذكور نمساويون في القرن 19",
    "19th-century Swiss male opera singers": "مغنو أوبرا ذكور سويسريون في القرن 19",
    "20th-century Democratic Republic of Congo male singers": "مغنون ذكور كونغويون ديمقراطيون في القرن 20",
    "20th-century Ukrainian male singers": "مغنون ذكور أوكرانيون في القرن 20",
    "21st-century Chilean male artists": "فنانون ذكور تشيليون في القرن 21",
    "21st-century male actors from Georgia (country)": "ممثلون ذكور من جورجيا في القرن 21"
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
@pytest.mark.fast
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = resolve_label_ar(category)
    assert result == expected
