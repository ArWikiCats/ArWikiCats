import re
from ..helps.print_bot import output_test
from ..make2_bots.reg_lines import YEARS_REGEX


def move_3(text_str: str) -> str:
    """
    A function that takes in a string and searches for a specific pattern within it. The function replaces underscores in the string with spaces and then uses a regular expression to search for a pattern of the form '{first_part} حسب {by_part} في {date}'.

    Parameters:
    - text_str (str): The input string.

    Returns:
    - str: The modified string if a match is found, otherwise the original string.
    """

    # ---
    # تصنيف:اتحاد الرجبي حسب البلد في 1989
    text_str = text_str.replace("_", " ")
    # ---
    new_text = text_str
    # ---
    if result := re.search(rf"^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>{YEARS_REGEX})$", text_str):
        # [[تصنيف:اتحاد الرجبي في 1989 حسب البلد]]
        # ---
        first_part = result.group("first_part")
        by_part = result.group("by_part")
        date = result.group("date")
        # ---
        new_text = f"{first_part} في {date} حسب {by_part}"
        # ---
        output_test(f"move_by_in: new_text: {new_text}")
    else:
        output_test("move_by_in: no match")
    # ---
    if new_text != text_str:
        new_text = re.sub(r"\s+", " ", new_text)
        new_text = re.sub(r"\bق\.م\b", "ق م", new_text)
        new_text = new_text.replace(" في في ", " في ")
    # ---
    return new_text


def move_by_in(text_str: str) -> str:
    """
    A function that takes in a string and searches for a specific pattern within it. The function replaces underscores in the string with spaces and then uses a regular expression to search for a pattern of the form '{first_part} حسب {by_part} في {date}'.

    Parameters:
    - text_str (str): The input string.

    Returns:
    - str: The modified string if a match is found, otherwise the original string.
    """

    # ---
    # تصنيف:اتحاد الرجبي حسب البلد في 1989
    text_str = text_str.replace("_", " ")
    # ---
    new_text = text_str
    # ---
    if result := re.search(rf"^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>{YEARS_REGEX})$", text_str):
        # [[تصنيف:اتحاد الرجبي في 1989 حسب البلد]]
        # ---
        first_part = result.group("first_part")
        by_part = result.group("by_part")
        date = result.group("date")
        # ---
        new_text = f"{first_part} في {date} حسب {by_part}"
        # ---
        output_test(f"move_by_in: new_text: {new_text}")
    else:
        output_test("move_by_in: no match")
    # ---
    if new_text != text_str:
        new_text = re.sub(r"\s+", " ", new_text)
        new_text = re.sub(r"\bق\.م\b", "ق م", new_text)
        new_text = new_text.replace(" في في ", " في ")
    # ---
    return new_text


def move_years_first(text_str: str) -> str:
    """
    Generates a function comment for the given function body in a markdown code block with the correct language syntax.

    Args:
        text_str (str): The string to be processed.

    Returns:
        str: The processed string.
    """
    # ---
    new = text_str
    # ---
    pattern = rf"^(?P<first_part>{YEARS_REGEX})\sفي\s(?P<second_part>[^0-9]*)$"
    if match := re.match(pattern, text_str):
        # ---
        first_part = match.group("first_part").strip()
        second_part = match.group("second_part").strip()
        # ---
        output_test(f"{first_part=}")
        output_test(f"{second_part=}")
        # ---
        skip_it = [
            "أفلام",
            "الأفلام",
        ]
        # ---
        if second_part in skip_it:
            return text_str
        # ---- "^.*?_في_.*?_في_.*?$"
        if " في x" in second_part:
            output_test('second_part.find(" في ") != -1:')
            return text_str
        # ---
        # إعادة ترتيب الجملة
        new = f"{second_part} في {first_part}"
        # ---
        if result := re.search(r"^(.*)\sحسب\s([\s\w]+)$", second_part):
            output_test("<<yellow>> find حسب in result:")
            new = f"{result.group(1)} في {first_part}" + f" حسب {result.group(2)}"
    else:
        output_test("move_years no match")
    # ---
    if new != text_str:
        new = re.sub(r"\s+", " ", new)
        new = re.sub(r"\bق\.م\b", "ق م", new)
        new = new.replace(" في في ", " في ")
    # ---
    return new


def move_years(text_str: str) -> str:
    # ---
    text_str = text_str.replace("_", " ").strip()
    # ---
    cat_ns = False
    # ---
    if text_str.startswith("تصنيف:"):
        cat_ns = True
        text_str = text_str.replace("تصنيف:", "")
    # ---
    new_text = move_years_first(text_str)
    # ---
    if new_text == text_str:
        new_text = move_by_in(text_str)
    # ---
    if cat_ns:
        new_text = f"تصنيف:{new_text}"
    # ---
    return new_text
