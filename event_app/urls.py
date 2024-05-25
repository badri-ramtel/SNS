from django.urls import path
from event_app import views


urlpatterns = [
    path('', views.events, name= 'eventapp-event'),
    path('viewevent/<str:pk>', views.viewEvent, name= 'eventapp-viewevent'),
]
