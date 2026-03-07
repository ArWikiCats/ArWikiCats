"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers_male import males_resolver_labels

test_data2 = {
    "Category:Turkish expatriate sports-people": "تصنيف:رياضيون أتراك مغتربون",
    # jobs
    "eugenicists": "علماء متخصصون في تحسين النسل",
    "politicians who committed suicide": "سياسيون أقدموا على الانتحار",
    "archers": "نبالون",
    "male archers": "نبالون ذكور",
    "football managers": "مدربو كرة قدم",
    # jobs + expatriate
    "expatriate football managers": "مدربو كرة قدم مغتربون",
    "expatriate male actors": "ممثلون ذكور مغتربون",
    "expatriate actors": "ممثلون مغتربون",
    "male actors": "ممثلون ذكور",
    "yemeni writers": "كتاب يمنيون",
    "yemeni male writers": "كتاب ذكور يمنيون",
    "greek male writers": "كتاب ذكور يونانيون",
    "male alpine skiers": "متزحلقو منحدرات ثلجية ذكور",
    "male artistic gymnasts": "لاعبو جمباز فني ذكور",
    "male artists": "فنانون ذكور",
    "male athletes": "لاعبو قوى ذكور",
    "male badminton players": "لاعبو تنس ريشة ذكور",
    "male ballet dancers": "راقصو باليه ذكور",
    "male biathletes": "لاعبو بياثلون ذكور",
    "male bloggers": "مدونون ذكور",
    "male bobsledders": "متزلجون جماعيون ذكور",
    "male boxers": "ملاكمون ذكور",
    "male canoeists": "متسابقو قوارب الكانوي ذكور",
    "male classical composers": "ملحنون كلاسيكيون ذكور",
    "male classical pianists": "عازفو بيانو كلاسيكيون ذكور",
    "male comedians": "كوميديون ذكور",
    "male composers": "ملحنون ذكور",
    "male conductors (music)": "قادة فرق موسيقية ذكور",
    "male critics": "نقاد ذكور",
    "male cross-country skiers": "متزحلقون ريفيون ذكور",
    "male cyclists": "دراجون ذكور",
    "male dancers": "راقصون ذكور",
    "male divers": "غواصون ذكور",
    "male dramatists and playwrights": "كتاب دراما ومسرح ذكور",
    "male dramatists": "دراميون ذكور",
    "male entertainers": "فنانون ترفيهيون ذكور",
    "male equestrians": "فرسان خيول ذكور",
    "male essayists": "كتاب مقالات ذكور",
    "male fencers": "مبارزون ذكور",
    "male field hockey defenders": "مدافعو هوكي ميدان ذكور",
    "male field hockey players": "لاعبو هوكي ميدان ذكور",
    "male figure skaters": "متزلجون فنيون ذكور",
    "male film actors": "ممثلو أفلام ذكور",
    "male folk singers": "مغنو فولك ذكور",
    "male freestyle skiers": "ممارسو تزلج حر ذكور",
    "male freestyle swimmers": "سباحو تزلج حر ذكور",
    "male golfers": "لاعبو غولف ذكور",
    "male guitarists": "عازفو قيثارة ذكور",
    "male ice dancers": "راقصو جليد ذكور",
    "male jazz musicians": "موسيقيو جاز ذكور",
    "male journalists": "صحفيون ذكور",
    "male judoka": "لاعبو جودو ذكور",
    "male kabaddi players": "لاعبو كابادي ذكور",
    "male karateka": "ممارسو كاراتيه ذكور",
    "male kickboxers": "مقاتلو كيك بوكسنغ ذكور",
    "male long-distance runners": "عداؤو مسافات طويلة ذكور",
    "male lugers": "زاحفون ثلجيون ذكور",
    "male mandolinists": "عازفو مندولين ذكور",
    "male martial artists": "ممارسو فنون قتالية ذكور",
    "male middle-distance runners": "عداؤو مسافات متوسطة ذكور",
    "male mixed martial artists": "مقاتلو فنون قتالية مختلطة ذكور",
    "male models": "عارضو أزياء ذكور",
    "male modern pentathletes": "متسابقو خماسي حديث ذكور",
    "male muay thai practitioners": "ممارسو موياي تاي ذكور",
    "male musical theatre actors": "ممثلو مسرحيات موسيقية ذكور",
    "male musicians": "موسيقيون ذكور",
    "male non-fiction writers": "كتاب غير روائيين ذكور",
    "male nordic combined skiers": "متزحلقو تزلج نوردي مزدوج ذكور",
    "male novelists": "روائيون ذكور",
    "male opera composers": "ملحنو أوبرا ذكور",
    "male opera singers": "مغنو أوبرا ذكور",
    "male painters": "رسامون ذكور",
    "male pair skaters": "متزلجون فنيون على الجليد ذكور",
    "male photographers": "مصورون ذكور",
    "male pianists": "عازفو بيانو ذكور",
    "male poets": "شعراء ذكور",
    "male pop singers": "مغنو بوب ذكور",
    "male pornographic film actors": "ممثلو أفلام إباحية ذكور",
    "male professional wrestlers": "مصارعون محترفون ذكور",
    "male radio actors": "ممثلو راديو ذكور",
    "male rappers": "مغنو راب ذكور",
    "male rowers": "مجدفون ذكور",
    "male runners": "عداؤون ذكور",
    "male sailors (sport)": "بحارة رياضيون ذكور",
    "male screenwriters": "كتاب سيناريو ذكور",
    "male short story writers": "كتاب قصة قصيرة ذكور",
    "male silent film actors": "ممثلو أفلام صامتة ذكور",
    "male singer-songwriters": "مغنون وكتاب أغاني ذكور",
    "male singers": "مغنون ذكور",
    "male single skaters": "متزلجون فرديون ذكور",
    "male skeleton racers": "متزلجون صدريون ذكور",
    "male ski jumpers": "متزلجو قفز ذكور",
    "male skiers": "متزحلقون ذكور",
    "male snowboarders": "متزلجون على الثلج ذكور",
    "male soap opera actors": "ممثلو مسلسلات طويلة ذكور",
    "male songwriters": "كتاب أغان ذكور",
    "male speed skaters": "متزلجو سرعة ذكور",
    "male sport shooters": "لاعبو رماية ذكور",
    "male sport wrestlers": "مصارعون رياضيون ذكور",
    "male stage actors": "ممثلو مسرح ذكور",
    "male steeplechase runners": "عداؤو موانع ذكور",
    "male swimmers": "سباحون ذكور",
    "male synchronized swimmers": "سباحون إيقاعيون ذكور",
    "male table tennis players": "لاعبو كرة طاولة ذكور",
    "male taekwondo practitioners": "لاعبو تايكوندو ذكور",
    "male television actors": "ممثلو تلفزيون ذكور",
    "male tennis players": "لاعبو كرة مضرب ذكور",
    "male triathletes": "لاعبو ترياثلون ذكور",
    "male video game actors": "ممثلو ألعاب فيديو ذكور",
    "male violinists": "عازفو كمان ذكور",
    "male voice actors": "ممثلو أداء صوتي ذكور",
    "male water polo players": "لاعبو كرة ماء ذكور",
    "male web series actors": "ممثلو مسلسلات ويب ذكور",
    "male weightlifters": "رباعون ذكور",
    "male wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ذكور",
    "male wrestlers": "مصارعون ذكور",
    "male writers": "كتاب ذكور",
}

test_data_2 = {
    "Category:Pakistani expatriate male actors": "تصنيف:ممثلون ذكور باكستانيون مغتربون",
    "Category:expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
    "Category:Pakistani expatriate footballers": "تصنيف:لاعبو كرة قدم باكستانيون مغتربون",
    "educators": "معلمون",
    "medical doctors": "أطباء",
    "singers": "مغنون",
    "northern ireland": "",
    "republic of ireland": "",
    "republic-of ireland": "",

}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
@pytest.mark.fast
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = males_resolver_labels(category)
    assert result == expected


@pytest.mark.parametrize("category,expected", test_data_2.items(), ids=test_data_2.keys())
@pytest.mark.fast
def test_mens_2(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = males_resolver_labels(category)
    assert result == expected


@pytest.mark.fast
def test_people_key() -> None:
    result = males_resolver_labels("people")
    assert result == ""
