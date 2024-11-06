from django.shortcuts import render

def employee(request):
    return render(request, 'employee/employee.html')

def item(request):
    return render(request, 'employee/item.html')

def confirm(request):
    return render(request, 'employee/confirm.html')


def new_seat(request):
    return render(request, 'employee/new_seat.html')