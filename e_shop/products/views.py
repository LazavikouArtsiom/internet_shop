from django.shortcuts import render
from django.http import Http404
from .models import Sale, Product
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SaleSerializer, ProductSerializer, ProductFilter
from django.db.models import Q
 

class ProductsBySales(ListAPIView):
    serializer_class = ProductSerializer
    filterset_fields = ['category']

    def get_queryset(self):
        return (Product.
                objects.
                prefetch_related('sales', 'attributes').
                select_related('category', 'manufacturer',).
                exclude(sales=None)
                )


class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get_queryset(self):
        category = self.kwargs['category_slug']
        if category is not None:
            return (Product.
                    objects.
                    prefetch_related('category', 'attributes').
                    filter(category__slug=category)
                    )   
        raise Http404

class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'slug' 

    def get_queryset(self):
        category = self.kwargs['category_slug']
        product = self.kwargs['slug']
        if product and category:
            return (Product.
                    objects.
                    select_related('category').
                    prefetch_related('attributes').
                    filter(category__slug=category))
        raise Http404
