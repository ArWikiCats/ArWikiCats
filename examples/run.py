
import sys
from pathlib import Path

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from ArWikiCats import resolve_arabic_category_label as po

print(po("Category:2015 American television"))
