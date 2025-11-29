"""
# TODO: ADD SOME DATA FROM D:/categories_bot/langlinks/z2_data/COUNTRY_YEAR.json
category:yemen at the 2020 fifa women's world cup
# """

COUNTRY_YEAR_PARAMS = [
    "{year1}",
    "{country1}",
]


COUNTRY_YEAR_DATA = {
    "category:{year1} in {country1}": "تصنيف:{country1} في {year1}",  # 34632
    "category:{year1} establishments in {country1}": "تصنيف:تأسيسات سنة {year1} في {country1}",  # 19853
    "category:{year1} events in {country1}": "تصنيف:أحداث {year1} في {country1}",  # 7413
    "category:{year1} disestablishments in {country1}": "تصنيف:انحلالات سنة {year1} في {country1}",  # 4600
    "category:{year1} sports events in {country1}": "تصنيف:أحداث {year1} الرياضية في {country1}",  # 6108
    "category:{year1} crimes in {country1}": "تصنيف:جرائم {year1} في {country1}",  # 3966
    "category:{year1} murders in {country1}": "تصنيف:جرائم قتل في {country1} في {year1}",
    "category:{year1} disasters in {country1}": "تصنيف:كوارث في {country1} في {year1}",  # 2140
    "category:{year1} in {country1} by month": "تصنيف:أحداث {year1} في {country1} حسب الشهر",  # 1808
    "category:{year1} elections in {country1}": "تصنيف:انتخابات {country1} في {year1}",  # 1550
    "category:{year1} events in {country1} by month": "تصنيف:أحداث {year1} في {country1} حسب الشهر",  # 1382
    "category:years of the {year1} in {country1}": "تصنيف:سنوات {year1} في {country1}",  # 922
    "category:{year1} in sports in {country1}": "تصنيف:الرياضة في {country1} في {year1}",  # 630
    "category:{year1} in {country1} by city": "تصنيف:{country1} في {year1} حسب المدينة",  # 486
    "category:{country1} at the {year1} fifa world cup": "تصنيف:{country1} في كأس العالم {year1}",  # 466
    "category:{year1} in {country1} (state)": "تصنيف:ولاية {country1} في {year1}",  # 353
    "category:{year1} establishments in {country1} territory": "تصنيف:تأسيسات سنة {year1} في إقليم {country1}",  # 231
    "category:{year1} establishments in {country1} (state)": "تصنيف:تأسيسات سنة {year1} في ولاية {country1}",  # 262
    "category:terrorist incidents in {country1} in {year1}": "تصنيف:حوادث إرهابية في {country1} في {year1}",  # 333
    "category:railway stations in {country1} opened in {year1}": "تصنيف:محطات السكك الحديدية في {country1} افتتحت في {year1}",  # 345
    "category:{year1} in {country1} territory": "تصنيف:إقليم {country1} في {year1}",  # 289
    "category:{year1} architecture in {country1}": "تصنيف:عمارة {year1} في {country1}",  # 317
    "category:{year1} in new {country1}": "تصنيف:{country1} الجديدة في {year1}",  # 253
    "category:{year1} in {country1} by state": "تصنيف:{year1} في {country1} حسب الولاية",  # 280
    "category:{year1} in {country1} by state or territory": "تصنيف:{country1} في {year1} حسب الولاية",  # 243
    "category:{year1} mass shootings in {country1}": "تصنيف:إطلاق نار عشوائي في {country1} في {year1}",  # 215
    "category:attacks in {country1} in {year1}": "تصنيف:هجمات في {country1} في {year1}",  # 247
    "category:{year1} roman catholic bishops in {country1}": "تصنيف:أساقفة كاثوليك رومان في {country1} في {year1}",  # 233
    "category:{year1} establishments in new {country1}": "تصنيف:تأسيسات سنة {year1} في {country1} الجديدة",  # 154
    "category:{year1} in {country1} city": "تصنيف:مدينة {country1} في {year1}",  # 150
    "category:{year1} religious buildings and structures in {country1}": "تصنيف:مبان ومنشآت دينية في {country1} في {year1}",  # 165
    "category:{year1} churches in {country1}": "تصنيف:كنائس في {country1} في {year1}",  # 172
    "category:{year1} in {country1} (u.s. state)": "تصنيف:ولاية {country1} في {year1}",  # 155
    "category:{country1} at uefa euro {year1}": "تصنيف:{country1} في بطولة أمم أوروبا {year1}",  # 183
    "category:{year1} mosques in {country1}": "تصنيف:مساجد في {country1} في {year1}",  # 175
    "category:{year1} in sport in {country1}": "تصنيف:أحداث {year1} الرياضية في {country1}",  # 143
    "category:terrorist incidents in {country1} in the {year1}": "تصنيف:حوادث إرهابية في {country1} في {year1}",  # 173
    "category:{year1} establishments in {country1} (u.s. state)": "تصنيف:تأسيسات سنة {year1} في ولاية {country1}",  # 138
    "category:railway stations in {country1} opened in the {year1}": "تصنيف:محطات السكك الحديدية في {country1} افتتحت في {year1}",  # 170
    "category:{year1} crimes in {country1} by month": "تصنيف:جرائم {year1} في {country1} حسب الشهر",  # 167
    "category:{year1} mayors of places in {country1}": "تصنيف:رؤساء بلديات في {country1} في {year1}",  # 153
    "category:{year1} in {country1}, d.c.": "تصنيف:{country1} العاصمة في {year1}",  # 145
    "category:{year1} establishments in {country1} city": "تصنيف:تأسيسات سنة {year1} في مدينة {country1}",  # 124
    "category:{year1} executions by {country1}": "تصنيف:إعدامات في {country1} في {year1}",  # 96
    "category:{year1} people from {country1}": "تصنيف:أشخاص من {country1} في {year1}",  # 115
    "category:{year1} fires in {country1}": "تصنيف:حرائق في {country1} في {year1}",  # 120
    "category:{year1} establishments in {country1}, d.c.": "تصنيف:تأسيسات سنة {year1} في {country1} العاصمة",  # 112
    "category:{year1} {country1} politicians": "تصنيف:سياسيو {country1} في {year1}",  # 88
    "category:{year1} in {country1} by province or territory": "تصنيف:{country1} في {year1} حسب المقاطعة أو الإقليم",  # 137
    "category:{year1} mass murder in {country1}": "تصنيف:قتل جماعي في {country1} في {year1}",  # 84
    "category:{year1} roman catholic archbishops in {country1}": "تصنيف:رؤساء أساقفة رومان كاثوليك في {country1} في {year1}",  # 129
    "category:{year1} in sports in {country1} (state)": "تصنيف:الرياضة في ولاية {country1} في {year1}",  # 131
    "category:{year1} in sports in {country1} city": "تصنيف:الرياضة في مدينة {country1} في {year1}",  # 126
    "category:{year1} tour de {country1}": "تصنيف:سباق طواف {country1} في {year1}",  # 110
    "category:{year1} monarchs in {country1}": "تصنيف:ملكيون في {country1} في {year1}",  # 82
    "category:{year1} in {country1} (country)": "تصنيف:{country1} في {year1}",  # 99
    "category:{year1} disestablishments in {country1} (state)": "تصنيف:انحلالات سنة {year1} في ولاية {country1}",  # 71
    "category:{country1} at the {year1} fifa women's world cup": "تصنيف:{country1} في كأس العالم لكرة القدم للسيدات {year1}",  # 97
    "category:{year1} roman catholic church buildings in {country1}": "تصنيف:مبان كنائس رومانية كاثوليكية في {country1} في {year1}",  # 92
    "category:{year1} in ottoman {country1}": "تصنيف:{country1} العثمانية في {year1}",  # 65
    "category:{year1} natural disasters in {country1}": "تصنيف:كوارث طبيعية في {country1} في {year1}",  # 84
    "category:{year1} floods in {country1}": "تصنيف:فيضانات في {country1} في {year1}",  # 62
    "category:{year1} awards in {country1}": "تصنيف:جوائز {year1} في {country1}",  # 78
    "category:aviation accidents and incidents in {country1} in {year1}": "تصنيف:حوادث طيران في {country1} في {year1}",  # 83
    "category:{year1} establishments in {country1} by state or union territory": "تصنيف:تأسيسات سنة {year1} في {country1} حسب الولاية أو الإقليم الاتحادي",  # 72
    "category:{year1} {country1} elections": "تصنيف:انتخابات {country1} في {year1}",  # 79
    "category:candidates in the {year1} {country1} elections": "تصنيف:مرشحون في انتخابات {country1} في {year1}",  # 73
    "category:{year1} military history of {country1}": "تصنيف:تاريخ {country1} العسكري في {year1}",  # 57
    "category:{year1} controversies in {country1}": "تصنيف:خلافات في {country1} في {year1}",  # 53
    "category:attacks in {country1} in the {year1}": "تصنيف:هجمات في {country1} في {year1}",  # 64
    "category:{year1} members of {country1} general assembly": "تصنيف:أعضاء جمعية {country1} العامة في {year1}",  # 57
    "category:{country1} at the {year1} copa américa": "تصنيف:{country1} في كوبا أمريكا {year1}",  # 57
    "category:{year1} in the colony of {country1}": "تصنيف:{country1} في {year1}",  # 54
    "category:{year1} festivals in {country1}": "تصنيف:مهرجانات {year1} في {country1}",  # 55
    "category:{year1} members of {country1} legislature": "تصنيف:أعضاء هيئة {country1} التشريعية في {year1}",  # 54
    "category:{year1} {country1} state court judges": "تصنيف:قضاة محكمة ولاية {country1} في {year1}",  # 54
}
