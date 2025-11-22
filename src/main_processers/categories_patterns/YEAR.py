"""
!
"""
# TODO: ADD SOME DATA FROM D:/categories_bot/langlinks/z2_data/YEAR.json

YEAR_DATA = {
    "Category:{YEAR1}": "تصنيف:{YEAR1}",  # 2387
    "Category:{YEAR1} by country": "تصنيف:{YEAR1} حسب البلد",  # 1111
    "Category:{YEAR1} deaths": "تصنيف:وفيات {YEAR1}",  # 2045
    "Category:{YEAR1} events": "تصنيف:أحداث {YEAR1}",  # 2020
    "Category:{YEAR1} endings": "تصنيف:نهايات {YEAR1}",  # 1970
    "Category:{YEAR1} by continent": "تصنيف:أحداث {YEAR1} حسب القارة",  # 1098
    "Category:{YEAR1} beginnings": "تصنيف:بدايات {YEAR1}",  # 1946
    "Category:{YEAR1} births": "تصنيف:مواليد {YEAR1}",  # 1923
    "Category:{YEAR1} in sports": "تصنيف:أحداث {YEAR1} الرياضية",  # 1295
    "Category:{YEAR1} establishments": "تصنيف:تأسيسات سنة {YEAR1}",  # 1243
    "Category:{YEAR1} sports events": "تصنيف:أحداث {YEAR1} الرياضية",  # 1295
    "Category:{YEAR1} works": "تصنيف:أعمال في {YEAR1}",  # 945
    "Category:{YEAR1} events by continent": "تصنيف:أحداث {YEAR1} حسب القارة",  # 967
    "Category:{YEAR1} events by country": "تصنيف:أحداث {YEAR1} حسب البلد",  # 956
    "Category:{YEAR1} disestablishments": "تصنيف:انحلالات سنة {YEAR1}",  # 699
    "Category:{YEAR1} establishments by country": "تصنيف:تأسيسات سنة {YEAR1} حسب البلد",  # 731
    "Category:Conflicts in {YEAR1}": "تصنيف:نزاعات في {YEAR1}",  # 817
    "Category:Buildings and structures completed in {YEAR1}": "تصنيف:مبان ومنشآت اكتملت في {YEAR1}",  # 791
    "Category:{YEAR1} in the arts": "تصنيف:الفنون في {YEAR1}",  # 734
    "Category:States and territories established in {YEAR1}": "تصنيف:دول وأقاليم أسست في {YEAR1}",  # 644
    "Category:{YEAR1} BC": "تصنيف:{YEAR1} ق م",  # 649
    "Category:{YEAR1} establishments by continent": "تصنيف:تأسيسات سنة {YEAR1} حسب القارة",  # 523
    "Category:{YEAR1} crimes": "تصنيف:جرائم {YEAR1}",  # 601
    "Category:{YEAR1} in religion": "تصنيف:الدين في {YEAR1}",  # 592
    "Category:{YEAR1} books": "تصنيف:كتب {YEAR1}",  # 581
    "Category:Religious buildings and structures completed in {YEAR1}": "تصنيف:مبان دينية اكتملت في {YEAR1}",  # 396
    "Category:{YEAR1} in politics": "تصنيف:السياسة في {YEAR1}",  # 552
    "Category:{YEAR1} in military history": "تصنيف:التاريخ العسكري في {YEAR1}",  # 570
    "Category:{YEAR1} in science": "تصنيف:العلم في {YEAR1}",  # 540
    "Category:Populated places established in {YEAR1}": "تصنيف:أماكن مأهولة أسست في {YEAR1}",  # 521
    "Category:{YEAR1} in literature": "تصنيف:الأدب في {YEAR1}",  # 474
    "Category:{YEAR1} in law": "تصنيف:القانون في {YEAR1}",  # 477
    "Category:{YEAR1} disestablishments by continent": "تصنيف:انحلالات سنة {YEAR1} حسب القارة",  # 368
    "Category:{YEAR1} in international relations": "تصنيف:علاقات دولية في {YEAR1}",  # 468
    "Category:{YEAR1} disestablishments by country": "تصنيف:انحلالات سنة {YEAR1} حسب البلد",  # 347
    "Category:{YEAR1} in art": "تصنيف:الفن في {YEAR1}",  # 449
    "Category:{YEAR1} BC deaths": "تصنيف:وفيات {YEAR1} ق م",  # 440
    "Category:{YEAR1} in the Ottoman Empire": "تصنيف:الدولة العثمانية في {YEAR1}",  # 349
    "Category:{YEAR1} in Christianity": "تصنيف:المسيحية في {YEAR1}",  # 369
    "Category:States and territories disestablished in {YEAR1}": "تصنيف:دول وأقاليم انحلت في {YEAR1}",  # 406
    "Category:Organizations established in {YEAR1}": "تصنيف:منظمات أسست في {YEAR1}",  # 259
    "Category:{YEAR1} in education": "تصنيف:التعليم في {YEAR1}",  # 258
    "Category:{YEAR1} in association football": "تصنيف:كرة القدم في {YEAR1}",  # 350
    "Category:{YEAR1} introductions": "تصنيف:استحداثات {YEAR1}",  # 275
    "Category:Fiction set in {YEAR1}": "تصنيف:أعمال خيالية في {YEAR1}",  # 206
    "Category:{YEAR1} in the Spanish Empire": "تصنيف:الإمبراطورية الإسبانية في {YEAR1}",  # 315
    "Category:{YEAR1} paintings": "تصنيف:لوحات {YEAR1}",  # 346
    "Category:{YEAR1} in economic history": "تصنيف:الاقتصاد في {YEAR1}",  # 251
    "Category:{YEAR1} treaties": "تصنيف:معاهدات في {YEAR1}",  # 283
    "Category:{YEAR1} in transport": "تصنيف:النقل في {YEAR1}",  # 279
    "Category:{YEAR1} murders": "تصنيف:قتل في {YEAR1}",  # 300
    "Category:{YEAR1} non-fiction books": "تصنيف:كتب غير خيالية {YEAR1}",  # 312
    "Category:{YEAR1} disasters": "تصنيف:كوارث {YEAR1}",  # 322
    "Category:{YEAR1} novels": "تصنيف:روايات {YEAR1}",  # 317
    "Category:{YEAR1} in the environment": "تصنيف:البيئة في {YEAR1}",  # 283
    "Category:Films set in {YEAR1}": "تصنيف:أفلام تقع أحداثها في {YEAR1}",  # 283
    "Category:{YEAR1} establishments in the Spanish Empire": "تصنيف:تأسيسات سنة {YEAR1} في الإمبراطورية الإسبانية",  # 256
    "Category:Educational organizations established in {YEAR1}": "تصنيف:منظمات تعليمية أسست في {YEAR1}",  # 276
    "Category:{YEAR1} domestic association football cups": "تصنيف:كؤوس كرة قدم محلية {YEAR1}",  # 288
    "Category:{YEAR1} in theatre": "تصنيف:المسرح في {YEAR1}",  # 262
    "Category:{YEAR1} in economics": "تصنيف:{YEAR1} في الاقتصاد",  # 287
    "Category:{YEAR1} crimes by continent": "تصنيف:جرائم {YEAR1} حسب القارة",  # 285
    "Category:{YEAR1} in domestic association football": "تصنيف:كرة قدم محلية في {YEAR1}",  # 285
    "Category:{YEAR1} in music": "تصنيف:موسيقى في {YEAR1}",  # 169
    "Category:Companies established in {YEAR1}": "تصنيف:شركات أسست في {YEAR1}",  # 282
    "Category:Educational institutions established in {YEAR1}": "تصنيف:هيئات تعليمية أسست في {YEAR1}",  # 266
    "Category:{YEAR1} establishments in the Ottoman Empire": "تصنيف:تأسيسات سنة {YEAR1} في الدولة العثمانية",  # 211
    "Category:Species described in {YEAR1}": "تصنيف:أنواع وصفت في {YEAR1}",  # 271
    "Category:Taxa described in {YEAR1}": "تصنيف:أصنوفات وصفت في {YEAR1}",  # 270
    "Category:Infrastructure completed in {YEAR1}": "تصنيف:بنية تحتية اكتملت في {YEAR1}",  # 268
    "Category:Animals described in {YEAR1}": "تصنيف:حيوانات وصفت في {YEAR1}",  # 266
    "Category:{YEAR1} domestic association football leagues": "تصنيف:دوريات كرة قدم محلية {YEAR1}",  # 142
    "Category:Maritime incidents in {YEAR1}": "تصنيف:حوادث بحرية في {YEAR1}",  # 256
    "Category:{YEAR1} architecture": "تصنيف:عمارة {YEAR1}",  # 215
    "Category:Plants described in {YEAR1}": "تصنيف:نباتات وصفت في {YEAR1}",  # 260
    "Category:{YEAR1} plays": "تصنيف:مسرحيات {YEAR1}",  # 257
    "Category:Churches completed in {YEAR1}": "تصنيف:كنائس اكتملت في {YEAR1}",  # 247
    "Category:Mammals described in {YEAR1}": "تصنيف:ثدييات وصفت في {YEAR1}",  # 247
    "Category:{YEAR1} murders by continent": "تصنيف:جرائم قتل حسب القارة {YEAR1}",  # 157
    "Category:Mosques completed in {YEAR1}": "تصنيف:مساجد اكتملت في {YEAR1}",  # 243
    "Category:Murder in {YEAR1}": "تصنيف:قتل في {YEAR1}",  # 241
    "Category:Astronomical objects discovered in {YEAR1}": "تصنيف:أجرام فلكية اكتشفت في {YEAR1}",  # 242
    "Category:{YEAR1} documents": "تصنيف:وثائق في {YEAR1}",  # 179
    "Category:Companies established in {YEAR1} by country": "تصنيف:شركات أسست في {YEAR1} حسب البلد",  # 235
    "Category:{YEAR1} by city": "تصنيف:{YEAR1} حسب المدينة",  # 233
    "Category:Transport infrastructure completed in {YEAR1}": "تصنيف:بنية تحتية للنقل اكتملت في {YEAR1}",  # 233
    "Category:{YEAR1} natural disasters": "تصنيف:كوارث طبيعية في {YEAR1}",  # 132
    "Category:Publications established in {YEAR1}": "تصنيف:منشورات أسست في {YEAR1}",  # 217
    "Category:{YEAR1} events by month": "تصنيف:أحداث {YEAR1} حسب الشهر",  # 228
    "Category:{YEAR1} crimes by country": "تصنيف:جرائم {YEAR1} حسب البلد",  # 224
    "Category:{YEAR1} by month": "تصنيف:أحداث {YEAR1} حسب الشهر",  # 225
    "Category:States and territories established in the {YEAR1}": "تصنيف:دول وأقاليم أسست في {YEAR1}",  # 224
    "Category:{YEAR1} conflicts": "تصنيف:نزاعات في {YEAR1}",  # 215
    "Category:{YEAR1} in paleontology": "تصنيف:علم الأحياء القديمة في {YEAR1}",  # 215
    "Category:Birds described in {YEAR1}": "تصنيف:طيور وصفت في {YEAR1}",  # 225
    "Category:{YEAR1} elections": "تصنيف:انتخابات في {YEAR1}",  # 214
    "Category:Fish described in {YEAR1}": "تصنيف:أسماك وصفت في {YEAR1}",  # 222
    "Category:{YEAR1} in rail transport": "تصنيف:السكك الحديدية في {YEAR1}",  # 182
    "Category:Houses completed in {YEAR1}": "تصنيف:منازل اكتملت في {YEAR1}",  # 213
    "Category:{YEAR1} murders by country": "تصنيف:جرائم قتل في {YEAR1} حسب البلد",  # 187
    "Category:Articles with unsourced statements from {YEAR1}": "تصنيف:مقالات ذات عبارات بحاجة لمصادر منذ {YEAR1}",  # 212
    "Category:People murdered in {YEAR1}": "تصنيف:أشخاص قتلوا في {YEAR1}",  # 210
    "Category:{YEAR1} in health": "تصنيف:الصحة في {YEAR1}",  # 194
    "Category:Fungi described in {YEAR1}": "تصنيف:فطريات وصفت في {YEAR1}",  # 206
    "Category:{YEAR1} in biology": "تصنيف:علم الأحياء في {YEAR1}",  # 180
    "Category:{YEAR1} ships": "تصنيف:سفن {YEAR1}",  # 200
    "Category:Fossil taxa described in {YEAR1}": "تصنيف:أصنوفات أحفورية وصفت في {YEAR1}",  # 201
    "Category:Insects described in {YEAR1}": "تصنيف:حشرات وصفت في {YEAR1}",  # 199
    "Category:Manufacturing companies established in {YEAR1}": "تصنيف:شركات تصنيع أسست في {YEAR1}",  # 194
    "Category:Military units and formations established in {YEAR1}": "تصنيف:وحدات وتشكيلات عسكرية أسست في {YEAR1}",  # 196
    "Category:{YEAR1} in the Russian Empire": "تصنيف:الإمبراطورية الروسية في {YEAR1}",  # 192
    "Category:Reptiles described in {YEAR1}": "تصنيف:زواحف وصفت في {YEAR1}",  # 192
    "Category:{YEAR1} in sports by country": "تصنيف:ألعاب رياضية في {YEAR1} حسب البلد",  # 190
    "Category:Awards established in {YEAR1}": "تصنيف:جوائز أسست في {YEAR1}",  # 190
    "Category:{YEAR1} songs": "تصنيف:أغاني {YEAR1}",  # 172
    "Category:{YEAR1} elections by country": "تصنيف:انتخابات {YEAR1} حسب البلد",  # 189
    "Category:{YEAR1} in sport by continent": "تصنيف:رياضة في {YEAR1} حسب القارة",  # 181
    "Category:Universities and colleges established in {YEAR1}": "تصنيف:جامعات وكليات أسست في {YEAR1}",  # 189
    "Category:{YEAR1} in mass media": "تصنيف:وسائل الإعلام في {YEAR1}",  # 126
    "Category:Clean-up categories from {YEAR1}": "تصنيف:تصنيفات تهذيب منذ {YEAR1}",  # 188
    "Category:{YEAR1} short stories": "تصنيف:قصص قصيرة {YEAR1}",  # 177
    "Category:{YEAR1} sculptures": "تصنيف:منحوتات {YEAR1}",  # 179
    "Category:{YEAR1} disasters by country": "تصنيف:كوارث في {YEAR1} حسب البلد",  # 86
    "Category:{YEAR1} poems": "تصنيف:قصائد {YEAR1}",  # 180
    "Category:Articles containing potentially dated statements from {YEAR1}": "تصنيف:مقالات فيها عبارات متقادمة منذ {YEAR1}",  # 183
    "Category:Residential buildings completed in {YEAR1}": "تصنيف:مبان سكنية اكتملت في {YEAR1}",  # 182
    "Category:{YEAR1} in technology": "تصنيف:التقانة في {YEAR1}",  # 164
    "Category:Articles lacking reliable references from {YEAR1}": "تصنيف:مقالات ينقصها مصادر موثوق بها منذ {YEAR1}",  # 181
    "Category:{YEAR1} in association football by continent": "تصنيف:كرة القدم في {YEAR1} حسب القارة",  # 180
    "Category:Event venues established in {YEAR1}": "تصنيف:صالات أحداث أسست في {YEAR1}",  # 170
    "Category:{YEAR1} establishments in the Russian Empire": "تصنيف:تأسيسات سنة {YEAR1} في الإمبراطورية الروسية",  # 152
    "Category:Articles lacking sources from {YEAR1}": "تصنيف:مقالات بدون مصدر منذ {YEAR1}",  # 178
    "Category:Museums established in {YEAR1}": "تصنيف:متاحف أسست في {YEAR1}",  # 129
    "Category:{YEAR1} earthquakes": "تصنيف:زلازل {YEAR1}",  # 171
    "Category:{YEAR1} in film": "تصنيف:{YEAR1} في الأفلام",  # 140
    "Category:States and territories disestablished in the {YEAR1}": "تصنيف:دول وأقاليم انحلت في {YEAR1}",  # 174
    "Category:Mass murder in {YEAR1}": "تصنيف:قتل جماعي في {YEAR1}",  # 172
    "Category:Railway stations opened in {YEAR1}": "تصنيف:محطات السكك الحديدية افتتحت في {YEAR1}",  # 169
    "Category:Articles with dead external links from {YEAR1}": "تصنيف:مقالات ذات وصلات خارجية مكسورة منذ {YEAR1}",  # 171
    "Category:Sports clubs and teams established in {YEAR1}": "تصنيف:أندية رياضية أسست في {YEAR1}",  # 152
    "Category:Sports organizations established in {YEAR1}": "تصنيف:منظمات رياضية أسست في {YEAR1}",  # 170
    "Category:{YEAR1} in English sport": "تصنيف:رياضة إنجليزية في {YEAR1}",  # 164
    "Category:Organizations disestablished in {YEAR1}": "تصنيف:منظمات انحلت في {YEAR1}",  # 170
    "Category:Religious organizations established in {YEAR1}": "تصنيف:منظمات دينية أسست في {YEAR1}",  # 169
    "Category:Political parties established in {YEAR1}": "تصنيف:أحزاب سياسية أسست في {YEAR1}",  # 168
    "Category:Association football clubs established in {YEAR1}": "تصنيف:أندية كرة قدم أسست في {YEAR1}",  # 167
    "Category:Government agencies established in {YEAR1}": "تصنيف:وكالات حكومية أسست في {YEAR1}",  # 165
    "Category:{YEAR1} in tennis": "تصنيف:كرة المضرب في {YEAR1}",  # 164
    "Category:Transport disasters in {YEAR1}": "تصنيف:كوارث نقل في {YEAR1}",  # 149
    "Category:{YEAR1} in football": "تصنيف:{YEAR1} في كرة القدم",  # 163
    "Category:Banks established in {YEAR1}": "تصنيف:بنوك أسست في {YEAR1}",  # 150
    "Category:Wikipedia articles needing page number citations from {YEAR1}": "تصنيف:مقالات بحاجة لتحديد رقم صفحة المرجع منذ {YEAR1}",  # 164
    "Category:{YEAR1} BC births": "تصنيف:مواليد {YEAR1} ق م",  # 161
    "Category:{YEAR1} speculative fiction novels": "تصنيف:روايات خيال تأملي {YEAR1}",  # 90
    "Category:{YEAR1} in rugby union": "تصنيف:اتحاد الرجبي في {YEAR1}",  # 114
    "Category:{YEAR1} conferences": "تصنيف:مؤتمرات {YEAR1}",  # 161
    "Category:{YEAR1} in women's history": "تصنيف:تاريخ المرأة في {YEAR1}",  # 107
    "Category:Buildings and structures completed in the {YEAR1}": "تصنيف:مبان ومنشآت اكتملت في {YEAR1}",  # 161
    "Category:Magazines established in {YEAR1}": "تصنيف:مجلات أسست في {YEAR1}",  # 159
    "Category:Massacres in {YEAR1}": "تصنيف:مذابح في {YEAR1}",  # 161
    "Category:Recurring events established in {YEAR1}": "تصنيف:أحداث دورية أسست في {YEAR1}",  # 161
    "Category:{YEAR1} suicides": "تصنيف:انتحار في {YEAR1}",  # 146
    "Category:{YEAR1} films": "تصنيف:أفلام إنتاج {YEAR1}",  # 154
    "Category:Fictional characters introduced in {YEAR1}": "تصنيف:شخصيات خيالية ظهرت في {YEAR1}",  # 140
    "Category:Transport companies established in {YEAR1}": "تصنيف:شركات نقل أسست في {YEAR1}",  # 150
    "Category:Newspapers established in {YEAR1}": "تصنيف:صحف أسست في {YEAR1}",  # 158
    "Category:Recurring sporting events established in {YEAR1}": "تصنيف:أحداث رياضية دورية أسست في {YEAR1}",  # 153
    "Category:{YEAR1} in politics by country": "تصنيف:السياسة في {YEAR1} حسب البلد",  # 153
    "Category:Bridges completed in {YEAR1}": "تصنيف:جسور اكتملت في {YEAR1}",  # 94
    "Category:{YEAR1} in English tennis": "تصنيف:كرة مضرب إنجليزية في {YEAR1}",  # 152
    "Category:Sports venues completed in {YEAR1}": "تصنيف:ملاعب رياضية اكتملت في {YEAR1}",  # 133
    "Category:Fiction set in the {YEAR1}": "تصنيف:أعمال خيالية في {YEAR1}",  # 98
    "Category:{YEAR1} compositions": "تصنيف:مؤلفات موسيقية من عام {YEAR1}",  # 92
    "Category:{YEAR1} short films": "تصنيف:أفلام قصيرة {YEAR1}",  # 136
    "Category:Articles needing additional references from {YEAR1}": "تصنيف:مقالات بحاجة لمصادر أكثر منذ {YEAR1}",  # 149
    "Category:{YEAR1} in English football": "تصنيف:كرة القدم الإنجليزية في {YEAR1}",  # 148
    "Category:Financial services companies established in {YEAR1}": "تصنيف:شركات خدمات مالية أسست في {YEAR1}",  # 148
    "Category:Orphaned articles from {YEAR1}": "تصنيف:مقالات يتيمة منذ {YEAR1}",  # 148
    "Category:{YEAR1} riots": "تصنيف:شغب في {YEAR1}",  # 135
    "Category:{YEAR1} in women's sport": "تصنيف:رياضة نسوية في {YEAR1}",  # 72
    "Category:{YEAR1} science fiction novels": "تصنيف:روايات خيال علمي {YEAR1}",  # 103
    "Category:Products introduced in {YEAR1}": "تصنيف:منتجات عرضت في {YEAR1}",  # 146
    "Category:{YEAR1} in women's sport by continent": "تصنيف:رياضة نسائية في {YEAR1} حسب القارة",  # 128
    "Category:{YEAR1} in women's sport by country": "تصنيف:رياضة نسائية في {YEAR1} حسب البلد",  # 99
    "Category:{YEAR1} FA Cup": "تصنيف:كأس الاتحاد الإنجليزي {YEAR1}",  # 144
    "Category:{YEAR1} in English football cups": "تصنيف:كؤوس كرة قدم إنجليزية في {YEAR1}",  # 144
    "Category:{YEAR1} in women's tennis": "تصنيف:كرة المضرب للسيدات في {YEAR1}",  # 139
    "Category:Flags introduced in {YEAR1}": "تصنيف:أعلام استحدثت في {YEAR1}",  # 56
    "Category:{YEAR1} in aviation": "تصنيف:الطيران في {YEAR1}",  # 117
    "Category:{YEAR1} in cycle racing": "تصنيف:سباق الدراجات الهوائية في سنة {YEAR1}",  # 116
    "Category:Hospitals established in {YEAR1}": "تصنيف:مستشفيات أسست في {YEAR1}",  # 140
    "Category:{YEAR1} fantasy novels": "تصنيف:روايات فانتازيا {YEAR1}",  # 134
    "Category:{YEAR1} in Spanish sport": "تصنيف:رياضة إسبانية في {YEAR1}",  # 140
    "Category:{YEAR1} in road cycling": "تصنيف:سباق الدراجات على الطريق في {YEAR1}",  # 79
    "Category:Commercial buildings completed in {YEAR1}": "تصنيف:مبان تجارية اكتملت في {YEAR1}",  # 133
    "Category:Publications disestablished in {YEAR1}": "تصنيف:منشورات انحلت في {YEAR1}",  # 135
    "Category:Roman Catholic churches completed in {YEAR1}": "تصنيف:كنائس رومانية كاثوليكية اكتملت في {YEAR1}",  # 138
    "Category:Vehicle manufacturing companies established in {YEAR1}": "تصنيف:شركات تصنيع مركبات أسست في {YEAR1}",  # 132
    "Category:Vehicles introduced in {YEAR1}": "تصنيف:مركبات عرضت في {YEAR1}",  # 69
    "Category:Protists described in {YEAR1}": "تصنيف:طلائعيات وصفت في {YEAR1}",  # 137
    "Category:{YEAR1} Wimbledon Championships": "تصنيف:بطولة ويمبلدون {YEAR1}",  # 134
    "Category:{YEAR1} in German sport": "تصنيف:رياضة ألمانية في {YEAR1}",  # 134
    "Category:{YEAR1} in basketball": "تصنيف:كرة السلة في {YEAR1}",  # 82
    "Category:{YEAR1} in the Spanish East Indies": "تصنيف:جزر الهند الشرقية الإسبانية في {YEAR1}",  # 122
    "Category:{YEAR1} Scottish Cup": "تصنيف:كأس المملكة المتحدة {YEAR1}",  # 135
    "Category:{YEAR1} comedy films": "تصنيف:أفلام كوميدية {YEAR1}",  # 88
    "Category:{YEAR1} in rugby union by country": "تصنيف:اتحاد الرجبي في {YEAR1} حسب البلد",  # 117
    "Category:{YEAR1} drama films": "تصنيف:أفلام درامية {YEAR1}",  # 95
    "Category:{YEAR1} children's books": "تصنيف:كتب أطفال {YEAR1}",  # 130
    "Category:{YEAR1} in Great Britain": "تصنيف:بريطانيا العظمى في {YEAR1}",  # 122
    "Category:Arts organizations established in {YEAR1}": "تصنيف:منظمات فنية أسست في {YEAR1}",  # 126
    "Category:Bacteria described in {YEAR1}": "تصنيف:بكتيريا وصفت في {YEAR1}",  # 131
    "Category:Films set in the {YEAR1}": "تصنيف:أفلام تقع أحداثها في {YEAR1}",  # 131
    "Category:Political parties disestablished in {YEAR1}": "تصنيف:أحزاب سياسية انحلت في {YEAR1}",  # 131
    "Category:{YEAR1} in Uruguay": "تصنيف:أوروغواي في {YEAR1}",  # 126
    "Category:{YEAR1} in Quebec": "تصنيف:كيبك في {YEAR1}",  # 111
    "Category:{YEAR1} in English football leagues": "تصنيف:دوريات كرة قدم إنجليزية في {YEAR1}",  # 130
    "Category:Entertainment companies established in {YEAR1}": "تصنيف:شركات ترفيه أسست في {YEAR1}",  # 129
    "Category:Ministries established in {YEAR1}": "تصنيف:وزارات أسست في {YEAR1}",  # 129
    "Category:{YEAR1} festivals": "تصنيف:مهرجانات {YEAR1}",  # 128
    "Category:{YEAR1} establishments in the Spanish East Indies": "تصنيف:تأسيسات سنة {YEAR1} في جزر الهند الشرقية الإسبانية",  # 91
    "Category:Religious buildings and structures completed in the {YEAR1}": "تصنيف:مبان ومنشآت دينية اكتملت في {YEAR1}",  # 74
    "Category:{YEAR1} sports events by month": "تصنيف:أحداث {YEAR1} الرياضية حسب الشهر",  # 128
    "Category:{YEAR1} in sports by month": "تصنيف:أحداث {YEAR1} الرياضية حسب الشهر",  # 127
    "Category:Populated places established in the {YEAR1}": "تصنيف:أماكن مأهولة أسست في {YEAR1}",  # 122
    "Category:Treaties concluded in {YEAR1}": "تصنيف:معاهدات أبرمت في {YEAR1}",  # 125
    "Category:{YEAR1} in Spanish football": "تصنيف:كرة القدم الإسبانية في {YEAR1}",  # 126
    "Category:Protected areas established in {YEAR1}": "تصنيف:مناطق محمية أسست في {YEAR1}",  # 122
    "Category:{YEAR1} animated films": "تصنيف:أفلام رسوم متحركة {YEAR1}",  # 63
    "Category:{YEAR1} in motorsport": "تصنيف:رياضة محركات في {YEAR1}",  # 106
    "Category:{YEAR1} in motorsport by country": "تصنيف:رياضة المحركات في {YEAR1} حسب البلد",  # 100
    "Category:Symbols introduced in {YEAR1}": "تصنيف:رموز استحدثت في {YEAR1}",  # 77
    "Category:{YEAR1} in English rugby union": "تصنيف:اتحاد الرجبي الإنجليزي في {YEAR1}",  # 123
    "Category:{YEAR1} establishments in the Thirteen Colonies": "تصنيف:تأسيسات سنة {YEAR1} في المستعمرات الثلاثة عشرة",  # 102
    "Category:{YEAR1} in animation": "تصنيف:الرسوم المتحركة في {YEAR1}",  # 83
    "Category:{YEAR1} in English women's sport": "تصنيف:رياضة إنجليزية نسائية في {YEAR1}",  # 122
    "Category:{YEAR1} in New Zealand sport": "تصنيف:رياضة نيوزيلندية في {YEAR1}",  # 122
    "Category:Amphibians described in {YEAR1}": "تصنيف:برمائيات وصفت في {YEAR1}",  # 121
    "Category:Companies disestablished in {YEAR1}": "تصنيف:شركات انحلت في {YEAR1}",  # 119
    "Category:Mass media companies established in {YEAR1}": "تصنيف:شركات إعلامية أسست في {YEAR1}",  # 122
    "Category:Political organizations established in {YEAR1}": "تصنيف:منظمات سياسية أسست في {YEAR1}",  # 107
    "Category:Aviation accidents and incidents in {YEAR1}": "تصنيف:حوادث طيران في {YEAR1}",  # 119
    "Category:Television series set in {YEAR1}": "تصنيف:مسلسلات تلفزيونية تقع أحداثها في {YEAR1}",  # 106
    "Category:Airports established in {YEAR1}": "تصنيف:مطارات أسست في سنة {YEAR1}",  # 100
    "Category:Buildings and structures demolished in {YEAR1}": "تصنيف:مبان ومنشآت هدمت في {YEAR1}",  # 118
    "Category:Currencies introduced in {YEAR1}": "تصنيف:عملات عرضت في {YEAR1}",  # 66
    "Category:Sports leagues established in {YEAR1}": "تصنيف:دوريات رياضية أسست في {YEAR1}",  # 73
    "Category:Technology companies established in {YEAR1}": "تصنيف:شركات تكنولوجيا أسست في {YEAR1}",  # 116
    "Category:Treaties entered into force in {YEAR1}": "تصنيف:معاهدات دخلت حيز التنفيذ في {YEAR1}",  # 113
    "Category:{YEAR1} in Peruvian sport": "تصنيف:رياضة بيروية في {YEAR1}",  # 115
    "Category:Magazines disestablished in {YEAR1}": "تصنيف:مجلات انحلت في {YEAR1}",  # 115
    "Category:Victims of aviation accidents or incidents in {YEAR1}": "تصنيف:ضحايا حوادث طيران في {YEAR1}",  # 115
    "Category:{YEAR1} in hockey": "تصنيف:{YEAR1} في الهوكي",  # 114
    "Category:{YEAR1} in winter sports": "تصنيف:الرياضة الشتوية في {YEAR1}",  # 91
    "Category:{YEAR1} horror films": "تصنيف:أفلام رعب إنتاج {YEAR1}",  # 60
    "Category:{YEAR1} in German football": "تصنيف:كرة القدم الألمانية في {YEAR1}",  # 113
    "Category:{YEAR1} in women's association football": "تصنيف:كرة القدم للسيدات في {YEAR1}",  # 106
    "Category:Basketball teams established in {YEAR1}": "تصنيف:أندية كرة سلة أسست سنة {YEAR1}",  # 99
    "Category:Energy companies established in {YEAR1}": "تصنيف:شركات طاقة أسست في {YEAR1}",  # 113
    "Category:Hotels established in {YEAR1}": "تصنيف:فنادق أسست في {YEAR1}",  # 101
    "Category:Towers completed in {YEAR1}": "تصنيف:أبراج اكتملت في {YEAR1}",  # 113
    "Category:{YEAR1} establishments in Quebec": "تصنيف:تأسيسات سنة {YEAR1} في كيبك",  # 93
    "Category:{YEAR1} comics debuts": "تصنيف:قصص مصورة ظهرت لأول مرة في {YEAR1}",  # 75
    "Category:Railway stations in Great Britain opened in {YEAR1}": "تصنيف:محطات السكك الحديدية في بريطانيا العظمى افتتحت في {YEAR1}",  # 113
    "Category:{YEAR1} mergers and acquisitions": "تصنيف:عمليات الدمج والاستحواذ {YEAR1}",  # 110
    "Category:{YEAR1} romantic comedy films": "تصنيف:أفلام كوميديا رومانسية {YEAR1}",  # 87
    "Category:{YEAR1} in athletics (track and field)": "تصنيف:{YEAR1} في ألعاب القوى (المضمار والميدان)",  # 62
    "Category:{YEAR1} awards": "تصنيف:جوائز {YEAR1}",  # 111
    "Category:{YEAR1} crime films": "تصنيف:أفلام جريمة في {YEAR1}",  # 68
    "Category:{YEAR1} comedy-drama films": "تصنيف:أفلام كوميديا درامية {YEAR1}",  # 74
    "Category:{YEAR1} in Spanish road cycling": "تصنيف:سباقات دراجات على الطريق إسبانية في {YEAR1}",  # 109
    "Category:{YEAR1} film awards": "تصنيف:جوائز الأفلام {YEAR1}",  # 108
    "Category:{YEAR1} musical films": "تصنيف:أفلام موسيقية {YEAR1}",  # 105
    "Category:Libraries established in {YEAR1}": "تصنيف:مكتبات أسست في {YEAR1}",  # 96
    "Category:{YEAR1} fires": "تصنيف:حرائق {YEAR1}",  # 94
    "Category:{YEAR1} in Alberta": "تصنيف:ألبرتا في {YEAR1}",  # 87
    "Category:Government buildings completed in {YEAR1}": "تصنيف:مبان حكومية اكتملت في {YEAR1}",  # 108
    "Category:{YEAR1} in the sport of athletics": "تصنيف:ألعاب قوى المضمار والميدان في {YEAR1}",  # 52
    "Category:National sports teams established in {YEAR1}": "تصنيف:منتخبات رياضية وطنية أسست في {YEAR1}",  # 106
    "Category:Non-renewable resource companies established in {YEAR1}": "تصنيف:شركات موارد غير متجددة أسست في {YEAR1}",  # 106
    "Category:{YEAR1} essays": "تصنيف:مقالات {YEAR1}",  # 101
    "Category:{YEAR1} in Antarctica": "تصنيف:القارة القطبية الجنوبية في {YEAR1}",  # 95
    "Category:{YEAR1} in handball": "تصنيف:كرة اليد في {YEAR1}",  # 101
    "Category:{YEAR1} in multi-sport events": "تصنيف:أحداث رياضية متعددة في {YEAR1}",  # 81
    "Category:Hotel buildings completed in {YEAR1}": "تصنيف:مبان فنادق اكتملت في {YEAR1}",  # 100
    "Category:Video games set in {YEAR1}": "تصنيف:ألعاب فيديو تقع أحداثها في {YEAR1}",  # 65
    "Category:{YEAR1} establishments in Great Britain": "تصنيف:تأسيسات سنة {YEAR1} في بريطانيا العظمى",  # 94
    "Category:{YEAR1} protests": "تصنيف:احتجاجات {YEAR1}",  # 97
    "Category:{YEAR1} in television": "تصنيف:التلفاز في {YEAR1}",  # 82
    "Category:{YEAR1} in chess": "تصنيف:الشطرنج في {YEAR1}",  # 92
    "Category:Cars introduced in {YEAR1}": "تصنيف:سيارات اخترعت في {YEAR1}",  # 55
    "Category:Airlines established in {YEAR1}": "تصنيف:شركات طيران أسست سنة {YEAR1}",  # 94
    "Category:Works set in the {YEAR1}": "تصنيف:أعمال تقع أحداثها في {YEAR1}",  # 98
    "Category:{YEAR1} rugby union tournaments for national teams": "تصنيف:بطولات اتحاد رغبي للمنتخبات الوطنية في {YEAR1}",  # 102
    "Category:{YEAR1} in comics": "تصنيف:قصص مصورة في {YEAR1}",  # 100
    "Category:{YEAR1} in Hong Kong sport": "تصنيف:رياضة هونغ كونغية في {YEAR1}",  # 102
    "Category:{YEAR1} in Peruvian football": "تصنيف:كرة القدم البيروية في {YEAR1}",  # 102
    "Category:Mass media franchises introduced in {YEAR1}": "تصنيف:امتيازات إعلامية استحدثت في {YEAR1}",  # 84
    "Category:Sports clubs and teams disestablished in {YEAR1}": "تصنيف:أندية رياضية انحلت في {YEAR1}",  # 98
    "Category:{YEAR1} romantic drama films": "تصنيف:أفلام رومانسية درامية {YEAR1}",  # 73
    "Category:Explosions in {YEAR1}": "تصنيف:انفجارات في {YEAR1}",  # 100
    "Category:{YEAR1} referendums": "تصنيف:استفتاءات في {YEAR1}",  # 76
    "Category:{YEAR1} in Albanian sport": "تصنيف:رياضة ألبانية في {YEAR1}",  # 98
    "Category:{YEAR1} in computing": "تصنيف:علم الحاسوب في {YEAR1}",  # 96
    "Category:Mosques completed in the {YEAR1}": "تصنيف:مساجد اكتملت في {YEAR1}",  # 98
    "Category:Musical groups established in {YEAR1}": "تصنيف:فرق موسيقية أسست في {YEAR1}",  # 97
    "Category:Academic journals established in {YEAR1}": "تصنيف:نشرات دورية أكاديمية أسست في {YEAR1}",  # 96
    "Category:Wikipedia articles in need of updating from {YEAR1}": "تصنيف:مقالات بحاجة للتحديث منذ {YEAR1}",  # 97
    "Category:Association football clubs disestablished in {YEAR1}": "تصنيف:أندية كرة قدم انحلت في {YEAR1}",  # 96
    "Category:Novels set in the {YEAR1}": "تصنيف:روايات تقع أحداثها في {YEAR1}",  # 96
    "Category:{YEAR1} in the Thirteen Colonies": "تصنيف:المستعمرات الثلاثة عشرة في {YEAR1}",  # 90
    "Category:{YEAR1} documentary films": "تصنيف:أفلام وثائقية {YEAR1}",  # 88
    "Category:{YEAR1} in Spanish football leagues": "تصنيف:دوريات كرة قدم إسبانية في {YEAR1}",  # 95
    "Category:Beetles described in {YEAR1}": "تصنيف:خنافس وصفت في {YEAR1}",  # 95
    "Category:{YEAR1} crime drama films": "تصنيف:أفلام جريمة درامية في {YEAR1}",  # 70
    "Category:{YEAR1} in radio": "تصنيف:راديو في {YEAR1}",  # 77
    "Category:Hospital buildings completed in {YEAR1}": "تصنيف:مباني مستشفيات اكتملت في {YEAR1}",  # 90
    "Category:{YEAR1} in volleyball": "تصنيف:كرة الطائرة في {YEAR1}",  # 76
    "Category:Cabinets established in {YEAR1}": "تصنيف:مجالس وزراء أسست في {YEAR1}",  # 93
    "Category:Computer-related introductions in {YEAR1}": "تصنيف:استحداثات متعلقة بالحواسيب في {YEAR1}",  # 92
    "Category:Electronics companies established in {YEAR1}": "تصنيف:شركات إلكترونيات أسست في {YEAR1}",  # 93
    "Category:Theatres completed in {YEAR1}": "تصنيف:مسارح اكتملت في {YEAR1}",  # 92
    "Category:{YEAR1} in television by country": "تصنيف:التلفاز في {YEAR1} حسب البلد",  # 74
    "Category:Organizations established in the {YEAR1}": "تصنيف:منظمات أسست في {YEAR1}",  # 74
    "Category:{YEAR1} in outer space": "تصنيف:الفضاء في {YEAR1}",  # 88
    "Category:Conglomerate companies established in {YEAR1}": "تصنيف:تكتل شركات أسست في {YEAR1}",  # 90
    "Category:{YEAR1} UCI Road World Championships": "تصنيف:بطولة العالم لسباق الدراجات على الطريق {YEAR1}",  # 89
    "Category:Churches completed in the {YEAR1}": "تصنيف:كنائس اكتملت في {YEAR1}",  # 89
    "Category:Wikipedia articles needing factual verification from {YEAR1}": "تصنيف:مقالات بحاجة للتحقق من المعلومات منذ {YEAR1}",  # 89
    "Category:{YEAR1} meteorology": "تصنيف:الأرصاد الجوية في {YEAR1}",  # 63
    "Category:{YEAR1} in case law": "تصنيف:السوابق القضائية في {YEAR1}",  # 78
    "Category:{YEAR1} establishments in Alberta": "تصنيف:تأسيسات سنة {YEAR1} في ألبرتا",  # 69
    "Category:{YEAR1} in ice hockey": "تصنيف:هوكي الجليد في {YEAR1}",  # 77
    "Category:Office buildings completed in {YEAR1}": "تصنيف:مبان إدارية اكتملت في {YEAR1}",  # 88
    "Category:{YEAR1} operas": "تصنيف:أوبيرات {YEAR1}",  # 68
    "Category:{YEAR1} U.S. National Championships (tennis)": "تصنيف:البطولات الوطنية الأمريكية {YEAR1} (كرة مضرب)",  # 86
    "Category:{YEAR1} animated short films": "تصنيف:أفلام رسوم متحركة قصيرة {YEAR1}",  # 72
    "Category:{YEAR1} software": "تصنيف:برمجيات {YEAR1}",  # 86
    "Category:Literary characters introduced in {YEAR1}": "تصنيف:شخصيات أدبية عرضت في {YEAR1}",  # 87
    "Category:Military units and formations disestablished in {YEAR1}": "تصنيف:وحدات وتشكيلات عسكرية انحلت في {YEAR1}",  # 87
    "Category:Music venues completed in {YEAR1}": "تصنيف:صالات الموسيقى اكتملت في {YEAR1}",  # 59
    "Category:Food and drink companies established in {YEAR1}": "تصنيف:شركات أطعمة ومشروبات أسست في {YEAR1}",  # 84
    "Category:{YEAR1} in international association football": "تصنيف:كرة قدم دولية في {YEAR1}",  # 85
    "Category:{YEAR1} in Albanian football": "تصنيف:كرة القدم الألبانية في {YEAR1}",  # 85
    "Category:{YEAR1} television series endings": "تصنيف:مسلسلات تلفزيونية انتهت في {YEAR1}",  # 58
    "Category:Christian organizations established in {YEAR1}": "تصنيف:منظمات مسيحية أسست في {YEAR1}",  # 84
    "Category:Festivals established in {YEAR1}": "تصنيف:مهرجانات أسست في {YEAR1}",  # 84
    "Category:German companies established in {YEAR1}": "تصنيف:شركات ألمانية أسست في {YEAR1}",  # 85
    "Category:Publishing companies established in {YEAR1}": "تصنيف:شركات نشر أسست في {YEAR1}",  # 51
    "Category:{YEAR1} manga": "تصنيف:مانغا {YEAR1}",  # 83
    "Category:Chemical companies established in {YEAR1}": "تصنيف:شركات كيميائية أسست في {YEAR1}",  # 84
    "Category:{YEAR1} in water polo": "تصنيف:كرة الماء في {YEAR1}",  # 74
    "Category:{YEAR1} independent films": "تصنيف:أفلام مستقلة {YEAR1}",  # 81
    "Category:{YEAR1} in Hong Kong football": "تصنيف:كرة القدم الهونغ الكونغية في {YEAR1}",  # 75
    "Category:{YEAR1} in Hong Kong football leagues": "تصنيف:دوريات كرة قدم هونغ كونغية في {YEAR1}",  # 83
    "Category:{YEAR1} in spaceflight": "تصنيف:رحلات الفضاء في {YEAR1}",  # 83
    "Category:Religious organizations established in the {YEAR1}": "تصنيف:منظمات دينية أسست في {YEAR1}",  # 69
    "Category:Restaurants established in {YEAR1}": "تصنيف:مطاعم أسست في {YEAR1}",  # 83
    "Category:Companies disestablished in {YEAR1} by country": "تصنيف:شركات انحلت في {YEAR1} حسب البلد",  # 82
    "Category:Manufacturing companies disestablished in {YEAR1}": "تصنيف:شركات تصنيع انحلت في {YEAR1}",  # 82
    "Category:Performing groups established in {YEAR1}": "تصنيف:مجموعات أداء أسست في {YEAR1}",  # 82
    "Category:Retail companies established in {YEAR1}": "تصنيف:شركات تجارة التجزئة أسست في {YEAR1}",  # 78
    "Category:Television channels and stations established in {YEAR1}": "تصنيف:قنوات وشبكات تلفزيونية أسست في {YEAR1}",  # 66
    "Category:{YEAR1} health disasters": "تصنيف:كوارث صحية في {YEAR1}",  # 78
    "Category:{YEAR1} controversies": "تصنيف:خلافات {YEAR1}",  # 79
    "Category:{YEAR1} film festivals": "تصنيف:مهرجانات سينمائية {YEAR1}",  # 81
    "Category:Cars discontinued in {YEAR1}": "تصنيف:سيارات توقفت في {YEAR1}",  # 81
    "Category:Design companies established in {YEAR1}": "تصنيف:شركات تصميم أسست في {YEAR1}",  # 79
    "Category:{YEAR1} mass shootings": "تصنيف:إطلاق نار عشوائي {YEAR1}",  # 73
    "Category:{YEAR1} in German football cups": "تصنيف:كؤوس كرة قدم ألمانية في {YEAR1}",  # 80
    "Category:Video games set in the {YEAR1}": "تصنيف:ألعاب فيديو تقع أحداثها في {YEAR1}",  # 80
    "Category:{YEAR1} black comedy films": "تصنيف:أفلام كوميدية سوداء {YEAR1}",  # 52
    "Category:{YEAR1} Vuelta a España": "تصنيف:طواف إسبانيا {YEAR1}",  # 79
    "Category:{YEAR1} United Nations Security Council resolutions": "تصنيف:قرارات مجلس الأمن التابع للأمم المتحدة عام {YEAR1}",  # 77
    "Category:Molluscs described in {YEAR1}": "تصنيف:رخويات وصفت في {YEAR1}",  # 79
    "Category:Research institutes established in {YEAR1}": "تصنيف:معاهد أبحاث أسست في {YEAR1}",  # 56
    "Category:{YEAR1} in baseball": "تصنيف:كرة القاعدة في {YEAR1}",  # 67
    "Category:{YEAR1} in German motorsport": "تصنيف:رياضة محركات ألمانية في {YEAR1}",  # 77
    "Category:Lists of {YEAR1} films by country or language": "تصنيف:قوائم أفلام حسب البلد أو اللغة {YEAR1}",  # 71
    "Category:{YEAR1} in German football leagues": "تصنيف:دوريات كرة قدم ألمانية في {YEAR1}",  # 76
    "Category:{YEAR1} Formula One races": "تصنيف:سباقات فورمولا 1 في سنة {YEAR1}",  # 71
    "Category:{YEAR1} in Formula One": "تصنيف:{YEAR1} في فورمولا 1",  # 73
    "Category:{YEAR1} in Republic of Ireland association football": "تصنيف:كرة قدم أيرلندية في {YEAR1}",  # 74
    "Category:{YEAR1} beauty pageants": "تصنيف:مسابقات ملكة جمال {YEAR1}",  # 75
    "Category:Dams completed in {YEAR1}": "تصنيف:سدود اكتملت في {YEAR1}",  # 75
    "Category:Youth organizations established in {YEAR1}": "تصنيف:منظمات شبابية أسست في {YEAR1}",  # 73
    "Category:{YEAR1}-related lists": "تصنيف:قوائم متعلقة {YEAR1}",  # 60
    "Category:{YEAR1} Giro d'Italia": "تصنيف:طواف إيطاليا {YEAR1}",  # 75
    "Category:{YEAR1} in Caribbean sport": "تصنيف:رياضة كاريبية في {YEAR1}",  # 75
    "Category:{YEAR1} archaeological discoveries": "تصنيف:اكتشافات أثرية في {YEAR1}",  # 74
    "Category:{YEAR1} fiction books": "تصنيف:كتب خيالية {YEAR1}",  # 72
    "Category:{YEAR1} in men's sport": "تصنيف:رياضة رجالية في {YEAR1}",  # 68
    "Category:{YEAR1} albums": "تصنيف:ألبومات {YEAR1}",  # 73
    "Category:Educational institutions established in the {YEAR1}": "تصنيف:هيئات تعليمية أسست في {YEAR1}",  # 74
    "Category:Educational organizations established in the {YEAR1}": "تصنيف:منظمات تعليمية أسست في {YEAR1}",  # 61
    "Category:Infrastructure completed in the {YEAR1}": "تصنيف:بنية تحتية اكتملت في {YEAR1}",  # 73
    "Category:Nations at sport events in {YEAR1}": "تصنيف:بلدان في أحداث رياضية في {YEAR1}",  # 68
    "Category:{YEAR1} Davis Cup": "تصنيف:كأس ديفيز {YEAR1}",  # 73
    "Category:{YEAR1} in video gaming": "تصنيف:ألعاب الفيديو في عام {YEAR1}",  # 56
    "Category:Art museums and galleries established in {YEAR1}": "تصنيف:متاحف فنية ومعارض أسست في {YEAR1}",  # 64
    "Category:Wikipedia articles needing rewrite from {YEAR1}": "تصنيف:مقالات بحاجة لإعادة الكتابة منذ {YEAR1}",  # 73
    "Category:Energy infrastructure completed in {YEAR1}": "تصنيف:بنية تحتية للطاقة اكتملت في {YEAR1}",  # 72
    "Category:Radio stations established in {YEAR1}": "تصنيف:محطات إذاعية أسست في {YEAR1}",  # 68
    "Category:{YEAR1} establishments in Oregon": "تصنيف:تأسيسات سنة {YEAR1} في أوريغون",  # 62
    "Category:{YEAR1} LGBTQ-related films": "تصنيف:أفلام متعلقة بإل جي بي تي {YEAR1}",  # 62
    "Category:{YEAR1} video games": "تصنيف:ألعاب فيديو {YEAR1}",  # 70
    "Category:Library buildings completed in {YEAR1}": "تصنيف:مبان مكتبات اكتملت في {YEAR1}",  # 70
    "Category:{YEAR1} anime films": "تصنيف:أفلام أنمي {YEAR1}",  # 66
    "Category:Products and services discontinued in {YEAR1}": "تصنيف:منتجات وخدمات توقفت في {YEAR1}",  # 70
    "Category:{YEAR1} fantasy films": "تصنيف:أفلام فانتازيا {YEAR1}",  # 62
    "Category:{YEAR1} LGBT-related films": "تصنيف:أفلام متعلقة بإل جي بي تي {YEAR1}",  # 61
    "Category:{YEAR1} comics endings": "تصنيف:قصص مصورة انتهت في {YEAR1}",  # 68
    "Category:{YEAR1} in Icelandic sport": "تصنيف:رياضة آيسلندية في {YEAR1}",  # 68
    "Category:Attacks on buildings and structures in {YEAR1}": "تصنيف:هجمات على مبان ومنشآت في {YEAR1}",  # 68
    "Category:Audiovisual introductions in {YEAR1}": "تصنيف:استحداثات سمعية بصرية في {YEAR1}",  # 68
    "Category:Health care companies established in {YEAR1}": "تصنيف:شركات رعاية صحية أسست في {YEAR1}",  # 68
    "Category:Holding companies established in {YEAR1}": "تصنيف:شركات قابضة أسست في {YEAR1}",  # 68
    "Category:Spacecraft launched in {YEAR1}": "تصنيف:مركبات فضائية أطلقت في {YEAR1}",  # 66
    "Category:Vehicles discontinued in {YEAR1}": "تصنيف:مركبات توقفت في {YEAR1}",  # 68
    "Category:{YEAR1} in field hockey": "تصنيف:هوكي الميدان في {YEAR1}",  # 66
    "Category:{YEAR1} adventure films": "تصنيف:أفلام مغامرات {YEAR1}",  # 52
    "Category:{YEAR1} children's films": "تصنيف:أفلام أطفال {YEAR1}",  # 57
    "Category:Attacks in {YEAR1}": "تصنيف:هجمات في {YEAR1}",  # 67
    "Category:Wikipedia articles needing clarification from {YEAR1}": "تصنيف:مقالات بحاجة للتوضيح منذ {YEAR1}",  # 67
    "Category:{YEAR1} in martial arts": "تصنيف:الفنون القتالية في {YEAR1}",  # 56
    "Category:{YEAR1} in Spanish motorsport": "تصنيف:رياضة محركات إسبانية في {YEAR1}",  # 65
    "Category:Computer companies established in {YEAR1}": "تصنيف:شركات حوسبة أسست في {YEAR1}",  # 66
    "Category:Islamic organizations established in {YEAR1}": "تصنيف:منظمات إسلامية أسست في {YEAR1}",  # 66
    "Category:{YEAR1} in LGBT history": "تصنيف:{YEAR1} في تاريخ المثلية",  # 59
    "Category:{YEAR1} in cricket": "تصنيف:الكريكت في {YEAR1}",  # 57
    "Category:{YEAR1} romance films": "تصنيف:أفلام رومانسية {YEAR1}",  # 55
    "Category:Articles lacking in-text citations from {YEAR1}": "تصنيف:مقالات ينقصها استشهادات مضمنة منذ {YEAR1}",  # 65
    "Category:Musical groups disestablished in {YEAR1}": "تصنيف:فرق موسيقية انحلت في {YEAR1}",  # 64
    "Category:Television series set in the {YEAR1}": "تصنيف:مسلسلات تلفزيونية تقع أحداثها في {YEAR1}",  # 64
    "Category:Terrorist incidents in {YEAR1}": "تصنيف:حوادث إرهابية في {YEAR1}",  # 65
    "Category:{YEAR1} in LGBTQ history": "تصنيف:تاريخ المثلية في {YEAR1}",  # 64
    "Category:{YEAR1} industrial disasters": "تصنيف:كوارث صناعية {YEAR1}",  # 51
    "Category:{YEAR1} in Islam": "تصنيف:الإسلام في {YEAR1}",  # 62
    "Category:{YEAR1} competitions": "تصنيف:منافسات {YEAR1}",  # 63
    "Category:{YEAR1} in Nova Scotia": "تصنيف:نوفا سكوشا في {YEAR1}",  # 59
    "Category:{YEAR1} censuses": "تصنيف:تعداد السكان في {YEAR1}",  # 63
    "Category:{YEAR1} in Oregon": "تصنيف:أوريغون في {YEAR1}",  # 53
    "Category:Butterflies described in {YEAR1}": "تصنيف:فراشات وصفت في {YEAR1}",  # 63
    "Category:{YEAR1} in labor relations": "تصنيف:علاقات عمالية في {YEAR1}",  # 59
    "Category:Trade unions established in {YEAR1}": "تصنيف:نقابات عمالية أسست في {YEAR1}",  # 58
    "Category:Articles needing cleanup from {YEAR1}": "تصنيف:مقالات بحاجة لتهذيب منذ {YEAR1}",  # 61
    "Category:Crustaceans described in {YEAR1}": "تصنيف:قشريات وصفت في {YEAR1}",  # 60
    "Category:{YEAR1} people": "تصنيف:أشخاص في {YEAR1}",  # 60
    "Category:{YEAR1} United States presidential election": "تصنيف:انتخابات الرئاسة الأمريكية {YEAR1}",  # 59
    "Category:{YEAR1} in gymnastics": "تصنيف:الجمباز في {YEAR1}",  # 53
    "Category:{YEAR1} in men's association football": "تصنيف:كرة القدم للرجال في {YEAR1}",  # 60
    "Category:{YEAR1} in association football by country": "تصنيف:كرة القدم في {YEAR1} حسب البلد",  # 59
    "Category:Articles with empty sections from {YEAR1}": "تصنيف:مقالات بها أقسام فارغة منذ {YEAR1}",  # 60
    "Category:Record labels established in {YEAR1}": "تصنيف:شركات تسجيلات أسست في {YEAR1}",  # 52
    "Category:{YEAR1} in United States case law": "تصنيف:السوابق القضائية الأمريكية في {YEAR1}",  # 51
    "Category:Battles in {YEAR1}": "تصنيف:معارك في {YEAR1}",  # 58
    "Category:Candidates in the {YEAR1} United States presidential election": "تصنيف:مرشحو الرئاسة الأمريكية لعام {YEAR1}",  # 56
    "Category:Performing groups disestablished in {YEAR1}": "تصنيف:مجموعات أداء انحلت في {YEAR1}",  # 59
    "Category:Recurring events disestablished in {YEAR1}": "تصنيف:أحداث دورية انحلت في {YEAR1}",  # 58
    "Category:Transport infrastructure completed in the {YEAR1}": "تصنيف:بنية تحتية للنقل اكتملت في {YEAR1}",  # 59
    "Category:UK MPs {YEAR1}": "تصنيف:أعضاء برلمان المملكة المتحدة {YEAR1}",  # 58
    "Category:{YEAR1} in medicine": "تصنيف:الطب في {YEAR1}",  # 52
    "Category:Populated places disestablished in the {YEAR1}": "تصنيف:أماكن مأهولة انحلت في {YEAR1}",  # 57
    "Category:Spiders described in {YEAR1}": "تصنيف:عناكب وصفت في {YEAR1}",  # 57
    "Category:Television characters introduced in {YEAR1}": "تصنيف:شخصيات تلفزيونية ظهرت في {YEAR1}",  # 54
    "Category:{YEAR1} Football League Cup": "تصنيف:كأس الرابطة الإنجليزية للمحترفين {YEAR1}",  # 56
    "Category:Entertainment companies disestablished in {YEAR1}": "تصنيف:شركات ترفيه انحلت في {YEAR1}",  # 56
    "Category:Politicians assassinated in {YEAR1}": "تصنيف:سياسيون مغتالون في {YEAR1}",  # 55
    "Category:Programming languages created in {YEAR1}": "تصنيف:لغات برمجة أنشئت في {YEAR1}",  # 56
    "Category:{YEAR1} in Northern Ireland sport": "تصنيف:رياضة أيرلندية شمالية في {YEAR1}",  # 55
    "Category:{YEAR1} events in New Zealand by month": "تصنيف:نيوزيلنديون حسب الشهر في أحداث {YEAR1}",  # 55
    "Category:{YEAR1} in Albanian football leagues": "تصنيف:دوريات كرة قدم ألبانية في {YEAR1}",  # 55
    "Category:Populated places disestablished in {YEAR1}": "تصنيف:أماكن مأهولة انحلت في {YEAR1}",  # 55
    "Category:{YEAR1} war films": "تصنيف:أفلام حربية {YEAR1}",  # 51
    "Category:Handball clubs established in {YEAR1}": "تصنيف:أندية كرة يد أسست في {YEAR1}",  # 54
    "Category:Roman Catholic churches completed in the {YEAR1}": "تصنيف:كنائس رومانية كاثوليكية اكتملت في {YEAR1}",  # 53
    "Category:{YEAR1} Australian Open": "تصنيف:أستراليا المفتوحة {YEAR1}",  # 53
    "Category:Bridges completed in the {YEAR1}": "تصنيف:جسور اكتملت في {YEAR1}",  # 51
    "Category:Software companies established in {YEAR1}": "تصنيف:شركات برمجيات أسست في {YEAR1}",  # 51
    "Category:{YEAR1} in the Basque Country (autonomous community)": "تصنيف:منطقة الباسك ذاتية الحكم في {YEAR1}",  # 51
    "Category:{YEAR1} in basketball leagues": "تصنيف:دوريات كرة سلة في {YEAR1}",  # 51
    "Category:Musical groups reestablished in {YEAR1}": "تصنيف:فرق موسيقية أعيد تأسيسها في {YEAR1}",  # 52
    "Category:{YEAR1} in Barbados": "تصنيف:بربادوس في {YEAR1}",  # 51
    "Category:Hockey clubs established in {YEAR1}": "تصنيف:أندية هوكي تأسست في {YEAR1}",  # 51
    "Category:Recurring sporting events disestablished in {YEAR1}": "تصنيف:أحداث رياضية دورية انحلت في {YEAR1}",  # 51
}
