import datetime
from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import ItemForm
from .models import Item

@require_http_methods(['GET', 'POST'])
def article(request):
    if request.method == 'GET':
        order = request.GET.get("or")
        search = request.GET.get("ss")
        now = datetime.datetime.now()
        items = Item.objects.all()
        print("hola")
        print(items)
        return render(
            request,
            "inventory/base.html",
            {
                "day": now,
                "form": ItemForm(),
                "items": items
            }
        )

    if request.method == 'POST':
        # Create new item
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned = form.cleaned_data
            item = Item.objects.create()
            print(cleaned)
            item.name = cleaned['name']
            item.sku = cleaned['sku']
            item.location = cleaned['location']
            item.sell_price = cleaned['sell_price']
            item.buy_price = cleaned['buy_price']
            item.img = cleaned['img']
            item.save()
            return HttpResponse('/thanke/')
        return render(request, 'inventory/base.html', {})
