from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(ProductAttribute)
admin.site.register(Manufacturer)
admin.site.register(Cart)
