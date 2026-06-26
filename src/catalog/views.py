from django.shortcuts import get_object_or_404, render

from src.documents.models import Document

from .models import Category, Product


def category_modal(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = (
        category.products.filter(is_published=True)
        .order_by("order", "name")
    )
    gallery_images = []
    for product in products:
        if product.cover_image:
            gallery_images.append(
                {"url": product.cover_image.url, "alt": product.name}
            )
    if not gallery_images and category.cover_image:
        gallery_images.append(
            {"url": category.cover_image.url, "alt": category.name}
        )
    document = Document.objects.filter(category=category).first()
    return render(
        request,
        "partials/modals/category.html",
        {
            "category": category,
            "gallery_images": gallery_images,
            "document": document,
        },
    )


def product_modal(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("category").prefetch_related("specs"),
        slug=slug,
        is_published=True,
    )
    return render(request, "partials/modals/product.html", {"product": product})
