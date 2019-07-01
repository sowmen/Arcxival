from django.contrib import admin

# Register your models here.
from .models import student,project

admin.site.register(student)
admin.site.register(project)