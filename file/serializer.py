from django.core.files.storage import FileSystemStorage

from rest_framework import serializers

from file.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file', 'type_file']
        template_name = 'file_upload.html'


    def form_valid(self, form):
        file = self.request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        type_file = '.' + filename.split('.')[-1]  # определение расширения файла
        form.instance.type_file = type_file
        return super().form_valid(form)