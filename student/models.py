from django.db import models

# Create your models here.
class Student(models.Model):
    Fname  = models.CharField(max_length=35)
    Lname  = models.CharField(max_length=35)
    Age = models.CharField(max_length=3)
    Email = models.CharField(max_length=100)
    Enr = models.CharField(max_length=25)
    Uni = models.CharField(max_length=100)

    def str(self):
        return self.Fname