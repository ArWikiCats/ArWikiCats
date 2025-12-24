from typing import Any, Dict

footballers_get_endswith: Dict[str, Dict[str, Any]] = {
    " women's footballers": {
        "lab": "لاعبات {}",
        "remove": " women's footballers",
        "example": "Category:Spanish women's footballers",
    },
    " female footballers": {
        "lab": "لاعبات {}",
        "remove": " female footballers",
        "example": "Category:Brazilian female footballers",
    },
    "c. footballers": {
        "lab": "لاعبو {}",
        "remove": " footballers",
        "example": "Category:Heartland F.C. footballers",
    },
    " footballers": {
        "lab": "لاعبو {}",
        "remove": " footballers",
        "example": "Category:German footballers",
    },
}

to_get_endswith: Dict[str, Dict[str, Any]] = {
    "squad navigational boxes": {
        "lab": "صناديق تصفح تشكيلات {}",
        "example": "Category:1996 Basketball Olympic squad navigational boxes",
    },
    "sports navigational boxes": {
        "lab": "صناديق تصفح الرياضة في {}",
        "example": "Category:Yemen sports navigational boxes",
    },
    "navigational boxes": {
        "lab": "صناديق تصفح {}",
        "example": "",
    },
    "leagues seasons": {
        "lab": "مواسم دوريات {}",
        "example": "",
    },
    "alumni": {
        "lab": "خريجو {}",
        "example": "",
    },
    "board members": {
        "lab": "أعضاء مجلس {}",
        "example": "",
    },
    "faculty": {
        "lab": "أعضاء هيئة تدريس {}",
        "example": "",
    },
    "trustees": {
        "lab": "أمناء {}",
        "example": "",
    },
    "award winners": {
        "lab": "حائزو جوائز {}",
        "example": "",
    },
    "awards winners": {
        "lab": "حائزو جوائز {}",
        "example": "",
    },
    "sidebars": {
        "lab": "أشرطة جانبية {}",
        "example": "",
    },
    "charts": {
        "lab": "مخططات {}",
        "example": "",
    },
    "commissioners": {
        "lab": "مفوضو {}",
        "example": "Category:Major Indoor Soccer League (1978–1992) commissioners",
    },
    # "commentators": { "lab": "معلقو {}", "example": "Category:Major Indoor Soccer League (1978–1992) commentators", },
    "events": {
        "lab": "أحداث {}",
        "example": "",
    },
    "tournaments": {
        "lab": "بطولات {}",
        "example": "",
    },
}

to_get_startswith: Dict[str, Dict[str, Any]] = {
    "academic staff of": {
        "lab": "أعضاء هيئة تدريس {}",
        "example": "",
    },
    "association football matches navigational boxes by teams:": {
        "lab": "صناديق تصفح مباريات كرة قدم حسب الفرق:{}",
        "example": "Category:Association football matches navigational boxes by teams:Egypt",
    },
    "21st century members of ": {
        "lab": "أعضاء {} في القرن 21",
        "example": "Category:21st-century members of the Louisiana State Legislature",
    },
    "20th century members of ": {"lab": "أعضاء {} في القرن 20", "example": ""},
    "19th century members of ": {"lab": "أعضاء {} في القرن 19", "example": ""},
    "18th century members of ": {"lab": "أعضاء {} في القرن 18", "example": ""},
    "17th century members of ": {"lab": "أعضاء {} في القرن 17", "example": ""},
    "21st century women members of ": {"lab": "عضوات {} في القرن 21", "example": ""},
    "20th century women members of ": {"lab": "عضوات {} في القرن 20", "example": ""},
    "19th century women members of ": {"lab": "عضوات {} في القرن 19", "example": ""},
    "18th century women members of ": {"lab": "عضوات {} في القرن 18", "example": ""},
    "17th century women members of ": {"lab": "عضوات {} في القرن 17", "example": ""},
    "presidents of ": {"lab": "رؤساء {}", "example": ""},
    "family of ": {"lab": "عائلة {}", "example": ""},
    "lists of ": {"lab": "قوائم {}", "example": ""},
    "children of ": {"lab": "أبناء {}", "example": ""},
    "discoveries by ": {"lab": "اكتشافات بواسطة {}", "example": ""},
    "__films about ": {"lab": "أفلام عن {}", "example": ""},
}
