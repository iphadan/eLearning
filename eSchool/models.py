from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    coursePhoto=models.ImageField(upload_to='upload/coursePhoto',blank=True,null=True,default='upload/defaultPhoto/defaultUserImg.jpeg')
    courseTeacher=models.CharField(max_length=100)
    teacherDescription=models.TextField
    teacherPhoto=models.ImageField(upload_to='upload/teacherPhoto',blank=True,null=True,default='upload/defaultPhoto/defaultUserImg.jpeg')
    price=models.FloatField(default=0.0,null=True,blank=True)

    def __str__(self) -> str:
        return  self.title

class AdminUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.first_name + " " + self.user.last_name
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=14,default='0900000000')
    gender=models.CharField(max_length=8,default="Male")
    #teacher might be another user of the system if so then we will make its own model to save all details including certifications
    photo=models.ImageField(upload_to='upload/studentPhoto',blank=True,null=True,default='upload/defaultPhoto/defaultUserImg.jpeg')
    courses=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self) -> str:
        return self.firstName + " " + self.lastName