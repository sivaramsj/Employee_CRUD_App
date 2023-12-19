from django.shortcuts import render
from crudApp.models import Employee

# Create your views here.
def retrieve_list(request):
    employee=Employee.objects.all()
    return render(request,'crudApp\employee_List.html',{'employee':employee})
