from django.shortcuts import render, redirect
from reception_system.models import Seat
# from .forms import SeatForm

def employee(request):
    return render(request, 'employee/employee.html')

def item(request):
    return render(request, 'employee/item.html')

def confirm(request):
    return render(request, 'employee/confirm.html')

# def new_seat(request):
    # if request.method == 'POST':
    #     form = SeatForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # フォームを保存
    #         return redirect('employee_item')  # 成功したら別ページへリダイレクト
    # else:
    #     form = SeatForm()

    # return render(request, 'employee/new_seat.html', {'form': form})

def new_seat(request):
    if request.method == 'POST':
        # フォームから送信されたデータを取得
        status = request.POST.get('status')
        table_number = request.POST.get('table_number')
        seats = request.POST.get('seats')
        connection = request.POST.get('connection')

        # 新しいテーブル情報を保存
        Seat.objects.create(
            table_typ=status,
            table_number=table_number,
            recommended_capacity=seats,
            table_connect=connection
        )

    def confirm(request):
        tables = seats.objects.all()  # データベースからテーブル情報を取得
        return render(request, 'confirm.html', {'confirm': confirm})

        # データ保存後に一覧ページにリダイレクト
        

    return render(request, 'employee/new_seat.html')