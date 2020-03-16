from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

apipatterns = [

]

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include((apipatterns, 'api'), namespace='api')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns