

from typing import Dict, Any

footballers_get_endswith: Dict[str, Dict[str, Any]] = {
    " women's footballers": {
        "lab": "لاعبات {}",
        "Find_wd": True,
        "Find_ko": True,
        "remove": " women's footballers",
        "example": "Category:Spanish women's footballers",
    },
    " female footballers": {
        "lab": "لاعبات {}",
        "Find_wd": True,
        "Find_ko": True,
        "remove": " female footballers",
        "example": "Category:Brazilian female footballers",
    },
    "c. footballers": {
        "lab": "لاعبو {}",
        "Find_wd": True,
        "Find_ko": False,
        "remove": " footballers",
        "example": "Category:Heartland F.C. footballers",
    },
    " footballers": {
        "lab": "لاعبو {}",
        "Find_wd": True,
        "Find_ko": True,
        "remove": " footballers",
        "example": "Category:German footballers",
    },
}

to_get_endswith: Dict[str, Dict[str, Any]] = {
    "squad navigational boxes": {
        "lab": "صناديق تصفح تشكيلات {}",
        "Find_wd": False,
        "example": "Category:1996 Basketball Olympic squad navigational boxes",
    },
    "sports navigational boxes": {
        "lab": "صناديق تصفح الرياضة في {}",
        "Find_wd": False,
        "example": "Category:Yemen sports navigational boxes",
    },
    "navigational boxes": {
        "lab": "صناديق تصفح {}",
        "Find_wd": False,
        "example": "",
    },
    "leagues seasons": {
        "lab": "مواسم دوريات {}",
        "Find_wd": True,
        "example": "",
    },
    "alumni": {
        "lab": "خريجو {}",
        "Find_wd": True,
        "example": "",
    },
    "board members": {
        "lab": "أعضاء مجلس {}",
        "Find_wd": True,
        "example": "",
    },
    "faculty": {
        "lab": "أعضاء هيئة تدريس {}",
        "Find_wd": True,
        "example": "",
    },
    "trustees": {
        "lab": "أمناء {}",
        "Find_wd": True,
        "example": "",
    },
    "award winners": {
        "lab": "حائزو جوائز {}",
        "Find_wd": False,
        "example": "",
    },
    "awards winners": {
        "lab": "حائزو جوائز {}",
        "Find_wd": False,
        "example": "",
    },
    "sidebars": {
        "lab": "أشرطة جانبية {}",
        "Find_wd": False,
        "example": "",
    },
    "charts": {
        "lab": "مخططات {}",
        "Find_wd": False,
        "example": "",
    },
    "commissioners": {
        "lab": "مفوضو {}",
        "Find_wd": False,
        "example": "Category:Major Indoor Soccer League (1978–1992) commissioners",
    },
    "commentators": {
        "lab": "معلقو {}",
        "Find_wd": False,
        "example": "Category:Major Indoor Soccer League (1978–1992) commentators",
    },
    "events": {
        "lab": "أحداث {}",
        "Find_wd": False,
        "example": "",
    },
    "tournaments": {
        "lab": "بطولات {}",
        "Find_wd": False,
        "example": "",
    },
}

to_get_startswith: Dict[str, Dict[str, Any]] = {
    "association football matches navigational boxes by teams:": {
        "lab": "صناديق تصفح مباريات كرة قدم حسب الفرق:{}",
        "Find_wd": False,
        "example": "Category:Association football matches navigational boxes by teams:Egypt",
    },
    "21st century members of ": {
        "lab": "أعضاء {} في القرن 21",
        "Find_wd": False,
        "example": "Category:21st-century members of the Louisiana State Legislature",
    },
    "20th century members of ": {
        "lab": "أعضاء {} في القرن 20",
        "Find_wd": False,
        "example": ""
    },
    "19th century members of ": {
        "lab": "أعضاء {} في القرن 19",
        "Find_wd": False,
        "example": ""
    },
    "18th century members of ": {
        "lab": "أعضاء {} في القرن 18",
        "Find_wd": False,
        "example": ""
    },
    "17th century members of ": {
        "lab": "أعضاء {} في القرن 17",
        "Find_wd": False,
        "example": ""
    },
    "21st century women members of ": {
        "lab": "عضوات {} في القرن 21",
        "Find_wd": False,
        "example": ""
    },
    "20th century women members of ": {
        "lab": "عضوات {} في القرن 20",
        "Find_wd": False,
        "example": ""
    },
    "19th century women members of ": {
        "lab": "عضوات {} في القرن 19",
        "Find_wd": False,
        "example": ""
    },
    "18th century women members of ": {
        "lab": "عضوات {} في القرن 18",
        "Find_wd": False,
        "example": ""
    },
    "17th century women members of ": {
        "lab": "عضوات {} في القرن 17",
        "Find_wd": False,
        "example": ""
    },
    "presidents of ": {
        "lab": "رؤساء {}",
        "Find_wd": False,
        "example": ""
    },
    "family of ": {
        "lab": "عائلة {}",
        "Find_wd": False,
        "example": ""
    },
    "lists of ": {
        "lab": "قوائم {}",
        "Find_wd": False,
        "example": ""
    },
    "children of ": {
        "lab": "أطفال {}",
        "Find_wd": False,
        "example": ""
    },
    "discoveries by ": {
        "lab": "اكتشافات بواسطة {}",
        "Find_wd": True,
        "example": ""
    },
    "__films about ": {
        "lab": "أفلام عن {}",
        "Find_wd": False,
        "example": ""
    },
}
