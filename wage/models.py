from django.db import models
from baseInfo.models import Employee
# Create your models here.
class WageSum(models.Model):
    year              = models.IntegerField()
    month             = models.IntegerField()
    number_of_workers = models.IntegerField()
    sum_gross_amount  = models.DecimalField(max_digits= 50,decimal_places=10)
    sum_tax_amount    = models.DecimalField(max_digits= 50,decimal_places=10)

    def __str__(self):
        return "{}-{}".format(self.year,self.month)

class WageDetail(models.Model):
    wage_sum       = models.ForeignKey(WageSum,on_delete=models.CASCADE)
    employee       = models.ForeignKey(Employee, on_delete=models.CASCADE)
    

