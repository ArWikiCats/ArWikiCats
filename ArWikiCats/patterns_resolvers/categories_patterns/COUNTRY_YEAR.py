"""
# TODO: ADD SOME DATA FROM D:/categories_bot/langlinks/z2_data/COUNTRY_YEAR.json
yemen at 2020 fifa women's world cup
#"""

COUNTRY_YEAR_PARAMS = [
    "{year1}",
    "{country1}",
]

COUNTRY_YEAR_DATA_TO_CHECK = {
    "{year1} establishments in new {country1}": "تأسيسات سنة {year1} في {country1} الجديدة",  # 154
    "{year1} in ottoman {country1}": "{country1} العثمانية في {year1}",  # 65
}

# NOTE: patterns with only en-ar should be in formatted_data_en_ar_only countries_names.py to handle countries without gender details
# NOTE: patterns with only en-ar-time should be in COUNTRY_YEAR_DATA to handle countries-time without gender details

# 18th-century people of Dutch Empire
COUNTRY_YEAR_DATA = {
    # "{year1} {country1} politicians": "سياسيو {country1} في {year1}",  # 88
    "{year1} disestablishments in {country1}": "انحلالات سنة {year1} في {country1}",  # 4600
    "{year1} disestablishments in {country1} (state)": "انحلالات سنة {year1} في ولاية {country1}",  # 71
    "{year1} establishments in {country1}": "تأسيسات سنة {year1} في {country1}",  # 19853
    "{year1} establishments in {country1} territory": "تأسيسات سنة {year1} في إقليم {country1}",  # 231
    "{year1} establishments in {country1} (state)": "تأسيسات سنة {year1} في ولاية {country1}",  # 262
    "{year1} establishments in {country1} (u.s. state)": "تأسيسات سنة {year1} في ولاية {country1}",  # 138
    "{year1} establishments in {country1} city": "تأسيسات سنة {year1} في مدينة {country1}",  # 124
    "{year1} establishments in {country1}, d.c.": "تأسيسات سنة {year1} في {country1} العاصمة",  # 112
    "{year1} establishments in {country1} by state or union territory": "تأسيسات سنة {year1} في {country1} حسب الولاية أو الإقليم الاتحادي",  # 72
    # "20th-century executions by Gambia": "إعدامات في غامبيا في القرن 20",
    # "14th-century lords of Monaco": "لوردات موناكو في القرن 14",
    "{year1} lords of {country1}": "لوردات {country1} في {year1}",
    "{year1} kings of {country1}": "ملوك {country1} في {year1}",
    "{year1} {country1}": "{year1} في {country1}",  # 34632
    "{year1} in {country1}": "{year1} في {country1}",  # 34632
    "{year1} synagogues in {country1}": "كنس في {country1} في {year1}",
    "{year1} prime ministers of {country1}": "رؤساء وزراء {country1} في {year1}",
    "{year1} heads of state of {country1}": "قادة {country1} في {year1}",
    "{year1} elections in {country1}": "انتخابات {year1} في {country1}",  # 1550
    "{year1} people of {country1}": "أشخاص من {country1} {year1}",  # 34632
    "{year1} events in {country1}": "أحداث {year1} في {country1}",  # 7413
    "{year1} sports events in {country1}": "أحداث {year1} الرياضية في {country1}",  # 6108
    "{year1} crimes in {country1}": "جرائم {year1} في {country1}",  # 3966
    "{year1} murders in {country1}": "جرائم قتل في {country1} في {year1}",
    "{year1} disasters in {country1}": "كوارث في {country1} في {year1}",  # 2140
    "{year1} in {country1} by month": "{year1} في {country1} حسب الشهر",  # 1808
    "{year1} events in {country1} by month": "أحداث {year1} في {country1} حسب الشهر",  # 1382
    "years of {year1} in {country1}": "سنوات {year1} في {country1}",  # 922
    "{year1} in sports in {country1}": "الرياضة في {country1} في {year1}",  # 630
    "{year1} in {country1} by city": "{country1} في {year1} حسب المدينة",  # 486
    "{country1} at {year1} fifa world cup": "{country1} في كأس العالم {year1}",  # 466
    "{year1} in {country1} (state)": "ولاية {country1} في {year1}",  # 353
    "terrorist incidents in {country1} in {year1}": "حوادث إرهابية في {country1} في {year1}",  # 333
    "railway stations in {country1} opened in {year1}": "محطات السكك الحديدية في {country1} افتتحت في {year1}",  # 345
    "{year1} in {country1} territory": "إقليم {country1} في {year1}",  # 289
    "{year1} architecture in {country1}": "عمارة {year1} في {country1}",  # 317
    "{year1} in {country1} by state": "{year1} في {country1} حسب الولاية",  # 280
    "{year1} in {country1} by state or territory": "{country1} في {year1} حسب الولاية",  # 243
    "{year1} mass shootings in {country1}": "إطلاق نار عشوائي في {country1} في {year1}",  # 215
    "attacks in {country1} in {year1}": "هجمات في {country1} في {year1}",  # 247
    "{year1} roman catholic bishops in {country1}": "أساقفة كاثوليك رومان في {country1} في {year1}",  # 233
    "{year1} in {country1} city": "مدينة {country1} في {year1}",  # 150
    "{year1} religious buildings and structures in {country1}": "مبان ومنشآت دينية في {country1} في {year1}",  # 165
    "{year1} churches in {country1}": "كنائس في {country1} في {year1}",  # 172
    "{year1} in {country1} (u.s. state)": "ولاية {country1} في {year1}",  # 155
    "{country1} at uefa euro {year1}": "{country1} في بطولة أمم أوروبا {year1}",  # 183
    "{year1} mosques in {country1}": "مساجد في {country1} في {year1}",  # 175
    "{year1} in sport in {country1}": "أحداث {year1} الرياضية في {country1}",  # 143
    "{year1} crimes in {country1} by month": "جرائم {year1} في {country1} حسب الشهر",  # 167
    "{year1} mayors of places in {country1}": "رؤساء بلديات في {country1} في {year1}",  # 153
    "{year1} in {country1}, d.c.": "{country1} العاصمة في {year1}",  # 145
    "{year1} executions by {country1}": "إعدامات في {country1} في {year1}",  # 96
    "{year1} people from {country1}": "أشخاص من {country1} في {year1}",  # 115
    "{year1} fires in {country1}": "حرائق في {country1} في {year1}",  # 120
    "{year1} in {country1} by province or territory": "{country1} في {year1} حسب المقاطعة أو الإقليم",  # 137
    "{year1} mass murder in {country1}": "قتل جماعي في {country1} في {year1}",  # 84
    "{year1} roman catholic archbishops in {country1}": "رؤساء أساقفة رومان كاثوليك في {country1} في {year1}",  # 129
    "{year1} in sports in {country1} (state)": "الرياضة في ولاية {country1} في {year1}",  # 131
    "{year1} in sports in {country1} city": "الرياضة في مدينة {country1} في {year1}",  # 126
    "{year1} tour de {country1}": "سباق طواف {country1} في {year1}",  # 110
    "{year1} monarchs in {country1}": "ملكيون في {country1} في {year1}",  # 82
    "{year1} in {country1} (country)": "{country1} في {year1}",  # 99
    "{country1} at {year1} fifa women's world cup": "{country1} في كأس العالم لكرة القدم للسيدات {year1}",  # 97
    "{year1} roman catholic church buildings in {country1}": "مبان كنائس رومانية كاثوليكية في {country1} في {year1}",  # 92
    "{year1} natural disasters in {country1}": "كوارث طبيعية في {country1} في {year1}",  # 84
    "{year1} floods in {country1}": "فيضانات في {country1} في {year1}",  # 62
    "{year1} awards in {country1}": "جوائز {year1} في {country1}",  # 78
    "aviation accidents and incidents in {country1} in {year1}": "حوادث طيران في {country1} في {year1}",  # 83
    "{year1} {country1} elections": "انتخابات {country1} في {year1}",  # 79
    "candidates in {year1} {country1} elections": "مرشحون في انتخابات {country1} في {year1}",  # 73
    "{year1} military history of {country1}": "تاريخ {country1} العسكري في {year1}",  # 57
    "{year1} controversies in {country1}": "خلافات في {country1} في {year1}",  # 53
    "{year1} members of {country1} general assembly": "أعضاء جمعية {country1} العامة في {year1}",  # 57
    "{country1} at {year1} copa américa": "{country1} في كوبا أمريكا {year1}",  # 57
    "{year1} in colony of {country1}": "{country1} في {year1}",  # 54
    "{year1} festivals in {country1}": "مهرجانات {year1} في {country1}",  # 55
    "{year1} members of {country1} legislature": "أعضاء هيئة {country1} التشريعية في {year1}",  # 54
    "{year1} {country1} state court judges": "قضاة محكمة ولاية {country1} في {year1}",  # 54
}
