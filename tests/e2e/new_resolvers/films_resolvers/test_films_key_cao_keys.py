"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar

fast_data_drama = {
    "2010 in animation": "رسوم متحركة في 2010",
    "Non-fiction works about the United States Army": "أعمال غير خيالية عن القوات المسلحة الأمريكية",
    "lists of non-fiction works": "قوائم أعمال غير خيالية",
    "non-fiction works about crime in canada": "أعمال غير خيالية عن جريمة في كندا",
    "non-fiction works about espionage": "أعمال غير خيالية عن التجسس",
    "non-fiction works about law in canada": "أعمال غير خيالية عن قانون في كندا",
    "non-fiction works about serial killers": "أعمال غير خيالية عن قتلة متسلسلون",
    "non-fiction works about united states air force": "أعمال غير خيالية عن القوات الجوية الأمريكية",
    "non-fiction works about united states navy": "أعمال غير خيالية عن البحرية الأمريكية",
    "non-fiction works": "أعمال غير خيالية",
    "Clubs in Hong Kong": "أندية في هونغ كونغ",
}


@pytest.mark.parametrize("category, expected", fast_data_drama.items(), ids=fast_data_drama.keys())
@pytest.mark.fast
def test_fast_data_drama(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
