import datetime
import sys
import operator
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import ItemForm, StockForm
from .models import Item, Stock

# delete element with confirmation
# update element with previous fields when click article name
# table header on click queryparam sort=table.header.name
# input search queryparam ss
#   add settimeout through javascript but later
# table footer with paginator, stock being shown / stock total
# add stock
# sell item
# Sort if order has been given
# Filter if search has been given
# add pagination, store in cookies default
# show stock list when clicked on table cell "stock"
# show enlarged image in modal when onClick

# add users, roles, employee, manager, admin.
# add login


@require_http_methods(['GET', 'POST'])
def article(request):
    if request.method == 'GET':
        order = request.GET.get("order") or 'name'
        search = request.GET.get("search") or None
        pages = request.GET.get("pages") or 2
        headers = Item.get_fields()
        items = Item.objects.all().filter(status=True)
        items_list = []
        for el in items:
            items_list.append({
                "pk": el.pk,
                "img": el.img,
                "name": el.name.upper(),
                "sku": el.sku.upper(),
                "location": el.location.upper(),
                "sell_price": el.sell_price,
                "buy_price": el.buy_price,
                "stock": el.count_stock()
            })
        items_list = sorted(items_list, key=operator.itemgetter(order))
        paginator = Paginator(items_list, pages)
        page = request.GET.get('page')
        paginated = paginator.get_page(page)
        return render(
            request,
            "inventory/base.html",
            {
                "headers": headers,
                "pagination": paginated
            }
        )


@require_http_methods(['GET', 'PUT', 'DELETE'])
def item_detail(request):
    pass


@require_http_methods(['GET', 'POST'])
def create_item(request):
    if request.method == 'GET':
        return render(
                    request,
                    'inventory/create_item.html', 
                    {"form": ItemForm()}
                    )
    elif request.method == 'POST':
        # Create new item
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                cleaned = form.cleaned_data
                item = Item.objects.create()
                item.name = cleaned['name']
                item.sku = cleaned['sku']
                item.location = cleaned['location']
                item.sell_price = cleaned['sell_price']
                item.buy_price = cleaned['buy_price']
                item.img = cleaned['img']
                item.save()
                stock = Stock.objects.create(item=item)
                stock.buy_price = cleaned['buy_price']
                stock.amount = cleaned['initial_stock']
                stock.save()
            except Exception as e:
                print("Error {}".format(e))
            messages.success(request, "Articulo agregado exitosamente!")
            return redirect('inventory:index')
        else:
            return HttpResponse(form.errors)


@require_http_methods(['GET'])
def list_stock(request, pk):
    obj = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        # Get article or 404
        return render(
            request,
            'inventory/list_stock.html',
            {"stock_list": obj.get_stock(obj.pk)})


@require_http_methods(['GET', 'POST'])
def create_stock(request, pk):
    try:
        obj = get_object_or_404(Item, pk=pk)
    except Item.DoesNotExist:
        raise Http404("El articulo ingresado no existe")

    if request.method == 'GET':
        # Get article or 404
        return render(
                    request,
                    'inventory/create_stock.html',
                    {"form": StockForm(), "item": pk}
                     )

    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            stock = Stock.objects.create(
                                        item=obj,
                                        buy_price=clean['buy_price'],
                                        amount=clean['amount'])
            stock.save()
            messages.success(request, 'Se agrego stock correctamente!')
        return redirect('inventory:index')


@require_http_methods(['GET', 'POST'])
def delete_item(request, pk):
    try:
        obj = get_object_or_404(Item, pk=pk)
    except Item.DoesNotExist:
        raise Http404("El articulo ingresado no existe")

    if request.method == 'GET':
        # Get article or 404
        return render(request, 'inventory/delete_item.html', {"item": obj})

    if request.method == 'POST':
        obj.status = False
        # should also delete stocks related
        obj.save()
        stocks = Stock.objects.all().filter(item=obj, status=True)
        for stock in stocks:
            stock.status = False
            stock.save()
        messages.success(
                        request,
                        "{} se ha borrado exitosamente".format(obj.name))
        return redirect('inventory:index')
