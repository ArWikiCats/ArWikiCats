#
import pytest

from ArWikiCats import resolve_label_ar

data0_no_label = {
    "Defunct Christian organizations based in United States": "تصنيف:منظمات مسيحية سابقة مقرها في الولايات المتحدة",
    "Defunct Christian schools in Canada": "تصنيف:مدارس مسيحية سابقة في كندا",
    "Defunct Christian schools in United States": "تصنيف:مدارس مسيحية سابقة في الولايات المتحدة",
    "Defunct Islamic organizations based in United States": "تصنيف:منظمات إسلامية سابقة مقرها في الولايات المتحدة",
    "Defunct Jewish organizations based in United States": "تصنيف:منظمات يهودية سابقة مقرها في الولايات المتحدة",
    "Defunct national sports teams by country": "فرق رياضية وطنية سابقة حسب البلد",
    "defunct american football venues": "ملاعب كرة قدم أمريكية سابقة",
    "defunct amusement parks": "متنزهات ملاهي سابقة",
    "defunct art museums and galleries": "متاحف فنية ومعارض سابقة",
    "defunct asian restaurants": "مطاعم آسيوية سابقة",
    "defunct athletics venues": "ملاعب ألعاب قوى سابقة",
    "defunct baseball venues": "ملاعب كرة قاعدة سابقة",
    "defunct basketball venues": "ملاعب كرة سلة سابقة",
    "defunct clubs and societies": "أندية وجمعيات سابقة",
    "defunct comedy clubs": "أندية كوميدية سابقة",
    "defunct communist parties": "أحزاب شيوعية سابقة",
    "defunct cycling races": "سباقات سباق دراجات هوائية سابقة",
    "defunct elementary schools": "مدارس إبتدائية سابقة",
    "defunct european restaurants": "مطاعم أوروبية سابقة",
    "defunct far-right political parties": "أحزاب اليمين المتطرف سابقة",
    "defunct feminist organizations": "منظمات نسوية سابقة",
    "defunct football clubs": "أندية كرة قدم سابقة",
    "defunct football venues": "ملاعب كرة قدم سابقة",
    "defunct french restaurants": "مطاعم فرنسية سابقة",
    "defunct golf tournaments": "بطولات غولف سابقة",
    "defunct high schools": "مدارس ثانوية سابقة",
    "defunct ice hockey venues": "ملاعب هوكي جليد سابقة",
    "defunct italian restaurants": "مطاعم إيطالية سابقة",
    "defunct japanese restaurants": "مطاعم يابانية سابقة",
    "defunct liberal parties": "أحزاب ليبرالية سابقة",
    "defunct lower houses": "المجالس الدنيا سابقة",
    "defunct mexican restaurants": "مطاعم مكسيكية سابقة",
    "defunct middle schools": "مدارس إعدادية سابقة",
    "defunct motorsport venues": "ملاعب رياضة محركات سابقة",
    "defunct multi-national basketball leagues": "دوريات كرة سلة متعددة الجنسيات سابقة",
    "defunct private schools": "مدارس خاصة سابقة",
    "defunct private universities and colleges": "جامعات وكليات خاصة سابقة",
    "defunct professional sports leagues": "دوريات رياضية للمحترفين سابقة",
    "defunct public high schools": "مدارس ثانوية عامة سابقة",
    "defunct radio networks": "شبكات مذياع سابقة",
    "defunct radio stations": "محطات إذاعية سابقة",
    "defunct railway stations": "محطات السكك الحديدية سابقة",
    "defunct right-wing parties": "أحزاب يمينية سابقة",
    "defunct rugby league venues": "ملاعب دوري رجبي سابقة",
    "defunct rugby union stadiums": "ملاعب اتحاد رجبي سابقة",
    "defunct soccer clubs": "أندية كرة قدم سابقة",
    "defunct soccer venues": "ملاعب كرة قدم سابقة",
    "defunct socialist parties": "أحزاب اشتراكية سابقة",
    "defunct softball venues": "ملاعب كرة لينة سابقة",
    "defunct sports governing bodies": "هيئات تنظيم رياضية سابقة",
    "defunct television channels": "قنوات تلفزيونية سابقة",
    "defunct television networks": "شبكات تلفزيونية سابقة",
    "defunct tennis tournaments": "بطولات كرة مضرب سابقة",
    "defunct tourist attractions": "مواقع جذب سياحي سابقة",
    "defunct trade unions": "نقابات عمالية سابقة",
    "defunct women's basketball competitions": "منافسات كرة سلة نسائية سابقة",
    "defunct women's basketball leagues": "دوريات كرة سلة نسائية سابقة",
    "defunct women's football clubs": "أندية كرة قدم نسائية سابقة",
    "defunct women's soccer leagues": "دوريات كرة قدم نسائية سابقة",
}


@pytest.mark.parametrize("category, expected", data0_no_label.items(), ids=data0_no_label.keys())
@pytest.mark.skip2
def test_2_skip2_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
