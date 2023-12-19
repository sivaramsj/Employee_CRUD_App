from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    emp_salary=models.IntegerField()
    emp_Address=models.CharField(max_length=50)