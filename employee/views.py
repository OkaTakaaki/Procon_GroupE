from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from reception_system.models import Seat
from .forms import SeatForm
from reception_system.views import castomerCall

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


# views.py
def new_seat(request):
    if request.method == 'POST':
        form = SeatForm(request.POST)
        if form.is_valid():
            seat = form.save(commit=False)
            seat.save()
            print(seat)

            return redirect('employee:employee_complate')  # 保存が成功した場合リダイレクト
        
        else:
            print(form.errors)  # バリデーションエラーを表示

    else:
        form = SeatForm()  # GETリクエストの場合、空のフォームを表示

    return render(request, 'employee/new_seat.html', {'form': form})


def complate(request):
    return render(request, 'employee/complate.html')

def table_detail(request, table_id):
    # テーブルの詳細情報を取得
    table = get_object_or_404(Seat, id=table_id)
    if request.method == 'POST':
        # POST データから値を取得して、BooleanField を適切に処理する
        table.table_number = request.POST.get('table_number', table.table_number)
        table.recommended_capacity = request.POST.get('recommended_capacity', table.recommended_capacity)
        table.table_type = request.POST.get('table_type', table.table_type)
        table.table_resevation = 'table_reservation' in request.POST
        table.electrical_outlet = 'electrical_outlet' in request.POST
        table.clean_status = 'clean_status' in request.POST 
        table.table_connect = 'table_connect' in request.POST 
        
        if table.table_resevation == False:
            return castomerCall(request)


        # モデルを保存
        table.save()
        return redirect('employee:employee_confirm')  # 編集後にリダイレクトするURLに変更してください
    return render(request, 'employee/table_detail.html', {'table': table})

