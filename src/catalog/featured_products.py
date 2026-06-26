"""10 продуктів для головної сторінки (структура з DOCX клієнта)."""

from pathlib import Path

from src.catalog.category_content import CATEGORY_DESCRIPTIONS

_BASE = Path(__file__).resolve().parents[2]
IMAGES = _BASE / "TZ" / "images_extracted" / "all"

_ANILOX_FULL = CATEGORY_DESCRIPTIONS["Анілоксові вали та формні гільзи"]
_ANILOX_SPLIT = _ANILOX_FULL.split("Формна гільза (sleeve) для флексодруку", 1)
ANILOX_CERAMIC_DESC = _ANILOX_SPLIT[0].strip()
ANILOX_SLEEVE_DESC = (
    "Формна гільза (sleeve) для флексодруку\n\n"
    + _ANILOX_SPLIT[1].strip()
    if len(_ANILOX_SPLIT) > 1
    else ""
)

_EQUIP = CATEGORY_DESCRIPTIONS["Обладнання та комплектуючі"]

FEATURED_ARTICLES = (
    "VT-CAT",
    "AX-CER",
    "SL-0095",
    "EQ-BRS",
    "EQ-RKL",
    "EQ-LOAD",
    "EQ-USW",
    "EQ-SLW",
    "EQ-BAG",
    "EQ-FLEX",
)

FEATURED_PRODUCTS = [
    {
        "category": "Вали тиснення",
        "name": "Вали тиснення (каландри)",
        "article": "VT-CAT",
        "cover": IMAGES / "раздел_вали_тиснення_p1_img3_569x440.png",
        "short_desc": (
            "Металеві та гумові каландри для тиснення текстури, візерунків "
            "та логотипів на папері, плівці, шкірі, металі та текстилі."
        ),
        "full_desc": CATEGORY_DESCRIPTIONS["Вали тиснення"],
        "use_category_gallery": True,
        "order": 1,
    },
    {
        "category": "Анілоксові вали та формні гільзи",
        "name": "Анілоксові керамічні вали",
        "article": "AX-CER",
        "cover": IMAGES / "раздел_анилоксовые_и_формные_валы_p1_img2_784x591.png",
        "short_desc": (
            "Хромовані та керамічні анілоксові вали для точного перенесення "
            "фарби у флексодруку. Підбір за лініатурою та об'ємом осередків."
        ),
        "full_desc": ANILOX_CERAMIC_DESC,
        "order": 2,
    },
    {
        "category": "Анілоксові вали та формні гільзи",
        "name": "Формна гільза (sleeve) для флексодруку",
        "article": "SL-0095",
        "cover": IMAGES / "раздел_анилоксовые_и_формные_валы_p1_img3_291x203.png",
        "short_desc": (
            "Флексогільзи твердістю 95 Sh.A для наклейки флексоформ. "
            "Товщина стінки 3–100 мм, низьке осьове биття."
        ),
        "full_desc": ANILOX_SLEEVE_DESC,
        "order": 3,
    },
    {
        "category": "Обладнання та комплектуючі",
        "name": "Щітки для чищення валиків Anilox",
        "article": "EQ-BRS",
        "cover": IMAGES / "раздел_обладнання_та_комплектуючи_p1_img3_271x174.png",
        "short_desc": "Сталевий дріт високої якості — ефективне очищення без пошкодження керамічного шару.",
        "full_desc": _EQUIP.split("2. Ракельні ножі")[0].replace("1. ", "").strip(),
        "order": 4,
    },
    {
        "category": "Обладнання та комплектуючі",
        "name": "Ракельні ножі",
        "article": "EQ-RKL",
        "cover": IMAGES / "раздел_обладнання_та_комплектуючи_p1_img4_822x566.png",
        "short_desc": "Ракель 0,15–0,20 мм з ламелевою кромкою для чистого зняття фарби у флексодруку.",
        "full_desc": _EQUIP.split("3. Електронні навантажувачі")[0].split("2. Ракельні ножі", 1)[1].strip(),
        "order": 5,
    },
    {
        "category": "Обладнання та комплектуючі",
        "name": "Електронні навантажувачі",
        "article": "EQ-LOAD",
        "cover": IMAGES / "раздел_обладнання_та_комплектуючи_p1_img6_881x505.png",
        "short_desc": "Підйом котушок 1000 і 1500 кг. Гальмо стоянки, захист оператора, акумуляторне живлення.",
        "full_desc": _EQUIP.split("4. Машина для ультразвукового")[0].split("3. Електронні навантажувачі", 1)[1].strip(),
        "order": 6,
    },
    {
        "category": "Обладнання та комплектуючі",
        "name": "Машина для ультразвукового миття анілоксових гільз",
        "article": "EQ-USW",
        "cover": IMAGES / "раздел_обладнання_та_комплектуючи_p1_img4_822x566.png",
        "short_desc": "Ультразвукова мийка для видалення засохлої фарби з комірок керамічних валів.",
        "full_desc": _EQUIP.split("5. Машина для склеювання")[0].split("4. Машина для ультразвукового", 1)[1].strip(),
        "order": 7,
    },
    {
        "category": "Обладнання та комплектуючі",
        "name": "Машина для склеювання та намотування рукава",
        "article": "EQ-SLW",
        "cover": IMAGES / "раздел_обладнання_та_комплектуючи_p1_img7_1705x1279.jpeg",
        "short_desc": "Формування термоусадочних етикеток. Обробка ПВХ, ПЕТГ, ОПС, ХІТ та інших плівок.",
        "full_desc": _EQUIP.split("6. Пакеторобна машина")[0].split("5. Машина для склеювання", 1)[1].strip(),
        "order": 8,
    },
    {
        "category": "Обладнання та комплектуючі",
        "name": "Пакеторобна машина",
        "article": "EQ-BAG",
        "cover": IMAGES / "раздел_обладнання_та_комплектуючи_p1_img7_1705x1279.jpeg",
        "short_desc": "Автоматичне виготовлення пакетів «майка», фасувальних, Doy-pack та інших типів упаковки.",
        "full_desc": _EQUIP.split("7. Машина для флексодруку")[0].split("6. Пакеторобна машина", 1)[1].strip(),
        "order": 9,
    },
    {
        "category": "Обладнання та комплектуючі",
        "name": "Машина для флексодруку",
        "article": "EQ-FLEX",
        "cover": IMAGES / "раздел_обладнання_та_комплектуючи_p1_img5_1004x753.png",
        "short_desc": "Ярусні, планетарні та лінійні флексографічні машини під ваші потреби та конфігурації.",
        "full_desc": _EQUIP.split("7. Машина для флексодруку", 1)[1].strip(),
        "order": 10,
    },
]
