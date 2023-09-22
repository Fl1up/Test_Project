from django.contrib import admin

from file.models import File


# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_at", "processed")   # отображение на дисплее
    # list_filter =    # фильтр
    # search_fields =   # поля поиска
