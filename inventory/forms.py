from django import forms
from django.forms import ModelForm
from .models import Item, Stock


class ItemForm(ModelForm):
    initial_stock = forms.IntegerField()

    class Meta:
        model = Item
        fields = [
            'name',
            'sku',
            'location',
            'sell_price',
            'buy_price',
            'img',
        ]


class StockForm(ModelForm):

    class Meta:
        model = Stock
        fields = [
            'amount',
            'buy_price',
        ]
