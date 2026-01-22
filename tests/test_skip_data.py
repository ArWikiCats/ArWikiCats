#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

executed_data_1 = {
    "People from the Spanish Netherlands executed for witchcraft": "أشخاص من هولندا الإسبانية أعدموا بتهمة السحر",
    "People executed in British North America by hanging": "أشخاص أعدموا في أمريكا الشمالية البريطانية بالشنق",
    "People executed in the Holy Roman Empire by burning": "أشخاص أعدموا في الإمبراطورية الرومانية المقدسة بالحرق",
    "People executed in the Holy Roman Empire by decapitation": "أشخاص أعدموا في الإمبراطورية الرومانية المقدسة بقطع الرأس",
    "French people executed by guillotine during the French Revolution": "فرنسيون أعدموا بالمقصلة خلال الثورة الفرنسية",
    "Members of the Communist Party of the Soviet Union executed by the Soviet Union": "أعضاء الحزب الشيوعي في الاتحاد السوفيتي أعدموا من قبل الاتحاد السوفيتي",
    "People executed by Kingdom of England by burning": "أشخاص أعدموا من قبل مملكة إنجلترا بالحرق",
    "People executed by the House of Lancaster": "أشخاص أعدموا من قبل الهاوس في لانكستر",
    "People executed by the House of York": "أشخاص أعدموا من قبل الهاوس في يورك",
    "People executed by the International Military Tribunal in Nuremberg": "أشخاص أعدموا من قبل المحكمة العسكرية الدولية في نورنبيرغ",
    "People executed by the Jin dynasty (266–420) by decapitation": "أشخاص أعدموا من قبل أسرة جين (266–420) بقطع الرأس",
    "People executed by the Kingdom of England by burning": "أشخاص أعدموا من قبل مملكة إنجلترا بالحرق",
    "People executed by the Kingdom of England by decapitation": "أشخاص أعدموا من قبل مملكة إنجلترا بقطع الرأس",
    "People executed by the Kingdom of England by firearm": "أشخاص أعدموا من قبل مملكة إنجلترا بسلاح ناري",
    "People executed by the Kingdom of England by hanging": "أشخاص أعدموا من قبل مملكة إنجلترا بالشنق",
    "People executed by the Kingdom of Ireland by hanging": "أشخاص أعدموا من قبل مملكة أيرلندا بالشنق",
    "People executed by the Kingdom of Scotland by burning": "أشخاص أعدموا من قبل مملكة إسكتلندا بالحرق",
    "People executed by the Kingdom of Scotland by decapitation": "أشخاص أعدموا من قبل مملكة إسكتلندا بقطع الرأس",
    "People executed by the Kingdom of Scotland by hanging": "أشخاص أعدموا من قبل مملكة إسكتلندا بالشنق",
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
    "People from Thuringia executed by Nazi Germany": "أشخاص من تورينغن أعدموا من قبل ألمانيا النازية",
}

fast_data_1 = {
    "Works about foreign relations of the United States": "أعمال عن علاقات خارجية الولايات المتحدة",
    "Books about foreign relations of the United States": "كتب عن علاقات خارجية الولايات المتحدة",
    "National youth sports teams of the United States": "منتخبات رياضية وطنية شبابية الولايات المتحدة",
    "Women's national sports teams of the United States": "منتخبات رياضية وطنية نسائية الولايات المتحدة",
    "Men's national sports teams of the United States": "منتخبات رياضية وطنية رجالية الولايات المتحدة",
    "Members of the Riksdag 2010–2010": "أعضاء البرلمان السويدي 2010–2010",
    "wheelchair basketball players in turkey": "لاعبو كرة سلة على كراسي متحركة في تركيا",
    "field hockey players in germany": "لاعبو هوكي ميدان في ألمانيا",
    "baseball players in florida": "لاعبو كرة قاعدة في فلوريدا",
    "baseball players in south korea": "لاعبو كرة قاعدة في كوريا الجنوبية",
    "basketball players in lebanon": "لاعبو كرة سلة في لبنان",
    "sport in khartoum": "الرياضة في الخرطوم",
    "sport in ottoman empire": "الرياضة في الدولة العثمانية",
    "sport in tuzla": "الرياضة في توزلا",
    "sport in veria": "الرياضة في فيريا",
    "sport in álava": "الرياضة في ألافا (مقاطعة)",
    "Women from Dutch Caribbean": "نساء من كاريبيون هولنديون",
    "Women from Kingdom of Prussia": "نساء من مملكة بروسيا",
    "Women from Kingdom of Travancore": "نساء من مملكة ترافنكور",
    "Women from Overseas France": "نساء من مقاطعات وأقاليم ما وراء البحار الفرنسية",
    "Defunct political parties of Islamic Republic of Iran": "أحزاب سياسية سابقة في الجمهورية الإسلامية الإيرانية",
    "People executed by hanging by country": "أشخاص أعدموا حرقاً حسب البلد",
    "Cultural depictions of sportspeople": "تصوير ثقافي عن رياضيون",
    "Scheduled sports events": "أحداث رياضية مقررة",
}

to_test = [
    ("test_sports_events_2", fast_data_1),
]


@pytest.mark.parametrize("category, expected", fast_data_1.items(), ids=fast_data_1.keys())
@pytest.mark.skip2
def test_fast_data_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


# test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
