"""Наповнення сайту контентом з ТЗ (тексти, зображення, PDF)."""

from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils.text import slugify

from src.catalog.models import Category, CategoryImage, Product, Specification
from src.catalog.category_content import CATEGORY_GALLERY
from src.core.models import SiteSettings
from src.core.tz_seed_data import (
    CATEGORIES,
    GALLERY_PHOTOS,
    GENERAL_DOC,
    IMAGES,
    PRICE_ITEMS,
    PRODUCTS,
    SITE_SETTINGS,
)
from src.documents.models import Document
from src.gallery.models import Photo
from src.pricing.models import PriceItem


def _save_file(field, src: Path, dest_name: str):
    if not src.exists():
        return False
    with src.open("rb") as fh:
        field.save(dest_name, File(fh), save=False)
    return True


class Command(BaseCommand):
    help = "Заповнює сайт текстами, зображеннями та PDF з папки TZ"

    def handle(self, *args, **options):
        self.stdout.write("Наповнення з ТЗ…")

        settings_obj = SiteSettings.load()
        for key, value in SITE_SETTINGS.items():
            if key == "hero_image":
                continue
            setattr(settings_obj, key, value)
        hero = SITE_SETTINGS["hero_image"]
        if hero.exists():
            _save_file(settings_obj.hero_image, hero, hero.name)
        settings_obj.save()
        self.stdout.write(self.style.SUCCESS("✓ Налаштування сайту"))

        valid_names = {d["name"] for d in CATEGORIES}
        Category.objects.exclude(name__in=valid_names).delete()

        cats = {}
        for data in CATEGORIES:
            cat, _ = Category.objects.update_or_create(
                name=data["name"],
                defaults={
                    "slug": slugify(data["name"], allow_unicode=True),
                    "description": data["description"],
                    "order": data["order"],
                    "is_active": True,
                },
            )
            cover = data["cover"]
            if cover.exists():
                _save_file(cat.cover_image, cover, cover.name)
                cat.save()
            cats[data["name"]] = cat
        self.stdout.write(self.style.SUCCESS(f"✓ Категорії ({len(cats)})"))

        CategoryImage.objects.all().delete()
        gallery_count = 0
        for cat_name, items in CATEGORY_GALLERY.items():
            cat = cats.get(cat_name)
            if not cat:
                continue
            for order, (fname, alt) in enumerate(items, start=1):
                src = IMAGES / fname
                if not src.exists():
                    self.stdout.write(self.style.WARNING(f"  пропущено: {fname}"))
                    continue
                img = CategoryImage(category=cat, alt=alt, order=order)
                _save_file(img.image, src, fname)
                img.save()
                gallery_count += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Фото категорій ({gallery_count})"))

        Product.objects.all().delete()
        product_count = 0
        for pdata in PRODUCTS:
            cat = cats.get(pdata["category"])
            if not cat:
                continue
            product = Product.objects.create(
                category=cat,
                name=pdata["name"],
                article=pdata["article"],
                slug=slugify(pdata["name"], allow_unicode=True),
                short_desc=pdata["short_desc"],
                full_desc=pdata["full_desc"],
                order=pdata["order"],
                is_published=True,
            )
            cover = pdata.get("cover")
            if cover and cover.exists():
                _save_file(product.cover_image, cover, cover.name)
                product.save()
            for i, (label, value) in enumerate(pdata.get("specs", [])):
                Specification.objects.create(
                    product=product, label=label, value=value, order=i + 1
                )
            product_count += 1
        self.stdout.write(self.style.SUCCESS(f"✓ Продукти ({product_count})"))

        Photo.objects.all().delete()
        for i, (fname, caption) in enumerate(GALLERY_PHOTOS):
            src = IMAGES / fname
            if not src.exists():
                self.stdout.write(self.style.WARNING(f"  пропущено: {fname}"))
                continue
            photo = Photo(order=i + 1, caption=caption, alt=caption, is_active=True)
            _save_file(photo.image, src, fname)
            photo.save()
        self.stdout.write(self.style.SUCCESS(f"✓ Галерея ({len(GALLERY_PHOTOS)} фото)"))

        PriceItem.objects.all().delete()
        for cat_name, article, name, desc, order in PRICE_ITEMS:
            PriceItem.objects.create(
                category=cats.get(cat_name),
                article=article,
                name=name,
                description=desc,
                price_note="За запитом",
                order=order,
                is_active=True,
            )
        self.stdout.write(self.style.SUCCESS(f"✓ Прайс-лист ({len(PRICE_ITEMS)} позицій)"))

        Document.objects.all().delete()
        doc_order = 0
        for data in CATEGORIES:
            cat = cats.get(data["name"])
            pdf = data["doc_pdf"]
            if not pdf.exists():
                continue
            doc_order += 1
            doc = Document(
                category=cat,
                title=data["doc_title"],
                order=doc_order,
            )
            _save_file(doc.file, pdf, pdf.name)
            doc.save()

        general_pdf = GENERAL_DOC["pdf"]
        if general_pdf.exists():
            doc_order += 1
            doc = Document(title=GENERAL_DOC["title"], order=doc_order)
            _save_file(doc.file, general_pdf, general_pdf.name)
            doc.save()

        self.stdout.write(self.style.SUCCESS(f"✓ E-Каталог ({doc_order} PDF)"))
        self.stdout.write(self.style.SUCCESS("Готово!"))
