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
    "21st-century male actors from Georgia (country)": "ممثلون ذكور من جورجيا في القرن 21",
    "Argentine male bobsledders": "متزلجون جماعيون ذكور أرجنتينيون",
    "Argentine male singer-songwriters": "مغنون وكتاب أغاني ذكور أرجنتينيون",
    "Argentine male singers": "مغنون ذكور أرجنتينيون",
    "Austrian male artistic gymnasts": "لاعبو جمباز فني ذكور نمساويون",
    "Bangladeshi male actors": "ممثلون ذكور بنغلاديشيون",
    "Bangladeshi male golfers": "لاعبو غولف ذكور بنغلاديشيون",
    "Belarusian male freestyle skiers": "ممارسو تزلج حر ذكور بيلاروسيون",
    "Belarusian male skiers": "متزحلقون ذكور بيلاروسيون",
    "Brazilian male classical composers": "ملحنون كلاسيكيون ذكور برازيليون",
    "British male actors by medium": "ممثلون ذكور بريطانيون حسب الوسط",
    "Bulgarian male stage actors": "ممثلو مسرح ذكور بلغاريون",
    "Comorian male canoeists": "متسابقو قوارب الكانوي ذكور قمريون",
    "Costa Rican male judoka": "لاعبو جودو ذكور كوستاريكيون",
    "Djiboutian male judoka": "لاعبو جودو ذكور جيبوتيون",
    "Djiboutian male martial artists": "ممارسو فنون قتالية ذكور جيبوتيون",
    "Egyptian male table tennis players": "لاعبو كرة طاولة ذكور مصريون",
    "Expatriate male actors in China": "ممثلون ذكور مغتربون في الصين",
    "Filipino male singer-songwriters": "مغنون وكتاب أغاني ذكور فلبينيون",
    "French male bass guitarists": "عازفو غيتار باس ذكور فرنسيون",
    "Ghanaian male Muay Thai practitioners": "ممارسو موياي تاي ذكور غانيون",
    "Ghanaian male kickboxers": "مقاتلو كيك بوكسنغ ذكور غانيون",
    "Guinean male swimmers": "سباحون ذكور غينيون",
    "Icelandic male stage actors": "ممثلو مسرح ذكور آيسلنديون",
    "Indian male equestrians": "فرسان خيول ذكور هنود",
    "Indian male playback singers": "مغنو أفلام ذكور هنود",
    "Irish male rappers": "مغنو راب ذكور أيرلنديون",
    "Israeli male classical pianists": "عازفو بيانو كلاسيكيون ذكور إسرائيليون",
    "Kazakhstani male weightlifters": "رباعون ذكور كازاخستانيون",
    "Latvian male novelists": "روائيون ذكور لاتفيون",
    "Latvian male poets": "شعراء ذكور لاتفيون",
    "Lebanese male radio actors": "ممثلو راديو ذكور لبنانيون",
    "Lists of male golfers": "قوائم لاعبو غولف ذكور",
    "Malagasy male weightlifters": "رباعون ذكور مدغشقريون",
    "Nepalese male actors": "ممثلون ذكور نيباليون",
    "Norwegian male ski jumpers": "متزلجو قفز ذكور نرويجيون",
    "Polish male biathletes": "لاعبو بياثلون ذكور بولنديون",
    "Puerto Rican male judoka": "لاعبو جودو ذكور بورتوريكيون",
    "Rhodesian male martial artists": "ممارسو فنون قتالية ذكور رودوسيون",
    "Serbian male short story writers": "كتاب قصة قصيرة ذكور صرب",
    "Soviet male swimmers": "سباحون ذكور سوفيت",
    "Spanish male classical pianists": "عازفو بيانو كلاسيكيون ذكور إسبان",
    "Spanish male pianists": "عازفو بيانو ذكور إسبان",
    "Thai male actors by medium": "ممثلون ذكور تايلنديون حسب الوسط",
    "Thai male composers": "ملحنون ذكور تايلنديون",
    "Thai male sailors (sport)": "بحارة رياضيون ذكور تايلنديون",
    "Ugandan male mixed martial artists": "مقاتلو فنون قتالية مختلطة ذكور أوغنديون",
    "Welsh male short story writers": "كتاب قصة قصيرة ذكور ويلزيون"
}


@pytest.mark.parametrize("category,expected", test_data2.items(), ids=test_data2.keys())
@pytest.mark.fast
def test_nat_pattern_multi(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = resolve_label_ar(category)
    assert result == expected
