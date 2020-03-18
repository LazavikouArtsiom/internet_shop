from django.contrib import admin
from django.urls import path, include
from .views import SalesViewSet, ProductListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'special_offers', SalesViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
    path('<str:category_slug>/', ProductListAPIView.as_view(), name='product_list_by_category'),
    #path('<int:id>/<str:slug>/', product_detail, name='product_detail' )
]