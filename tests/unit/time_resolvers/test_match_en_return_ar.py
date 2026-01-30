# test_convert_time_to_arabic.py
import pytest

from ArWikiCats.time_formats.time_to_arabic import match_en_return_ar

en_return_ar = {
    "Category:2020s in Yemen": {"2020s": "عقد 2020"},
    "events from 2010s to 2025": {"2010s": "عقد 2010", "2025": "2025"},
    "March 1917 events": {"March 1917": "مارس 1917"},
    "2020s in space": {"2020s": "عقد 2020"},
    "1990–91 in football": {"1990–91": "1990–91"},
    "events from 2020 to 2025": {"2020": "2020", "2025": "2025"},
    "2012-2013 in football": {"2012-2013": "2012-2013"},
    "2012-13 in football": {"2012-13": "2012-13"},
    "Category:10s": {"10s": "عقد 10"},
    "Category:10s BC": {"10s BC": "عقد 10 ق م"},
    "Category:10s BC births": {"10s BC": "عقد 10 ق م"},
    "Category:10s BC conflicts": {"10s BC": "عقد 10 ق م"},
    "Category:10s BC deaths": {"10s BC": "عقد 10 ق م"},
    "Category:Bridges completed in the 19th century": {"19th century": "القرن 19"},
    "Category:Bridges completed in the 1st century": {"1st century": "القرن 1"},
    "Category:Bridges completed in the 1st millennium": {"1st millennium": "الألفية 1"},
    "Category:Bridges completed in the 2000s": {"2000s": "عقد 2000"},
    "Category:Bridges completed in the 2010s": {"2010s": "عقد 2010"},
    "Category:Bridges completed in the 2020s": {"2020s": "عقد 2020"},
    "Category:Bridges completed in the 20th century": {"20th century": "القرن 20"},
    "Category:Bridges completed in the 21st century": {"21st century": "القرن 21"},
    "Category:Bridges completed in the 2nd century": {"2nd century": "القرن 2"},
    "Category:Bridges completed in the 2nd millennium": {"2nd millennium": "الألفية 2"},
    "Category:Bridges completed in the 7th century": {"7th century": "القرن 7"},
    "Category:Bridges completed in the 2nd millennium BC": {"2nd millennium BC": "الألفية 2 ق م"},
    "Category:Bridges completed in the 2nd century BC": {"2nd century BC": "القرن 2 ق م"},
    "Category:Bridges completed in the 1st century BC": {"1st century BC": "القرن 1 ق م"},
    "Category:Bridges completed in the 1st millennium BC": {"1st millennium BC": "الألفية 1 ق م"},
    "Category:Bridges completed in the 4th century BC": {"4th century BC": "القرن 4 ق م"},
    "Category:Bridges completed in the 4th-century BCE": {"4th-century BCE": "القرن 4 ق م"},
    "Category:7th-century BC disestablishments": {"7th-century BC": "القرن 7 ق م"},
    "Category:19th century-related lists": {"19th century": "القرن 19"},
    "Category:19th-century Afghan monarchs": {"19th-century": "القرن 19"},
    "Category:21st-century Afghan monarchs": {"21st-century": "القرن 21"},
    "Category:7th centuryBC Afghan monarchs": {"7th centuryBC": "القرن 7 ق م"},
    "Category:January events": {},
}


@pytest.mark.parametrize("en_text, expected", en_return_ar.items(), ids=en_return_ar.keys())
@pytest.mark.fast
def test_match_en_return_ar(en_text: str, expected: dict[str, str]) -> None:
    """Test various English time expressions for correct Arabic conversion."""
    result = match_en_return_ar(en_text)
    assert result == expected, f"{en_text} → {result}, {expected=}"
