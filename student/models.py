from django.db import models

# Create your models here.

class student(models.Model):
        reg_number = models.CharField(max_length=10)
        name = models.CharField(max_length=250)
        email = models.EmailField()

        def __str__(self):
            return self.reg_number + ' ' + self.name