"""
"Soviet Jews in military": "يهود سوفيت في عسكرية",
"Russian Jews in military": "يهود روس في عسكرية",
"""
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data_dumpskip

data_0 = {
    "Members of the Riksdag 2010–2010": "أعضاء البرلمان السويدي 2010–2010",
    "People executed in British North America by hanging": "أشخاص أعدموا في أمريكا الشمالية البريطانية بالشنق",
    "People executed in the Holy Roman Empire by burning": "أشخاص أعدموا في الإمبراطورية الرومانية المقدسة بالحرق",
    "People executed in the Holy Roman Empire by decapitation": "أشخاص أعدموا في الإمبراطورية الرومانية المقدسة بقطع الرأس",
    "Members of the Communist Party of the Soviet Union executed by the Soviet Union": "أعضاء الحزب الشيوعي في الاتحاد السوفيتي أعدموا من قبل الاتحاد السوفيتي",
    "People executed in the Philippines during World War II": "أشخاص أعدموا في الفلبين خلال الحرب العالمية الثانية",
    "People from Baden-Württemberg executed by Nazi Germany": "أشخاص من بادن-فورتمبيرغ أعدموا من قبل ألمانيا النازية",
    "People from Bavaria executed by Nazi Germany": "أشخاص من بافاريا أعدموا من قبل ألمانيا النازية",
    "People from Berlin executed by Nazi Germany": "أشخاص من برلين أعدموا من قبل ألمانيا النازية",
    "People from Brandenburg executed by Nazi Germany": "أشخاص من براندنبورغ أعدموا من قبل ألمانيا النازية",
    "People from Bremen (state) executed by Nazi Germany": "أشخاص من ولاية بريمن أعدموا من قبل ألمانيا النازية",
    "People from Georgia (country) executed by the Soviet Union": "أشخاص من جورجيا أعدموا من قبل الاتحاد السوفيتي",
    "People from Hamburg executed by Nazi Germany": "أشخاص من هامبورغ أعدموا من قبل ألمانيا النازية",
    "People from Hesse executed by Nazi Germany": "أشخاص من هسن أعدموا من قبل ألمانيا النازية",
    "People from Lower Saxony executed by Nazi Germany": "أشخاص من سكسونيا السفلى أعدموا من قبل ألمانيا النازية",
    "People from Mecklenburg-Vorpommern executed by Nazi Germany": "أشخاص من مكلنبورغ فوربومرن أعدموا من قبل ألمانيا النازية",
    "People from North Rhine-Westphalia executed by Nazi Germany": "أشخاص من شمال الراين-وستفاليا أعدموا من قبل ألمانيا النازية",
    "People from Rhineland-Palatinate executed by Nazi Germany": "أشخاص من راينلند بالاتينات أعدموا من قبل ألمانيا النازية",
    "People from Saxony executed by Nazi Germany": "أشخاص من ساكسونيا أعدموا من قبل ألمانيا النازية",
    "People from Saxony-Anhalt executed by Nazi Germany": "أشخاص من ساكسونيا أنهالت أعدموا من قبل ألمانيا النازية",
    "People from Schleswig-Holstein executed by Nazi Germany": "أشخاص من شليسفيغ هولشتاين أعدموا من قبل ألمانيا النازية",
    "People from Thuringia executed by Nazi Germany": "أشخاص من تورينغن أعدموا من قبل ألمانيا النازية"
}

fast_data_1 = {
    "russian empire-united states relations": "العلاقات بين الإمبراطورية الروسية والولايات المتحدة",
    "south korean presidential election 2017": "الانتخابات الرئاسية الكورية الجنوبية 2017",
    "republic of ireland women's national football team": "منتخب جمهورية أيرلندا لكرة القدم للسيدات",

}

to_test = [
    ("test_sports_events_0", data_0),
    ("test_sports_events_1", fast_data_1),
]


@pytest.mark.parametrize("category, expected", fast_data_1.items(), ids=fast_data_1.keys())
@pytest.mark.skip2
def test_fast_data_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data_dumpskip(to_test, resolve_label_ar, run_same=True)
