"""Мапінг WebP-асетів для seed_media (hero, категорії, продукти, галерея)."""

from pathlib import Path

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
    ("gallery-07-ornament.webp", "Текстура тиснення — орнамент"),
    ("gallery-08-fabric-result.webp", "Результат тиснення на тканині"),
    ("gallery-09-aniloks-sleeves.webp", "Анілоксові та формні вали"),
    ("gallery-10-sleeves.webp", "Формні гільзи (sleeves)"),
    ("gallery-11-flexo-machine.webp", "Флексографічна машина"),
    ("gallery-12-brushes.webp", "Щітки для чищення анілоксів"),
    ("gallery-13-doctor-blade.webp", "Ракельний ніж"),
    ("gallery-14-print-machine.webp", "Промислова друкарська машина"),
    ("gallery-15-loader.webp", "Електронний навантажувач"),
    ("gallery-16-bag-machine.webp", "Пакеторобне обладнання"),
    ("gallery-17-parts.webp", "Комплектуючі для друку"),
]

# (файл у TZ/images_extracted/all → webp у data/seed_media/webp)
WEBP_CONVERSIONS = [
    ("раздел_обладнання_та_комплектуючи_p1_img5_1004x753.png", HERO_IMAGE),
    ("раздел_вали_тиснення_p1_img3_569x440.png", CATEGORY_COVERS["Вали тиснення"]),
    (
        "раздел_анилоксовые_и_формные_валы_p1_img2_784x591.png",
        CATEGORY_COVERS["Анілоксові вали та формні гільзи"],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img2_795x657.png",
        CATEGORY_COVERS["Обладнання та комплектуючі"],
    ),
    ("раздел_вали_тиснення_p1_img2_342x188.png", CATEGORY_GALLERY["Вали тиснення"][0]),
    ("раздел_вали_тиснення_p1_img3_569x440.png", CATEGORY_GALLERY["Вали тиснення"][1]),
    ("раздел_вали_тиснення_p1_img4_468x400.png", CATEGORY_GALLERY["Вали тиснення"][2]),
    ("раздел_вали_тиснення_p1_img5_453x284.png", CATEGORY_GALLERY["Вали тиснення"][3]),
    ("раздел_вали_тиснення_p1_img6_415x307.png", CATEGORY_GALLERY["Вали тиснення"][4]),
    ("раздел_вали_тиснення_p1_img7_293x296.png", CATEGORY_GALLERY["Вали тиснення"][5]),
    (
        "раздел_анилоксовые_и_формные_валы_p1_img2_784x591.png",
        CATEGORY_GALLERY["Анілоксові вали та формні гільзи"][0],
    ),
    (
        "раздел_анилоксовые_и_формные_валы_p1_img3_291x203.png",
        CATEGORY_GALLERY["Анілоксові вали та формні гільзи"][1],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img2_795x657.png",
        CATEGORY_GALLERY["Обладнання та комплектуючі"][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img3_271x174.png",
        CATEGORY_GALLERY["Обладнання та комплектуючі"][1],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img4_822x566.png",
        CATEGORY_GALLERY["Обладнання та комплектуючі"][2],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img5_1004x753.png",
        CATEGORY_GALLERY["Обладнання та комплектуючі"][3],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img6_881x505.png",
        CATEGORY_GALLERY["Обладнання та комплектуючі"][4],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img7_1705x1279.jpeg",
        CATEGORY_GALLERY["Обладнання та комплектуючі"][5],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img8_804x484.png",
        CATEGORY_GALLERY["Обладнання та комплектуючі"][6],
    ),
    ("раздел_вали_тиснення_p1_img3_569x440.png", PRODUCT_COVERS["VT-CAT"]),
    (
        "раздел_анилоксовые_и_формные_валы_p1_img2_784x591.png",
        PRODUCT_COVERS["AX-CER"],
    ),
    ("раздел_анилоксовые_и_формные_валы_p1_img3_291x203.png", PRODUCT_COVERS["SL-0095"]),
    ("раздел_обладнання_та_комплектуючи_p1_img3_271x174.png", PRODUCT_COVERS["EQ-BRS"]),
    ("раздел_обладнання_та_комплектуючи_p1_img4_822x566.png", PRODUCT_COVERS["EQ-RKL"]),
    ("раздел_обладнання_та_комплектуючи_p1_img6_881x505.png", PRODUCT_COVERS["EQ-LOAD"]),
    ("раздел_обладнання_та_комплектуючи_p1_img4_822x566.png", PRODUCT_COVERS["EQ-USW"]),
    (
        "раздел_обладнання_та_комплектуючи_p1_img7_1705x1279.jpeg",
        PRODUCT_COVERS["EQ-SLW"],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img7_1705x1279.jpeg",
        PRODUCT_COVERS["EQ-BAG"],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img5_1004x753.png",
        PRODUCT_COVERS["EQ-FLEX"],
    ),
    ("первая_страничка_p1_img2_784x591.png", GALLERY_PHOTOS[0][0]),
    ("первая_страничка_p1_img3_569x440.png", GALLERY_PHOTOS[1][0]),
    ("первая_страничка_p1_img4_804x484.png", GALLERY_PHOTOS[2][0]),
    ("раздел_вали_тиснення_p1_img2_342x188.png", GALLERY_PHOTOS[3][0]),
    ("раздел_вали_тиснення_p1_img4_468x400.png", GALLERY_PHOTOS[4][0]),
    ("раздел_вали_тиснення_p1_img5_453x284.png", GALLERY_PHOTOS[5][0]),
    ("раздел_вали_тиснення_p1_img6_415x307.png", GALLERY_PHOTOS[6][0]),
    ("раздел_вали_тиснення_p1_img7_293x296.png", GALLERY_PHOTOS[7][0]),
    (
        "раздел_анилоксовые_и_формные_валы_p1_img2_784x591.png",
        GALLERY_PHOTOS[8][0],
    ),
    (
        "раздел_анилоксовые_и_формные_валы_p1_img3_291x203.png",
        GALLERY_PHOTOS[9][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img2_795x657.png",
        GALLERY_PHOTOS[10][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img3_271x174.png",
        GALLERY_PHOTOS[11][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img4_822x566.png",
        GALLERY_PHOTOS[12][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img5_1004x753.png",
        GALLERY_PHOTOS[13][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img6_881x505.png",
        GALLERY_PHOTOS[14][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img7_1705x1279.jpeg",
        GALLERY_PHOTOS[15][0],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img8_804x484.png",
        GALLERY_PHOTOS[16][0],
    ),
]
