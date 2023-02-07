from django.urls import include, path
from . import views



urlpatterns = [
    path('GetHashURL/<path:url>', views.get_hash),# Хеш по ссылке
    path('GetClicksNumShortURL/<str:hash_url>/', views.get_num_click_url), # Колчество всех кликов для ссылки
    path('GetClicksStat/<str:hash_url>/', views.get_num_click_url_stats) # Колчество всех кликов для ссылки с датой
]
