from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='mainapp-home'),
    path('president/', views.president, name='mainapp-president'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('advertise/<str:pk>', views.advertise, name='advertise')
]