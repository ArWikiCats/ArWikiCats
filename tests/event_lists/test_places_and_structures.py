#
from src import new_func_lab

data ={
    "Category:Airlines established in 1968": "تصنيف:شركات طيران أنشئت في 1968",
    "Category:Airlines of Afghanistan": "تصنيف:شركات طيران أفغانستان",
    "Category:Bridges in Wales by type": "تصنيف:جسور في ويلز حسب الفئة",
    "Category:British Rail": "تصنيف:السكك الحديدية البريطانية",
    "Category:Cargo airlines of the Philippines": "تصنيف:شركات الشحن الجوي في الفلبين",
    "Category:History of British Rail": "تصنيف:تاريخ السكك الحديدية البريطانية",
    "Category:Vehicle manufacturing companies disestablished in 1904": "تصنيف:شركات تصنيع مركبات انحلت في 1904",
    "Category:design companies disestablished in 1905": "تصنيف:شركات تصميم انحلت في 1905",
    "Category:landmarks in Yemen": "تصنيف:معالم في اليمن",
    "Category:parks in the Roman Empire": "تصنيف:متنزهات في الإمبراطورية الرومانية"
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
