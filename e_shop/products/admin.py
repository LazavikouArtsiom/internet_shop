from django.contrib import admin
from .models import (Product, Sale, Category,
                    Attribute, ProductAttribute, Manufacturer,
                    CartItems)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',\
                    'stock', 'available', 'created_at'\
                    ,'updated_at', 'new', 'recomended']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 30
    ordering = ['price', 'name']
    search_fields = ['name']
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_editable = ['slug',]
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

admin.site.register(Sale)
admin.site.register(Attribute)
admin.site.register(ProductAttribute)
admin.site.register(Manufacturer)
admin.site.register(CartItems)

