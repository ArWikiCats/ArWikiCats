""" """

from __future__ import annotations

import pytest

from ArWikiCats import resolve_label_ar

data_1 = {
    "Adaptations of works by Albanian writers": "أعمال مقتبسة عن أعمال كتاب ألبان",
    "Adaptations of works by Estonian writers": "أعمال مقتبسة عن أعمال كتاب إستونيون",
    "Adaptations of works by Greek writers": "أعمال مقتبسة عن أعمال كتاب يونانيون",
    "Adaptations of works by Irish writers": "أعمال مقتبسة عن أعمال كتاب أيرلنديون",
    "Adaptations of works by Italian writers": "أعمال مقتبسة عن أعمال كتاب إيطاليون",
    "Alternative rock albums by American artists": "ألبومات روك بديل بواسطة فنانون أمريكيون",
    "Alternative rock albums by Bosnia and Herzegovina artists": "ألبومات روك بديل بواسطة فنانون بوسنيون",
    "Black metal albums by Singaporean artists": "ألبومات بلاك ميتال بواسطة فنانون سنغافوريون",
    "Christian music albums by South African artists": "ألبومات موسيقى مسيحية بواسطة فنانون جنوب إفريقيون",
    "Christian rock albums by South African artists": "ألبومات روك مسيحي بواسطة فنانون جنوب إفريقيون",
    "Compilation albums by Spanish artists": "ألبومات تجميعية بواسطة فنانون إسبان",
    "Dance music albums by Hong Kong artists": "ألبومات موسيقى الرقص بواسطة فنانون هونغ كونغيون",
    "Dance music albums by Swiss artists": "ألبومات موسيقى الرقص بواسطة فنانون سويسريون",
    "Electronic albums by Iranian artists": "ألبومات إليكترونيك بواسطة فنانون إيرانيون",
    "Films by South African directors": "أفلام مخرجون جنوب إفريقيون",
    "Films by South African producers": "أفلام منتجون جنوب إفريقيون",
    "Funk albums by Danish artists": "ألبومات فانك بواسطة فنانون دنماركيون",
    "Hardcore punk albums by British artists": "ألبومات هاردكور بانك بواسطة فنانون بريطانيون",
    "Indie rock albums by Danish artists": "ألبومات إيندي روك بواسطة فنانون دنماركيون",
    "Indie rock albums by Manx artists": "ألبومات إيندي روك بواسطة فنانون مانكسيون",
    "Indie rock albums by South African artists": "ألبومات إيندي روك بواسطة فنانون جنوب إفريقيون",
    "Pop albums by Czech artists": "ألبومات بوب بواسطة فنانون تشيكيون",
    "Prisoners sentenced to death by Papua New Guinea": "مسجونون حكم عليهم بالإعدام بواسطة بابوا غينيا الجديدة",
    "Synth-pop albums by Danish artists": "ألبومات سينثبوب بواسطة فنانون دنماركيون",
    "Thrash metal albums by English artists": "ألبومات ثراش ميتال بواسطة فنانون إنجليز",
    "Video albums by Welsh artists": "ألبومات فيديو بواسطة فنانون ويلزيون",
    "Works by British classical composers": "أعمال ملحنون كلاسيكيون بريطانيون",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_by_people_or_job(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
