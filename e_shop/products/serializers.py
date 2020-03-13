from rest_framework import serializers
from .models import *

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['name','procent']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'parental_category']

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['name']

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']

class ProductSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    sale = SaleSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id','name','price','sale',
                  'manufacturer', 'category']

