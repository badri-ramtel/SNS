from django.urls import path
from about_app import views

urlpatterns = [
    path('about/', views.aboutUs, name='aboutapp-about'),
    path('vision/', views.vision, name='aboutapp-vision'),
    path('terms/', views.terms, name='aboutapp-terms'),
]