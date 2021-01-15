from django.contrib import admin
from . models import Student
from django_mongoengine import mongo_admin  as admin

admin.site.register(Student)