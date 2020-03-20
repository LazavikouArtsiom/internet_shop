from rest_framework import serializers
from .models import Sale, Category, Attribute, Manufacturer, Product

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ['name','percent']

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
    category = CategorySerializer(read_only=True)
    sale = SaleSerializer(many=True, read_only=True)
    attributes = AttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id','name', 'price','sale',
                  'manufacturer', 'category', 'attributes']
