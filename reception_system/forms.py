from .models import Reception
from django import forms

# 人数を指定するフォーム
class ReceptionCountForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['reception_count']

class AdditionalReceptionInfoForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ['seat', 'payment_status', 'conditions', 'reception_time']