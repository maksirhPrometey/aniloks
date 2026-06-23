from django.shortcuts import get_object_or_404, render

from src.documents.models import Document

from .models import Category, Product


def category_modal(request, slug):
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = (
        category.products.filter(is_published=True)
        .prefetch_related("specs")
        .order_by("order", "name")
    )
    document = Document.objects.filter(category=category).first()
    return render(
        request,
        "partials/modals/category.html",
        {"category": category, "products": products, "document": document},
    )


def product_modal(request, slug):
    product = get_object_or_404(
        Product.objects.select_related("category").prefetch_related("specs"),
        slug=slug,
        is_published=True,
    )
    return render(request, "partials/modals/product.html", {"product": product})
