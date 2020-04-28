from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html', {'name':'Shadow'})

def add(request):
    # perform operations here
    val1 = request.POST['num1'] # string by default
    val2 = request.POST['num2'] # string by default   
    res = int(val1) + int(val2)

    return render(request,'result.html',{'result':res})