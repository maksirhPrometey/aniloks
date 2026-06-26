"""Конвертує зображення з TZ / data/seed_media/source у WebP у data/seed_media/webp/."""

from pathlib import Path

from django.core.management.base import BaseCommand
from PIL import Image

from src.core.media_seed_data import TZ_IMAGES, WEBP_CONVERSIONS, WEBP_DIR


def _resolve_src(src_ref: str | Path) -> Path:
    if isinstance(src_ref, Path):
        return src_ref
    return TZ_IMAGES / src_ref


def _to_webp(src: Path, dst: Path, quality: int = 85) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(dst, format="WEBP", quality=quality, method=6)


class Command(BaseCommand):
    help = "Конвертує джерельні зображення у data/seed_media/webp/"

    def add_arguments(self, parser):
        parser.add_argument(
            "--quality",
            type=int,
            default=85,
            help="Якість WebP (1–100, за замовчуванням 85)",
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Перезаписати наявні WebP",
        )

    def handle(self, *args, **options):
        quality = options["quality"]
        force = options["force"]
        converted = 0
        skipped = 0
        missing = 0

        self.stdout.write(f"TZ: {TZ_IMAGES}")
        self.stdout.write(f"Ціль: {WEBP_DIR}")

        cache: dict[str, Path] = {}

        for src_ref, webp_name in WEBP_CONVERSIONS:
            dst = WEBP_DIR / webp_name
            if dst.exists() and not force:
                skipped += 1
                continue

            src = _resolve_src(src_ref)
            cache_key = str(src.resolve())

            if not src.exists():
                label = src_ref if isinstance(src_ref, str) else src_ref.name
                self.stdout.write(self.style.WARNING(f"  немає джерела: {label}"))
                missing += 1
                continue

            if cache_key in cache and cache[cache_key].exists() and not force:
                dst.write_bytes(cache[cache_key].read_bytes())
                converted += 1
                self.stdout.write(f"  копія → {webp_name}")
                continue

            _to_webp(src, dst, quality=quality)
            cache[cache_key] = dst
            converted += 1
            self.stdout.write(self.style.SUCCESS(f"  ✓ {webp_name}"))

        unique = len({w for _, w in WEBP_CONVERSIONS})
        self.stdout.write(
            self.style.SUCCESS(
                f"Готово: {converted} нових, {skipped} вже є, {missing} без джерела, "
                f"унікальних webp: {unique}"
            )
        )
