from django.db import models
from src.catalog.models import Category


class PriceItem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prices",
        verbose_name="Категорія",
    )
    article = models.CharField("Артикль", max_length=50, blank=True)
    name = models.CharField("Назва", max_length=255)
    description = models.TextField("Опис", blank=True)
    price_note = models.CharField("Ціна (примітка)", max_length=100, blank=True, default="За запитом")
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    is_active = models.BooleanField("Активне", default=True)

    class Meta:
        verbose_name = "Позиція прайсу"
        verbose_name_plural = "Прайс-лист"
        ordering = ["category", "order", "name"]

    def __str__(self) -> str:
        return self.name
