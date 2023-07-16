from django.db import models

# Create your models here.

class Student(models.Model):
     
     roll_number = models.IntegerField()
     first_name = models.CharField(max_length=255,default="unknown",null=True)
     last_name = models.CharField(max_length=255)
     age = models.IntegerField()
     blood_group = models.CharField(max_length=3,null=True)
     
     def __str__(self):
          return  f"{self.roll_number} : {self.first_name}"
