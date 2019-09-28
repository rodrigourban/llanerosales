from django import forms
from .models import OrderList, Order


class OrderListForm(forms.ModelForm):
    class Meta:
        model = OrderList
        fields = ('title', 'description')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

