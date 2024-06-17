from django.shortcuts import render

# Create your views here.


def home(request):
    

    return render(request,'index.html')

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
