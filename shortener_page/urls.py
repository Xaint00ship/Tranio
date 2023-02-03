from django.urls import path
from shortener_page import views



urlpatterns = [
    path('home/', views.render_home_page),
    path('<str:hash_url>/', views.redirect_real_url),
]
