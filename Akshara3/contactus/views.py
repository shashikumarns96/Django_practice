from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addr(request):
    return HttpResponse("<h1>ADDR PAGE1</h1>")