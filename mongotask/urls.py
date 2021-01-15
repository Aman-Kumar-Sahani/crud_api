from django.contrib import admin
from django.urls import path
from django.conf import settings
from django_mongoengine import mongo_admin
from student.views import StudentAPI,StudentDetailsBy_ID
from user.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mongoadmin/', mongo_admin.site.urls),
    path('studata/',StudentAPI.as_view()),
    path('stuid/<str:id>/',StudentDetailsBy_ID.as_view()),
    path('register/',Register.as_view()),
]
