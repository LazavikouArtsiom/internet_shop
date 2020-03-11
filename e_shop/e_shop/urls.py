from django.contrib import admin
from django.urls import path, include

apipatterns = [
path('', include('products.urls')),
path('', include('users.urls')),
]

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include((apipatterns, 'api'), namespace='api')),
)
