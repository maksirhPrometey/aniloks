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

PRODUCT_COVERS = {
    "VT-0024": "product-vt-steel-steel.webp",
    "VT-0031": "product-vt-steel-rubber.webp",
    "VT-0040": "product-vt-steel-paper.webp",
    "AX-CHR": "product-aniloks-chrome.webp",
    "AX-0150": "product-aniloks-ceramic-150.webp",
    "AX-0300": "product-aniloks-ceramic-300.webp",
    "SL-0095": "product-sleeve-95.webp",
    "EQ-BRS": "product-brushes.webp",
    "EQ-RKL18": "product-doctor-blade.webp",
    "EQ-L1000": "product-loader-1000.webp",
    "EQ-L1500": "product-loader-1500.webp",
    "EQ-USW": "product-ultrasonic-wash.webp",
    "EQ-SLW": "product-sleeve-winder.webp",
    "EQ-BAG": "product-bag-machine.webp",
    "EQ-FLX-ST": "product-flexo-stack.webp",
    "EQ-FLX-CI": "product-flexo-ci.webp",
    "EQ-FLX-IL": "product-flexo-inline.webp",
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
    ("раздел_вали_тиснення_p1_img2_342x188.png", PRODUCT_COVERS["VT-0024"]),
    ("раздел_вали_тиснення_p1_img6_415x307.png", PRODUCT_COVERS["VT-0031"]),
    ("раздел_вали_тиснення_p1_img5_453x284.png", PRODUCT_COVERS["VT-0040"]),
    (
        "раздел_анилоксовые_и_формные_валы_p1_img2_784x591.png",
        PRODUCT_COVERS["AX-CHR"],
    ),
    ("первая_страничка_p1_img3_569x440.png", PRODUCT_COVERS["AX-0150"]),
    ("раздел_вали_тиснення_p1_img4_468x400.png", PRODUCT_COVERS["AX-0300"]),
    ("раздел_анилоксовые_и_формные_валы_p1_img3_291x203.png", PRODUCT_COVERS["SL-0095"]),
    ("раздел_обладнання_та_комплектуючи_p1_img3_271x174.png", PRODUCT_COVERS["EQ-BRS"]),
    ("раздел_обладнання_та_комплектуючи_p1_img4_822x566.png", PRODUCT_COVERS["EQ-RKL18"]),
    ("раздел_обладнання_та_комплектуючи_p1_img6_881x505.png", PRODUCT_COVERS["EQ-L1000"]),
    (
        "раздел_обладнання_та_комплектуючи_p1_img6_881x505.png",
        PRODUCT_COVERS["EQ-L1500"],
    ),
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
        PRODUCT_COVERS["EQ-FLX-ST"],
    ),
    (
        "раздел_обладнання_та_комплектуючи_p1_img2_795x657.png",
        PRODUCT_COVERS["EQ-FLX-CI"],
    ),
    ("первая_страничка_p1_img4_804x484.png", PRODUCT_COVERS["EQ-FLX-IL"]),
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
