"""
Tests
"""

import pytest

from ArWikiCats.make_bots.languages_bot.langs_w import Lang_work
# from ArWikiCats.make_bots.languages_bot.resolve_languages_new import resolve_languages_labels as Lang_work

test_data = {
    "Category:Persian-language singers of Tajikistan": "تصنيف:مغنون باللغة الفارسية في طاجيكستان",
    "Category:2010 Tamil-language television seasons": "تصنيف:مواسم تلفزيونية باللغة التاميلية 2010",
    "Category:Urdu-language fiction": "تصنيف:خيالية باللغة الأردية",
    "Category:Cantonese-language singers": "تصنيف:مغنون باللغة الكانتونية",
    "Category:Yiddish-language singers of Austria": "تصنيف:مغنون باللغة اليديشية في النمسا",
    "Category:Yiddish-language singers of Russia": "تصنيف:مغنون باللغة اليديشية في روسيا",
    "Category:Tajik-language singers of Russia": "تصنيف:مغنون باللغة الطاجيكية في روسيا",
    "Category:Persian-language singers of Russia": "تصنيف:مغنون باللغة الفارسية في روسيا",
    "Category:Hebrew-language singers of Russia": "تصنيف:مغنون باللغة العبرية في روسيا",
    "Category:German-language singers of Russia": "تصنيف:مغنون باللغة الألمانية في روسيا",
    "Category:Azerbaijani-language singers of Russia": "تصنيف:مغنون باللغة الأذربيجانية في روسيا",
    "category:urdu-language non-fiction writers": "تصنيف:كتاب غير روائيين باللغة الأردية",
    "bengali-language romantic comedy films": "أفلام كوميدية رومانسية باللغة البنغالية",
    "cantonese-language speculative fiction films": "أفلام خيالية تأملية باللغة الكانتونية"

}


def test_sample_jobs_mens_data() -> None:
    result = Lang_work("abkhazian-language writers")
    assert result == "كتاب باللغة الأبخازية"
