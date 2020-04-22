from django.urls import path
from .views import files_list
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('files/', files_list),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)