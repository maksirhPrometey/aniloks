from django.shortcuts import get_object_or_404, render

from .models import Category, Product

VT_CAT_ARTICLE = "VT-CAT"


def _product_gallery_images(product: Product) -> list[dict[str, str]]:
    if product.article == VT_CAT_ARTICLE:
        return [
            {"url": img.image.url, "alt": img.alt or product.name}
            for img in product.category.images.all()
            if img.image
        ]

    if product.cover_image:
        return [{"url": product.cover_image.url, "alt": product.name}]
    return []


def product_modal(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("category").prefetch_related(
            "category__images",
        ),
        slug=slug,
        is_published=True,
        is_featured=True,
    )
    return render(
        request,
        "partials/modals/product.html",
        {
            "product": product,
            "gallery_images": _product_gallery_images(product),
        },
    )


def category_modal(request, slug):
    category = get_object_or_404(
        Category.objects.prefetch_related("images"),
        slug=slug,
        is_active=True,
    )
    gallery_images = [
        {"url": img.image.url, "alt": img.alt or category.name}
        for img in category.images.all()
        if img.image
    ]
    if not gallery_images and category.cover_image:
        gallery_images.append(
            {"url": category.cover_image.url, "alt": category.name}
        )
    return render(
        request,
        "partials/modals/category.html",
        {
            "category": category,
            "gallery_images": gallery_images,
        },
    )
