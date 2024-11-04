from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf.urls.static import static
from core import settings
=======
from django.conf import settings
from django.conf.urls.static import static
>>>>>>> fee56e2cb06e326d3c88430ce515af65c7588a97

urlpatterns = [
    path('', include('produto.urls')),
    path('', include('usuario.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
>>>>>>> fee56e2cb06e326d3c88430ce515af65c7588a97
