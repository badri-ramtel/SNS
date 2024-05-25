from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='mainapp-home'),
    path('slider', views.slider, name='mainapp-slider'),
    path('president/', views.president, name='mainapp-president'),
    path('subscribe/', views.subscribe, name='subscribe'),
    # path('advertise/', views.ads, name='advertise')
]