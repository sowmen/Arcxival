

from django.urls import path
from . import views

urlpatterns = [

    path('', views.shome, name = 'shome'),
    path('newproject/', views.newproject, name = 'newproject'),
    path('newproject/ajax/load-sessions/', views.load_sessions, name='ajax_load_sessions'),
    path('<str:project_id>/', views.projectdetails, name='projectdetails'),
]