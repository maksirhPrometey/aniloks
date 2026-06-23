from django.db.models import Count, Prefetch, Q
from django.http import HttpResponse
from django.shortcuts import render

from src.catalog.models import Category, Product
from src.contacts.forms import ContactForm
from src.documents.models import Document
from src.gallery.models import Photo, Video
from src.pricing.models import PriceItem


def healthz(request):
    return HttpResponse("ok", content_type="text/plain")


def home(request):
    product_slugs = dict(
        Product.objects.filter(is_published=True)
        .exclude(article="")
        .values_list("article", "slug")
    )
    price_qs = PriceItem.objects.filter(is_active=True).select_related("category")
    price_items = []
    for item in price_qs:
        item.product_slug = product_slugs.get(item.article, "")
        price_items.append(item)

    categories = (
        Category.objects.filter(is_active=True)
        .annotate(product_count=Count("products", filter=Q(products__is_published=True)))
        .prefetch_related(
            Prefetch(
                "products",
                queryset=Product.objects.filter(is_published=True).order_by("order", "name"),
            )
        )
        .order_by("order")
    )

    return render(request, "pages/home.html", {
        "page_title": "Обладнання для Друку",
        "meta_description": (
            "Постачання обладнання та комплектуючих для поліграфічної та "
            "пакувальної промисловості України. Вали тиснення, анілоксові вали, "
            "флексографічне обладнання від виробника з Китаю."
        ),
        "categories": categories,
        "photos": Photo.objects.filter(is_active=True).order_by("order")[:12],
        "videos": Video.objects.filter(is_active=True).order_by("order")[:6],
        "price_items": price_items,
        "documents": Document.objects.all().select_related("category").order_by("category", "order"),
        "form": ContactForm(),
    })
