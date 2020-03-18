from django.contrib import admin
from django.urls import path, include
from .views import SalesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'special_offers', SalesViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]