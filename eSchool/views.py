from django.shortcuts import render ,redirect
from . import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , logout ,authenticate
# Create your views here.


def home(request):
    students = models.Student.objects.all()
    courses=models.Course.objects.all()


    context={
        "students":students,
        "courses":courses
    }
    

    return render(request,'index.html',context=context)
def landing(request):
    students = models.Student.objects.all()
    courses=models.Course.objects.all()


    context={
        "students":students,
        "courses":courses
    }
    

    return render(request,'home.html',context=context)
def about(request):

    return render(request,'about.html')

def courseDetail(request,id):
    try:
        course=models.Course.objects.get(pk=id)
        context={
            "course":course
        }
        return render(request,'course-details.html',context)
  
    except:
        messages.info(request,"Course that Does not Exist")
        return render(request,"home")

    return render(request,'courses.html')
def course(request):
    courses=models.Course.objects.all().order_by('-courseStudentsCount')
    context={
        'courses':courses
    }
    return render(request,'courses.html',context)

def learing_path(request):

    return render(request,'index.html')

def events(request):
    return render(request,'events.html')

def pricing(request):

    return render(request,'pricing.html')

def contact(request):

    return render(request,'contact.html')

def learning(request,id):
    if request.user.is_authenticated:
        print(request.user.username)
        try:
            course= models.Course.objects.get(id=id)
            context={
                'course':course
            }
            return render(request,"learning.html",context)
        except:
            messages.error(request,"Course Not Found!")
            return render(request,"404.html")
    else :
        messages.error(request,'Login Before Accessing a Course')
        return render(request,'login.html')
def registerStudent(request):
    if request.method == 'POST':
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        username=request.POST.get('username')
        photo=request.FILES.get('photo')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        repassword=request.POST.get('repassword')
        

        if password == repassword:
            try:

                user = User.objects.create(
                    username=username,
                    email=email,
                    password=password,
                    first_name=firstName,
                    last_name=lastName
                )                
                user.save()
                try:
                    student=models.Student.objects.create(user=user,phone=phone,gender=gender,photo=photo)
                    messages.success(request,f"Dear User {student.user.username}, welcome !")
                    return render(request,"login.html")
                except:
                    user.delete()
                    messages.error(request,"something went wrong, try again later ")
                    return render(request,'registration.html')

            except Exception:
                
                messages.error(request,f"User with username {username} exist already! ")
                return render(request,'registration.html')

        else:
            messages.error(request,"your password does\'t match")
            return render(request,'registration.html')
    return render(request,'registration.html')




  

def registerCourse(request):
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        category=request.POST.get('category')
        price=request.POST.get('price')
        coursePhoto=request.FILES.get('coursePhoto')
        courseTeacher=request.POST.get('courseTeacher')
        teacherDescription=request.POST.get('teacherDescription')
        teacherPhoto=request.FILES.get('teacherPhoto')
        try:
            course=models.Course.objects.create(title=title,description=description,category = category,coursePhoto = coursePhoto,courseTeacher = courseTeacher,teacherDescription=teacherDescription,teacherPhoto = teacherPhoto,price=price)
            messages.success(request,"Course Successfully Added!")
            return render(request,'index.html')
        except Exception:
            messages.success(request,"Something went wrong, Please try again!")
            return render(request,'registerCourse.html')
    else:
        return render(request,'registerCourse.html')

    


    
def handle404(request,exception):
    return render(request,'404.html')

def loginUser(request):
    if request.method == 'POST':
        #next_url = "/eLearning/learning/1"
        username = request.POST.get('username')
        password = request.POST.get('password')        
        user = authenticate(username=username, password=password)
        next_url = request.GET.get('next')
        if user:
            login(request,user)
            if next_url and not next_url == "/eLearning/logout/":
                return redirect(next_url)
            return redirect('home')
        else:
            messages.error(request,'username or password is incorrect')
            return render(request,'login.html')
    elif request.user.is_authenticated :
        return redirect('home')
    return render(request,'login.html')



def logoutUser(request):
    if request.user.is_authenticated :
        logout(request)
        messages.info(request,'Logged Out')
        return render(request,'login.html')
    else:
        return render(request,'login.html')
def sendEmail(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        message=request.POST.get('message')

        try:
            models.Contact.objects.create(name=name,email=email,subject=subject,message=message)
            messages.success(request,"Message sent")
            return render(request,'contact.html')
        except:
            messages.error(request,"Message not sent, try again later ")
            return render(request,'contact.html')
    else:
        return render(request,'contact.html')

