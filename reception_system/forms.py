from .models import Reception
from django import forms

# 人数を指定するフォーム
class NumPeopleForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['reception_count']

class SeatingTypeForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['conditions']

class SeatSpecificationForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['seat']
