from django.db import models

from django.contrib.auth.models import User

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
     
     
     
     

# class Study(models.Model):
     
#      date= models.DateField(auto_now=True)
#      subject = models.CharField(max_length=55,default='Unknown')
#      time = models.DecimalField(max_digits=5,decimal_places=2)
#      is_complete = models.BooleanField(default=True)
     
     
#      def __str__(self):
#           return f'{self.subject}  - {self.date}'
     
     
     
# connecting tables with ForeignKey(One To Many)


class Subject(models.Model):
     name = models.CharField(max_length=30,unique=True)
     desc= models.TextField(null=True,blank=True, default='desc not added')
     
     def __str__(self):
          return self.name



class Study(models.Model):
     date= models.DateField(auto_now=True)
     subject = models.ForeignKey(Subject,on_delete = models.CASCADE,null=True,blank=True) # connect with Subject Model with oneToMany filed
     time = models.DecimalField(max_digits=5,decimal_places=2)
     is_complete = models.BooleanField(default=True)
          
     
     def __str__(self):
          return f'{self.subject}  - {self.date}'




#  One to One

# User - username , password, first_name , last_name 



class UserDetail(models.Model):
     user= models.OneToOneField(User,on_delete=models.CASCADE)
     mobile_number= models.BigIntegerField()
     age = models.IntegerField()
     
     def __str__(self):
          return f'{self.mobile_number}  {self.age}'
     
     

# Task 

# create book project 
# create a book model - fields(6) - book name , book author , no of pages, publish date, author email id,price
# page 1 - All book data in table( sr , book name ,price) , action (view, delete, update)
# page 2 - Add Book
# page 3 - show all details of particular book 
# page 4 - update particular book details 

