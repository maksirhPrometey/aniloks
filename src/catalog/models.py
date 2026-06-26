from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField("Назва", max_length=200)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Опис", blank=True)
    cover_image = models.ImageField("Обкладинка", upload_to="categories/", blank=True, null=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["order", "name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class CategoryImage(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Категорія",
    )
    image = models.ImageField("Фото", upload_to="categories/gallery/")
    alt = models.CharField("Alt текст", max_length=200, blank=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Фото категорії"
        verbose_name_plural = "Фото категорії"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.category.name} — фото {self.order}"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категорія",
    )
    name = models.CharField("Назва", max_length=255)
    article = models.CharField("Артикль", max_length=50, blank=True)
    slug = models.SlugField("Slug", unique=True, blank=True)
    short_desc = models.TextField("Короткий опис", blank=True)
    full_desc = models.TextField("Повний опис", blank=True)
    cover_image = models.ImageField("Головне фото", upload_to="products/", blank=True, null=True)
    is_published = models.BooleanField("Опубліковано", default=True)
    is_featured = models.BooleanField("На головній", default=False)
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        ordering = ["order", "name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Продукт",
    )
    image = models.ImageField("Фото", upload_to="products/gallery/")
    alt = models.CharField("Alt текст", max_length=200, blank=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Фото продукту"
        verbose_name_plural = "Фото продукту"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.product.name} — фото {self.order}"


class Specification(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="specs",
        verbose_name="Продукт",
    )
    label = models.CharField("Параметр", max_length=100)
    value = models.CharField("Значення", max_length=200)
    order = models.PositiveSmallIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Специфікація"
        verbose_name_plural = "Специфікації"
        ordering = ["order"]

    def __str__(self) -> str:
        return f"{self.label}: {self.value}"
