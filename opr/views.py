from django.shortcuts import render
from django.http import HttpResponse, request

# import models in views

from . models import Student,Teacher

# Create your views here.

# student= [
# {"first_name":'rio','last_name':'mario','age':23},
# {"first_name":'ram','last_name':'walke','age':20},
# ]

######################### get data in database #########################

# for all() method
def all_data(request):
     
     student_data = Student.objects.all()
     teacher_data = Teacher.objects.all()
     
     # for student in student_data:
     #      print(student.first_name,student.last_name,student.age)
     
     # print(student_data[1])
     
     # return HttpResponse("Hello, world!")
     
     return render(request,'all_data.html',{'student_data':student_data,'teacher_data':teacher_data})


# for get() method

def single_data(request):
     
     student = Student.objects.get(id=1)
     teacher = Teacher.objects.get(subject='marathi')
     print(student)
     
     return render(request,'single_data.html',{'user':student,'teacher':teacher})



# for filter() method

def filter_data(request):
     marathi_teachers = Teacher.objects.filter(subject='marathi')
     math_teachers = Teacher.objects.filter(subject='math')
     
     return render(request,'filter_data.html',{'marathi_teachers':marathi_teachers,'math_teachers':math_teachers})



######################### add data in database ( Create ) #########################

# direct add data
def add_data(request):
     
     Student.objects.create(roll_number=5,first_name='ram',last_name='mario',age=23)
     # print('data added')
     
     # Student.objects.create(roll_number=6,first_name='radha',last_name='dekate',age=22)
     
     # Teacher.objects.create(age=25,first_name='rahul',)
     
     # Student.objects.create(roll_number=8,first_name=None,age=30)
     return HttpResponse('data added')



# get data from templates and then add into database

def get_add_data(request):
     
     
     if request.method== "POST":
     

          roll_no = request.POST.get('roll')
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          age = request.POST.get('age') 
          Student.objects.create(roll_number=roll_no,first_name=first_name,last_name=last_name,age=age)
          
          return HttpResponse("data added")

          
     return render(request,'get_add_data.html')


# Todays Task-

# opr/student-add/ - add student into database
# opr/student-details/ - show students list

# opr/teacher-add/ - add teacher into database
# opr/teacher-details/ - show teachers list
