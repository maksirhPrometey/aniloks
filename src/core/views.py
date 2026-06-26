from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render

from src.catalog.models import Category, Product
from src.contacts.forms import ContactForm
from src.documents.models import Document


def healthz(request):
    return HttpResponse("ok", content_type="text/plain")


def home(request):
    categories = (
        Category.objects.filter(is_active=True)
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
        "documents": Document.objects.all().select_related("category").order_by("category", "order"),
        "form": ContactForm(),
    })
