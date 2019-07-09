from django.db import models
from teacher.models import course,session
import os
from customuser.models import User

# Create your models here.

class student(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=10, primary_key=True, default='000')
    name = models.CharField(max_length=250)
    # email = models.EmailField()

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
    project_id = models.CharField(max_length=100, primary_key=True, default='pid')
    group_name = models.CharField(max_length=100)
    course_code = models.ForeignKey(course, on_delete=models.SET_DEFAULT, default=111, verbose_name='course')
    session = models.ForeignKey(session, on_delete=models.SET_DEFAULT, default=222, verbose_name='session')
    # group_name = models.ForeignKey(group, on_delete=models.CASCADE)
    member1_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member1', default='mem1')
    member2_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member2', default='mem2')
    member3_reg = models.ForeignKey(student, on_delete=models.CASCADE, related_name='member3', default='mem3')

    def __str__(self):
        return self.project_title

class file(models.Model):
    file_name=models.CharField(max_length=100)
    project_id=models.ForeignKey(project, on_delete=models.CASCADE)
    file_size=models.CharField(max_length=255)
    def get_file_path(self, filename):
        return os.path.join(self.project_id.course_code.course_code, self.project_id.project_id, filename)

    file_content = models.FileField(upload_to='', null=True)

    def __str__(self):
        return "(" + self.project_id.project_id + ")" + self.file_name

