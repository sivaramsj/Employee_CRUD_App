from django.shortcuts import render
from crudApp.models import Employee
from crudApp.forms import Employee_form

# Create your views here.
def retrieve_list(request):
    employee=Employee.objects.all()
    return render(request,'crudApp/employee_List.html',{'employee':employee})

def create_view(request):
    form=Employee_form()
    return render(request,'crudApp/create.html',{'form':form})
