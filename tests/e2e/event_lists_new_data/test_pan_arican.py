#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

pan_arican = {
    "Members of the Pan-African Parliament": "أعضاء البرلمان الإفريقي",
    "Members of the Pan-African Parliament from Algeria": "أعضاء البرلمان الإفريقي من الجزائر",
    "Members of the Pan-African Parliament from Angola": "أعضاء البرلمان الإفريقي من أنغولا",
    "Members of the Pan-African Parliament from Benin": "أعضاء البرلمان الإفريقي من بنين",
    "Members of the Pan-African Parliament from Botswana": "أعضاء البرلمان الإفريقي من بوتسوانا",
    "Members of the Pan-African Parliament from Burkina Faso": "أعضاء البرلمان الإفريقي من بوركينا فاسو",
    "Members of the Pan-African Parliament from Burundi": "أعضاء البرلمان الإفريقي من بوروندي",
    "Members of the Pan-African Parliament from Cameroon": "أعضاء البرلمان الإفريقي من الكاميرون",
    "Members of the Pan-African Parliament from Cape Verde": "أعضاء البرلمان الإفريقي من الرأس الأخضر",
    "Members of the Pan-African Parliament from Chad": "أعضاء البرلمان الإفريقي من تشاد",
    "Members of the Pan-African Parliament from Djibouti": "أعضاء البرلمان الإفريقي من جيبوتي",
    "Members of the Pan-African Parliament from Egypt": "أعضاء البرلمان الإفريقي من مصر",
    "Members of the Pan-African Parliament from Equatorial Guinea": "أعضاء البرلمان الإفريقي من غينيا الاستوائية",
    "Members of the Pan-African Parliament from Eswatini": "أعضاء البرلمان الإفريقي من إسواتيني",
    "Members of the Pan-African Parliament from Gabon": "أعضاء البرلمان الإفريقي من الغابون",
    "Members of the Pan-African Parliament from Ghana": "أعضاء البرلمان الإفريقي من غانا",
    "Members of the Pan-African Parliament from Lesotho": "أعضاء البرلمان الإفريقي من ليسوتو",
    "Members of the Pan-African Parliament from Libya": "أعضاء البرلمان الإفريقي من ليبيا",
    "Members of the Pan-African Parliament from Mali": "أعضاء البرلمان الإفريقي من مالي",
    "Members of the Pan-African Parliament from Mozambique": "أعضاء البرلمان الإفريقي من موزمبيق",
    "Members of the Pan-African Parliament from Namibia": "أعضاء البرلمان الإفريقي من ناميبيا",
    "Members of the Pan-African Parliament from Niger": "أعضاء البرلمان الإفريقي من النيجر",
    "Members of the Pan-African Parliament from Nigeria": "أعضاء البرلمان الإفريقي من نيجيريا",
    "Members of the Pan-African Parliament from Rwanda": "أعضاء البرلمان الإفريقي من رواندا",
    "Members of the Pan-African Parliament from Senegal": "أعضاء البرلمان الإفريقي من السنغال",
    "Members of the Pan-African Parliament from Sierra Leone": "أعضاء البرلمان الإفريقي من سيراليون",
    "Members of the Pan-African Parliament from South Africa": "أعضاء البرلمان الإفريقي من جنوب إفريقيا",
    "Members of the Pan-African Parliament from South Sudan": "أعضاء البرلمان الإفريقي من جنوب السودان",
    "Members of the Pan-African Parliament from Sudan": "أعضاء البرلمان الإفريقي من السودان",
    "Members of the Pan-African Parliament from Tanzania": "أعضاء البرلمان الإفريقي من تنزانيا",
    "Members of the Pan-African Parliament from the Central African Republic": "أعضاء البرلمان الإفريقي من جمهورية إفريقيا الوسطى",
    "Members of the Pan-African Parliament from the Gambia": "أعضاء البرلمان الإفريقي من غامبيا",
    "Members of the Pan-African Parliament from republic of congo": "أعضاء البرلمان الإفريقي من جمهورية الكونغو",
    "Members of the Pan-African Parliament from the Sahrawi Arab Democratic Republic": "أعضاء البرلمان الإفريقي من الجمهورية العربية الصحراوية الديمقراطية",
    "Members of the Pan-African Parliament from Togo": "أعضاء البرلمان الإفريقي من توغو",
    "Members of the Pan-African Parliament from Tunisia": "أعضاء البرلمان الإفريقي من تونس",
    "Members of the Pan-African Parliament from Uganda": "أعضاء البرلمان الإفريقي من أوغندا",
    "Members of the Pan-African Parliament from Zambia": "أعضاء البرلمان الإفريقي من زامبيا",
    "Members of the Pan-African Parliament from Zimbabwe": "أعضاء البرلمان الإفريقي من زيمبابوي",
}


@pytest.mark.dump
def test_pan_arican() -> None:
    expected, diff_result = one_dump_test(pan_arican, resolve_label_ar)

    dump_diff(diff_result, "test_pan_arican")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(pan_arican):,}"


@pytest.mark.parametrize("category, expected", pan_arican.items(), ids=pan_arican.keys())
@pytest.mark.slow
def test_pan_arican_dump(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
