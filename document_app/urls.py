from django.urls import path
from document_app import views


urlpatterns = [
    path('lac/', views.lac, name= 'documentapp-lac'),
    path('reference/', views.reference, name= 'documentapp-reference'),
    path('appreciation/', views.appreciation, name= 'documentapp-appreciation'),
    path('register/', views.register, name= 'documentapp-register'),
]
