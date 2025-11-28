"""
Tests
"""

import pytest
from load_one_data import dump_diff

from src.make_bots.ma_bots.ar_lab import find_ar_label
from src.make_bots.ma_bots.ye_ts_bot import translate_general_category

data_list = [
    {
        "tito": " in ",
        "category": "1450s disestablishments in arizona territory",
        "output": "انحلالات عقد 1450 في إقليم أريزونا",
    },
    {
        "tito": " in ",
        "category": "1450s disestablishments in the papal states",
        "output": "انحلالات عقد 1450 في الدولة البابوية",
    },
    {
        "tito": " in ",
        "category": "january 1450 sorts-events in north america",
        "output": "أحداث يناير 1450 الرياضية في أمريكا الشمالية",
    },
    {"tito": " in ", "category": "july 1450 sorts-events in china", "output": "أحداث يوليو 1450 الرياضية في الصين"},
    {"tito": " in ", "category": "1450s crimes in california", "output": "جرائم عقد 1450 في كاليفورنيا"},
    {"tito": " in ", "category": "1450s crimes in asia", "output": "جرائم عقد 1450 في آسيا"},
    {"tito": " in ", "category": "20th century synagogues in australia", "output": "كنس القرن 20 في أستراليا"},
    {
        "tito": " in ",
        "category": "november 1450 sorts-events in germany",
        "output": "أحداث نوفمبر 1450 الرياضية في ألمانيا",
    },
    {"tito": " in ", "category": "1450s establishments in england", "output": "تأسيسات عقد 1450 في إنجلترا"},
    {"tito": " in ", "category": "may 1450 crimes in asia", "output": "جرائم مايو 1450 في آسيا"},
    {
        "tito": " in ",
        "category": "november 1450 sorts-events in the united states",
        "output": "أحداث نوفمبر 1450 الرياضية في الولايات المتحدة",
    },
    {
        "tito": " in ",
        "category": "june 1450 sorts-events in the united states",
        "output": "أحداث يونيو 1450 الرياضية في الولايات المتحدة",
    },
    {
        "tito": " in ",
        "category": "august 1450 sorts-events in the united states",
        "output": "أحداث أغسطس 1450 الرياضية في الولايات المتحدة",
    },
    {"tito": " in ", "category": "march 1450 sorts-events in europe", "output": "أحداث مارس 1450 الرياضية في أوروبا"},
    {"tito": " in ", "category": "1450s establishments in asia", "output": "تأسيسات عقد 1450 في آسيا"},
    {"tito": " in ", "category": "september 1450 crimes in europe", "output": "جرائم سبتمبر 1450 في أوروبا"},
    {
        "tito": " in ",
        "category": "2nd millennium establishments in el salvador",
        "output": "تأسيسات الألفية 2 في السلفادور",
    },
    {"tito": " in ", "category": "july 1450 crimes in north america", "output": "جرائم يوليو 1450 في أمريكا الشمالية"},
    {
        "tito": " from ",
        "category": "16th century astronomers from the holy roman empire",
        "output": "فلكيون في القرن 16 من الإمبراطورية الرومانية المقدسة",
    },
    {"tito": " in ", "category": "21st century disestablishments in wales", "output": "انحلالات القرن 21 في ويلز"},
    {
        "tito": " by ",
        "category": "10th century chinese people by occupation",
        "output": "صينيون في القرن 10 حسب المهنة",
    },
    {"tito": " in ", "category": "1450s disasters in ireland", "output": "كوارث عقد 1450 في أيرلندا"},
    {
        "tito": " in ",
        "category": "1450s disestablishments in west virginia",
        "output": "انحلالات عقد 1450 في فيرجينيا الغربية",
    },
    {
        "tito": " in ",
        "category": "17th century disestablishments in the dutch empire",
        "output": "انحلالات القرن 17 في الإمبراطورية الهولندية",
    },
    {"tito": " in ", "category": "1450s disestablishments in oceania", "output": "انحلالات عقد 1450 في أوقيانوسيا"},
    {"tito": " in ", "category": "21st century executions in kentucky", "output": "إعدامات في القرن 21 في كنتاكي"},
    {"tito": " in ", "category": "july 1450 sorts-events in austria", "output": "أحداث يوليو 1450 الرياضية في النمسا"},
    {
        "tito": " by ",
        "category": "15th century swiss people by occupation",
        "output": "سويسريون في القرن 15 حسب المهنة",
    },
    {"tito": " in ", "category": "1450s murders in sri lanka", "output": "جرائم قتل عقد 1450 في سريلانكا"},
    {"tito": " in ", "category": "1450s disestablishments in minnesota", "output": "انحلالات عقد 1450 في منيسوتا"},
    {
        "tito": " in ",
        "category": "april 1450 sorts-events in north america",
        "output": "أحداث أبريل 1450 الرياضية في أمريكا الشمالية",
    },
    {"tito": " in ", "category": "21st century disestablishments in korea", "output": "انحلالات القرن 21 في كوريا"},
    {
        "tito": " in ",
        "category": "1450s establishments in the french colonial empire",
        "output": "تأسيسات عقد 1450 في الإمبراطورية الاستعمارية الفرنسية",
    },
    {"tito": " in ", "category": "1450s establishments in shanghai", "output": "تأسيسات عقد 1450 في شانغهاي"},
    {"tito": " in ", "category": "1450s crimes in germany", "output": "جرائم عقد 1450 في ألمانيا"},
    {"tito": " in ", "category": "april 1450 sorts-events in europe", "output": "أحداث أبريل 1450 الرياضية في أوروبا"},
    {"tito": " in ", "category": "1450s establishments in grenada", "output": "تأسيسات عقد 1450 في غرينادا"},
    {"tito": " in ", "category": "15th century establishments in poland", "output": "تأسيسات القرن 15 في بولندا"},
    {"tito": " in ", "category": "1450s murders in peru", "output": "جرائم قتل عقد 1450 في بيرو"},
    {
        "tito": " in ",
        "category": "october 1450 sorts-events in africa",
        "output": "أحداث أكتوبر 1450 الرياضية في إفريقيا",
    },
    {
        "tito": " by ",
        "category": "20th century croatian people by occupation",
        "output": "كروات في القرن 20 حسب المهنة",
    },
    {
        "tito": " in ",
        "category": "1450s establishments in the holy roman empire",
        "output": "تأسيسات عقد 1450 في الإمبراطورية الرومانية المقدسة",
    },
    {"tito": " in ", "category": "1450s establishments in taiwan", "output": "تأسيسات عقد 1450 في تايوان"},
    {"tito": " in ", "category": "july 1450 sorts-events in africa", "output": "أحداث يوليو 1450 الرياضية في إفريقيا"},
    {"tito": " in ", "category": "1450s establishments in malta", "output": "تأسيسات عقد 1450 في مالطا"},
    {"tito": " in ", "category": "1450s establishments in indonesia", "output": "تأسيسات عقد 1450 في إندونيسيا"},
    {
        "tito": " in ",
        "category": "16th century roman catholic bishops in hungary",
        "output": "أساقفة كاثوليك رومان في القرن 16 في المجر",
    },
    {
        "tito": " in ",
        "category": "september 1450 sorts-events in new zealand",
        "output": "أحداث سبتمبر 1450 الرياضية في نيوزيلندا",
    },
    {"tito": " in ", "category": "1450s disestablishments in hawaii", "output": "انحلالات عقد 1450 في هاواي"},
    {
        "tito": " in ",
        "category": "january 1450 sorts-events in austria",
        "output": "أحداث يناير 1450 الرياضية في النمسا",
    },
    {
        "tito": " in ",
        "category": "60s establishments in the roman empire",
        "output": "تأسيسات عقد 60 في الإمبراطورية الرومانية",
    },
    {"tito": " by ", "category": "5th century bc establishments by country", "output": "تأسيسات القرن 5 ق م حسب البلد"},
    {"tito": " in ", "category": "1st millennium establishments in morocco", "output": "تأسيسات الألفية 1 في المغرب"},
    {"tito": " in ", "category": "may 1450 sorts-events in europe", "output": "أحداث مايو 1450 الرياضية في أوروبا"},
    {
        "tito": " in ",
        "category": "17th century roman catholic archbishops in serbia",
        "output": "رؤساء أساقفة رومان كاثوليك القرن 17 في صربيا",
    },
    {"tito": " in ", "category": "1450s establishments in greenland", "output": "تأسيسات عقد 1450 في جرينلاند"},
    {
        "tito": " in ",
        "category": "may 1450 sorts-events in switzerland",
        "output": "أحداث مايو 1450 الرياضية في سويسرا",
    },
    {"tito": " in ", "category": "april 1450 crimes in south america", "output": "جرائم أبريل 1450 في أمريكا الجنوبية"},
    {"tito": " in ", "category": "may 1450 crimes in europe", "output": "جرائم مايو 1450 في أوروبا"},
    {"tito": " in ", "category": "1450s establishments in bavaria", "output": "تأسيسات عقد 1450 في بافاريا"},
    {
        "tito": " in ",
        "category": "1450s establishments in the united kingdom",
        "output": "تأسيسات عقد 1450 في المملكة المتحدة",
    },
    {"tito": " in ", "category": "august 1450 crimes in asia", "output": "جرائم أغسطس 1450 في آسيا"},
    {"tito": " in ", "category": "19th century establishments in yukon", "output": "تأسيسات القرن 19 في يوكون"},
    {"tito": " in ", "category": "december 1450 crimes in europe", "output": "جرائم ديسمبر 1450 في أوروبا"},
    {
        "tito": " in ",
        "category": "1450s architecture in the united states",
        "output": "عمارة عقد 1450 في الولايات المتحدة",
    },
    {"tito": " in ", "category": "june 1450 sorts-events in canada", "output": "أحداث يونيو 1450 الرياضية في كندا"},
    {
        "tito": " in ",
        "category": "january 1450 sorts-events in germany",
        "output": "أحداث يناير 1450 الرياضية في ألمانيا",
    },
    {
        "tito": " in ",
        "category": "april 1450 sorts-events in the united kingdom",
        "output": "أحداث أبريل 1450 الرياضية في المملكة المتحدة",
    },
    {
        "tito": " in ",
        "category": "august 1450 sorts-events in north america",
        "output": "أحداث أغسطس 1450 الرياضية في أمريكا الشمالية",
    },
    {"tito": " in ", "category": "1450s disestablishments in canada", "output": "انحلالات عقد 1450 في كندا"},
    {
        "tito": " in ",
        "category": "1st millennium bc establishments in the roman empire",
        "output": "تأسيسات الألفية 1 ق م في الإمبراطورية الرومانية",
    },
    {"tito": " in ", "category": "april 1450 crimes in asia", "output": "جرائم أبريل 1450 في آسيا"},
    {
        "tito": " in ",
        "category": "18th century roman catholic bishops in china",
        "output": "أساقفة كاثوليك رومان في القرن 18 في الصين",
    },
    {
        "tito": " in ",
        "category": "february 1450 crimes in south america",
        "output": "جرائم فبراير 1450 في أمريكا الجنوبية",
    },
    {
        "tito": " in ",
        "category": "1450s establishments in saint vincent and the grenadines",
        "output": "تأسيسات عقد 1450 في سانت فينسنت والغرينادين",
    },
    {
        "tito": " and ",
        "category": "21st century welsh dramatists and playwrights",
        "output": "دراميون ويلزيون في القرن 21 وكتاب مسرحيون",
    },
    {
        "tito": " in ",
        "category": "1450s mass shootings in oceania",
        "output": "إطلاق نار عشوائي عقد 1450 في أوقيانوسيا",
    },
    {"tito": " in ", "category": "21st century disasters in namibia", "output": "كوارث القرن 21 في ناميبيا"},
    {
        "tito": " in ",
        "category": "october 1450 crimes in north america",
        "output": "جرائم أكتوبر 1450 في أمريكا الشمالية",
    },
    {
        "tito": " in ",
        "category": "september 1450 sorts-events in north america",
        "output": "أحداث سبتمبر 1450 الرياضية في أمريكا الشمالية",
    },
    {
        "tito": " in ",
        "category": "march 1450 sorts-events in oceania",
        "output": "أحداث مارس 1450 الرياضية في أوقيانوسيا",
    },
    {"tito": " in ", "category": "21st century fires in south america", "output": "حرائق القرن 21 في أمريكا الجنوبية"},
    {"tito": " in ", "category": "august 1450 sorts-events in spain", "output": "أحداث أغسطس 1450 الرياضية في إسبانيا"},
    {
        "tito": " in ",
        "category": "16th century monarchs in the middle east",
        "output": "ملكيون في القرن 16 في الشرق الأوسط",
    },
    {"tito": " in ", "category": "21st century crimes in croatia", "output": "جرائم القرن 21 في كرواتيا"},
    {"tito": " in ", "category": "1450s establishments in kentucky", "output": "تأسيسات عقد 1450 في كنتاكي"},
    {
        "tito": " by ",
        "category": "13th century philosophers by nationality",
        "output": "فلاسفة في القرن 13 حسب الجنسية",
    },
    {"tito": " in ", "category": "2nd millennium disestablishments in hawaii", "output": "انحلالات الألفية 2 في هاواي"},
    {
        "tito": " in ",
        "category": "october 1450 sorts-events in poland",
        "output": "أحداث أكتوبر 1450 الرياضية في بولندا",
    },
    {"tito": " in ", "category": "1450s murders in honduras", "output": "جرائم قتل عقد 1450 في هندوراس"},
    {"tito": " in ", "category": "1450s disasters in kazakhstan", "output": "كوارث عقد 1450 في كازاخستان"},
    {
        "tito": " in ",
        "category": "19th century establishments in  kingdom-of sicily",
        "output": "تأسيسات القرن 19 في مملكة صقلية",
    },
    {
        "tito": " in ",
        "category": "january 1450 crimes in north america",
        "output": "جرائم يناير 1450 في أمريكا الشمالية",
    },
    {"tito": " in ", "category": "20th century disestablishments in alberta", "output": "انحلالات القرن 20 في ألبرتا"},
    {"tito": " in ", "category": "1450s murders in switzerland", "output": "جرائم قتل عقد 1450 في سويسرا"},
    {"tito": " of ", "category": "6th century kings of italy", "output": "ملوك القرن 6 إيطاليا"},
    {"tito": " in ", "category": "february 1450 crimes in asia", "output": "جرائم فبراير 1450 في آسيا"},
    {"tito": " in ", "category": "19th century establishments in nepal", "output": "تأسيسات القرن 19 في نيبال"},
    {"tito": " in ", "category": "september 1450 crimes in asia", "output": "جرائم سبتمبر 1450 في آسيا"},
    {
        "tito": " in ",
        "category": "1450s disestablishments in the british empire",
        "output": "انحلالات عقد 1450 في الإمبراطورية البريطانية",
    },
    {"tito": " in ", "category": "1450s disasters in north america", "output": "كوارث عقد 1450 في أمريكا الشمالية"},
    {
        "tito": " by ",
        "category": "14th century people by nationality and occupation",
        "output": "أشخاص في القرن 14 حسب الجنسية والمهنة",
    },
    {"tito": " in ", "category": "1450s disestablishments in tunisia", "output": "انحلالات عقد 1450 في تونس"},
    {
        "tito": " in ",
        "category": "march 1450 sorts-events in the united kingdom",
        "output": "أحداث مارس 1450 الرياضية في المملكة المتحدة",
    },
    {
        "tito": " in ",
        "category": "1450s disestablishments in georgia (country)",
        "output": "انحلالات عقد 1450 في جورجيا",
    },
    {
        "tito": " in ",
        "category": "june 1450 sorts-events in south america",
        "output": "أحداث يونيو 1450 الرياضية في أمريكا الجنوبية",
    },
    {
        "tito": " in ",
        "category": "5th century disestablishments in the byzantine empire",
        "output": "انحلالات القرن 5 في الإمبراطورية البيزنطية",
    },
    {"tito": " in ", "category": "1450s establishments in the caribbean", "output": "تأسيسات عقد 1450 في الكاريبي"},
    {
        "tito": " in ",
        "category": "april 1450 sorts-events in south america",
        "output": "أحداث أبريل 1450 الرياضية في أمريكا الجنوبية",
    },
    {
        "tito": " in ",
        "category": "october 1450 sorts-events in france",
        "output": "أحداث أكتوبر 1450 الرياضية في فرنسا",
    },
    {
        "tito": " in ",
        "category": "september 1450 sorts-events in japan",
        "output": "أحداث سبتمبر 1450 الرياضية في اليابان",
    },
    {
        "tito": " from ",
        "category": "21st century singer-songwriters from northern ireland",
        "output": "مغنون وكتاب أغاني في القرن 21 من أيرلندا الشمالية",
    },
    {"tito": " in ", "category": "1450s establishments in uttar pradesh", "output": "تأسيسات عقد 1450 في أتر برديش"},
    {"tito": " in ", "category": "february 1450 sorts-events in asia", "output": "أحداث فبراير 1450 الرياضية في آسيا"},
    {
        "tito": " from ",
        "category": "18th century actors from the holy roman empire",
        "output": "ممثلون في القرن 18 من الإمبراطورية الرومانية المقدسة",
    },
    {
        "tito": " of ",
        "category": "20th century governors of ottoman empire",
        "output": "حكام القرن 20 الدولة العثمانية",
    },
    {"tito": " in ", "category": "20th century mosques in asia", "output": "مساجد القرن 20 في آسيا"},
    {
        "tito": " in ",
        "category": "april 1450 sorts-events in malaysia",
        "output": "أحداث أبريل 1450 الرياضية في ماليزيا",
    },
    {"tito": " by ", "category": "1450s establishments by country", "output": "تأسيسات عقد 1450 حسب البلد"},
    {
        "tito": " in ",
        "category": "august 1450 sorts-events in the united kingdom",
        "output": "أحداث أغسطس 1450 الرياضية في المملكة المتحدة",
    },
    {
        "tito": " in ",
        "category": "1450s establishments in south america",
        "output": "تأسيسات عقد 1450 في أمريكا الجنوبية",
    },
    {
        "tito": " in ",
        "category": "july 1450 sorts-events in indonesia",
        "output": "أحداث يوليو 1450 الرياضية في إندونيسيا",
    },
    {"tito": " in ", "category": "1450s establishments in south africa", "output": "تأسيسات عقد 1450 في جنوب إفريقيا"},
    {
        "tito": " by ",
        "category": "19th century male composers by nationality",
        "output": "ملحنون ذكور في القرن 19 حسب الجنسية",
    },
    {
        "tito": " in ",
        "category": "september 1450 sorts-events in turkey",
        "output": "أحداث سبتمبر 1450 الرياضية في تركيا",
    },
    {"tito": " in ", "category": "1450s disestablishments in africa", "output": "انحلالات عقد 1450 في إفريقيا"},
    {
        "tito": " in ",
        "category": "april 1450 sorts-events in the united states",
        "output": "أحداث أبريل 1450 الرياضية في الولايات المتحدة",
    },
    {
        "tito": " in ",
        "category": "february 1450 sorts-events in germany",
        "output": "أحداث فبراير 1450 الرياضية في ألمانيا",
    },
    {"tito": " in ", "category": "1450s establishments in mali", "output": "تأسيسات عقد 1450 في مالي"},
    {"tito": " in ", "category": "1450s establishments in kiribati", "output": "تأسيسات عقد 1450 في كيريباتي"},
    {"tito": " by ", "category": "20th century chemists by nationality", "output": "كيميائيون في القرن 20 حسب الجنسية"},
    {
        "tito": " in ",
        "category": "1450s establishments in west virginia",
        "output": "تأسيسات عقد 1450 في فيرجينيا الغربية",
    },
    {"tito": " in ", "category": "march 1450 sorts-events in mexico", "output": "أحداث مارس 1450 الرياضية في المكسيك"},
    {"tito": " in ", "category": "21st century establishments in kosovo", "output": "تأسيسات القرن 21 في كوسوفو"},
    {
        "tito": " in ",
        "category": "19th century roman catholic bishops in argentina",
        "output": "أساقفة كاثوليك رومان في القرن 19 في الأرجنتين",
    },
    {
        "tito": " in ",
        "category": "august 1450 sorts-events in south korea",
        "output": "أحداث أغسطس 1450 الرياضية في كوريا الجنوبية",
    },
    {"tito": " in ", "category": "3rd century bishops in germania", "output": "أساقفة في القرن 3 في جرمانية"},
    {
        "tito": " in ",
        "category": "july 1450 sorts-events in australia",
        "output": "أحداث يوليو 1450 الرياضية في أستراليا",
    },
    {
        "tito": " in ",
        "category": "november 1450 sorts-events in canada",
        "output": "أحداث نوفمبر 1450 الرياضية في كندا",
    },
    {
        "tito": " in ",
        "category": "18th century roman catholic bishops in paraguay",
        "output": "أساقفة كاثوليك رومان في القرن 18 في باراغواي",
    },
    {"tito": " in ", "category": "1450s murders in ireland", "output": "جرائم قتل عقد 1450 في أيرلندا"},
    {"tito": " in ", "category": "march 1450 sorts-events in china", "output": "أحداث مارس 1450 الرياضية في الصين"},
    {"tito": " in ", "category": "july 1450 sorts-events in asia", "output": "أحداث يوليو 1450 الرياضية في آسيا"},
    {
        "tito": " in ",
        "category": "2nd millennium disestablishments in prince edward island",
        "output": "انحلالات الألفية 2 في جزيرة الأمير إدوارد",
    },
    {"tito": " in ", "category": "1450s establishments in germany", "output": "تأسيسات عقد 1450 في ألمانيا"},
    {
        "tito": " in ",
        "category": "december 1450 sorts-events in the philippines",
        "output": "أحداث ديسمبر 1450 الرياضية في الفلبين",
    },
    {"tito": " in ", "category": "1450s establishments in armenia", "output": "تأسيسات عقد 1450 في أرمينيا"},
    {"tito": " in ", "category": "1450s disestablishments in nebraska", "output": "انحلالات عقد 1450 في نبراسكا"},
    {
        "tito": " in ",
        "category": "january 1450 sorts-events in europe",
        "output": "أحداث يناير 1450 الرياضية في أوروبا",
    },
    {"tito": " in ", "category": "1450s establishments in france", "output": "تأسيسات عقد 1450 في فرنسا"},
    {"tito": " in ", "category": "15th century synagogues in portugal", "output": "كنس القرن 15 في البرتغال"},
    {"tito": " in ", "category": "2nd millennium disestablishments in india", "output": "انحلالات الألفية 2 في الهند"},
    {"tito": " in ", "category": "1450s disasters in kyrgyzstan", "output": "كوارث عقد 1450 في قيرغيزستان"},
    {"tito": " in ", "category": "1450s murders in singapore", "output": "جرائم قتل عقد 1450 في سنغافورة"},
    {"tito": " in ", "category": "2nd millennium establishments in morocco", "output": "تأسيسات الألفية 2 في المغرب"},
    {"tito": " in ", "category": "2nd millennium establishments in arkansas", "output": "تأسيسات الألفية 2 في أركنساس"},
    {"tito": " in ", "category": "1450s disestablishments in nauru", "output": "انحلالات عقد 1450 في ناورو"},
    {"tito": " in ", "category": "1450s establishments in meghalaya", "output": "تأسيسات عقد 1450 في ميغالايا"},
    {
        "tito": " in ",
        "category": "november 1450 sorts-events in oceania",
        "output": "أحداث نوفمبر 1450 الرياضية في أوقيانوسيا",
    },
    {"tito": " in ", "category": "1450s establishments in montenegro", "output": "تأسيسات عقد 1450 في الجبل الأسود"},
    {"tito": " in ", "category": "16th century architecture in romania", "output": "عمارة القرن 16 في رومانيا"},
    {
        "tito": " in ",
        "category": "2nd millennium establishments in massachusetts",
        "output": "تأسيسات الألفية 2 في ماساتشوستس",
    },
    {"tito": " in ", "category": "1450s disasters in norway", "output": "كوارث عقد 1450 في النرويج"},
    {"tito": " in ", "category": "1450s establishments in slovenia", "output": "تأسيسات عقد 1450 في سلوفينيا"},
    {
        "tito": " in ",
        "category": "1450s disestablishments in south america",
        "output": "انحلالات عقد 1450 في أمريكا الجنوبية",
    },
    {"tito": " in ", "category": "may 1450 sorts-events in asia", "output": "أحداث مايو 1450 الرياضية في آسيا"},
    {"tito": " by ", "category": "3rd century asian people by nationality", "output": "آسيويين في القرن 3 حسب الجنسية"},
    {
        "tito": " in ",
        "category": "1450s disestablishments in rhode island",
        "output": "انحلالات عقد 1450 في رود آيلاند",
    },
    {"tito": " in ", "category": "1450s establishments in burma", "output": "تأسيسات عقد 1450 في بورما"},
    {"tito": " in ", "category": "1450s establishments in sikkim", "output": "تأسيسات عقد 1450 في سيكيم"},
    {
        "tito": " in ",
        "category": "6th century disestablishments in the byzantine empire",
        "output": "انحلالات القرن 6 في الإمبراطورية البيزنطية",
    },
    {"tito": " in ", "category": "1450s crimes in peshawar", "output": "جرائم عقد 1450 في بيشاور"},
    {"tito": " in ", "category": "1450s disestablishments in oklahoma", "output": "انحلالات عقد 1450 في أوكلاهوما"},
    {"tito": " in ", "category": "15th century mosques in iran", "output": "مساجد القرن 15 في إيران"},
    {
        "tito": " by ",
        "category": "16th century iranian people by occupation",
        "output": "إيرانيون في القرن 16 حسب المهنة",
    },
    {"tito": " in ", "category": "1450s crimes in hong kong", "output": "جرائم عقد 1450 في هونغ كونغ"},
    {"tito": " in ", "category": "1450s disestablishments in idaho", "output": "انحلالات عقد 1450 في أيداهو"},
    {
        "tito": " in ",
        "category": "19th century establishments in  kingdom-of hanover",
        "output": "تأسيسات القرن 19 في مملكة هانوفر",
    },
    {
        "tito": " in ",
        "category": "october 1450 sorts-events in the united states",
        "output": "أحداث أكتوبر 1450 الرياضية في الولايات المتحدة",
    },
    {"tito": " in ", "category": "february 1450 crimes in europe", "output": "جرائم فبراير 1450 في أوروبا"},
    {
        "tito": " from ",
        "category": "20th century people from south dakota",
        "output": "أشخاص في القرن 20 من داكوتا الجنوبية",
    },
    {
        "tito": " in ",
        "category": "1450s establishments in georgia (u.s. state)",
        "output": "تأسيسات عقد 1450 في ولاية جورجيا",
    },
    {"tito": " in ", "category": "june 1450 sorts-events in austria", "output": "أحداث يونيو 1450 الرياضية في النمسا"},
    {
        "tito": " from ",
        "category": "18th century historians from the russian empire",
        "output": "مؤرخون في القرن 18 من الإمبراطورية الروسية",
    },
    {
        "tito": " in ",
        "category": "1450s establishments in the community of madrid",
        "output": "تأسيسات عقد 1450 في منطقة مدريد",
    },
    {"tito": " in ", "category": "2nd millennium establishments in lebanon", "output": "تأسيسات الألفية 2 في لبنان"},
    {
        "tito": " in ",
        "category": "17th century disestablishments in sri lanka",
        "output": "انحلالات القرن 17 في سريلانكا",
    },
    {
        "tito": " in ",
        "category": "1450s disasters in the united arab emirates",
        "output": "كوارث عقد 1450 في الإمارات العربية المتحدة",
    },
    {"tito": " by ", "category": "21st century yemeni people by occupation", "output": "يمنيون في القرن 21 حسب المهنة"},
    {
        "tito": " in ",
        "category": "450s disestablishments in the roman empire",
        "output": "انحلالات عقد 450 في الإمبراطورية الرومانية",
    },
    {
        "tito": " in ",
        "category": "3rd millennium establishments in british overseas territories",
        "output": "تأسيسات الألفية 3 في أقاليم ما وراء البحار البريطانية",
    },
    {
        "tito": " in ",
        "category": "1450s disestablishments in cape verde",
        "output": "انحلالات عقد 1450 في الرأس الأخضر",
    },
    {"tito": " in ", "category": "may 1450 sorts-events in africa", "output": "أحداث مايو 1450 الرياضية في إفريقيا"},
    {
        "tito": " and ",
        "category": "18th century religious buildings and structures",
        "output": "مبان دينية القرن 18 ومنشآت",
    },
    {"tito": " in ", "category": "1450s disestablishments in france", "output": "انحلالات عقد 1450 في فرنسا"},
    {
        "tito": " in ",
        "category": "august 1450 sorts-events in australia",
        "output": "أحداث أغسطس 1450 الرياضية في أستراليا",
    },
    {"tito": " in ", "category": "1450s establishments in burkina faso", "output": "تأسيسات عقد 1450 في بوركينا فاسو"},
    {"tito": " in ", "category": "1450s establishments in malaysia", "output": "تأسيسات عقد 1450 في ماليزيا"},
    {
        "tito": " in ",
        "category": "3rd millennium establishments in south korea",
        "output": "تأسيسات الألفية 3 في كوريا الجنوبية",
    },
    {"tito": " in ", "category": "september 1450 crimes in africa", "output": "جرائم سبتمبر 1450 في إفريقيا"},
    {"tito": " in ", "category": "1450s establishments in colorado", "output": "تأسيسات عقد 1450 في كولورادو"},
    {
        "tito": " and ",
        "category": "19th century british dramatists and playwrights",
        "output": "دراميون بريطانيون في القرن 19 وكتاب مسرحيون",
    },
    {"tito": " by ", "category": "1450s disestablishments by continent", "output": "انحلالات عقد 1450 حسب القارة"},
    {
        "tito": " in ",
        "category": "2nd millennium disestablishments in the democratic-republic-of-the-congo",
        "output": "انحلالات الألفية 2 في جمهورية الكونغو الديمقراطية",
    },
    {
        "tito": " in ",
        "category": "august 1450 sorts-events in oceania",
        "output": "أحداث أغسطس 1450 الرياضية في أوقيانوسيا",
    },
    {"tito": " in ", "category": "17th century disestablishments in ireland", "output": "انحلالات القرن 17 في أيرلندا"},
    {
        "tito": " from ",
        "category": "20th century photographers from northern ireland",
        "output": "مصورون في القرن 20 من أيرلندا الشمالية",
    },
    {
        "tito": " in ",
        "category": "1450s disestablishments in british columbia",
        "output": "انحلالات عقد 1450 في كولومبيا البريطانية",
    },
    {
        "tito": " in ",
        "category": "december 1450 sorts-events in the united states",
        "output": "أحداث ديسمبر 1450 الرياضية في الولايات المتحدة",
    },
    {"tito": " in ", "category": "20th century crimes in slovenia", "output": "جرائم القرن 20 في سلوفينيا"},
    {"tito": " in ", "category": "april 1450 sorts-events in france", "output": "أحداث أبريل 1450 الرياضية في فرنسا"},
    {"tito": " in ", "category": "2nd millennium establishments in thailand", "output": "تأسيسات الألفية 2 في تايلاند"},
    {"tito": " in ", "category": "14th century establishments in bohemia", "output": "تأسيسات القرن 14 في بوهيميا"},
    {"tito": " in ", "category": "1450s disestablishments in vermont", "output": "انحلالات عقد 1450 في فيرمونت"},
    {
        "tito": " in ",
        "category": "june 1450 crimes in the united states",
        "output": "جرائم يونيو 1450 في الولايات المتحدة",
    },
    {"tito": " in ", "category": "1450s establishments in italy", "output": "تأسيسات عقد 1450 في إيطاليا"},
    {"tito": " in ", "category": "january 1450 sorts-events in russia", "output": "أحداث يناير 1450 الرياضية في روسيا"},
    {
        "tito": " in ",
        "category": "april 1450 sorts-events in oceania",
        "output": "أحداث أبريل 1450 الرياضية في أوقيانوسيا",
    },
    {"tito": " in ", "category": "1450s disestablishments in taiwan", "output": "انحلالات عقد 1450 في تايوان"},
    {"tito": " in ", "category": "1450s disestablishments in the netherlands", "output": "انحلالات عقد 1450 في هولندا"},
    {
        "tito": " in ",
        "category": "18th century roman catholic church buildings in austria",
        "output": "مبان كنائس رومانية كاثوليكية القرن 18 في النمسا",
    },
    {"tito": " in ", "category": "1450s establishments in saskatchewan", "output": "تأسيسات عقد 1450 في ساسكاتشوان"},
    {
        "tito": " in ",
        "category": "21st century disestablishments in south dakota",
        "output": "انحلالات القرن 21 في داكوتا الجنوبية",
    },
    {
        "tito": " in ",
        "category": "19th century mosques in the ottoman empire",
        "output": "مساجد القرن 19 في الدولة العثمانية",
    },
]


