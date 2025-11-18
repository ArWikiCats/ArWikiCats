"""
Tests
"""
import pytest

from src.make2_bots.sports_bots.sport_lab_suffixes import get_teams_new

get_teams_new_data = {
    "acrobatic gymnastics junior world championships": "بطولة العالم الجمباز الاكروباتيكي للناشئين",
    "acrobatic gymnastics world championships": "بطولة العالم الجمباز الاكروباتيكي",
    "beach volleyball world championships": "بطولة العالم لكرة الطائرة الشاطئية",
    "biathlon world cup": "كأس العالم للبياثلون",
    "college television series": "مسلسلات تلفزيونية كليات",
    "cross-country skiing world championships": "بطولة العالم للتزلج الريفي",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "domestic football leagues": "دوريات كرة قدم محلية",
    "domestic football": "كرة قدم محلية",
    "domestic handball leagues": "دوريات كرة يد محلية",
    "domestic women's football leagues": "دوريات كرة قدم محلية للسيدات",
    "domestic women's handball leagues": "دوريات كرة يد محلية للسيدات",
    "dressage championships": "بطولات ترويض خيول",
    "esports television series": "مسلسلات تلفزيونية رياضة إلكترونية",
    "esports world cup": "كأس العالم للرياضة إلكترونية",
    "football league": "دوري كرة القدم",
    "high school television series": "مسلسلات تلفزيونية مدارس ثانوية",
    "indoor hockey": "هوكي داخل الصالات",
    "men's hockey world cup": "كأس العالم للهوكي للرجال",
    "men's international basketball": "كرة سلة دولية للرجال",
    "men's international football": "كرة قدم دولية للرجال",
    "men's rugby world cup": "كأس العالم للرجبي للرجال",
    "motocross world championship": "بطولة العالم للموتو كروس",
    "national football team results": "نتائج منتخبات كرة قدم وطنية",
    "national tennis league": "دوريات كرة مضرب وطنية",
    "netball world cup": "كأس العالم لكرة الشبكة",
    "racquetball world championships": "بطولة العالم لكرة الراح",
    "rugby league world cup": "كأس العالم لدوري الرجبي",
    "sailing world championships": "بطولة العالم للإبحار",
    "summer olympics basketball": "كرة السلة في الألعاب الأولمبية الصيفية",
    "summer olympics field hockey": "هوكي الميدان في الألعاب الأولمبية الصيفية",
    "summer olympics football": "كرة القدم في الألعاب الأولمبية الصيفية",
    "summer olympics handball": "كرة اليد في الألعاب الأولمبية الصيفية",
    "summer olympics rugby sevens": "سباعيات الرجبي في الألعاب الأولمبية الصيفية",
    "summer olympics volleyball": "كرة الطائرة في الألعاب الأولمبية الصيفية",
    "summer olympics water polo": "كرة الماء في الألعاب الأولمبية الصيفية",
    "wheelchair basketball world championships": "بطولة العالم لكرة السلة على الكراسي المتحركة",
    "women's cricket world cup": "كأس العالم للكريكت للسيدات",
    "women's field hockey world cup": "كأس العالم لهوكي الميدان للسيدات",
    "women's hockey world cup": "كأس العالم للهوكي للسيدات",
    "women's international basketball": "كرة سلة دولية للسيدات",
    "women's international football": "كرة قدم دولية للسيدات",
    "women's softball world cup": "كأس العالم للكرة اللينة للسيدات",
    "women's world wheelchair basketball championship": "بطولة العالم لكرة السلة على الكراسي المتحركة للسيدات",
    "world amateur boxing championships": "بطولة العالم للبوكسينغ للهواة",
    "world archery championships": "بطولة العالم للنبالة",
    "world athletics championships": "بطولة العالم لألعاب القوى",
    "world boxing championships": "بطولة العالم للبوكسينغ",
    "world junior ice hockey championships": "بطولة العالم لهوكي الجليد للناشئين",
    "world junior short track speed skating championships": "بطولة العالم للتزلج على مسار قصير للناشئين",
    "world junior wrestling championships": "بطولة العالم للمصارعة للناشئين",
    "world netball championship": "بطولة العالم لكرة الشبكة",
    "world netball championships": "بطولة العالم لكرة الشبكة",
    "world outdoor bowls championship": "بطولة العالم للبولينج في الهواء الطلق",
    "world taekwondo championships": "بطولة العالم للتايكوندو",
    "world wrestling championships": "بطولة العالم للمصارعة",
    "wrestling world cup": "كأس العالم للمصارعة",
}


@pytest.mark.parametrize("category, expected", get_teams_new_data.items(), ids=list(get_teams_new_data.keys()))
@pytest.mark.fast
def _test_get_teams_new_data(category, expected) -> None:

    label = get_teams_new(category)
    assert isinstance(label, str)
    assert label.strip() == expected


def test_get_teams_new():
    # Test with a basic input
    result = get_teams_new("football team")
    assert result == "فريق كرة قدم"

    # Test with empty string
    result_empty = get_teams_new("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_teams_new("basketball team")
    assert isinstance(result_various, str)
