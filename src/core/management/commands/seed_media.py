"""Заповнює ImageField з data/seed_media/webp/ (для prod після seed_from_tz)."""

from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand

from src.catalog.models import Category, Product
from src.core.media_seed_data import (
    CATEGORY_COVERS,
    GALLERY_PHOTOS,
    HERO_IMAGE,
    PRODUCT_COVERS,
    WEBP_DIR,
)
from src.core.models import SiteSettings
from src.gallery.models import Photo


def _attach(field, webp_path: Path, force: bool) -> bool:
    if not webp_path.exists():
        return False
    if field and not force:
        try:
            if field.name:
                return False
        except (ValueError, AttributeError):
            pass
    with webp_path.open("rb") as fh:
        field.save(webp_path.name, File(fh), save=False)
    return True


class Command(BaseCommand):
    help = "Завантажує WebP-зображення з data/seed_media/webp/ у моделі сайту"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Перезаписати наявні зображення",
        )
        parser.add_argument(
            "--gallery-only",
            action="store_true",
            help="Лише галерея",
        )
        parser.add_argument(
            "--skip-gallery",
            action="store_true",
            help="Без галереї",
        )

    def handle(self, *args, **options):
        force = options["force"]
        gallery_only = options["gallery_only"]
        skip_gallery = options["skip_gallery"]

        if not WEBP_DIR.is_dir():
            self.stderr.write(
                self.style.ERROR(
                    f"Немає папки {WEBP_DIR}. Спочатку: python manage.py build_seed_webp"
                )
            )
            return

        if not gallery_only:
            self._seed_hero(force)
            self._seed_categories(force)
            self._seed_products(force)

        if not skip_gallery:
            self._seed_gallery(force)

        self.stdout.write(self.style.SUCCESS("Зображення завантажено."))

    def _seed_hero(self, force: bool) -> None:
        settings_obj = SiteSettings.load()
        path = WEBP_DIR / HERO_IMAGE
        if _attach(settings_obj.hero_image, path, force):
            settings_obj.save()
            self.stdout.write(self.style.SUCCESS("✓ Hero"))
        else:
            self._warn_missing("Hero", path, settings_obj.hero_image, force)

    def _seed_categories(self, force: bool) -> None:
        count = 0
        for name, webp_name in CATEGORY_COVERS.items():
            cat = Category.objects.filter(name=name).first()
            if not cat:
                self.stdout.write(self.style.WARNING(f"  категорія не знайдена: {name}"))
                continue
            path = WEBP_DIR / webp_name
            if _attach(cat.cover_image, path, force):
                cat.save()
                count += 1
            else:
                self._warn_missing(f"Категорія «{name}»", path, cat.cover_image, force)
        self.stdout.write(self.style.SUCCESS(f"✓ Категорії ({count})"))

    def _seed_products(self, force: bool) -> None:
        count = 0
        for article, webp_name in PRODUCT_COVERS.items():
            product = Product.objects.filter(article=article).first()
            if not product:
                self.stdout.write(
                    self.style.WARNING(f"  продукт не знайдений: {article}")
                )
                continue
            path = WEBP_DIR / webp_name
            if _attach(product.cover_image, path, force):
                product.save()
                count += 1
            else:
                self._warn_missing(
                    f"Продукт {article}", path, product.cover_image, force
                )
        self.stdout.write(self.style.SUCCESS(f"✓ Продукти ({count})"))

    def _seed_gallery(self, force: bool) -> None:
        if force:
            Photo.objects.all().delete()

        count = 0
        for i, (webp_name, caption) in enumerate(GALLERY_PHOTOS):
            path = WEBP_DIR / webp_name
            if not path.exists():
                self.stdout.write(self.style.WARNING(f"  немає файлу: {webp_name}"))
                continue

            photo = Photo.objects.filter(order=i + 1).first()
            if photo and not force:
                if photo.image.name:
                    continue
            if not photo:
                photo = Photo(
                    order=i + 1,
                    caption=caption,
                    alt=caption,
                    is_active=True,
                )
            else:
                photo.caption = caption
                photo.alt = caption
                photo.is_active = True

            with path.open("rb") as fh:
                photo.image.save(webp_name, File(fh), save=False)
            photo.save()
            count += 1

        self.stdout.write(self.style.SUCCESS(f"✓ Галерея ({count})"))

    def _warn_missing(self, label, path: Path, field, force: bool) -> None:
        if not path.exists():
            self.stdout.write(self.style.WARNING(f"  немає файлу для {label}: {path.name}"))
        elif not force and field and field.name:
            self.stdout.write(f"  пропущено (вже є): {label}")
