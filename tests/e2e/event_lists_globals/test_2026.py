#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_0 = {
    "Canadian football people": "أعلام كرة قدم كندية",
    "Canadian football leagues": "دوريات كرة قدم كندية",
    "1880s in film by country": "الأفلام في عقد 1880 حسب البلد",
    "18th-century people of the Dutch Empire": "أشخاص في القرن 18 في الإمبراطورية الهولندية",
    "20th-century presidents of Russia": "رؤساء في القرن 20 في روسيا",
    "20th century members of maine legislature": "أعضاء هيئة مين التشريعية في القرن 20",
    "Wheelchair basketball at the Summer Paralympics navigational boxes": "صناديق تصفح كرة السلة على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Wheelchair fencing at the Summer Paralympics navigational boxes": "صناديق تصفح مبارزة سيف الشيش على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Wheelchair tennis at the Summer Paralympics navigational boxes": "صناديق تصفح كرة المضرب على الكراسي المتحركة في الألعاب البارالمبية الصيفية",
    "Athletics at the Universiade navigational boxes": "صناديق تصفح ألعاب القوى في الألعاب الجامعية",
    "Athletics at the Summer Universiade navigational boxes": "صناديق تصفح ألعاب القوى في الألعاب الجامعية الصيفية",
    "Nations at multi-sport events navigational boxes": "صناديق تصفح بلدان في الأحداث الرياضية المتعددة",
    "American Civil War by state navigational boxes": "صناديق تصفح الحرب الأهلية الأمريكية حسب الولاية",
    "Canadian football teams": "فرق كرة القدم الكندية",
    "Canadian football on television": "كرة القدم الكندية على التلفاز",
    "Attacks on diplomatic missions of Russia": "هجمات على بعثات دبلوماسية روسيا",
    "Italian defectors to the Soviet Union": "إيطاليون منشقون إلى الاتحاد السوفيتي",
    "Works by Antigua and Barbuda people": "أعمال أنتيغويون وبربوديون",
}

data1 = {
    "2026 animated television series debuts": "مسلسلات تلفزيونية رسوم متحركة بدأ عرضها في 2026",
    "2026 anime television series debuts": "مسلسلات أنمي متلفزة بدأ عرضها في 2026",
    "2026 English local elections": "الانتخابات المحلية الإنجليزية 2026",
    "2026 in New Zealand cricket": "الكريكت النيوزيلندية في 2026",
    "2026 United Kingdom local elections": "الانتخابات المحلية البريطانية 2026",
    "2026 United States local elections": "الانتخابات المحلية الأمريكية 2026",
    "Short-track speed skating at the 2026 Winter Olympics": "التزلج على مسار قصير في الألعاب الأولمبية الشتوية 2026",
    "Women government ministers of Nauru": "وزيرات ناورونيات",
    "lists of american non-fiction television series episodes": "قوائم حلقات مسلسلات تلفزيونية غير خيالية أمريكية",
    "lists of australian non-fiction television series episodes": "قوائم حلقات مسلسلات تلفزيونية غير خيالية أسترالية",
    "lists of british non-fiction television series episodes": "قوائم حلقات مسلسلات تلفزيونية غير خيالية بريطانية",
    "lists of canadian non-fiction television series episodes": "قوائم حلقات مسلسلات تلفزيونية غير خيالية كندية",
    "lists of non-fiction television series episodes": "قوائم حلقات مسلسلات تلفزيونية غير خيالية",
    "20th century synagogues in switzerland": "كنس في سويسرا في القرن 20",
    "20th century prime ministers of japan": "رؤساء وزراء اليابان في القرن 20",
    "2010–11 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2010–11",
    "2011–12 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2011–12",
    "2012–13 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2012–13",
    "2013–14 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2013–14",
    "2014–15 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2014–15",
    "2015–16 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2015–16",
    "2016–17 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2016–17",
    "2017–18 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2017–18",
    "2018–19 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2018–19",
    "2019–20 in Antigua and Barbuda football": "كرة القدم الأنتيغوية والبربودية في 2019–20",
}

data2 = {
    "Lists of Antigua and Barbuda people": "قوائم أنتيغويون وبربوديون",
    "Antigua and Barbuda football templates": "قوالب كرة القدم الأنتيغوية والبربودية",
    "10th century chinese people by occupation": "صينيون في القرن 10 حسب المهنة",
    "15th century swiss people by occupation": "سويسريون في القرن 15 حسب المهنة",
    "16th century iranian people by occupation": "إيرانيون في القرن 16 حسب المهنة",
    "20th century croatian people by occupation": "كروات في القرن 20 حسب المهنة",
    "21st century yemeni people by occupation": "يمنيون في القرن 21 حسب المهنة",
    "3rd century asian people by nationality": "آسيويون في القرن 3 حسب الجنسية",
    "20th century american people by occupation": "أمريكيون في القرن 20 حسب المهنة",
}

to_test = [
    ("test_2026_data_0", data_0),
    ("test_2026_data_1", data1),
    ("test_2026_data_2", data2),
]

test_data_all = data1 | data_0 | data2


@pytest.mark.parametrize("category, expected", test_data_all.items(), ids=test_data_all.keys())
@pytest.mark.fast
def test_2026_data_1(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
