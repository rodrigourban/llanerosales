from django import forms
from django.forms import ModelForm
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'sku',
            'location',
            'sell_price',
            'buy_price',
            'img'
        ]