@pytest.mark.parametrize("tab", data_list, ids=lambda x: x["category"])
def test_find_ar_label_and_event2(tab) -> None:
    label_no_event2 = find_ar_label(tab["category"], tab["tito"], use_event2=False)
    label_with_event2 = find_ar_label(tab["category"], tab["tito"], use_event2=True)
    # ---
    assert label_no_event2 != tab["output"]
    assert label_with_event2 == tab["output"]


@pytest.mark.parametrize("tab", data_list, ids=lambda x: x["category"])
def test_translate_general_category_event2(tab) -> None:
    label = translate_general_category(tab["category"])
    # ---
    assert label == tab["output"]


fast_data_list = [
    {
        "tito": " in ",
        "category": "1450s disestablishments in arizona territory",
        "output": "انحلالات عقد 1450 في إقليم أريزونا",
    },
    {
        "tito": " in ",
        "category": "1450s disestablishments in the papal states",
        "output": "انحلالات عقد 1450 في الدولة البابوية",
    },
    {
        "tito": " in ",
        "category": "january 1450 sorts-events in north america",
        "output": "أحداث يناير 1450 الرياضية في أمريكا الشمالية",
    },
    {"tito": " in ", "category": "july 1450 sorts-events in china", "output": "أحداث يوليو 1450 الرياضية في الصين"},
    {"tito": " in ", "category": "1450s crimes in california", "output": "جرائم عقد 1450 في كاليفورنيا"},
    {"tito": " in ", "category": "1450s crimes in asia", "output": "جرائم عقد 1450 في آسيا"},
    {"tito": " in ", "category": "20th century synagogues in australia", "output": "كنس القرن 20 في أستراليا"},
    {
        "tito": " in ",
        "category": "november 1450 sorts-events in germany",
        "output": "أحداث نوفمبر 1450 الرياضية في ألمانيا",
    },
    {"tito": " in ", "category": "1450s establishments in england", "output": "تأسيسات عقد 1450 في إنجلترا"},
    {"tito": " in ", "category": "may 1450 crimes in asia", "output": "جرائم مايو 1450 في آسيا"},
    {
        "tito": " in ",
        "category": "november 1450 sorts-events in the united states",
        "output": "أحداث نوفمبر 1450 الرياضية في الولايات المتحدة",
    },
]


