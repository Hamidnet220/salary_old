from django.urls import path,re_path
from django.contrib.auth.admin import User
from . import views

urlpatterns = [
    path('add/employee',views.employee_add),
    path('cities/',views.cities,name='cities')
]

