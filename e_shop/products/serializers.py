from rest_framework import serializers
from .models import Sale, Category, Attribute, Manufacturer, Product
import django_filters

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['name', 'percent']

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
    manufacturer = ManufacturerSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    sales = SaleSerializer(many=True, read_only=True)
    attributes = AttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['slug', 'name', 'price', 'sales',
                  'manufacturer', 'category', 'attributes',
                  'is_new', 'is_recomended']
        
        lookup_field = 'slug'        

class ProductFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
    class Meta:
        model = Product
        fields = {'name': ['exact', 'icontains'],
                  'price': ['exact', 'gte', 'lte'],
                 }
        
