from django.urls import path
from rest_framework.routers import DefaultRouter

from file.apps import FileConfig
from file.views import FileDestroyAPIView, FileUpdateAPIView, FileRetrieveAPIView, FileListAPIView, \
    FileUploadAPIView

app_name = FileConfig.name

router = DefaultRouter()

urlpatterns = [
    path("file/", FileListAPIView.as_view(), name="file_list"),
    path("file/detail/<int:pk>", FileRetrieveAPIView.as_view(), name="file_detail"),
    path("file/update/<int:pk>", FileUpdateAPIView.as_view(), name="file_update"),
    path("file/delete/<int:pk>", FileDestroyAPIView.as_view(), name="file_delete"),

    path("file/upload", FileUploadAPIView.as_view(), name="file_delete")

] + router.urls