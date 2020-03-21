from django.contrib import admin
from django.urls import path, include
from .views import SalesViewSet, ProductList, ProductDetail
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register(r'special_offers', SalesViewSet)

urlpatterns = [
    #path(r'', include(router.urls)),
    path('<str:category_slug>/', ProductList.as_view(), name='product_list_by_category'),
    path('<str:category_slug>/<str:slug>/', ProductDetail.as_view(), name='product_detail_by_category'),

    #path('<int:id>/<str:slug>/', product_detail, name='product_detail' )
]