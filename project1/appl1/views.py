from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def func1(request):
    l1 =[1,2,4,5]
    d1 = {'a':1,'b':2,'c':3}
    return render(request, "appl1/home.html",{'list':l1,'d1':d1})

