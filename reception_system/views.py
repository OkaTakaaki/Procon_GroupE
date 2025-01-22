from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reception,Seat
from django.shortcuts import redirect
from .models import Reception
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from urllib.parse import urlencode
import urllib.parse
# from .forms import NumPeopleForm, SeatingTypeForm, SeatSpecificationForm
# from .forms import ReceptionCountForm
# import re

def index(request):
    return render(request,'reception_system/index.html')


def receptionNumber(request):
    if request.method == 'POST':
        seats = Seat.objects.all()
        seat = request.POST.getlist('select_seat')
        reception_count = request.POST.get('reception_count')
        print(seat)
        print(reception_count)
        vacant_seat = Seat.objects.filter(table_resevation=False)
        if not vacant_seat.exists(): #空席がない場合
            print("満席")
            context = {
                'seats': seats,
                'reception_count': reception_count
            }
            return render(request," reception_system/reserve.html", context)
        
        else:#空席がある場合
            print("空席")
            context = {
                'seats': seats,
                'reception_count': reception_count
            }
            query_string = urlencode({'reception_count': reception_count})
            url = reverse('reception_system:seatsview') + '?' + query_string
            return redirect(url)
    return render(request, 'reception_system/reception.html')

def language(request):
    return render(request, 'reception_system/reception_system/language.html')

def complate(request):
    return render(request, 'reception_system/complate.html')

def reserve(request):
    return render(request,'reception_system/condition.html')

def seatsview(request):
    seats = Seat.objects.all()
    recommended_capacity_list = []
    if request.method == 'POST':
        print("a")
        seat = request.POST.getlist('select_seat')
        reception_count = request.POST.get('reception_count')
        print("seat = {}".format(seat))
        print("reception_count = {}".format(reception_count))
        # for i in seat:
        #     recommended_capacity_list.append(Seat.objects.get(seat[i]).recommended_capacity)
        print("recommended_capacity_list = {}".format(recommended_capacity_list))
        print("-------------")
    context = {
        "seats" : seats
    }
    return render(request,'reception_system/seatsview.html', context)

def reserveSuccess(request):
    return render(request, 'reception_system/reserve_success.html')

