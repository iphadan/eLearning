# Generated by Django 5.0 on 2024-06-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSchool', '0007_course_coursestudentscount_alter_video_videourl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
