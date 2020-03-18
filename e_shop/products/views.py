from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Sale, Product, Category
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from .serializers import SaleSerializer
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


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

class ProductListAPIView(ListAPIView):

    def get(self, request, category_slug=None):
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = get_list_or_404(Product, category=category)
        return products
