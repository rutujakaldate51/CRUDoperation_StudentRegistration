from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name