@pytest.mark.parametrize("tab", fast_data_list, ids=lambda x: x["category"])
@pytest.mark.fast
def test_translate_general_category_event2_fast(tab) -> None:
    label = translate_general_category(tab["category"])
    # ---
    assert label == tab["output"]


data_list_bad = [
    ("september 1550 sorts-events in germany", " in ", "أحداث سبتمبر 1550 الرياضية في ألمانيا"),
    ("1550s disestablishments in yugoslavia", " in ", "انحلالات عقد 1550 في يوغوسلافيا"),
    ("20th century synagogues in switzerland", " in ", "كنس القرن 20 في سويسرا"),
    ("20th century disestablishments in the united kingdom", " in ", "انحلالات القرن 20 في المملكة المتحدة"),
    ("november 1550 sorts-events in north america", " in ", "أحداث نوفمبر 1550 الرياضية في أمريكا الشمالية"),
    ("1550s establishments in wisconsin", " in ", "تأسيسات عقد 1550 في ويسكونسن"),
    ("20th century disestablishments in sri lanka", " in ", "انحلالات القرن 20 في سريلانكا"),
    ("20th century roman catholic archbishops in colombia", " in ", "رؤساء أساقفة رومان كاثوليك القرن 20 في كولومبيا"),
    ("3rd millennium disestablishments in england", " in ", "انحلالات الألفية 3 في إنجلترا"),
    ("may 1550 sorts-events in the united states", " in ", "أحداث مايو 1550 الرياضية في الولايات المتحدة"),
    ("december 1550 sorts-events in the united states", " in ", "أحداث ديسمبر 1550 الرياضية في الولايات المتحدة"),
    ("1550s crimes in pakistan", " in ", "جرائم عقد 1550 في باكستان"),
    ("2nd millennium establishments in rhode island", " in ", "تأسيسات الألفية 2 في رود آيلاند"),
    ("1550s establishments in chile", " in ", "تأسيسات عقد 1550 في تشيلي"),
    ("1550s disestablishments in southeast asia", " in ", "انحلالات عقد 1550 في جنوب شرق آسيا"),
    ("december 1550 sorts-events in the united kingdom", " in ", "أحداث ديسمبر 1550 الرياضية في المملكة المتحدة"),
    ("20th century american people by occupation", " by ", "أمريكيون في القرن 20 حسب المهنة"),
    ("1550s establishments in jamaica", " in ", "تأسيسات عقد 1550 في جامايكا"),
    ("march 1550 sorts-events in belgium", " in ", "أحداث مارس 1550 الرياضية في بلجيكا"),
    ("20th century disasters in afghanistan", " in ", "كوارث القرن 20 في أفغانستان"),
    ("20th century churches in ethiopia", " in ", "كنائس القرن 20 في إثيوبيا"),
    ("april 1550 sorts-events in the united kingdom", " in ", "أحداث أبريل 1550 الرياضية في المملكة المتحدة"),
    ("1550s disestablishments in mississippi", " in ", "انحلالات عقد 1550 في مسيسيبي"),
    ("1550s establishments in maine", " in ", "تأسيسات عقد 1550 في مين"),
    ("1550s establishments in sweden", " in ", "تأسيسات عقد 1550 في السويد"),
    ("20th century churches in nigeria", " in ", "كنائس القرن 20 في نيجيريا"),
    (
        "20th century disestablishments in newfoundland and labrador",
        " in ",
        "انحلالات القرن 20 في نيوفاوندلاند واللابرادور",
    ),
    (
        "20th century disestablishments in the danish colonial empire",
        " in ",
        "انحلالات القرن 20 في الإمبراطورية الاستعمارية الدنماركية",
    ),
    ("20th century establishments in french guiana", " in ", "تأسيسات القرن 20 في غويانا الفرنسية"),
    ("20th century establishments in ireland", " in ", "تأسيسات القرن 20 في أيرلندا"),
    ("20th century members of maine legislature", " of ", "أعضاء القرن 20 هيئة مين التشريعية"),
    ("20th century monarchs by country", " by ", "ملكيون في القرن 20 حسب البلد"),
    ("20th century prime ministers of japan", " of ", "رؤساء وزراء القرن 20 اليابان"),
    ("august 1550 sorts-events in france", " in ", "أحداث أغسطس 1550 الرياضية في فرنسا"),
    ("february 1550 sorts-events in germany", " in ", "أحداث فبراير 1550 الرياضية في ألمانيا"),
    ("july 1550 crimes by continent", " by ", "جرائم يوليو 1550 حسب القارة"),
    ("july 1550 sorts-events in north america", " in ", "أحداث يوليو 1550 الرياضية في أمريكا الشمالية"),
    ("june 1550 sorts-events in malaysia", " in ", "أحداث يونيو 1550 الرياضية في ماليزيا"),
    ("march 1550 sorts-events in thailand", " in ", "أحداث مارس 1550 الرياضية في تايلاند"),
    ("november 1550 sorts-events in europe", " in ", "أحداث نوفمبر 1550 الرياضية في أوروبا"),
    ("november 1550 sorts-events in the united kingdom", " in ", "أحداث نوفمبر 1550 الرياضية في المملكة المتحدة"),
    ("october 1550 sorts-events in oceania", " in ", "أحداث أكتوبر 1550 الرياضية في أوقيانوسيا"),
]


def test_result_only_with_event2():
    expected_result = {}
    diff_result = {}
    for tab in data_list_bad:
        category, tito, expected = tab
        result = find_ar_label(category, tito, use_event2=True)
        result2 = find_ar_label(category, tito, use_event2=False)
        if result != expected and result2 != expected:
            expected_result[category] = expected
            diff_result[category] = result

    dump_diff(diff_result, "test_result_only_with_event2")
    assert diff_result == expected_result, f"Differences found: {len(diff_result)}"
