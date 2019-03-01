from django.urls import path,re_path
from django.contrib.auth.admin import User
from . import views

urlpatterns = [
    path('add/',views.employee_add)
]

