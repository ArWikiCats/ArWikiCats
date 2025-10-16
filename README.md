# خريطة عمل الكود: إنشاء فئات في ويكيبيديا العربية

```mermaid
graph TD
    A[إدخال النص المطلوب (Category Name)] --> B(make-main/m.py: تحليل الأوامر و إعداد المعطيات);
    B --> C{تحضير بيئة العمل (import) };
    C --> D(make-main/m.py: استدعاء دالة `event` من bot.py);
    D --> E(make-main/bot.py: استدعاء دالة `event` من main.py);
    E --> F(make-main/main.py: معالجة قائمة الفئات و بداية المعالجة);
    F --> G{ (make-main/main.py) : تكرار على قائمة الفئات المدخلة };
    G --> H(make-main/ma_bots/event_lab_bot.py: استدعاء `event_Lab` (توليد العنوان العربي للفئة));
    H --> I{ (make-main/ma_bots/event_lab_bot.py): change_cat(تصحيح اسم الفئة الانجليزية (اختياري)) };
    I --> J{ (make-main/ma_bots/event_lab_bot.py): تحديد نوع الفئة و التحضير للبحث عن العنوان المناسب (بناءً على نوع الفئة) };
    J --> K{ (make-main/ma_bots/event_lab_bot.py): استدعاء `get_list_of_and_cat3`  (لتحديد العنوان المناسب بناء على نوع الفئة) };
    K --> L{ (make-main/ma_bots/fax2.py): تحديد قائمة الكلمات المساعدة (مثل أفعال او صفات) };
    L --> M{ (make-main/ma_bots/fax2.py):  إيجاد العنوان العربي المناسب باستخدام قوائم (حسب نوع الفئة) };
    M --> N( (make-main/ma_bots/event_lab_bot.py): إذا لم يتم العثور على عنوان، يتم استدعاء دالة `event2` );
    N --> O{ (make-main/ma_bots/event2bot.py): معالجة العنوان (توليد العنوان العربي للفئة) };
    O --> P{ (make-main/ma_bots/event2bot.py): تحديد نوع الفئة و التحضير للبحث عن العنوان المناسب (بناءً على نوع الفئة) };
    P --> Q{ (make-main/ma_bots/event2bot.py):  استدعاء `Get_contry` (إذا كان عنوان فئة يتعلق بدولة ما) };
    Q --> R{ (make-main/ma_bots/contry_bot.py):  استدعاء  `Get_contry2`  (بناء على اسم الدولة) };
    R --> S{ (make-main/ma_bots/c_2_tit_bot2.py): استدعاء  `contry_2_tit`  (لتوليد العنوان العربي للدولة) };
    S --> T{ (make-main/ma_bots/c_2_tit_bot.py): استدعاء  `Get_c_t_lab`  (لتحديد العنوان المناسب للدولة) };
    T --> U(  (make-main/ma_bots/c_2_tit_bot.py): استدعاء  `Get_contry` (من جديد)   );
    U --> V(  (make-main/ma_bots/contry_bot.py): استدعاء  `Get_contry2` (من جديد)  );
    V --> W{ (make-main/ma_bots/c_2_tit_bot.py): استدعاء `Get_team_work_Club` (لتحديد العنوان المناسب للفريق) };
    W --> X(  (make-main/team_work.py): البحث في القوائم أو استخدام API لـ kooora.com  );
    X --> Y{ (make-main/ma_bots/event2bot.py): في حال عدم إيجاد عنوان، استخدام الدوال الأخرى (مثل `test4_2018_Jobs` و `test_films`) };
    Y --> Z( (make-main/bots/test_4.py و bots/test_5.py): استخدام  القوائم و الدوال المساعدة لتوليد العنوان العربي);
    Z --> AA( (make-main/ma_bots/event2bot.py): الحصول على العنوان النهائي و اضافته الى القائمة );
    AA --> BB{ (make-main/main.py) : إذا كان هناك سنة، يتم إضافتها إلى العنوان النهائي };
    BB --> CC(make-main/main.py: إرجاع قائمة العناوين المترجمة);
    CC --> DD[إخراج الترجمة (عرض النتائج)]
