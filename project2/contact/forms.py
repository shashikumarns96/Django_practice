from django import forms

class EmployeeForm(forms.Form):
    emp_id = forms.IntegerField()
    emp_name = forms.CharField()