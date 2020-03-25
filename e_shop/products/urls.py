from django.contrib import admin
from django.urls import path, include
from .views import ProductsBySales, ProductList, ProductDetail
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('special_offers/', ProductsBySales.as_view(), name='products_by_sales'),
    path('<str:category_slug>/', ProductList.as_view(), name='product_list_by_category'),
    path('<str:category_slug>/<str:slug>/', ProductDetail.as_view(), name='product_detail_by_category'),
]