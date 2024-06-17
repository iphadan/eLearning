# Generated by Django 5.0 on 2024-06-17 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eSchool', '0002_course_coursephoto_alter_course_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacherDescription',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eSchool.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eSchool.student')),
            ],
        ),
    ]
