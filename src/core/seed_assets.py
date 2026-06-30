"""Шляхи до джерел зображень для seed (DOCX / TZ / data/seed_media/source)."""

from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
TZ_IMAGES = BASE / "TZ" / "images_extracted" / "all"
SOURCE_DIR = BASE / "data" / "seed_media" / "source"

# З DOCX «раздел анилоксы и формные валы.docx»
ANILOX_CERAMIC_IMG = SOURCE_DIR / "anilox" / "anilox-ceramic.png"
FORM_SLEEVE_IMG = SOURCE_DIR / "anilox" / "form-sleeve.png"

# З DOCX «раздел вали тиснення.docx»
VALY_DIR = SOURCE_DIR / "valy-tisnennia"
VALY_COVER_IMG = VALY_DIR / "val-cover.jpeg"
VALY_CALENDER_02_IMG = VALY_DIR / "val-calender-02.jpeg"
VALY_STEEL_STEEL_IMG = VALY_DIR / "val-steel-steel.png"
VALY_TEXTURE_GEO_IMG = VALY_DIR / "val-texture-geo.jpeg"
VALY_TEXTURE_GRID_IMG = VALY_DIR / "val-texture-grid.jpeg"
VALY_FABRIC_RESULT_IMG = VALY_DIR / "val-fabric-result.png"

VALY_GALLERY = (
    (VALY_COVER_IMG, "Вал тиснення (каландр)"),
    (VALY_CALENDER_02_IMG, "Вал тиснення з текстурою"),
    (VALY_STEEL_STEEL_IMG, "Вал тиснення «сталь–сталь»"),
    (VALY_TEXTURE_GEO_IMG, "Текстура тиснення — геометричний візерунок"),
    (VALY_TEXTURE_GRID_IMG, "Текстура тиснення — сітка"),
    (VALY_FABRIC_RESULT_IMG, "Результат тиснення на тканині"),
)

# З DOCX «раздел оборудование и комплектующие.docx»
EQ_DIR = SOURCE_DIR / "equipment"
EQ_BRUSHES_IMG = EQ_DIR / "eq-brushes.png"
EQ_DOCTOR_BLADE_IMG = EQ_DIR / "eq-doctor-blade.png"
EQ_LOADER_IMG = EQ_DIR / "eq-loader.png"
EQ_ULTRASONIC_WASH_IMG = EQ_DIR / "eq-ultrasonic-wash.jpeg"
EQ_SLEEVE_WINDER_IMG = EQ_DIR / "eq-sleeve-winder.jpeg"
EQ_BAG_MACHINE_IMG = EQ_DIR / "eq-bag-machine.jpeg"
EQ_FLEXO_STACK_IMG = EQ_DIR / "eq-flexo-stack.png"

# З DOCX «Документ Microsoft Word.docx» — магнітні циліндри
MAGNETIC_CYLINDER_IMG = SOURCE_DIR / "magnetic-cylinder" / "magnetic-cylinder.png"

EQUIPMENT_GALLERY = (
    (EQ_BRUSHES_IMG, "Щітки для чищення анілоксів"),
    (EQ_DOCTOR_BLADE_IMG, "Ракельний ніж"),
    (EQ_LOADER_IMG, "Електронний навантажувач"),
    (EQ_ULTRASONIC_WASH_IMG, "Ультразвукова мийка анілоксових гільз"),
    (EQ_SLEEVE_WINDER_IMG, "Машина для склеювання"),
    (EQ_BAG_MACHINE_IMG, "Пакеторобне обладнання"),
    (EQ_FLEXO_STACK_IMG, "Флексографічна машина"),
    (MAGNETIC_CYLINDER_IMG, "Магнітні циліндри для ротаційного висікання"),
)
