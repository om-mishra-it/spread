from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UploadedFileViewSet

router = DefaultRouter()
router.register(r'files', UploadedFileViewSet, basename='uploadedfile')

urlpatterns = [
    path('api/', include(router.urls)),
]
