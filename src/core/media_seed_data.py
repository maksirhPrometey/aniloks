"""Мапінг WebP-асетів для seed_media (hero, категорії, продукти, галерея)."""

from pathlib import Path

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
WEBP_DIR = BASE / "data" / "seed_media" / "webp"
TZ_IMAGES = BASE / "TZ" / "images_extracted" / "all"

HERO_IMAGE = "hero.webp"

CATEGORY_COVERS = {
    "Вали тиснення": "category-valy-tisnennia.webp",
    "Анілоксові вали та формні гільзи": "category-aniloks.webp",
    "Обладнання та комплектуючі": "category-obladnannia.webp",
}

CATEGORY_GALLERY = {
    "Вали тиснення": [
        "cat-valy-01.webp",
        "cat-valy-02.webp",
        "cat-valy-03.webp",
        "cat-valy-04.webp",
        "cat-valy-05.webp",
        "cat-valy-06.webp",
    ],
    "Анілоксові вали та формні гільзи": [
        "cat-anilox-01.webp",
        "cat-anilox-02.webp",
    ],
    "Обладнання та комплектуючі": [
        "cat-eq-01.webp",
        "cat-eq-02.webp",
        "cat-eq-03.webp",
        "cat-eq-04.webp",
        "cat-eq-05.webp",
        "cat-eq-06.webp",
        "cat-eq-07.webp",
    ],
}

PRODUCT_COVERS = {
    "VT-CAT": "product-vt-category.webp",
    "AX-CER": "product-aniloks-ceramic.webp",
    "SL-0095": "product-sleeve-95.webp",
    "EQ-BRS": "product-brushes.webp",
    "EQ-RKL": "product-doctor-blade.webp",
    "EQ-LOAD": "product-loader-1000.webp",
    "EQ-USW": "product-ultrasonic-wash.webp",
    "EQ-SLW": "product-sleeve-winder.webp",
    "EQ-BAG": "product-bag-machine.webp",
    "EQ-FLEX": "product-flexo-stack.webp",
}

GALLERY_PHOTOS = [
    ("gallery-01-aniloks.webp", "Анілоксові вали та формні гільзи"),
    ("gallery-02-val-texture.webp", "Вал тиснення з текстурою"),
    ("gallery-03-flexo.webp", "Флексографічне обладнання"),
    ("gallery-04-val-on-shaft.webp", "Вал тиснення на валу"),
    ("gallery-05-geo-pattern.webp", "Текстура тиснення — геометричний візерунок"),
    ("gallery-06-grid-pattern.webp", "Текстура тиснення — сітка"),
    ("gallery-07-ornament.webp", "Вал тиснення — додатковий вигляд"),
    ("gallery-08-fabric-result.webp", "Результат тиснення на тканині"),
    ("gallery-09-aniloks-sleeves.webp", "Анілоксові та формні вали"),
    ("gallery-10-sleeves.webp", "Формні гільзи (sleeves)"),
    ("gallery-11-flexo-machine.webp", "Флексографічна машина"),
    ("gallery-12-brushes.webp", "Щітки для чищення анілоксів"),
    ("gallery-13-doctor-blade.webp", "Ракельний ніж"),
    ("gallery-14-print-machine.webp", "Електронний навантажувач"),
    ("gallery-15-loader.webp", "Ультразвукова мийка анілоксових гільз"),
    ("gallery-16-bag-machine.webp", "Машина для склеювання"),
    ("gallery-17-parts.webp", "Пакеторобне обладнання"),
]

