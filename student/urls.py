

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.shome, name = 'shome'),
    path('media/<str:pk>/', views.delete_file, name = "delete_file"),
    path('newproject/', views.newproject, name = 'newproject'),
    path('newproject/ajax/load-sessions/', views.load_sessions, name='ajax_load_sessions'),
   # path('upload/', views.upload, name='upload'),
    path('<str:project_id>/', views.projectdetails, name='projectdetails'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)