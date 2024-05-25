from django.urls import path
from contact_app import views


urlpatterns = [
    path('contact/', views.contact, name='contactapp-contact'),
    path('member/', views.member, name='contactapp-member'),
    path('vacancy/', views.vacancy, name='contactapp-vacancy'),
    path('view_vacancy/<str:pk>', views.view_vacancy, name='contactapp-view'),
    path('donate/', views.donate, name='contactapp-donate'),
]