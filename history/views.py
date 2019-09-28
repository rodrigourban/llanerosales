from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404
from django.shortcuts import (
    render,
    redirect,
    get_list_or_404,
    get_object_or_404
)
from django.views.decorators.http import require_http_methods
from .models import Sell
from .forms import SellForm, CancelForm
from inventory.models import Item, Stock


@require_http_methods(['GET'])
def sell_list(request):
    try:
        pages = request.GET.get("pages") or 5
        page = request.GET.get("page") or None
        headers = Sell.get_headers()
        sell_qs = Sell.objects.all()
        sell_list = []
        for qs in sell_qs:
            sell_list.append({
                'pk': qs.pk,
                'created_at': qs.created_at,
                'amount': qs.amount,
                'item_name': qs.stock.item.name,
                'buy_price': qs.stock.buy_price,
                'sell_price': qs.sell_price,
                'bruto': qs.get_bruto(),
                'neto': qs.get_neto(),
            })
        paginator = Paginator(sell_list, pages)
        paginated = paginator.get_page(page)
        print(paginated)
    except:
        print("Exception in sell_list")

    return render(
            request,
            "history/index.html",
            {
                "headers": headers,
                "pagination": paginated
            }
    )


@require_http_methods(['GET', 'POST'])
def sell_item(request, pk):
    try:
        obj = get_object_or_404(Item, pk=pk)
    except Item.DoesNotExist:
        raise Http404("El articulo ingresado no existe")

    if request.method == 'GET':
        return render(
            request,
            'history/sell_item.html',
            {"item": obj, "form": SellForm()}
            )
    elif request.method == 'POST':
        form = SellForm(request.POST)
        stock_list = Stock.objects.filter(item=obj, status=True).order_by('created_at')
        if form.is_valid():
            amount = form.cleaned_data['amount']
            sell_price = form.cleaned_data['amount']
            if obj.count_stock() >= amount:
                for stock in stock_list:
                    amount = stock.sell(amount, sell_price, user=request.user)
                    if not amount:
                        break
            else:
                messages.error(
                            request,
                            "Por favor ingresa una cantidad menor al stock"
                            )
                return redirect('history:sell-item', pk=pk)
        messages.success(
                        request,
                        "Se vendieron {} {}".format(amount, obj.name)
        )
        return redirect('inventory:index')


@require_http_methods(['GET', 'POST'])
def cancel_sell(request, pk):
    try:
        obj = get_object_or_404(Sell, pk=pk)
    except Item.DoesNotExist:
        raise Http404("El articulo ingresado no existe")

    if request.method == 'GET':
        return render(
                    request,
                    "history/cancel_sell.html",
                    {"form": CancelForm}
        )
    if request.method == 'POST':
        form = CancelForm(request.POST)
        if form.is_valid:
            if not form.cleaned_data['retrieve']:
                obj.cancel_sell()
            messages.success(
                            request,
                            "Venta cancelada exitosamente"
            )
        return redirect('history:index')
