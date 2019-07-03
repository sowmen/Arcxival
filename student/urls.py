

from django.urls import path
from . import views

urlpatterns = [

    path('', views.shome, name = 'shome'),
    path('newproject/', views.newproject, name = 'newproject'),

]