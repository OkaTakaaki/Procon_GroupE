from django.shortcuts import render, redirect
from reception_system.models import Seat

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

# 新しい座席の登録ページ
def new_seat(request):
    if request.method == 'POST':
        # フォームから送信されたデータを取得
        status = request.POST.get('status')
        table_number = request.POST.get('table_number')
        recommended_capacity = request.POST.get('seats')
        connection = request.POST.get('connection')

        # 新しいテーブル情報を保存
        Seat.objects.create(
            table_type=status,
            table_number=table_number,
            recommended_capacity=recommended_capacity,
            table_connect=connection,
            table_resevation=False
        )

        # データ保存後に確認ページへリダイレクト
        return redirect('confirm')

    return render(request, 'employee/new_seat.html')
