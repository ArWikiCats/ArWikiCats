#
from src import new_func_lab

data = {
    "Category:Afghan diplomats": "تصنيف:دبلوماسيون أفغان",
    "Category:Afghan emigrants": "تصنيف:مهاجرون أفغان",
    "Category:Afghan expatriates": "تصنيف:مغتربون أفغان",
    "Category:Ambassadors of Afghanistan to Argentina": "تصنيف:سفراء أفغانستان إلى الأرجنتين",
    "Category:Ambassadors of Afghanistan to Australia": "تصنيف:سفراء أفغانستان إلى أستراليا",
    "Category:Ambassadors of Afghanistan": "تصنيف:سفراء أفغانستان",
    "Category:Ambassadors of the Ottoman Empire": "تصنيف:سفراء الدولة العثمانية",
    "Category:Ambassadors to the Ottoman Empire": "تصنيف:سفراء لدى الدولة العثمانية",
    "Category:American nuclear medicine physicians": "تصنيف:أطباء طب نووي أمريكيون",
    "Category:American people by status": "تصنيف:أمريكيون حسب الحالة",
    "Category:American people of the Iraq War": "تصنيف:أمريكيون من حرب العراق",
    "Category:Argentine multi-instrumentalists": "تصنيف:عازفون على عدة آلات أرجنتينيون",
    "Category:Attacks on diplomatic missions": "تصنيف:هجمات على بعثات دبلوماسية",
    "Category:Australian Internet celebrities": "تصنيف:مشاهير إنترنت أستراليون",
    "Category:Canadian nuclear medicine physicians": "تصنيف:أطباء طب نووي كنديون",
    "Category:Croatian nuclear medicine physicians": "تصنيف:أطباء طب نووي كروات",
    "Category:European women in business": "تصنيف:سيدات أعمال أوروبيات",
    "Category:Expatriate male actors in New Zealand": "تصنيف:ممثلون ذكور مغتربون في نيوزيلندا",
    "Category:Expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
    "Category:German nuclear medicine physicians": "تصنيف:أطباء طب نووي ألمان",
    "Category:Immigrants to New Zealand": "تصنيف:مهاجرون إلى نيوزيلندا",
    "Category:Immigrants to the United Kingdom from Aden": "تصنيف:مهاجرون إلى المملكة المتحدة من عدن",
    "Category:Immigration to New Zealand": "تصنيف:الهجرة إلى نيوزيلندا",
    "Category:Internees at the Sheberghan Prison": "تصنيف:معتقلين في سجن شيبرغان",
    "Category:Iranian nuclear medicine physicians": "تصنيف:أطباء طب نووي إيرانيون",
    "Category:Israeli people of Northern Ireland descent": "تصنيف:إسرائيليون من أصل أيرلندي شمالي",
    "Category:Italian defectors to the Soviet Union": "تصنيف:إيطاليون منشقون إلى الاتحاد السوفيتي",
    "Category:Ivorian American": "تصنيف:أمريكيون إيفواريون",
    "Category:Ivorian diaspora in Asia": "تصنيف:شتات إيفواري في آسيا",
    "Category:Ivorian emigrants": "تصنيف:مهاجرون إيفواريون",
    "Category:Ivorian expatriates": "تصنيف:مغتربون إيفواريون",
    "Category:Medical doctors by specialty and nationality": "تصنيف:أطباء حسب التخصص والجنسية",
    "Category:Multi-instrumentalists": "تصنيف:عازفون على عدة آلات",
    "Category:People by nationality and status": "تصنيف:أشخاص حسب الجنسية والحالة",
    "Category:People executed by Afghanistan": "تصنيف:أشخاص أعدموا من قبل أفغانستان",
    "Category:People from Buenos Aires": "تصنيف:أشخاص من بوينس آيرس",
    "Category:People in arts occupations by nationality": "تصنيف:مهن أشخاص في الفنون حسب الجنسية",
    "Category:People of Ivorian descent": "تصنيف:أشخاص من أصل إيفواري",
    "Category:Polish businesspeople": "تصنيف:رجال أعمال بولنديون",
    "Category:Polish women by occupation": "تصنيف:بولنديات حسب المهنة",
    "Category:Polish women in business": "تصنيف:سيدات أعمال بولنديات",
    "Category:Portuguese healthcare managers": "تصنيف:مدراء رعاية صحية برتغاليون",
    "Category:Prisoners and detainees of Afghanistan": "تصنيف:سجناء ومعتقلون في أفغانستان",
    "Category:Prisons in Afghanistan": "تصنيف:سجون في أفغانستان",
    "Category:Scholars by subfield": "تصنيف:دارسون حسب الحقل الفرعي",
    "Category:Singers from Buenos Aires": "تصنيف:مغنون من بوينس آيرس",
    "Category:Women in business by nationality": "تصنيف:سيدات أعمال حسب الجنسية",
    "Category:women in business": "تصنيف:سيدات أعمال"
}


def ye_test_one_dataset(dataset):
    print(f"len of dataset: {len(dataset)}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = new_func_lab(cat)
        if result == ar:
            assert result == ar
        else:
            org[cat] = ar
            diff[cat] = result

    assert org == diff
