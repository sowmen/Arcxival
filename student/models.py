from django.db import models
from django.contrib.postgres.fields import ArrayField
from teacher.models import course,session

# Create your models here.

class student(models.Model):
    reg_number = models.CharField(max_length=10, primary_key=True, default='000')
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.reg_number + ' - ' + self.name

# class group(models.Model):
#     group_id = models.AutoField(primary_key=True)
#     group_name = models.CharField(max_length=100)
#     member1_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member1')
#     member2_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member2')
#     member3_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member3')
#     member4_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member4')

class project(models.Model):
    project_title = models.CharField(max_length=300)
    group_name = models.CharField(max_length=100)
    course_code = models.ForeignKey(course, on_delete=models.SET_DEFAULT, default=111, verbose_name='course')
    session = models.ForeignKey(session, on_delete=models.SET_DEFAULT, default=222, verbose_name='session')
    # group_name = models.ForeignKey(group, on_delete=models.CASCADE)
    member1_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member1', default='mem1')
    member2_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member2', default='mem2')
    member3_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member3', default='mem3')

    def __str__(self):
        return self.project_title