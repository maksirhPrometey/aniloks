from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import PriceItem


@admin.register(PriceItem)
class PriceItemAdmin(ModelAdmin):
    list_display = ("article", "name", "category", "price_note", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("article", "name")
