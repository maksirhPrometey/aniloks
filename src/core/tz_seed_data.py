"""Дані з ТЗ для наповнення сайту."""

from pathlib import Path

from src.catalog.category_content import CATEGORY_DESCRIPTIONS, CATEGORY_GALLERY
from src.catalog.featured_products import FEATURED_PRODUCTS

from src.core.seed_assets import (
    ANILOX_CERAMIC_IMG,
    EQ_BAG_MACHINE_IMG,
    EQ_BRUSHES_IMG,
    EQ_DOCTOR_BLADE_IMG,
    EQ_FLEXO_STACK_IMG,
    EQ_LOADER_IMG,
    EQ_SLEEVE_WINDER_IMG,
    EQ_ULTRASONIC_WASH_IMG,
    FORM_SLEEVE_IMG,
    VALY_CALENDER_02_IMG,
    VALY_COVER_IMG,
    VALY_FABRIC_RESULT_IMG,
    VALY_STEEL_STEEL_IMG,
    VALY_TEXTURE_GEO_IMG,
    VALY_TEXTURE_GRID_IMG,
)

BASE = Path(__file__).resolve().parents[2]
TZ = BASE / "TZ"

SITE_SETTINGS = {
    "site_name": "Обладнання для Друку",
    "slogan": "Ваш успіх – наш пріоритет",
    "hero_eyebrow": "Ваш успіх – наш пріоритет",
    "hero_title": "Обладнання та комплектуючі для поліграфії й пакування",
    "hero_subtitle": (
        "Постачаємо вали тиснення, анілоксові керамічні вали, формні гільзи та "
        "промислове обладнання для друкарень флексо-, офсетного й глибокого "
        "друку — напряму від виробника з Китаю."
    ),
    "about_text": (
        "Займаємося постачанням різноманітного обладнання, комплектуючих та "
        "запасних частин, витратних матеріалів для ринку друку України — "
        "напряму від виробника з Китаю."
    ),
    "clients_text": (
        "Наші клієнти: друкарні флексодруку, офсетного та глибокого друку, а також "
        "виробники пакувальної, полімерної, паперової та текстильної промисловості."
    ),
    "phone": "+38 (066) 988-32-42",
    "email": "nikolajcornejko@gmail.com",
    "working_hours": "Пн–Пт, 09:00–18:00",
    "hero_image": EQ_FLEXO_STACK_IMG,
}

CATEGORIES = [
    {
        "name": "Вали тиснення",
        "order": 1,
        "cover": VALY_COVER_IMG,
        "description": CATEGORY_DESCRIPTIONS["Вали тиснення"],
        "doc_pdf": TZ / "раздел вали тиснення.pdf",
        "doc_title": "Каталог: Вали тиснення (каландри)",
    },
    {
        "name": "Анілоксові вали та формні гільзи",
        "order": 2,
        "cover": ANILOX_CERAMIC_IMG,
        "description": CATEGORY_DESCRIPTIONS["Анілоксові вали та формні гільзи"],
        "doc_pdf": TZ / "раздел_анилоксовые_и_формные_валы.pdf",
        "doc_title": "Каталог: Анілоксові вали та формні гільзи",
    },
    {
        "name": "Обладнання та комплектуючі",
        "order": 3,
        "cover": EQ_FLEXO_STACK_IMG,
        "description": CATEGORY_DESCRIPTIONS["Обладнання та комплектуючі"],
        "doc_pdf": TZ / "раздел_обладнання_та_комплектуючи.pdf",
        "doc_title": "Каталог: Обладнання та комплектуючі",
    },
]

PRODUCTS = FEATURED_PRODUCTS

GALLERY_PHOTOS = [
    (ANILOX_CERAMIC_IMG, "Анілоксові вали та формні гільзи"),
    (VALY_COVER_IMG, "Вал тиснення з текстурою"),
    (EQ_FLEXO_STACK_IMG, "Флексографічне обладнання"),
    (VALY_STEEL_STEEL_IMG, "Вал тиснення на валу"),
    (VALY_TEXTURE_GEO_IMG, "Текстура тиснення — геометричний візерунок"),
    (VALY_TEXTURE_GRID_IMG, "Текстура тиснення — сітка"),
    (VALY_CALENDER_02_IMG, "Вал тиснення — додатковий вигляд"),
    (VALY_FABRIC_RESULT_IMG, "Результат тиснення на тканині"),
    (ANILOX_CERAMIC_IMG, "Анілоксові та формні вали"),
    (FORM_SLEEVE_IMG, "Формні гільзи (sleeves)"),
    (EQ_FLEXO_STACK_IMG, "Флексографічна машина"),
    (EQ_BRUSHES_IMG, "Щітки для чищення анілоксів"),
    (EQ_DOCTOR_BLADE_IMG, "Ракельний ніж"),
    (EQ_LOADER_IMG, "Електронний навантажувач"),
    (EQ_ULTRASONIC_WASH_IMG, "Ультразвукова мийка анілоксових гільз"),
    (EQ_SLEEVE_WINDER_IMG, "Машина для склеювання та намотування рукава"),
    (EQ_BAG_MACHINE_IMG, "Пакеторобне обладнання"),
]

PRICE_ITEMS = [
    (
        "Вали тиснення",
        "",
        "Вали тиснення (каландри)",
        "Сталь по сталі, сталь по гумі, сталь по паперу — параметри за запитом",
        1,
    ),
    (
        "Анілоксові вали та формні гільзи",
        "",
        "Анілоксові вали та формні гільзи",
        "Хромовані та керамічні вали, sleeves 95 Sh.A — підбір за ТЗ",
        2,
    ),
    (
        "Обладнання та комплектуючі",
        "",
        "Обладнання та комплектуючі",
        "Щітки, ракельні ножі, навантажувачі, мийки, пакеторобні та флексо-машини",
        3,
    ),
]

GENERAL_DOC = {
    "title": "Презентація компанії та асортименту",
    "pdf": TZ / "первая страничка.pdf",
}
