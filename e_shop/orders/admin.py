from django.contrib import admin
from .models import Cart

admin.site.unregister(Cart)
admin.site.register(Cart)