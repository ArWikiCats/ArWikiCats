""" """

import re


def get_color_table() -> dict[str, str]:
    """Build a mapping of color names to ANSI templates."""
    # new Define the color codes for different colors
    color_numbers = {
        # 'lightred': 101,
        # 'lightgreen': 102,
        # 'lightpurple': 105,
        # 'lightyellow': 103,
        # 'lightblue': 104,
        # 'lightcyan': 106,
        # 'aqua': 106,
        # 'lightaqua': 107,
        # 'lightwhite': 107,
        # 'lightgray': 107,
        "red": 91,
        "green": 92,
        "yellow": 93,
        "blue": 94,
        "purple": 95,
        "cyan": 96,
        "white": 97,
        "black": 98,
        "grey": 99,
        "gray": 100,
        "underline": 4,
        "invert": 7,
        "blink": 5,
        "lightblack": 108,
        "bold": 1,
    }
    color_table = {x: f"\033[{v}m%s\033[00m" for x, v in color_numbers.items()}

    # Add light versions of the colors to the color table
    for color in ["purple", "yellow", "blue", "red", "green", "cyan", "gray"]:
        color_table[f"light{color}"] = color_table.get(color, 0)

    # Add some additional color names to the color table
    color_table["aqua"] = color_table.get("cyan", 0)
    color_table["lightaqua"] = color_table.get("cyan", 0)
    color_table["lightgrey"] = color_table.get("gray", 0)
    color_table["grey"] = color_table.get("gray", 0)
    color_table["lightwhite"] = color_table.get("gray", 0)
    color_table["light"] = 0

    return color_table


color_table = get_color_table()


def make_str(textm: str) -> str:
    """
    Prints the given text with color formatting.

    The text can contain color tags like '<<color>>' where 'color' is the name of the color.
    The color will be applied to the text that follows the tag, until the end of the string or until a '<<default>>' tag is found.

    :param textm: The text to print. Can contain color tags.
    """
    # Define a pattern for color tags
    _color_pat = r"((:?\w+|previous);?(:?\w+|previous)?)"
    # Compile a regex for color tags
    colorTagR = re.compile(rf"(?:\03{{|<<){_color_pat}(?:}}|>>)")

    # Initialize a stack for color tags
    color_stack = ["default"]

    # If the input is not a string, print it as is and return
    if not isinstance(textm, str):
        return textm

    # If the text does not contain any color tags, print it as is and return
    if "\03" not in textm and "<<" not in textm:
        return textm

    # Split the text into parts based on the color tags
    text_parts = colorTagR.split(textm) + ["default"]

    # Enumerate the parts for processing
    enu = enumerate(zip(text_parts[::4], text_parts[1::4]))

    # Initialize the string to be printed
    toprint = ""

    # Process each part of the text
    for _, (text, next_color) in enu:
        # Get the current color from the color stack
        # print(f"i: {index}, {text=}, {next_color=}")
        current_color = color_stack[-1]

        # If the next color is 'previous', pop the color stack to get the previous color
        if next_color == "previous":
            if len(color_stack) > 1:  # keep the last element in the stack
                color_stack.pop()
            next_color = color_stack[-1]
        else:
            # If the next color is not 'previous', add it to the color stack
            color_stack.append(next_color)

        # Get the color code for the current color
        cc = color_table.get(current_color, "")

        # If the color code is not empty, apply it to the text
        if cc:
            text = cc % text

        # Add the colored text to the string to be printed
        toprint += text

    # Print the final colored text
    return toprint


__all__ = [
    "make_str",
]
