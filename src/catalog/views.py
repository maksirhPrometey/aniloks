from django.shortcuts import get_object_or_404, render

from src.documents.models import Document

from .models import Category


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
