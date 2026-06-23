"""Конвертує зображення з TZ у WebP у data/seed_media/webp/."""

from pathlib import Path

from django.core.management.base import BaseCommand
from PIL import Image

from src.core.media_seed_data import TZ_IMAGES, WEBP_CONVERSIONS, WEBP_DIR


def _to_webp(src: Path, dst: Path, quality: int = 85) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(dst, format="WEBP", quality=quality, method=6)


class Command(BaseCommand):
    help = "Конвертує зображення з TZ/images_extracted/all у data/seed_media/webp/"

    def add_arguments(self, parser):
        parser.add_argument(
            "--quality",
            type=int,
            default=85,
            help="Якість WebP (1–100, за замовчуванням 85)",
        )

    def handle(self, *args, **options):
        quality = options["quality"]
        converted = 0
        skipped = 0
        missing = 0

        self.stdout.write(f"Джерело: {TZ_IMAGES}")
        self.stdout.write(f"Ціль: {WEBP_DIR}")

        cache: dict[str, Path] = {}

        for src_name, webp_name in WEBP_CONVERSIONS:
            dst = WEBP_DIR / webp_name
            if dst.exists():
                skipped += 1
                continue

            src = TZ_IMAGES / src_name
            if not src.exists():
                self.stdout.write(self.style.WARNING(f"  немає джерела: {src_name}"))
                missing += 1
                continue

            if src_name in cache and cache[src_name].exists():
                dst.write_bytes(cache[src_name].read_bytes())
                converted += 1
                self.stdout.write(f"  копія → {webp_name}")
                continue

            _to_webp(src, dst, quality=quality)
            cache[src_name] = dst
            converted += 1
            self.stdout.write(self.style.SUCCESS(f"  ✓ {webp_name}"))

        unique = len({w for _, w in WEBP_CONVERSIONS})
        self.stdout.write(
            self.style.SUCCESS(
                f"Готово: {converted} нових, {skipped} вже є, {missing} без джерела, "
                f"унікальних webp: {unique}"
            )
        )
