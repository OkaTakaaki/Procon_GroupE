from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Reception,Seat
from django.db.models import Max, Count
from django.shortcuts import redirect
from .models import Reception
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse
# from .forms import NumPeopleForm, SeatingTypeForm, SeatSpecificationForm
# from .forms import ReceptionCountForm
from urllib.parse import urlencode
# import re



def index(request):
    return render(request,'reception_system/index.html')


def receptionNumber(request):
    print("receptionNumber")
    if request.method == 'POST':
        reception_count = request.POST.get('reception_count')
        seats=Seat.objects.all()
        request.session['reception_count'] = reception_count  # セッションに保存
        print("reception_count = {}".format(reception_count))
        vacant_seat = Seat.objects.filter(table_resevation=False)
        if not vacant_seat.exists():
            return redirect('reception_system:reserve')
        else:#空席がある場合
            print("空席")
            reception_count = int(reception_count)
            recommended_seats = []

            # 条件を満たす座席の組み合わせを見つける
            for i in range(len(seats)):
                for j in range(i, len(seats)):
                    selected_seats = seats[i:j+1]
                    seat_numbers = [seat.table_number for seat in selected_seats]
                    seat_numbers.sort()
                    are_adjacent = all(seat_numbers[k] + 1 == seat_numbers[k + 1] for k in range(len(seat_numbers) - 1))
                    total_capacity = sum(seat.recommended_capacity for seat in selected_seats)
                    if are_adjacent and reception_count <= total_capacity:
                        recommended_seats.append(selected_seats)

            # 最小の席数で条件を満たす座席を選択
            recommended_seats.sort(key=lambda x: len(x))
            min_seats = recommended_seats[:3]  # 上位3つの組み合わせを選択
            print("min_seats = {}".format(min_seats))
            for i in range(len(min_seats[0])):
                print("bbbbbbb = {}".format(min_seats[0][i]))
                i += 1
            context = {
                'recommended_seats': min_seats,
                'seats': seats,
                'reception_count': reception_count
            }
            query_string = urlencode({'context': context})
            url = reverse('reception_system:seatsview') + '?' + query_string
            return redirect(url)
    return render(request, 'reception_system/reception.html')

def complate(request):
    return render(request, 'reception_system/complate.html')

def reserve(request):
    if request.method == 'POST':
        # フォームからデータを取得
        # reception_number=request.POST.get('reception_number')
        seat_type = request.POST.get('seat_type')
        reception_count = request.POST.get('reception_count')
        outlet = request.POST.get('outlet')

        # セッションからreception_countを取得
        reception_count = request.session.get('reception_count')

        if seat_type == "カウンター":
            seat_type = 0
        elif seat_type == "テーブル":
            seat_type = 1
        elif seat_type == "ソファー":
            seat_type = 2
        print("JJJJ")
        seats = Seat.objects.filter(
            table_type=seat_type,
            electrical_outlet=(outlet == "True"),
            table_connect=False,
            table_resevation=True,
            recommended_capacity__gte=reception_count  # 追加条件
        ).annotate(reception_count=Count('reception_seat1') + Count('reception_seat2')).order_by('reception_count')
        print(seats)
        if seats.exists():
            seat = seats.first()

            # reception_numberの最大値を取得
            max_reception_number_dict = Reception.objects.all().aggregate(Max('reception_number'))
            max_reception_number = max_reception_number_dict['reception_number__max']
            if max_reception_number is not None:
                max_reception_number = int(max_reception_number)
            else:
                max_reception_number = 0

            # Receptionモデルにデータを保存
            Reception.objects.create(
                reception_number=max_reception_number + 1,
                reception_count=reception_count,
                table_type=seat_type,
                electrical_outlet=(outlet == "True"),
                table_connect=False,
                reception_time=timezone.now(),
                seat1=seat
            )
            print("aaa")
            seat.save()

            return redirect('reception_system:reserve_success')
        # # reception_numberの最大値を取得
        # max_reception_number = Reception.objects.all().aggregate(Max('reception_number'))['reception_number__max']
        # print(max_reception_number)
        # if max_reception_number is not None:
        #     max_reception_number = int(max_reception_number)
        # else:
        #     max_reception_number = 0
        # print("最大のreception_number:", max_reception_number)

        # print(seat_type, reception_count, outlet, seat_connect)

        # # モデルにデータを保存
        # Reception.objects.create(
        #     reception_number=max_reception_number+1,
        #     reception_count=reception_count,
        #     table_type=seat_type,
        #     electrical_outlet=outlet,
        #     table_connect=seat_connect,
        #     reception_time=timezone.now()
        # )
        # return redirect('reception_system:reserve_success')


    # 各seat_typeの座席数を取得
    counter_seats = Seat.objects.filter(table_type=0).count()
    table_seats = Seat.objects.filter(table_type=1).count()
    sofa_seats = Seat.objects.filter(table_type=2).count()

    context = {
        'counter_seats': counter_seats,
        'table_seats': table_seats,
        'sofa_seats': sofa_seats,
    }

    return render(request,'reception_system/condition.html',context)

