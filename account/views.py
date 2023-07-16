from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.

def login_fun(request):
     # return HttpResponse("This is login page")
     return render(request,'login.html')


