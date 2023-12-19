import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Employee_CRUD_App.settings')

import django
django.setup()

from crudApp.models import *
from faker import Faker
from random import *

faker=Faker()

def generate(n):
    for i in range(n):
        femp_no=randint(1,100)
        femp_name=faker.name()
        femp_salary=randint(10000,50000)
        femp_address=faker.city()
        emp_record =Employee.objects.get_or_create(emp_no=femp_no,emp_name=femp_name,emp_salary=femp_salary,emp_Address=femp_address)

generate(30)