def calculate_wait_time(request):
    if request.method == 'POST':
        seat_type = request.POST.get('seat_type')
        outlet = request.POST.get('outlet') == 'True'

        if seat_type is not None:
            seat_type = int(seat_type)
        else:
            print("seat_type = {}".format(seat_type))
            return JsonResponse({'wait_time': 0, 'error': 'Invalid seat_type'})
        # 待ち時間を計算するロジックを実装

        wait_time = 0
        # 条件に一致するReceptionの数を取得
        reception_count = Reception.objects.filter(
            table_type=seat_type,
            electrical_outlet=outlet,
            end_time__isnull=True
        ).count()

        # 仮の待ち時間計算ロジック
        if reception_count > 0:
            wait_time = reception_count * 5  # 例: 1つの受付につき5分の待ち時間

        return JsonResponse({'wait_time': wait_time})

    return JsonResponse({'wait_time': 0})

def seatsview(request):
    print("---------seatsview---------")
    seats = Seat.objects.all()
    reception_count = request.POST.get('reception_count')
    recommended_seats = []

    if not reception_count:
        reception_count = request.session.get('reception_count')
        reception_count = int(reception_count)

        # 条件を満たす座席の組み合わせを見つける
        for i in range(len(seats)):
            for j in range(i, len(seats)):
                selected_seats = seats[i:j+1]
                seat_numbers = [seat.table_number for seat in selected_seats]
                seat_numbers.sort()
                are_adjacent = all(seat_numbers[k] + 1 == seat_numbers[k + 1] for k in range(len(seat_numbers) - 1))
                total_capacity = sum(seat.recommended_capacity for seat in selected_seats)
                if are_adjacent and reception_count <= total_capacity:
                    recommended_seats.append(selected_seats)

        # 最小の席数で条件を満たす座席を選択
        recommended_seats.sort(key=lambda x: len(x))
        recommended_seats = recommended_seats[:3]  # 上位3つの組み合わせを選択
        print("recommended_seats = {}".format(recommended_seats))

    if request.method == 'POST':
        select_seat = request.POST.get('select_seat', "").split(",")
        selected_seats = Seat.objects.filter(table_number__in=select_seat)

        # 選択された座席の情報を取得
        seat_list = list(selected_seats[:2])  # 2つまで取得（それ以上は `seat1` と `seat2` に入らない）
        seat1 = seat_list[0] if len(seat_list) > 0 else None
        seat2 = seat_list[1] if len(seat_list) > 1 else None

        table_type = seat1.table_type if seat1 else 0  # 座席種別（1つ目の席のタイプを採用）
        electrical_outlet = seat1.electrical_outlet if seat1 else False  # コンセント有無
        table_connect = seat1.table_connect if seat1 else False  # 連結有無

        # reception_number の最大値を取得
        max_reception_number_dict = Reception.objects.all().aggregate(Max('reception_number'))
        max_reception_number = max_reception_number_dict['reception_number__max'] or 0

        Reception.objects.create(
            reception_number=max_reception_number + 1,
            reception_count=reception_count,
            seat1=seat1,
            seat2=seat2,
            table_type=table_type,
            electrical_outlet=electrical_outlet,
            table_connect=table_connect,
            reception_time=timezone.now()
        )

        return redirect('reception_system:reserve_success')

    else:
        context = {
            "reception_count": reception_count,
            "seats": seats,
            "recommended_seats": recommended_seats
        }
        return render(request, 'reception_system/seatsview.html', context)
    
def reserveSuccess(request):
    receptionnumber = Reception.objects.all().last().reception_number
    return render(request, 'reception_system/reserve_success.html',{'receptionnumber':receptionnumber})

def customerCall(request):
    waiting_call = Reception.objects.filter(seat1=None,end_time=None)
    vacasent_seat = Seat.objects.filter(table_resevation=False)
    for reception in waiting_call:
        for seat in vacasent_seat:
            # ここで比較処理を行う
            if (reception.table_type == seat.table_type and
                reception.electrical_outlet == seat.electrical_outlet and
                reception.table_connect == seat.table_connect):
                print("bbbbb")
                # 同じ条件を満たすReceptionオブジェクトをreception_timeが若い順に取得
                matching_receptions = Reception.objects.filter(
                    table_type=seat.table_type,
                    electrical_outlet=seat.electrical_outlet,
                    table_connect=seat.table_connect,
                    seat1=None,
                    end_time=None
                ).order_by('reception_time')

                if matching_receptions.exists():
                    # 最初のReceptionオブジェクトを取得
                    matching_reception = matching_receptions.first()
                    # seatを追加
                    matching_reception.seat = seat
                    matching_reception.save()
                    print(matching_reception)
                    print(f"一致: Reception {matching_reception.reception_number} に Seat {seat.table_number} を追加") # 一致する座席が見つかった場合はループを抜ける
                    return render(request, 'reception_system/customer_call.html',{'reception':matching_reception,'seat':seat})
    return redirect('employee:employee_confirm')