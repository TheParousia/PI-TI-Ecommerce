from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from produto import views

urlpatterns = [
    path('', views.frontend, name="frontend"),  # Mantendo apenas a view 'frontend'
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
