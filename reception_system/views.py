from django.shortcuts import render
from django.http import HttpResponse
from .models import Reception
from .forms import ReceptionCountForm

def index(request):
    return render(request,'reception_system/index.html')

def reception(request):
    if request.method == 'POST':
        # フォームのインスタンスを作成し、POSTデータを渡す
        receptionform = ReceptionCountForm(request.POST)
        if receptionform.is_valid():
            print("aaaaaa")
            # データベースには保存せずに、インスタンスのみを生成
            reception = receptionform.save(commit=False)
            print(reception)
            # 最終的にデータベースに保存
            reception.save()
            print("データが保存されました")
            return render(request, 'reception_system/reception.html', {'message': 'データが正常に保存されました'})
        else:
            # バリデーションエラーが発生した場合はエラーメッセージとともにフォームを再表示
            return render(request, 'reception_system/reception.html', {'form': receptionform})
    else:
        # GETリクエストの場合は空のフォームを渡す
        receptionform = ReceptionCountForm()
        return render(request, 'reception_system/reception.html', {'form': receptionform})


def language(request):
    return render(request, 'reception_system/language.html')

def complate(request):
    return render(request, 'reception_system/complate.html')