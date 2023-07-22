from django.db import models

# Create your models here.

class Student(models.Model):
     
     roll_number = models.IntegerField()
     first_name = models.CharField(max_length=255,default="unknown",null=True,blank=True)
     last_name = models.CharField(max_length=255,null=True,blank=True)
     age = models.IntegerField(default=0)
     
     
     def __str__(self):
          return f'{self.first_name}  {self.last_name}'
     
     
     
class Teacher(models.Model):
     first_name = models.CharField(max_length=55,default='unknown')
     last_name = models.CharField(max_length=55,default='unknown')
     subject = models.CharField(max_length=55,default='marathi')
     age = models.IntegerField(default=19)
     
     
     def __str__(self):
          return self.first_name + ' ' + self.last_name
     