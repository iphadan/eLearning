from django.shortcuts import render
from . import models
from django.contrib.auth.models import User
from django.contrib import messages
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
def registerStudent(request):
    if request.method == 'POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastNmae')
        username=request.POST.get('username')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        

        if password == repassword:
            user= None
            try:
                try :
                    count = User.objects.get(username=username)
                    if count:
                        messages.info(request,"username exist already")
                        raise Exception

                except Exception:
                    user=User.objects.create_user(username=username,email=email,password=password,firstName=firstName,lastName=lastName)
                    student=models.Student.objects.create(user=user,phone=phone,gender=gender)
                    messages.success(request,f"Dear {student.user.username}, welcome")
                    return render(request,"login.html")

            except Exception:
                messages.error(request,"something went wrong, try again later ")
                if not user  :
                    user.delete()
                return render(request,'registerStudent.html')

        else:
            messages.error(request,"your password does\'t match")
            return render(request,'registerStudent.html')



    ...
def registerCourse(request):
    ...
def handle404(request,exception):
    return render(request,'404.html')
