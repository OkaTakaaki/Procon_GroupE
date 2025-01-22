from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Reception,Seat
from django.db.models import Max
from django.shortcuts import redirect
from .models import Reception
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
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
        request.session['reception_count'] = reception_count  # セッションに保存
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
    if request.method == 'POST':
        # フォームからデータを取得
        # reception_number=request.POST.get('reception_number')
        seat_type = request.POST.get('seat_type')
        reception_count = request.POST.get('reception_count')
        outlet = request.POST.get('outlet')
        seat_connect = request.POST.get('seat_connect')

        # セッションからreception_countを取得
        reception_count = request.session.get('reception_count')

        if seat_type == "カウンター":
            seat_type = 0
        elif seat_type == "テーブル":
            seat_type = 1
        elif seat_type == "ソファー":
            seat_type = 2


        # reception_numberの最大値を取得
        max_reception_number = Reception.objects.all().aggregate(Max('reception_number'))['reception_number__max']
        print(max_reception_number)
        if max_reception_number is not None:
            print("aaaaaaaaaaaaa")
            max_reception_number = int(max_reception_number)
        else:
            print("bbbbbbbbbbbbb")
            max_reception_number = 0
        print("最大のreception_number:", max_reception_number)

        print(seat_type, reception_count, outlet, seat_connect)

        # モデルにデータを保存
        Reception.objects.create(
            reception_number=max_reception_number+1,
            reception_count=reception_count,
            table_type=seat_type,
            electrical_outlet=outlet,
            table_connect=seat_connect,
            reception_time=timezone.now()
        )
        return redirect('reception_system:reserve_success')
    
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
    receptionnumber = Reception.objects.all().last().reception_number
    
    return render(request, 'reception_system/reserve_success.html',{'receptionnumber':receptionnumber})

def customerCall(request):
    waiting_call = Reception.objects.filter(seat=None,end_time=None)
    vacasent_seat = Seat.objects.filter(table_resevation=False)
    count = 0
    for reception in waiting_call:
        for seat in vacasent_seat:
            # ここで比較処理を行う
            if reception.reception_number == seat.table_number:  # 例としてreception_numberとtable_numberを比較
                print(f"一致: Reception {reception.reception_number} と Seat {seat.table_number}")
                count += 1
    return render(request, 'reception_system/customer_call.html')