from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.forms import modelformset_factory
from .models import Order
from .forms import OrderListForm, OrderForm
# create order_list to hold order
# -fields: title, description
# -order should have an item and a amount
# Create order view should let you add any item with a amount
# -after it should be saved as a order_list, on click show order_list
# -with all orders
# To PDF, should let you transform to PDF
# Delete order_list, order on cascade


@require_http_methods(['GET'])
def order_list(request):
    return render(
        request,
        'orders/index.html'
    )

@require_http_methods(['GET', 'POST'])
def order_list_create(request):
    return render(
        request,
        'orders/create_order.html',
        {
            'orderlistform': OrderListForm(),
            'orderform': modelformset_factory(Order, fields=('__all__'))
        }
    )

@require_http_methods(['DELETE'])
def order_list_delete(request, pk):
    pass

@require_http_methods(['DELETE'])
def order_delete(request, pk):
    pass

@require_http_methods(['GET'])
def order_list_to_pdf(request):
    pass
