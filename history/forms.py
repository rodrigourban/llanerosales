from django import forms
from .models import Sell


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['amount', 'sell_price']
