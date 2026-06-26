from django.db import models

from .choices import OTHER_VALUE, resolve_subject_label


class ContactRequest(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    company = models.CharField("Компанія", max_length=150, blank=True)
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=30, blank=True)
    subject = models.CharField(
        "Категорія продукту",
        max_length=100,
        default=OTHER_VALUE,
    )
    message = models.TextField("Повідомлення")
    created_at = models.DateTimeField("Дата", auto_now_add=True)
    is_processed = models.BooleanField("Опрацьовано", default=False)

    class Meta:
        verbose_name = "Звернення"
        verbose_name_plural = "Звернення"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} — {self.get_subject_display()} ({self.created_at.strftime('%d.%m.%Y')})"

    def get_subject_display(self) -> str:
        return resolve_subject_label(self.subject)
