from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home-page"),
    path('course/',course,name="course")
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)