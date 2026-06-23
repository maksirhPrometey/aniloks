from django.db import models
from src.catalog.models import Category


class Document(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documents",
        verbose_name="Категорія",
    )
    title = models.CharField("Назва", max_length=255)
    file = models.FileField("PDF файл", upload_to="documents/")
    updated_at = models.DateTimeField("Оновлено", auto_now=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документи (E-Catalog)"
        ordering = ["category", "order", "title"]

    def __str__(self) -> str:
        return self.title
