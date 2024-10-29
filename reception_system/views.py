from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'reception_system/index.html')

def reception(request):
    return render(request, 'reception_system/reception.html')