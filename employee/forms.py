from django import forms
from reception_system.models import Seat  # 別アプリのモデルをインポート

class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ['table_type', 'table_number', 'recommended_capacity', 'table_connect']
