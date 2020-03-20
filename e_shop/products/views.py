from django.shortcuts import render
from .models import Sale, Product
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.generics import ListAPIView
from .serializers import SaleSerializer, ProductSerializer

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

#class ProductList(ListAPIView):
#    serializer_class = ProductSerializer(queryset, many=True)

#    def get_queryset(self, **kwargs):
#        queryset = Product.objects.all()
#        category = self.kwargs['category_slug']
#        if category is not None:
#            queryset = Product.objects.filter(category__slug=category)
#        return queryset

class ProductList(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.kwargs['category_slug']
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        return queryset
