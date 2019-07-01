from django.db import models
from teacher.models import course,session

# Create your models here.

class student(models.Model):
    reg_number = models.CharField(max_length=10)
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.reg_number + ' - ' + self.name

class project(models.Model):
    project_title = models.CharField(max_length=300)
    group_name = models.CharField(max_length=100)
    course_code = models.ForeignKey('teacher.course', on_delete=models.CASCADE)
    session = models.ForeignKey('teacher.session', on_delete=models.CASCADE)