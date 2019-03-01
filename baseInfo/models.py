from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobPlace(models.Model):
    title       = models.CharField(max_length = 50)
    description = models.TextField(blank = True ,null= True)

    def __str__(self):
        return "{}-{}".format(self.title,self.description)

class Employer(models.Model):
    title          = models.CharField(max_length = 100)
    insurance_code = models.CharField(max_length = 20)
    
    def __str__(self):
        return "{}-{}".format(self.title,self.insurance_code)

class EmployeeStatus(models.Model):
    title       = models.CharField(max_length = 25)
    description = models.TextField(blank = True , null = True)

    def __str__(self):
        return self.title

class Group(models.Model):
    year                = models.CharField(max_length = 4)
    employer            = models.ForeignKey(Employer,on_delete = models.CASCADE)
    title               = models.CharField(max_length = 50)
    daily_rate          = models.DecimalField(max_digits= 8 , decimal_places= 2)
    shift_right_ratio   = models.DecimalField(max_digits= 3 , decimal_places= 3)    
    commute_right_ratio = models.DecimalField(max_digits= 3 , decimal_places= 3)

    def __str__(self):
        return "{}-{}".format(self.year,self.title)


class Employee(models.Model):
    firstname    = models.CharField(max_length = 50)
    lastname     = models.CharField(max_length = 50)
    father_name  = models.CharField(max_length = 50)
    national_id  = models.CharField(max_length = 10)
    is_maride    = models.BooleanField()
    status       = models.ForeignKey(EmployeeStatus ,on_delete = models.SET_NULL,blank = True , null = True,)
    id_number    = models.CharField(max_length = 50)
    bank_account = models.CharField(max_length = 26)
    insurance_id = models.CharField(max_length = 8)
    jobPlace     = models.ForeignKey(JobPlace ,on_delete = models.SET_NULL,blank = True , null = True,)
    employer     = models.ForeignKey(Employer ,on_delete = models.SET_NULL,blank = True , null = True,)
    group        = models.ForeignKey(Group, on_delete = models.SET_NULL,blank = True , null = True,)
    description = models.TextField(blank=True,null = True)

    add_by_user = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__ (self):
        return "{}-{}".format(self.lastname,self.firstname)



class Const(models.Model):
    year              = models.CharField(max_length = 4)
    child_benefit     = models.DecimalField(max_digits= 10 , decimal_places= 2)
    tax_exempt_amount = models.DecimalField(max_digits= 10 , decimal_places= 2)

    def __str__(self):
        return self.year
        

class City(models.Model):
    name        = models.CharField(max_length = 25)
    desctiption = models.TextField(blank =True , null=True)

    def __str__(self):
        return self.name









