from django.shortcuts import render

def employee(request):
    return render(request, 'employee/employee.html')

def item(request):
    return render(request, 'employee/item.html')
