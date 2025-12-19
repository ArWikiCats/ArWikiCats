import re


def fixing(text: str) -> str:
    """Fix text."""
    text = re.sub(r"(انحلالات|تأسيسات)\s*سنة\s*(عقد|القرن|الألفية)", r"\g<1> \g<2>", text)
    text = text.replace("بعقد عقد", "بعقد")
    text = text.replace("بعقد القرن", "بالقرن")
    return text
