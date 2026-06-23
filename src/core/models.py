from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField("Назва сайту", max_length=120, default="Nikola")
    slogan = models.CharField("Слоган", max_length=200, blank=True)
    hero_image = models.ImageField("Hero зображення", upload_to="hero/", blank=True, null=True)
    hero_eyebrow = models.CharField("Hero eyebrow текст", max_length=100, blank=True)
    hero_title = models.CharField("Hero заголовок", max_length=200, blank=True)
    hero_subtitle = models.TextField("Hero підзаголовок", blank=True)
    about_text = models.TextField("Про компанію", blank=True)
    clients_text = models.TextField("Клієнтська база", blank=True)
    phone = models.CharField("Телефон", max_length=30, blank=True, default="+38 (066) 988-32-42")
    email = models.EmailField("Email", blank=True, default="nikolajcornejko@gmail.com")
    working_hours = models.CharField("Робочі години", max_length=100, blank=True)
    address = models.TextField("Адреса", blank=True)
    telegram = models.URLField("Telegram", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    facebook = models.URLField("Facebook", blank=True)

    class Meta:
        verbose_name = "Налаштування сайту"
        verbose_name_plural = "Налаштування сайту"

    def __str__(self) -> str:
        return self.site_name

    @property
    def phone_href(self) -> str:
        digits = "".join(c for c in self.phone if c.isdigit())
        if digits.startswith("38"):
            return f"+{digits}"
        return f"+38{digits}" if digits else ""

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
