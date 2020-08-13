from django import forms
from home.models import *

class EmployeeForm(forms.Form):
    eid = forms.IntegerField(label="Employee ID")
    ename = forms.CharField(max_length=30, label="Employee Name")
    emp = forms.CharField(max_length=30, label="Employer")
    esalary = forms.IntegerField(label="Salary")


# Model Based Form
class EmployeeModelForm(forms.ModelForm):
    #test = forms.IntegerField(label="New")
    class Meta:
        model = EmployeeModel
        #fields = ['eid', 'ename', 'esalary']
        #exclude = ['eid']
        fields = '__all__'