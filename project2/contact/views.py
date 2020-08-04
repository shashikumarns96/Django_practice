from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def func2(request):
    l1 =[1,2,3,4,5]
    d1={'a':1, 'b':2}
    str ="abcd"
    return render(request, "contact/page2.html",{'lista':l1,'dicta':d1,'strg':str})

def employee(request):
    form = EmployeeForm()

    if ('emp_id' in request.GET):
        print(request.GET)
        eid = request.GET['emp_id']
        ename = request.GET['emp_name']

        print("Emp ID", eid)
        print("Emp Name", ename)

    return render(request, "contact/page3.html", {'form':form})

def employee_post(request):
    form = EmployeeForm()
    if request.method == "POST":
        # re-creacted the form with POST data
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            eid = form.cleaned_data['emp_id']
            ename = form.cleaned_data['emp_name']
            print("eid is ", eid)
            print("ename is", ename)
            form = EmployeeForm()
    return render(request, "contact/page4.html", {'form':form})