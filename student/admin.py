from django.contrib import admin

# Register your models here.
from .models import student,project, file

admin.site.register(student)
admin.site.register(project)
admin.site.register(file)