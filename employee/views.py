from django.shortcuts import render, redirect
from reception_system.models import Seat
from .forms import SeatForm

# 従業員用ページ
def employee(request):
    return render(request, 'employee/employee.html')

# アイテム管理ページ
def item(request):
    return render(request, 'employee/item.html')

# 確認ページ
def confirm(request):
    tables = Seat.objects.all()
    return render(request, 'employee/confirm.html', {'tables': tables})

# # 新しい座席の登録ページ
# def new_seat(request):
#     if request.method == 'POST':
#         # フォームから送信されたデータを取得
#         table_type = request.POST.get('table_type')
#         table_number = request.POST.get('table_number')
#         recommended_capacity = request.POST.get('recommended_capacity')
#         table_connect = request.POST.get('connection')

#         # 入力されたデータを保存
#         new_seat = Seat.objects.create(
#             table_type=table_type,
#             table_number=table_number,
#             recommended_capacity=recommended_capacity,
#             table_connect=(table_connect == 'True'),  # 'True' の場合は連結する
#             table_resevation=False,  # 最初は使用されていないとしてデフォルトでFalse
#             electrical_outlet=False,  # コンセント有無はデフォルトでFalse
#             clean=False,  # 清掃済みはデフォルトでFalse
#         )
#         new_seat.save()

#         # データ保存後に確認ページへリダイレクト
#         return redirect('confirm')

#     return render(request, 'employee/new_seat.html')

def new_seat(request):
    if request.method =='POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee_new_seat')
    
    else:
        form = SeatForm()

    return render(request, 'employee/new_seat.html',{'form': form})