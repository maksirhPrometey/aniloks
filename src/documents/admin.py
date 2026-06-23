from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Document


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    list_display = ("title", "category", "updated_at", "order")
    list_editable = ("order",)
    list_filter = ("category",)
    search_fields = ("title",)
