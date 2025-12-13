#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

pan_arican = {
    "Category:Members of the Pan-African Parliament": "تصنيف:أعضاء البرلمان الإفريقي",
    "Category:Members of the Pan-African Parliament from Algeria": "تصنيف:أعضاء البرلمان الإفريقي من الجزائر",
    "Category:Members of the Pan-African Parliament from Angola": "تصنيف:أعضاء البرلمان الإفريقي من أنغولا",
    "Category:Members of the Pan-African Parliament from Benin": "تصنيف:أعضاء البرلمان الإفريقي من بنين",
    "Category:Members of the Pan-African Parliament from Botswana": "تصنيف:أعضاء البرلمان الإفريقي من بوتسوانا",
    "Category:Members of the Pan-African Parliament from Burkina Faso": "تصنيف:أعضاء البرلمان الإفريقي من بوركينا فاسو",
    "Category:Members of the Pan-African Parliament from Burundi": "تصنيف:أعضاء البرلمان الإفريقي من بوروندي",
    "Category:Members of the Pan-African Parliament from Cameroon": "تصنيف:أعضاء البرلمان الإفريقي من الكاميرون",
    "Category:Members of the Pan-African Parliament from Cape Verde": "تصنيف:أعضاء البرلمان الإفريقي من الرأس الأخضر",
    "Category:Members of the Pan-African Parliament from Chad": "تصنيف:أعضاء البرلمان الإفريقي من تشاد",
    "Category:Members of the Pan-African Parliament from Djibouti": "تصنيف:أعضاء البرلمان الإفريقي من جيبوتي",
    "Category:Members of the Pan-African Parliament from Egypt": "تصنيف:أعضاء البرلمان الإفريقي من مصر",
    "Category:Members of the Pan-African Parliament from Equatorial Guinea": "تصنيف:أعضاء البرلمان الإفريقي من غينيا الاستوائية",
    "Category:Members of the Pan-African Parliament from Eswatini": "تصنيف:أعضاء البرلمان الإفريقي من إسواتيني",
    "Category:Members of the Pan-African Parliament from Gabon": "تصنيف:أعضاء البرلمان الإفريقي من الغابون",
    "Category:Members of the Pan-African Parliament from Ghana": "تصنيف:أعضاء البرلمان الإفريقي من غانا",
    "Category:Members of the Pan-African Parliament from Lesotho": "تصنيف:أعضاء البرلمان الإفريقي من ليسوتو",
    "Category:Members of the Pan-African Parliament from Libya": "تصنيف:أعضاء البرلمان الإفريقي من ليبيا",
    "Category:Members of the Pan-African Parliament from Mali": "تصنيف:أعضاء البرلمان الإفريقي من مالي",
    "Category:Members of the Pan-African Parliament from Mozambique": "تصنيف:أعضاء البرلمان الإفريقي من موزمبيق",
    "Category:Members of the Pan-African Parliament from Namibia": "تصنيف:أعضاء البرلمان الإفريقي من ناميبيا",
    "Category:Members of the Pan-African Parliament from Niger": "تصنيف:أعضاء البرلمان الإفريقي من النيجر",
    "Category:Members of the Pan-African Parliament from Nigeria": "تصنيف:أعضاء البرلمان الإفريقي من نيجيريا",
    "Category:Members of the Pan-African Parliament from Rwanda": "تصنيف:أعضاء البرلمان الإفريقي من رواندا",
    "Category:Members of the Pan-African Parliament from Senegal": "تصنيف:أعضاء البرلمان الإفريقي من السنغال",
    "Category:Members of the Pan-African Parliament from Sierra Leone": "تصنيف:أعضاء البرلمان الإفريقي من سيراليون",
    "Category:Members of the Pan-African Parliament from South Africa": "تصنيف:أعضاء البرلمان الإفريقي من جنوب إفريقيا",
    "Category:Members of the Pan-African Parliament from South Sudan": "تصنيف:أعضاء البرلمان الإفريقي من جنوب السودان",
    "Category:Members of the Pan-African Parliament from Sudan": "تصنيف:أعضاء البرلمان الإفريقي من السودان",
    "Category:Members of the Pan-African Parliament from Tanzania": "تصنيف:أعضاء البرلمان الإفريقي من تنزانيا",
    "Category:Members of the Pan-African Parliament from the Central African Republic": "تصنيف:أعضاء البرلمان الإفريقي من جمهورية إفريقيا الوسطى",
    "Category:Members of the Pan-African Parliament from the Gambia": "تصنيف:أعضاء البرلمان الإفريقي من غامبيا",
    "Category:Members of the Pan-African Parliament from republic of congo": "تصنيف:أعضاء البرلمان الإفريقي من جمهورية الكونغو",
    "Category:Members of the Pan-African Parliament from the Sahrawi Arab Democratic Republic": "تصنيف:أعضاء البرلمان الإفريقي من الجمهورية العربية الصحراوية الديمقراطية",
    "Category:Members of the Pan-African Parliament from Togo": "تصنيف:أعضاء البرلمان الإفريقي من توغو",
    "Category:Members of the Pan-African Parliament from Tunisia": "تصنيف:أعضاء البرلمان الإفريقي من تونس",
    "Category:Members of the Pan-African Parliament from Uganda": "تصنيف:أعضاء البرلمان الإفريقي من أوغندا",
    "Category:Members of the Pan-African Parliament from Zambia": "تصنيف:أعضاء البرلمان الإفريقي من زامبيا",
    "Category:Members of the Pan-African Parliament from Zimbabwe": "تصنيف:أعضاء البرلمان الإفريقي من زيمبابوي",
}


@pytest.mark.dump
def test_pan_arican() -> None:
    expected, diff_result = one_dump_test(pan_arican, resolve_arabic_category_label)

    dump_diff(diff_result, "test_pan_arican")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(pan_arican):,}"


@pytest.mark.parametrize("category, expected", pan_arican.items(), ids=pan_arican.keys())
@pytest.mark.slow
def test_pan_arican_dump(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
