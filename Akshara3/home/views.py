from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import *
from home.models import EmployeeModel

# Very Important, used in project as well
# How to receive data from form using GET Request
def enter_emp(request):
    # request.GET = {eid:10,ename:Ajay,emp:TCS,esalary:50000}
    form1 = EmployeeForm()
    if request.method == "POST":
        form1 = EmployeeForm(request.POST)
        if form1.is_valid():
            eid = form1.cleaned_data['eid']
            ename = form1.cleaned_data['ename']
            emp = form1.cleaned_data['emp']
            sal = form1.cleaned_data['esalary']
            EmployeeModel.objects.create(eid=eid, ename=ename, emp=emp, esalary=sal)
            form1 = EmployeeForm()

        #EmployeeModel.objects.create(eid=eid, ename=ename, emp=emp, esalary=sal)

    return render(request, "home/enter_emp.html", {'form1': form1})

# Very Important, used in project
# how to receive data using form, POST method
def enter_emp_post(request):
    form1 = EmployeeForm()
    if request.method == "POST":
        # re-creacted the form with POST data
        form1 = EmployeeForm(request.POST)
        if form1.is_valid():
            eid = form1.cleaned_data['eid']
            ename = form1.cleaned_data['ename']
            emp = form1.cleaned_data['emp']
            sal = form1.cleaned_data['esalary']
            print('#################################')
            print("Emp ID", eid)
            print("Emp Name", ename)
            print("Emp", emp)
            print("Salary", sal)
            # all_emp = EmployeeModel.objects.all()
            # for emp1 in all_emp:
            #    if emp1.eid == eid
            EmployeeModel.objects.create(eid=eid, ename=ename, emp=emp, esalary=sal)
            # form1.save()
    return render(request, "home/enter_emp_post.html", {'form1': form1})


# CREATE
def enter_employee(request):
    form1 = EmployeeModelForm()
    if request.method == "POST":
        # re-creacted the form with POST data
        form1 = EmployeeModelForm(request.POST)
        if form1.is_valid():
            form1.save()
    return render(request, "home/enter_emp_post.html", {'form1': form1})


# READ
def show(request):
    all_emp = EmployeeModel.objects.all()
    return render(request, "home/show.html", {'all_emp': all_emp})

def delete(request, eno):
    #eno = 19
    emp = EmployeeModel.objects.get(eid=eno)
    emp.delete()
    return redirect("/home/show/")

def update(request, eno):
    emp = EmployeeModel.objects.get(eid=eno)
    if request.method == "POST":
        form1 = EmployeeModelForm(request.POST, instance=emp)
        if form1.is_valid():
            form1.save()
            return redirect("/home/show/")
    else:
        form1 = EmployeeModelForm(instance=emp)
    return render(request, "home/update.html", {'form1': form1})


def update_u(request, eno):
    emp = EmployeeModel.objects.get(eid=eno)
    if request.method == "POST":
        form1 = EmployeeModelForm(request.POST,instance=emp)
        if form1.is_valid():
            form1.save()
            return redirect('/home/show/')
    else:
        form1 = EmployeeModelForm(instance=emp)
    return render(request, "home/update.html", {'form1': form1})

def delete_d(request, ename):
    emp = EmployeeModel.objects.get(ename=ename)
    emp.delete()
    return redirect('/home/show/')
