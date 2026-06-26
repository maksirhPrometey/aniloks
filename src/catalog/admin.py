from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, CategoryImage, Product, ProductImage, Specification


class CategoryImageInline(TabularInline):
    model = CategoryImage
    extra = 0
    fields = ("image", "image_preview", "alt", "order")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:80px;border-radius:4px">',
                obj.image.url,
            )
        return "—"
    image_preview.short_description = "Превью"


class ProductImageInline(TabularInline):
    model = ProductImage
    extra = 0
    fields = ("image", "image_preview", "alt", "order")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:80px;border-radius:4px">',
                obj.image.url,
            )
        return "—"
    image_preview.short_description = "Превью"


class SpecificationInline(TabularInline):
    model = Specification
    extra = 0
    fields = ("label", "value", "order")


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [CategoryImageInline]


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ("name", "article", "category", "is_featured", "is_published", "order", "cover_preview")
    list_editable = ("is_featured", "is_published", "order")
    list_filter = ("category", "is_published")
    search_fields = ("name", "article")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline, SpecificationInline]
    fieldsets = (
        ("Основне", {
            "fields": ("category", "name", "article", "slug", "is_published", "order"),
        }),
        ("Вміст", {
            "fields": ("cover_image", "short_desc", "full_desc"),
        }),
    )

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="max-height:60px;border-radius:4px">',
                obj.cover_image.url,
            )
        return "—"
    cover_preview.short_description = "Фото"
