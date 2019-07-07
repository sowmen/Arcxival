from django.db import models
from customuser.models import user_type, User
# Create your models here.


class teacher(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    # email = models.EmailField()
    teacher_code = models.CharField(max_length=5, primary_key=True)

    def __str__(self):
        return self.teacher_code + ' - ' + self.name


class course(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    course_title = models.CharField(max_length=100)
    course_credit = models.FloatField()
    teacher_code = models.ForeignKey(teacher, on_delete=models.SET_DEFAULT, default='NoTea')

    def __str__(self):
        return self.course_code


class session(models.Model):
    course_code = models.ForeignKey(course, on_delete=models.SET_DEFAULT, default='def_cor')
    batch = models.CharField(max_length=4)
    session_id = models.CharField(max_length=100, primary_key=True, default='default-session')
    date = models.DateField(auto_now=False,auto_now_add=False)
    running = models.BooleanField(default=True)
    teacher_code = models.ForeignKey(teacher, on_delete=models.CASCADE, default='notea')

    def __str__(self):
        return self.batch + '-' + self.course_code.course_code