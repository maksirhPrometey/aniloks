from django.db import models


class Photo(models.Model):
    image = models.ImageField("Фото", upload_to="gallery/photos/")
    alt = models.CharField("Alt текст", max_length=200, blank=True)
    caption = models.CharField("Підпис", max_length=255, blank=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    is_active = models.BooleanField("Активне", default=True)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографії"
        ordering = ["order"]

    def __str__(self) -> str:
        return self.caption or f"Фото {self.pk}"


class Video(models.Model):
    title = models.CharField("Назва", max_length=255)
    embed_url = models.URLField("Посилання (YouTube embed)", blank=True)
    video_file = models.FileField("Відео файл", upload_to="gallery/videos/", blank=True, null=True)
    poster = models.ImageField("Постер", upload_to="gallery/posters/", blank=True, null=True)
    order = models.PositiveSmallIntegerField("Порядок", default=0)
    is_active = models.BooleanField("Активне", default=True)

    class Meta:
        verbose_name = "Відео"
        verbose_name_plural = "Відео"
        ordering = ["order"]

    def __str__(self) -> str:
        return self.title
