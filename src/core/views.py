from django.http import HttpResponse
from django.shortcuts import render

from src.catalog.models import Product
from src.contacts.forms import ContactForm


def healthz(request):
    return HttpResponse("ok", content_type="text/plain")


def home(request):
    featured_products = (
        Product.objects.filter(is_published=True, is_featured=True)
        .select_related("category")
        .prefetch_related("category__images")
        .order_by("order", "name")
    )

    return render(request, "pages/home.html", {
        "page_title": "Обладнання для Друку",
        "meta_description": (
            "Постачання обладнання та комплектуючих для поліграфічної та "
            "пакувальної промисловості України. Вали тиснення, анілоксові вали, "
            "флексографічне обладнання від виробника з Китаю."
        ),
        "featured_products": featured_products,
        "form": ContactForm(),
    })
