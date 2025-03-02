from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.viewsets import DocumentViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='documents')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include(router.urls)),
]
