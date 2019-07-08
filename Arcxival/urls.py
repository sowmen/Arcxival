"""Arcxival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing, name='landing'),
    path('login/', views.home, name='home'),
    # path('accounts/', include('allauth.urls')),
    # path('accounts/signup/', views.signup , name='signup'),
    # path('accounts/signup/student/', views.signup_student, name='signup_student'),
    # path('accounts/signup/teacher/', views.signup_teacher, name='signup_teacher'),
    path('teacherhome/', include('teacher.urls'), name='thome'),
    path('studenthome/', include('student.urls'), name='shome'),
    #path('<int:pk>/', views.delete_file, name = "delete_file"),
    path('logout/', views.logout_view, name='logout'),
    path('archive_Sessions/', views.archive_redirect_noid, name='noid'),
    path('archive_Projects/', views.archive_redirect_noid, name='noid'),
    path('archive_Courses/', views.archive_courses, name='archive_courses'),
    path('archive_Sessions/<str:pk>', views.archive_Sessions, name='archive_Sessions'),
    path('<str: pk>/', views.archive_Sessions, name='archive_Sessions'),
    path('archive_Projects/<str:pk>', views.archive_Projects, name='archive_Projects'),
    path('archive_Projects/<str:session_id>/<str:project_id>', views.projectdetails, name='projectdetails'),

    #path('media/<int:pk>/', views.delete_file, name="delete_file"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

