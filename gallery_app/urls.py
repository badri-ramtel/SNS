from django.urls import path
from gallery_app import views

urlpatterns = [
    path('', views.gallery, name='galleryapp-gallery'),
    path('photo/<str:pk>', views.viewPhoto, name='galleryapp-photo'),
]