from django.db import models

# Create your models here.
class teacher(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    teacher_code = models.CharField(max_length=5)

    def __str__(self):
        return self.teacher_code + ' - ' + self.name

class course(models.Model):
    course_code = models.CharField(max_length=10)
    course_title = models.CharField(max_length=100)
    course_credit = models.FloatField()

    def __str__(self):
        return self.course_code

class session(models.Model):
    course_code = models.ForeignKey('course', on_delete=models.CASCADE)
    batch = models.CharField(max_length=4)
    date = models.DateField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.batch + '-' + self.course_code.course_code