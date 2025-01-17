from django.shortcuts import render
from django.http import HttpResponse
from .models import Reception,Seat
from django.db.models import Max
from django.shortcuts import redirect
from .models import Reception
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import NumPeopleForm, SeatingTypeForm, SeatSpecificationForm
# from .forms import ReceptionCountForm
# import re

def index(request):
    return render(request,'reception_system/index.html')


def receptionNumber(request):
    if request.method == 'POST':
        reception_count = request.POST.get('reception_count')
        request.session['reception_count'] = reception_count  # セッションに保存
        print(reception_count)
        vacant_seat = Seat.objects.filter(table_resevation=False)
        if not vacant_seat.exists():
            return redirect('reception_system:reserve')
        else:
            print("No")
            return redirect('reception_system:seatsview')
    return render(request, 'reception_system/reception.html')

#         # GETリクエストの場合は空のフォームを渡す
# def select_reception_number():
#     reception = Reception.objects.all()
#     last = reception.last()
#     if last == None:
#         reception_number = "M-1"
#     else:
#         last_reception_number = last.reception_number
#         result = re.sub(r'[^0-9]', '', last_reception_number)
#         print("--------{}-------".format(result))
#         if len(result) == 1:
#             print("A")
#             reception_number = "M-" + str(int(result) + 1)
#         elif len(result) == 2:
#             print("B")
#             reception_number = "M-" + str(int(result) + 1)
#         elif len(result) == 3:
#             print("C")
#             reception_number = "M-" + str(int(result) + 1)
#         elif len(result) == 4:
#             print("D")
#             reception_number = "M-" + str(int(result) + 1)
#     print("--------{}-------".format(reception_number))
#     return reception_number

# # 人数選択画面
# def select_num_people(request):
#     if request.method == 'POST':
#         form = NumPeopleForm(request.POST)
#         reception_number = select_reception_number()
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.reception_number = reception_number
#             instance.save()
#             return redirect('reception_system/select_seating_type')  # 座席型指定画面へリダイレクト
#     else:
#         form = NumPeopleForm()
#     return render(request, 'reception_system/select_num_people.html', {'form': form})


# # 座席型指定画面
# def select_seating_type(request):
#     reservation = get_object_or_404(Reception)
#     if request.method == 'POST':
#         form = SeatingTypeForm(request.POST)
#         if form.is_valid():
#             reservation.seating_type = form.cleaned_data['seating_type']
#             reservation.save()
#             return redirect('reception_system/select_seat_specification')  # 座席指定画面へリダイレクト
#     else:
#         form = SeatingTypeForm()
#     return render(request, 'reception_system/select_seating_type.html', {'form': form})

# # 座席指定画面
# def select_seat_specification(request):
#     reservation = get_object_or_404(Reception, id=num)
#     if request.method == 'POST':
#         form = SeatSpecificationForm(request.POST)
#         if form.is_valid():
#             reservation.seat_specification = form.cleaned_data['seat_specification']
#             reservation.save()
#             return redirect('reception_system/complete_reservation')  # 受付完了画面へリダイレクト
#     else:
#         form = SeatSpecificationForm()
#     return render(request, 'reception_system/select_seat_specification.html', {'form': form})

# # 受付完了画面
# def complete_reservation(request):
#     reservation = get_object_or_404(Reception, id=num)
#     reservation.is_completed = True
#     reservation.save()
#     # セッションの予約IDを削除して状態をクリア
#     del request.session['reservation_id']
#     return render(request, 'reception_system/complete_reservation.html', {'reservation': reservation})



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
            table_connect=seat_connect
        )
        return redirect('reception_system:reserve_success')
    
    return render(request,'reception_system/condition.html')

def seatsview(request):
    seats = Seat.objects.all()
    if request.method == 'POST':
        seat = request.POST.get('seat')
        print(seat)
    return render(request,'reception_system/seatsview.html', {'seats':seats})



def reserveSuccess(request):
    receptionnumber = Reception.objects.all().last().reception_number
    
    return render(request, 'reception_system/reserve_success.html',{'receptionnumber':receptionnumber})

