from django.shortcuts import render

# Create your views here.
def func2(request):
    return render(request, "appl2/address.html")