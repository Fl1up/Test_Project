from rest_framework import permissions
from django.core.files.storage import default_storage
from PIL import Image
import json


class IsImage(permissions.BasePermission):
    """Кастомный класс для преобразования картинок"""
    def image(self, image):
        img = Image.open(image)

        if img.width > 800:
            img = img.resize((800, int(800 / img.width * img.height)))

        with default_storage.open('my_image.jpg', 'wb') as f:
            img.save(f, 'JPEG')


class IsText(permissions.BasePermission):
    """Кастомный класс для преобразования текста"""
    def text(self, text):
        dict = {}

        with open(text, "r") as f:
            content = f.readlines()
            for i in content:
                key, value = i.strip().split(': ')
                dict[key] = value

        with open('myfile.json', 'w') as f:
            json.dump(dict, f)


