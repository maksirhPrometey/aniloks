"""Динамічні варіанти категорії продукту для форми звернення."""

from __future__ import annotations

from django.db.models import Prefetch

LEGACY_SUBJECT_LABELS = {
    "embossing": "Вали тиснення",
    "anilox": "Анілоксові вали та формні гільзи",
    "equipment": "Обладнання та комплектуючи",
    "other": "Інше / загальна консультація",
}

OTHER_VALUE = "other"
OTHER_LABEL = "Інше / загальна консультація"


def build_subject_choices(*, compact=False):
    """Повертає choices для Select. compact=True — лише категорії без продуктів."""
    from src.catalog.models import Category, Product

    grouped: list[tuple[str, list[tuple[str, str]]]] = []
    flat_values: set[str] = {OTHER_VALUE}

    categories = (
        Category.objects.filter(is_active=True)
        .order_by("order", "name")
        .prefetch_related(
            Prefetch(
                "products",
                queryset=Product.objects.filter(is_published=True).order_by("order", "name"),
            )
        )
    )

    if not categories.exists():
        legacy_options = [
            (key, label)
            for key, label in LEGACY_SUBJECT_LABELS.items()
            if key != OTHER_VALUE
        ]
        legacy_options.append((OTHER_VALUE, OTHER_LABEL))
        flat_values.update(key for key, _ in legacy_options)
        return [("", legacy_options)], flat_values

    if compact:
        options: list[tuple[str, str]] = []
        for category in categories:
            value = f"category:{category.slug}"
            options.append((value, category.name))
            flat_values.add(value)
        options.append((OTHER_VALUE, OTHER_LABEL))
        return [("", options)], flat_values

    for category in categories:
        options: list[tuple[str, str]] = [
            (f"category:{category.slug}", f"Уся категорія «{category.name}»"),
        ]
        flat_values.add(f"category:{category.slug}")

        for product in category.products.all():
            options.append((product.slug, product.name))
            flat_values.add(product.slug)

        grouped.append((category.name, options))

    grouped.append(("", [(OTHER_VALUE, OTHER_LABEL)]))
    return grouped, flat_values


def resolve_subject_label(value: str) -> str:
    if not value:
        return "—"

    if value in LEGACY_SUBJECT_LABELS:
        return LEGACY_SUBJECT_LABELS[value]

    if value == OTHER_VALUE:
        return OTHER_LABEL

    if value.startswith("category:"):
        slug = value.removeprefix("category:")
        from src.catalog.models import Category

        category = Category.objects.filter(slug=slug).first()
        if category:
            return f"Уся категорія «{category.name}»"
        return slug

    from src.catalog.models import Product

    product = Product.objects.filter(slug=value).select_related("category").first()
    if product:
        if product.category:
            return f"{product.category.name} — {product.name}"
        return product.name

    return value
