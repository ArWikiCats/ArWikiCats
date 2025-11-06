#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff


def test_places_and_structures():

    data = {
        "Category:Bridges in Wales by type": "تصنيف:جسور في ويلز حسب الفئة",
        "Category:British Rail": "تصنيف:السكك الحديدية البريطانية",
        "Category:History of British Rail": "تصنيف:تاريخ السكك الحديدية البريطانية",
        "Category:design companies disestablished in 1905": "تصنيف:شركات تصميم انحلت في 1905",
        "Category:landmarks in Yemen": "تصنيف:معالم في اليمن",
        "Category:parks in the Roman Empire": "تصنيف:متنزهات في الإمبراطورية الرومانية"
    }

    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_places_and_structures")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_places_and_structures_2():

    data = {
        "Category:Airlines established in 1968": "تصنيف:شركات طيران أسست في 1968",
        "Category:Airlines of Afghanistan": "تصنيف:شركات طيران في أفغانستان",
        "Category:Cargo airlines of the Philippines": "تصنيف:شحن جوي في الفلبين",
        "Category:Vehicle manufacturing companies disestablished in 1904": "تصنيف:شركات تصنيع المركبات انحلت في 1904",

    }

    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_places_and_structures")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
