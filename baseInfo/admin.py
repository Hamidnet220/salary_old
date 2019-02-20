from django.contrib import admin
from .models import Employee,Employer,JobPlace,EmployeeStatus,Group,Const
# Register your models here.
admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(JobPlace)
admin.site.register(EmployeeStatus)
admin.site.register(Group)
admin.site.register(Const)