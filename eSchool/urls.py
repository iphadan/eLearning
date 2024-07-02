from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home"),
    path('course/',course,name="course"),

    path('login/',loginUser,name="login"),
    path('logout/',logoutUser,name="logout"),

    path('register/',registerStudent,name="registerStudent"),

    path('course/<int:id>',courseDetail,name="courseDetail"),
    path('learning/<int:id>',learning,name="learning"),
    path('events/',events,name="events"),

    path('pricing/',priceing,name="pricing"),
    



]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)