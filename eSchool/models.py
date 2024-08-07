from django.db import models
from django.contrib.auth.models import User
#functions
def video_directory_path(instance, filename):
    # file will be uploaded to 'upload/videos/<section_title>/<filename>'
    return 'upload/videos/{0}/{1}'.format(instance.section.course.title+"/"+instance.section.title, filename)

def file_directory_path(instance, filename):
    # file will be uploaded to 'upload/files/<video_title>/<filename>'
    return 'upload/files/{0}/{1}'.format(instance.video.section.course.title+"/"+instance.video.title, filename)
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField
    def __str__(self) -> str:
         return self.name

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(default="")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    coursePhoto=models.ImageField(upload_to='upload/coursePhoto',blank=True,null=True,default='upload/defaultPhoto/defaultUserImg.jpeg')
    courseTeacher=models.CharField(max_length=100)
    courseStudentsCount=models.PositiveIntegerField(default=0)
    #teacher might be another user of the system if so then we will make its own model to save all details including certifications
    teacherDescription=models.TextField(default="")
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
    phone=models.CharField(max_length=14,default='0900000000')
    gender=models.CharField(max_length=8,default="Male")
    photo=models.ImageField(upload_to='upload/studentPhoto',blank=True,null=True,default='upload/defaultPhoto/defaultUserImg.jpeg')
    courses=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self) -> str:
        return self.user.first_name + " " + self.user.last_name
class Payment(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.student.user.username + " -> " + self.course.title
    

#new added models 

class Section(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    description = models.TextField()
    def __str__(self) -> str:
        return self.title + " -> " + self.course.title 
    
class Video(models.Model):
 
    section=models.ForeignKey(Section,on_delete=models.CASCADE)   
    title=models.CharField(max_length=70)
    videoUrl= models.FileField(upload_to=video_directory_path,max_length=255)
   

    def __str__(self) -> str:
        return self.title + " -> " + self.section.title + " -> " + self.section.course.title

class VideoRelatedFile(models.Model):

    video=models.ForeignKey(Video,on_delete=models.CASCADE)
    title=models.CharField(max_length=70)
    fileUrl= models.FileField(upload_to=file_directory_path,max_length=255)
   
    def __str__(self) -> str:
        return self.title + " -> " + self.video.title

        

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message = models.TextField()

    

     
