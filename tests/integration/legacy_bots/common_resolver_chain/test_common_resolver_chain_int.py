"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.common_resolver_chain import get_type_lab
from utils.dump_runner import make_dump_test_name_data_callback

data_1 = {
    "medical and health organizations": "منظمات طبية وصحية",
    "electronic dance music albums": "ألبومات موسيقى الرقص الإلكترونية",
    "female field hockey players": "لاعبات هوكي ميدان",
    "history of austria hungary": "تاريخ الإمبراطورية النمساوية المجرية",
    "history of central african republic": "تاريخ جمهورية إفريقيا الوسطى",
    "history of north america": "تاريخ أمريكا الشمالية",
    "history of northern ireland": "تاريخ أيرلندا الشمالية",
    "port cities and towns": "مدن وبلدات ساحلية",
    "rivers of united states": "أنهار الولايات المتحدة",
    "taiwanese football club seasons": "مواسم أندية كرة قدم تايوانية",
    "united states senate candidates": "مرشحو مجلس الشيوخ الأمريكي",
    "weapons of mass destruction": "أسلحة دمار شامل",
    "welsh rugby union players": "لاعبو اتحاد رجبي ويلزيون",
    "religious buildings and structures": "مبان ومنشآت دينية",
    "united nations security council resolutions": "قرارات مجلس الأمن التابع للأمم المتحدة",
    "art museums and galleries": "متاحف فنية ومعارض",
    "television channels and stations": "قنوات وشبكات تلفزيونية",
    "australian rules football clubs": "أندية كرة قدم أسترالية",
    "military units and formations": "وحدات وتشكيلات عسكرية",
    "sports clubs and teams": "أندية وفرق رياضية",
    "african games bronze medalists": "فائزون بميداليات برونزية في الألعاب الإفريقية",
    "african games silver medalists": "فائزون بميداليات فضية في الألعاب الإفريقية",
    "central american and caribbean games medalists": "فائزون بميداليات ألعاب أمريكا الوسطى والكاريبي",
    "commonwealth games bronze medalists": "فائزون بميداليات برونزية في ألعاب الكومنولث",
    "islamic solidarity games silver medalists": "فائزون بميداليات فضية في ألعاب التضامن الإسلامي",
    "olympic field hockey players": "لاعبو هوكي ميدان أولمبيون",
    "olympic table tennis players": "لاعبو كرة طاولة أولمبيون",
    "pan american games medalists": "فائزون بميداليات دورة الألعاب الأمريكية",
    "democratic party united states senators": "أعضاء مجلس الشيوخ الأمريكي من الحزب الديمقراطي",
    "major league baseball players": "لاعبو دوري كرة القاعدة الرئيسي",
    "players of american football": "لاعبو كرة قدم أمريكية",
    "united states house-of-representatives": "مجلس النواب الأمريكي",
    "international field hockey competitions": "منافسات هوكي ميدان دولية",
    "international ice hockey competitions": "منافسات هوكي جليد دولية",
    "brazilian expatriate basketball people": "أعلام كرة سلة برازيليون مغتربون",
    "bulgarian expatriate basketball people": "أعلام كرة سلة بلغاريون مغتربون",
    "by university or college": "حسب الجامعة أو الكلية",
    "christian buildings and structures": "مبان ومنشآت مسيحية",
    "church of jesus christ of latter-day saints": "كنيسة يسوع المسيح لقديسي الأيام الأخيرة",
    "croatian expatriate basketball people": "أعلام كرة سلة كروات مغتربون",
    "defunct sports clubs and teams": "أندية وفرق رياضية سابقة",
    "demolished buildings and structures": "مبان ومنشآت مهدمة",
    "former buildings and structures": "مبان ومنشآت سابقة",
    "french expatriate rugby union players": "لاعبو اتحاد رجبي فرنسيون مغتربون",
    "golf clubs and courses": "نوادي الغولف والدورات",
    "lithuanian expatriate basketball people": "أعلام كرة سلة ليتوانيون مغتربون",
    "military and war museums": "متاحف عسكرية وحربية",
    "olympic silver medalists for the united states": "فائزون بميداليات فضية أولمبية من الولايات المتحدة",
    "parliament of united kingdom": "برلمان المملكة المتحدة",
    "private universities and colleges": "جامعات وكليات خاصة",
    "riots and civil disorder": "شغب وعصيان مدني",
    "roman catholic church buildings": "مبان كنائس رومانية كاثوليكية",
    "russian expatriate volleyball players": "لاعبو كرة طائرة روس مغتربون",
    "senegalese expatriate basketball people": "أعلام كرة سلة سنغاليون مغتربون",
    "south african expatriate sports-people": "رياضيون جنوب إفريقيون مغتربون",
    "south korean expatriate sports-people": "رياضيون كوريون جنوبيون مغتربون",
    "spanish expatriate handball players": "لاعبو كرة يد إسبان مغتربون",
    "swiss expatriate basketball people": "أعلام كرة سلة سويسريون مغتربون",
    "track and field athletes": "رياضيو المسار والميدان",
    "transport buildings and structures": "مبان ومنشآت نقل",
    "transportation buildings and structures": "مبان ومنشآت نقل",
    "tunisian expatriate basketball people": "أعلام كرة سلة تونسيون مغتربون",
    "united states air force": "القوات الجوية الأمريكية",
    "united states house-of-representatives elections": "انتخابات مجلس النواب الأمريكي",
    "university of": "جامعة",
    "forests and woodlands of": "غابات",
    "ports and harbours of": "مرافئ وموانئ",
    "agricultural buildings and structures": "مبان ومنشآت زراعية",
    "permanent representatives of bahrain": "مندوبو البحرين الدائمون",
    "permanent representatives of jamaica": "مندوبو جامايكا الدائمون",
    "permanent representatives of kazakhstan": "مندوبو كازاخستان الدائمون",
    "permanent representatives of kyrgyzstan": "مندوبو قيرغيزستان الدائمون",
    "trinidad and tobago emigrants": "ترنيداديون مهاجرون",
}


@pytest.mark.parametrize("category,output", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_get_type_lab_data(category: str, output: str) -> None:
    label = get_type_lab(category)
    assert label.strip() == output.strip()


to_test = [
    ("test_get_type_lab_data_1", data_1, get_type_lab),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
