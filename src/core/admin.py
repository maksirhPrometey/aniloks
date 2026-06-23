from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    fieldsets = (
        ("Основне", {
            "fields": ("site_name", "slogan"),
        }),
        ("Hero секція", {
            "fields": ("hero_image", "hero_eyebrow", "hero_title", "hero_subtitle"),
        }),
        ("Про компанію", {
            "fields": ("about_text", "clients_text"),
        }),
        ("Контакти", {
            "fields": ("phone", "email", "working_hours", "address"),
        }),
        ("Соцмережі", {
            "fields": ("telegram", "instagram", "facebook"),
        }),
    )
    readonly_fields = ("hero_preview",)

    def hero_preview(self, obj):
        if obj.hero_image:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:4px">',
                obj.hero_image.url,
            )
        return "—"
    hero_preview.short_description = "Превью"

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
