from django.shortcuts import render
from django.http import HttpResponse
from .models import Reception,Seat
from .forms import ReceptionCountForm
from django.shortcuts import redirect

def index(request):
    return render(request,'reception_system/index.html')


def receptionNumber(request):
    if request.method == 'POST':
        reception_count = request.POST.get('reception_count')
        print(reception_count)
        vacant_seat = Seat.objects.filter(table_resevation=False)
        if not vacant_seat.exists():
            return redirect('reception_system:reserve')
        else:
            print("No")
            return redirect('reception_system:seatsview')
    return render(request, 'reception_system/reception.html')
        # GETリクエストの場合は空のフォームを渡す

def language(request):
    return render(request, 'reception_system/language.html')

def complate(request):
    return render(request, 'reception_system/complate.html')

def reserve(request):
    return render(request,'reception_system/condition.html')

def seatsview(request):
    seats = Seat.objects.all()
    if request.method == 'POST':
        pass
    return render(request,'reception_system/seatsview.html', {'seats':seats})



def reserveSuccess(request):
    return render(request, 'reception_system/reserve_success.html')

