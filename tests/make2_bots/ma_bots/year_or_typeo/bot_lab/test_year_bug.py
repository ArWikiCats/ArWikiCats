import pytest
from load_one_data import dump_diff, ye_test_one_dataset

from src.make2_bots.ma_bots.year_or_typeo.bot_lab import (
    label_for_startwith_year_or_typeo,
)

examples = {
    "2000s American films": "أفلام أمريكية في عقد 2000",
    "2017 American television series debuts": "مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "2017 American television series endings": "مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "Paralympic competitors for Cape Verde": "منافسون في الألعاب البارالمبية من الرأس الأخضر",
    "1980 sports events in Europe": "أحداث 1980 الرياضية في أوروبا",
    "April 1983 sports events": "أحداث أبريل 1983 الرياضية",
    "April 1983 events in Europe": "أحداث أبريل 1983 في أوروبا",
    "July 2018 events by continent": "أحداث يوليو 2018 حسب القارة",
    "2000s films": "أفلام إنتاج عقد 2000",
    "00s establishments in the Roman Empire": "تأسيسات عقد 00 في الإمبراطورية الرومانية",
    "1000s disestablishments in Asia": "انحلالات عقد 1000 في آسيا",
    "1370s conflicts": "نزاعات عقد 1370",
    "1950s criminal comedy films": "أفلام كوميديا الجريمة عقد 1950",
    "1960s black comedy films": "أفلام كوميدية سوداء عقد 1960",
    "1960s criminal comedy films": "أفلام كوميديا الجريمة عقد 1960",
    "1970s black comedy films": "أفلام كوميدية سوداء عقد 1970",
    "1970s criminal comedy films": "أفلام كوميديا الجريمة عقد 1970",
    "1980s black comedy films": "أفلام كوميدية سوداء عقد 1980",
    "1980s criminal comedy films": "أفلام كوميديا الجريمة عقد 1980",
    "1990s BC disestablishments in Asia": "انحلالات عقد 1990 ق م في آسيا",
    "1990s disestablishments in Europe": "انحلالات عقد 1990 في أوروبا",
}


def test_label_for_startwith_year_or_typeo():
    expected, diff_result = ye_test_one_dataset(examples, label_for_startwith_year_or_typeo)

    dump_diff(diff_result, "test_label_for_startwith_year_or_typeo")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
