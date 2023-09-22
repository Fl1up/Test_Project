from django.core.files.storage import FileSystemStorage
from rest_framework import generics, status
from rest_framework.response import Response
from file.tasks import file_task
from file.models import File
from file.paginators import FilePaginator
from file.serializer import FileSerializer

# Create your views here.

class FileListAPIView(generics.ListAPIView):
    """Factors List"""
    serializer_class = FileSerializer
    queryset = File.objects.all()
    pagination_class = FilePaginator


class FileRetrieveAPIView(generics.RetrieveAPIView):
    """Factors Retrive"""
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)


class FileUpdateAPIView(generics.UpdateAPIView):
    """Factors Updaate"""
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def put(self, request, *args, **kwargs):
        file = self.get_object()
        serializer = self.get_serializer(file, data=request.data, parrtial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Файл отредактирован"}, status=status.HTTP_200_OK)


class FileDestroyAPIView(generics.DestroyAPIView):
    """Factors Delete"""
    queryset = File.objects.all()

    def delete(self, request, *args, **kwargs):
        file = self.get_object()
        self.perform_destroy(file)
        return Response({'message': 'Файл успешно удаленна'}, status=status.HTTP_200_OK)


class FileUploadAPIView(generics.CreateAPIView):
    """File load"""
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            file_task.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


