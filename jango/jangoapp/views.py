from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'jatin'})
def add(request):
    value1= int(request.POST["num1"])
    value2= int(request.POST["num2"])
    value3= value1 + value2
    return render(request,'result.html',{'result' : value3})