# (файл у TZ/images_extracted/all → webp у data/seed_media/webp)
WEBP_CONVERSIONS = [
    (EQ_FLEXO_STACK_IMG, HERO_IMAGE),
    (VALY_COVER_IMG, CATEGORY_COVERS["Вали тиснення"]),
    (
        ANILOX_CERAMIC_IMG,
        CATEGORY_COVERS["Анілоксові вали та формні гільзи"],
    ),
    (EQ_FLEXO_STACK_IMG, CATEGORY_COVERS["Обладнання та комплектуючі"]),
    (VALY_COVER_IMG, CATEGORY_GALLERY["Вали тиснення"][0]),
    (VALY_CALENDER_02_IMG, CATEGORY_GALLERY["Вали тиснення"][1]),
    (VALY_STEEL_STEEL_IMG, CATEGORY_GALLERY["Вали тиснення"][2]),
    (VALY_TEXTURE_GEO_IMG, CATEGORY_GALLERY["Вали тиснення"][3]),
    (VALY_TEXTURE_GRID_IMG, CATEGORY_GALLERY["Вали тиснення"][4]),
    (VALY_FABRIC_RESULT_IMG, CATEGORY_GALLERY["Вали тиснення"][5]),
    (
        ANILOX_CERAMIC_IMG,
        CATEGORY_GALLERY["Анілоксові вали та формні гільзи"][0],
    ),
    (
        FORM_SLEEVE_IMG,
        CATEGORY_GALLERY["Анілоксові вали та формні гільзи"][1],
    ),
    (EQ_BRUSHES_IMG, CATEGORY_GALLERY["Обладнання та комплектуючі"][0]),
    (EQ_DOCTOR_BLADE_IMG, CATEGORY_GALLERY["Обладнання та комплектуючі"][1]),
    (EQ_LOADER_IMG, CATEGORY_GALLERY["Обладнання та комплектуючі"][2]),
    (EQ_ULTRASONIC_WASH_IMG, CATEGORY_GALLERY["Обладнання та комплектуючі"][3]),
    (EQ_SLEEVE_WINDER_IMG, CATEGORY_GALLERY["Обладнання та комплектуючі"][4]),
    (EQ_BAG_MACHINE_IMG, CATEGORY_GALLERY["Обладнання та комплектуючі"][5]),
    (EQ_FLEXO_STACK_IMG, CATEGORY_GALLERY["Обладнання та комплектуючі"][6]),
    (VALY_COVER_IMG, PRODUCT_COVERS["VT-CAT"]),
    (
        ANILOX_CERAMIC_IMG,
        PRODUCT_COVERS["AX-CER"],
    ),
    (FORM_SLEEVE_IMG, PRODUCT_COVERS["SL-0095"]),
    (EQ_BRUSHES_IMG, PRODUCT_COVERS["EQ-BRS"]),
    (EQ_DOCTOR_BLADE_IMG, PRODUCT_COVERS["EQ-RKL"]),
    (EQ_LOADER_IMG, PRODUCT_COVERS["EQ-LOAD"]),
    (EQ_ULTRASONIC_WASH_IMG, PRODUCT_COVERS["EQ-USW"]),
    (EQ_SLEEVE_WINDER_IMG, PRODUCT_COVERS["EQ-SLW"]),
    (EQ_BAG_MACHINE_IMG, PRODUCT_COVERS["EQ-BAG"]),
    (EQ_FLEXO_STACK_IMG, PRODUCT_COVERS["EQ-FLEX"]),
    (ANILOX_CERAMIC_IMG, GALLERY_PHOTOS[0][0]),
    (VALY_COVER_IMG, GALLERY_PHOTOS[1][0]),
    (EQ_FLEXO_STACK_IMG, GALLERY_PHOTOS[2][0]),
    (VALY_STEEL_STEEL_IMG, GALLERY_PHOTOS[3][0]),
    (VALY_TEXTURE_GEO_IMG, GALLERY_PHOTOS[4][0]),
    (VALY_TEXTURE_GRID_IMG, GALLERY_PHOTOS[5][0]),
    (VALY_CALENDER_02_IMG, GALLERY_PHOTOS[6][0]),
    (VALY_FABRIC_RESULT_IMG, GALLERY_PHOTOS[7][0]),
    (
        ANILOX_CERAMIC_IMG,
        GALLERY_PHOTOS[8][0],
    ),
    (
        FORM_SLEEVE_IMG,
        GALLERY_PHOTOS[9][0],
    ),
    (EQ_FLEXO_STACK_IMG, GALLERY_PHOTOS[10][0]),
    (EQ_BRUSHES_IMG, GALLERY_PHOTOS[11][0]),
    (EQ_DOCTOR_BLADE_IMG, GALLERY_PHOTOS[12][0]),
    (EQ_LOADER_IMG, GALLERY_PHOTOS[13][0]),
    (EQ_ULTRASONIC_WASH_IMG, GALLERY_PHOTOS[14][0]),
    (EQ_SLEEVE_WINDER_IMG, GALLERY_PHOTOS[15][0]),
    (EQ_BAG_MACHINE_IMG, GALLERY_PHOTOS[16][0]),
]
