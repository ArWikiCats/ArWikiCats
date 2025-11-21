#
import pytest
from load_one_data import dump_diff, ye_test_one_dataset

from src import new_func_lab_final_label

data = {
    "Category:Georgia (U.S. state) attorneys general": "تصنيف:مدعي ولاية جورجيا العام",
    "Category:Georgia (U.S. state) ballot measures": "تصنيف:إجراءات اقتراع ولاية جورجيا",
    "Category:Georgia (U.S. state) city councils": "تصنيف:مجالس مدن ولاية جورجيا",
    "Category:Georgia (U.S. state) counties": "تصنيف:مقاطعات ولاية جورجيا",
    "Category:Georgia (U.S. state) Democratic-Republicans": "تصنيف:أعضاء الحزب الديمقراطي الجمهوري في ولاية جورجيا",
    "Category:Georgia (U.S. state) Democrats": "تصنيف:ديمقراطيون من ولاية جورجيا",
    "Category:Georgia (U.S. state) elections": "تصنيف:انتخابات ولاية جورجيا",
    "Category:Georgia (U.S. state) elections by decade": "تصنيف:انتخابات ولاية جورجيا حسب العقد",
    "Category:Georgia (U.S. state) elections by year": "تصنيف:انتخابات ولاية جورجيا حسب السنة",
    "Category:Georgia (U.S. state) Federalists": "تصنيف:أعضاء الحزب الفيدرالي الأمريكي في ولاية جورجيا",
    "Category:Georgia (U.S. state) Greenbacks": "تصنيف:أعضاء حزب الدولار الأمريكي في ولاية جورجيا",
    "Category:Georgia (U.S. state) Greens": "تصنيف:أعضاء حزب الخضر في ولاية جورجيا",
    "Category:Georgia (U.S. state) gubernatorial elections": "تصنيف:انتخابات حاكم ولاية جورجيا",
    "Category:Georgia (U.S. state) independents": "تصنيف:أعضاء في ولاية جورجيا",
    "Category:Georgia (U.S. state) in fiction": "تصنيف:ولاية جورجيا في الخيال",
    "Category:Georgia (U.S. state) in fiction by city": "تصنيف:ولاية جورجيا في الخيال حسب المدينة",
    "Category:Georgia (U.S. state) in the American Civil War": "تصنيف:ولاية جورجيا في الحرب الأهلية الأمريكية",
    "Category:Georgia (U.S. state) in the American Revolution": "تصنيف:ولاية جورجيا في الثورة الأمريكية",
    "Category:Georgia (U.S. state) in the War of 1812": "تصنيف:ولاية جورجيا في الحرب في 1812",
    "Category:Georgia (U.S. state) Jacksonians": "تصنيف:أعضاء جاكسونيون في ولاية جورجيا",
    "Category:Georgia (U.S. state) Know Nothings": "تصنيف:أعضاء حزب لا أدري في ولاية جورجيا",
    "Category:Georgia (U.S. state) law": "تصنيف:قانون ولاية جورجيا",
    "Category:Georgia (U.S. state) law-related lists": "تصنيف:قوائم متعلقة بقانون ولاية جورجيا",
    "Category:Georgia (U.S. state) lawyers": "تصنيف:محامون من ولاية جورجيا",
    "Category:Georgia (U.S. state) local politicians": "تصنيف:سياسيون محليون في ولاية جورجيا",
    "Category:Georgia (U.S. state) navigational boxes": "تصنيف:صناديق تصفح ولاية جورجيا",
    "Category:Georgia (U.S. state) politicians": "تصنيف:سياسيو ولاية جورجيا",
    "Category:Georgia (U.S. state) politicians by century": "تصنيف:سياسيو ولاية جورجيا حسب القرن",
    "Category:Georgia (U.S. state) politicians by party": "تصنيف:سياسيو ولاية جورجيا حسب الحزب",
    "Category:Georgia (U.S. state) politicians by populated place": "تصنيف:سياسيو ولاية جورجيا حسب المكان المأهول",
    "Category:Georgia (U.S. state) politicians convicted of crimes": "تصنيف:سياسيو ولاية جورجيا أدينوا بجرائم",
    "Category:Georgia (U.S. state) politics-related lists": "تصنيف:قوائم متعلقة بسياسة ولاية جورجيا",
    "Category:Georgia (U.S. state)-related lists": "تصنيف:قوائم متعلقة بولاية جورجيا",
    "Category:Georgia (U.S. state) Republicans": "تصنيف:أعضاء الحزب الجمهوري في ولاية جورجيا",
    "Category:Georgia (U.S. state) sheriffs": "تصنيف:مأمورو ولاية جورجيا",
    "Category:Georgia (U.S. state) socialists": "تصنيف:أعضاء الحزب الاشتراكي في ولاية جورجيا",
    "Category:Georgia (U.S. state) state court judges": "تصنيف:قضاة محكمة ولاية جورجيا",
    "Category:Georgia (U.S. state) state courts": "تصنيف:محكمة ولاية جورجيا",
    "Category:Georgia (U.S. state) state senators": "تصنيف:أعضاء مجلس شيوخ ولاية جورجيا",
    "Category:Georgia (U.S. state) templates": "تصنيف:قوالب ولاية جورجيا",
    "Category:Georgia (U.S. state) Unionists": "تصنيف:أعضاء الحزب الوحدوي في ولاية جورجيا",
    "Category:Georgia (U.S. state) Whigs": "تصنيف:أعضاء حزب اليمين في ولاية جورجيا"

}


