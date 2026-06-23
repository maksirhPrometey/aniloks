from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Photo, Video


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    list_display = ("photo_preview", "caption", "order", "is_active")
    list_editable = ("order", "is_active")

    def photo_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:60px;border-radius:4px">',
                obj.image.url,
            )
        return "—"
    photo_preview.short_description = "Фото"


@admin.register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")
