from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('shortener_page.urls')),
    path('API/', include('shortener_api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
