from django.shortcuts import render, redirect
# from .forms import SeatForm

def employee(request):
    return render(request, 'employee/employee.html')

def item(request):
    return render(request, 'employee/item.html')

def confirm(request):
    return render(request, 'employee/confirm.html')

def new_seat(request):
    # if request.method == 'POST':
    #     form = SeatForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # フォームを保存
    #         return redirect('employee_item')  # 成功したら別ページへリダイレクト
    # else:
    #     form = SeatForm()

    # return render(request, 'employee/new_seat.html', {'form': form})
    return render(request, 'employee/new_seat.html')