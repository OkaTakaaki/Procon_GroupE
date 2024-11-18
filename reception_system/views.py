from django.shortcuts import render
from django.http import HttpResponse
from .models import Reception
from .forms import ReceptionCountForm

def index(request):
    return render(request,'reception_system/index.html')

def receptionNumber(request):
    if request.method == 'POST':
        reception_count = request.POST.get('reception_count')
        print(reception_count)
        # データベースには保存せずに、インスタンスのみを生成
        reception = reception_count.save(commit=False)
        print(reception)
        # 最終的にデータベースに保存
        reception.save()
        print("データが保存されました")
        return render(request, 'reception_system/reception.html', {'message': 'データが正常に保存されました'})
    # else:
    #     # バリデーションエラーが発生した場合はエラーメッセージとともにフォームを再表示
    #     return render(request, 'reception_system/reception.html', {'form': receptionform})        # GETリクエストの場合は空のフォームを渡す
    return render(request, 'reception_system/reception.html',)

def language(request):
    return render(request, 'reception_system/language.html')

def complate(request):
    return render(request, 'reception_system/complate.html')

def reserve(request):
    return render(request, 'reception_system/condition.html')

def reserveSuccess(request):
    return render(request, 'reception_system/reserve_success.html')
def kari(request):
    return render(request, 'reception_system/kari.html')
