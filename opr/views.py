from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User

# import models in views

from . models import *

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
          
          # print(request.POST)
          
          roll_no = request.POST.get('roll')
          first_name = request.POST.get('first_name')
          last_name = request.POST.get('last_name')
          age = request.POST.get('age') 
          Student.objects.create(roll_number=roll_no,first_name=first_name,last_name=last_name,age=age)
          
          # return HttpResponse("data added")
          return redirect('about_us') # to go on different or same (page or route)

          
     return render(request,'get_add_data.html')


# Todays Task-

# opr/student-add/ - add student into database
# opr/student-details/ - show students list

# opr/teacher-add/ - add teacher into database
# opr/teacher-details/ - show teachers list



def about_us(request):
     
     a = Student.objects.all()
     # print('student data',a)
     
     # return HttpResponse('this working')
     return render(request,'about_us.html',{'students':a})




# def my_study(request):
     
     
#      if request.method == "POST":
#           print(request.POST)
          
#           subject = request.POST['subject']
#           time = request.POST['time']
          

#           try:
#                if request.POST['is_complete'] == "True":
#                     is_completed = True
               
#                else:
#                     is_completed = False
               
#           except:
#                is_completed= False
               
               
#           Study.objects.create(subject=subject,time=time,is_complete=is_completed)
          
#           return redirect('my_study_data')
     
#      else:
#           study_details= Study.objects.all()
#           print(study_details)
     
#           return render(request,'my_study_form.html',{'study_details':study_details})




# adding data into models with ForeignKey
def my_study(request):
     
     # for sub in subjects:
     #      print(sub.id , sub.name)
     # Study.objects.create(subject_id=1,time=2.5,is_complete=True)
     
     if request.method == "POST":
     
          subject = request.POST['subject']
          time = request.POST['time']
          
          try:
               if request.POST['is_complete'] == "True":
                    is_complete = True
               else:
                    is_complete= False  
          except:
               is_complete = False
               
          Study.objects.create(subject_id= subject,time=time,is_complete=is_complete )
          
          return redirect('my_study_data')
     
     else:
          subjects= Subject.objects.all()
          study_details= Study.objects.all()
          return render(request,'my_study_form.html',{'subjects':subjects,'study_details':study_details})
     




def signup(request):
     
     # return HttpResponse('this is working fine')
     
     if request.method == "POST":
          
          # print(request.POST)
          
          username  =   request.POST["username"]
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          email = request.POST['email']
          password = request.POST['password']
          
          mobile_number = request.POST['mobile_number']
          age = request.POST['age']
          
          user_data = User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
          print(user_data,user_data.username ,user_data.id)
          
          UserDetail.objects.create(user_id = user_data.id,mobile_number=mobile_number,age=age)
          
          return HttpResponse('account created')

     return render(request,'signup.html')


def remove_student_data(request):
     
     student_data = Student.objects.all()
     
     if request.method == "POST":
          
          id = request.POST.get('id')
          
          try:
               student = Student.objects.get(id=id)
               student.delete()
               return HttpResponse(f'data with id {id} was deleted')
               
          except:
               return HttpResponse(f"data with id {id} not found")

     return render(request,'remove_student_data.html',{'student_data': student_data})



def student_all_data(request):
     students = Student.objects.all()
     return render(request,'student_all_data.html',{'student_data':students})


def delete_student(request,id):
     
     try:
          student = Student.objects.get(id=id)
          student.delete()
          return HttpResponse(f'data delete with id {id}')
     
     except:
          return HttpResponse(f'data not found with id {id}')
     



def teacher_data(request):
     teachers  = Teacher.objects.all()
     return render(request,'teacher_data.html',{'teachers':teachers})

def teacher_data_delete(request,id):
     
     try :
          teacher =Teacher.objects.get(id=id)
          teacher.delete()
          return HttpResponse(f"data delete with id {id}")
     except:
          return HttpResponse(f"data not found with id {id}")
     
     
def teacher_single_data(request,id):
     try:
          teacher = Teacher.objects.get(id=id)
          return render(request,"teacher_single_data.html",{"teacher":teacher})
     except:
          return HttpResponse("data not found")
     


# Update the data

# step 1 - show all data to user
# step 2- get the id of the particular row which is clicked by user
# step 3 - find the data in database table with particular id 
# step 4 - send data to fond end and show this data in input box in form
# step 5 - if user submit the form update this data in database


def teachers_data_list(request):
     
     
     teachers = Teacher.objects.all()
     return render(request,'update_data/teachers_data_list.html',{'teachers':teachers})



def update_teacher_data(request,id):
     
     # print(request.method)
     
     if request.method== "POST":
          first_name   = request.POST['first_name']
          last_name = request.POST['last_name']
          subject = request.POST['subject']
          age = request.POST['age']
          
          try:
               teacher = Teacher.objects.get(id= id)
               # print('data before update')
               # print(teacher.first_name,teacher.last_name,teacher.subject,teacher.age)
               
               teacher.first_name = first_name
               teacher.last_name = last_name
               teacher.subject = subject
               teacher.age = age
               teacher.save()
               
               
               # print('data after update')
               # print(teacher.first_name,teacher.last_name,teacher.subject,teacher.age)
               return redirect('teachers_data_list')
               
          except:
               return HttpResponse('data not update')
          
     else:
          try:
               teacher = Teacher.objects.get(id=id)
               return render(request,'update_data/update_teacher_data.html',{'teacher':teacher})
          
          except:
               return HttpResponse('data not found')
          
          