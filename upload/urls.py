from django.urls import path
from . import views

urlpatterns = [
    path("", views.file_upload, name="upload"),
    path("success", views.upload_success, name="success")
]
