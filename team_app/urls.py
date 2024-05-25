from django.urls import path
from team_app import views


urlpatterns = [
    path('', views.team, name='teamapp-team'),
    path('viewcommittee/<str:pk>/', views.viewCommittee, name='teamapp-viewcommittee'),
]
