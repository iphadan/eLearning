from django.shortcuts import render
from . import models
# Create your views here.


def home(request):
    students = models.Student.objects.all()
    courses=models.Course.objects.all()


    context={
        "students":students,
        "courses":courses
    }
    

    return render(request,'index.html',context=context)

def about(request):

    return render(request,'courses.html')

def course(request):

    return render(request,'courses.html')

def learing_path(request):

    return render(request,'index.html')

def eventes(request):

    return render(request,'index.html')

def priceing(request):

    return render(request,'index.html')

def contact(request):

    return render(request,'index.html')

def GetStart(request):

    return render(request,'index.html')
def handle404(request,exception):
    return render(request,'404.html')
