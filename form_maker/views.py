from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def  index(request):
    # data=request.POST()
    # Name=data.get('name')
    # Rollno=data.get('rollno')
    return render(request,"index.html")