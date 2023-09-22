from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


# Create your models here.
class File(models.Model):
    file = models.FileField(verbose_name="Файл")
    uploaded_at = models.DateTimeField(default=timezone.now, verbose_name="Когда был загружен файл")
    processed = models.BooleanField(default=False, verbose_name="Обработан ли файл")
    type_file = models.CharField(**NULLABLE, max_length=50, verbose_name="Тип файла",)

    def __str__(self):
        return f"{self.file} {self.uploaded_at} {self.processed}"

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
