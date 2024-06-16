from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.products import views

router = DefaultRouter()

router.register('categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