@pytest.mark.fast
def test_us_counties():
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_us_counties")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


empty_data = {

    "Category:Georgia (U.S. state) Attorney General elections": "",
    "Category:Georgia (U.S. state) case law": "",
    "Category:Georgia (U.S. state) city council members": "",
    "Category:Georgia (U.S. state) city user templates": "",
    "Category:Georgia (U.S. state) college and university user templates": "",
    "Category:Georgia (U.S. state) commissioners of agriculture": "",
    "Category:Georgia (U.S. state) Constitutional Unionists": "",
    "Category:Georgia (U.S. state) county navigational boxes": "",
    "Category:Georgia (U.S. state) culture by city": "",
    "Category:Georgia (U.S. state) education navigational boxes": "",
    "Category:Georgia (U.S. state) education-related lists": "",
    "Category:Georgia (U.S. state) election templates": "",
    "Category:Georgia (U.S. state) geography-related lists": "",
    "Category:Georgia (U.S. state) government navigational boxes": "",
    "Category:Georgia (U.S. state) high school athletic conference navigational boxes": "",
    "Category:Georgia (U.S. state) history-related lists": "",
    "Category:Georgia (U.S. state) judicial elections": "",
    "Category:Georgia (U.S. state) labor commissioners": "",
    "Category:Georgia (U.S. state) legislative districts": "",
    "Category:Georgia (U.S. state) legislative sessions": "",
    "Category:Georgia (U.S. state) Libertarians": "",
    "Category:Georgia (U.S. state) lieutenant gubernatorial elections": "",
    "Category:Georgia (U.S. state) location map modules": "",
    "Category:Georgia (U.S. state) maps": "",
    "Category:Georgia (U.S. state) mass media navigational boxes": "",
    "Category:Georgia (U.S. state) militia": "",
    "Category:Georgia (U.S. state) militiamen in the American Revolution": "",
    "Category:Georgia (U.S. state) National Republicans": "",
    "Category:Georgia (U.S. state) Oppositionists": "",
    "Category:Georgia (U.S. state) placenames of Native American origin": "",
    "Category:Georgia (U.S. state) Populists": "",
    "Category:Georgia (U.S. state) portal": "",
    "Category:Georgia (U.S. state) postmasters": "",
    "Category:Georgia (U.S. state) presidential primaries": "",
    "Category:Georgia (U.S. state) Progressives (1912)": "",
    "Category:Georgia (U.S. state) Prohibitionists": "",
    "Category:Georgia (U.S. state) radio market navigational boxes": "",
    "Category:Georgia (U.S. state) railroads": "",
    "Category:Georgia (U.S. state) Sea Islands": "",
    "Category:Georgia (U.S. state) shopping mall templates": "",
    "Category:Georgia (U.S. state) society": "",
    "Category:Georgia (U.S. state) special elections": "",
    "Category:Georgia (U.S. state) sports-related lists": "",
    "Category:Georgia (U.S. state) state constitutional officer elections": "",
    "Category:Georgia (U.S. state) state forests": "",
    "Category:Georgia (U.S. state) statutes": "",
    "Category:Georgia (U.S. state) television station user templates": "",
    "Category:Georgia (U.S. state) transportation-related lists": "",
    "Category:Georgia (U. S. state) universities and colleges leaders navigational boxes": "",
    "Category:Georgia (U.S. state) universities and colleges navigational boxes": "",
    "Category:Georgia (U.S. state) user categories": "",
    "Category:Georgia (U.S. state) user templates": "",
    "Category:Georgia (U.S. state) Wikipedians": "",
    "Category:Georgia (U.S. state) wine": "",
}


@pytest.mark.fast
def test_us_counties_empty():
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_us_counties_empty")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
