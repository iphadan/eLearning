from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.Course)
admin.site.register(models.AdminUser)
admin.site.register(models.Category)
#new added models
admin.site.register(models.Section)
admin.site.register(models.Video)
admin.site.register(models.VideoRelatedFile)
