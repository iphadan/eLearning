from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("admin working")
def adminPost(request):
    return render(request,"adminPost.html")