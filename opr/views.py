from django.shortcuts import render
from django.http import HttpResponse, request

# import models in views

from . models import Student,Teacher

# Create your views here.

# student= [
# {"first_name":'rio','last_name':'mario','age':23},
# {"first_name":'ram','last_name':'walke','age':20},
# ]




def get_data(request):
     
     student_data = Student.objects.all()
     teacher_data = Teacher.objects.all()
     
     # for student in student_data:
     #      print(student.first_name,student.last_name,student.age)
     
     # print(student_data[1])
     
     # return HttpResponse("Hello, world!")
     
     return render(request,'student_data.html',{'student_data':student_data,'teacher_data':teacher_data})