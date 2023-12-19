from django.contrib import admin
from crudApp.models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list = ['emp_no', 'emp_name', 'emp_salary', 'emp_Address']

admin.site.register(Employee,EmployeeAdmin)
