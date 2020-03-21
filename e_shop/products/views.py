from django.shortcuts import render
from django.http import Http404
from .models import Sale, Product
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import SaleSerializer, ProductSerializer
from django.db.models import Q

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = 'pk'

    def get_permissions(self):

        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'list':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve':
            permission_classes = [AllowAny]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser] 
        return [permission() for permission in permission_classes]

class ProductList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category_slug']
        if category is not None:
            return Product.objects.select_related('category').filter(category__slug=category).order_by('-price')
        raise Http404

class ProductDetail(RetrieveAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'slug' 

    def get_queryset(self):
        category = self.kwargs['category_slug']
        product = self.kwargs['slug']
        if product and category:
            return Product.objects.filter(slug=product, category__slug=category)
        raise Http404
