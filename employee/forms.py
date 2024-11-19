
from django import forms

class SeatForm(forms.Form):
    TABLE_TYPE_CHOICES = [
        (1, 'テーブル席'),
        (2, 'カウンター席')
        
    ]
    table_type = forms.ChoiceField(
        choices=TABLE_TYPE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label = '座席種類'
    )
    
    table_number = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'テーブル番号を入力'}),
        label = 'テーブル番号'
    )

    SEATS_CHOICES = [
        (1, '1人席'),
        (2, '2人席'),
        (4, '4人席')
    ]
    seats = forms.ChoiceField(
        choices=SEATS_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label = '座席人数'
    )

    connection = forms.ChoiceField(
        choices=[(True, '座席連結する'), (False, '座席連結しない')], 
        widget=forms.RadioSelect(attrs={'class': 'form-control'}),
        label = '連結する'
    )
